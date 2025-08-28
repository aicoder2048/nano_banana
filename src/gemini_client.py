"""Gemini API client for NanoBanana Pro."""

import os
import time
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime
from io import BytesIO

import google.generativeai as genai
from PIL import Image

from .config import config

class GeminiClient:
    """Client for interacting with Google's Gemini API."""
    
    def __init__(self):
        self.api_key = config.get_api_key()
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")
        
        genai.configure(api_key=self.api_key)
        self._image_model = None
        self._text_model = None
    
    @property
    def image_model(self):
        """Get image generation model."""
        if self._image_model is None:
            self._image_model = genai.GenerativeModel(config.GEMINI_IMAGE_MODEL)
        return self._image_model
    
    @property
    def text_model(self):
        """Get text generation model."""
        if self._text_model is None:
            self._text_model = genai.GenerativeModel(config.GEMINI_TEXT_MODEL)
        return self._text_model
    
    def validate_images(self, image_paths: List[str]) -> Tuple[bool, str]:
        """Validate input images."""
        if len(image_paths) > 3:
            return False, "Maximum 3 images supported simultaneously"
        
        for path in image_paths:
            if not os.path.exists(path):
                return False, f"Image file not found: {path}"
            
            try:
                with Image.open(path) as img:
                    # Check format
                    if img.format not in ['PNG', 'JPEG', 'JPG']:
                        return False, f"Unsupported image format: {img.format}. Only PNG and JPEG are supported."
                    
                    # Check size (optional - Gemini handles resizing)
                    width, height = img.size
                    if width < 32 or height < 32:
                        return False, f"Image too small: {width}x{height}. Minimum 32x32 pixels required."
                    
            except Exception as e:
                return False, f"Invalid image file {path}: {str(e)}"
        
        return True, ""
    
    def generate_text_to_image(self, prompt: str, resolution: Optional[str] = None) -> Tuple[bool, str, Optional[List[bytes]]]:
        """Generate images from text prompt."""
        try:
            # Add resolution instruction if specified
            if resolution and resolution in config.RESOLUTION_PRESETS:
                resolution_text = config.RESOLUTION_PRESETS[resolution]
                prompt = f"{prompt} The output image should be exactly {resolution_text} pixels."
            
            # Generate content
            response = self.image_model.generate_content([prompt])
            
            # Extract images
            images = []
            text_response = None
            
            for part in response.candidates[0].content.parts:
                if part.text:
                    text_response = part.text
                elif part.inline_data:
                    images.append(part.inline_data.data)
            
            if not images:
                return False, "No images generated in response", None
            
            return True, text_response or "Image generated successfully", images
            
        except Exception as e:
            return False, f"Error generating image: {str(e)}", None
    
    def edit_image(self, prompt: str, image_paths: List[str], resolution: Optional[str] = None) -> Tuple[bool, str, Optional[List[bytes]]]:
        """Edit images using text prompts."""
        try:
            # Validate images
            is_valid, error_msg = self.validate_images(image_paths)
            if not is_valid:
                return False, error_msg, None
            
            # Prepare content
            content = [prompt]
            
            # Add images
            for image_path in image_paths:
                img = Image.open(image_path)
                content.append(img)
            
            # Add resolution instruction if specified
            if resolution and resolution in config.RESOLUTION_PRESETS:
                resolution_text = config.RESOLUTION_PRESETS[resolution]
                content[0] = f"{content[0]} The output image should be exactly {resolution_text} pixels."
            
            # Generate content
            response = self.image_model.generate_content(content)
            
            # Extract images
            images = []
            text_response = None
            
            for part in response.candidates[0].content.parts:
                if part.text:
                    text_response = part.text
                elif part.inline_data:
                    images.append(part.inline_data.data)
            
            if not images:
                return False, "No images generated in response", None
            
            return True, text_response or "Image edited successfully", images
            
        except FileNotFoundError as e:
            return False, f"Image file not found: {str(e)}", None
        except PermissionError as e:
            return False, f"Permission denied accessing image file: {str(e)}", None
        except Exception as e:
            # Provide more specific error messages based on error type
            error_msg = str(e).lower()
            if "quota" in error_msg or "limit" in error_msg:
                return False, f"API quota exceeded or rate limit hit: {str(e)}", None
            elif "network" in error_msg or "connection" in error_msg:
                return False, f"Network connection error: {str(e)}", None
            elif "authentication" in error_msg or "unauthorized" in error_msg:
                return False, f"API authentication failed: {str(e)}", None
            elif "safety" in error_msg or "blocked" in error_msg:
                return False, f"Content blocked by safety filters: {str(e)}", None
            else:
                return False, f"Error editing image: {str(e)}", None
    
    def chat_about_image(self, messages: List[Dict[str, Any]]) -> Tuple[bool, str]:
        """Have a conversation about images."""
        try:
            # Convert messages to Gemini format
            content = []
            for msg in messages:
                if msg['type'] == 'text':
                    content.append(msg['content'])
                elif msg['type'] == 'image':
                    if isinstance(msg['content'], str):
                        # Image path
                        img = Image.open(msg['content'])
                        content.append(img)
                    else:
                        # Assume PIL Image
                        content.append(msg['content'])
            
            response = self.image_model.generate_content(content)
            
            # Handle response
            images = []
            text_response = None
            
            for part in response.candidates[0].content.parts:
                if part.text:
                    text_response = part.text
                elif part.inline_data:
                    images.append(part.inline_data.data)
            
            return True, text_response or "Response generated", images if images else None
            
        except Exception as e:
            return False, f"Error in chat: {str(e)}", None
    
    def save_images(self, images: List[bytes], prefix: str = "generated_image") -> List[str]:
        """Save generated images to disk."""
        saved_files = []
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for i, image_data in enumerate(images):
            # Create filename
            if len(images) == 1:
                filename = f"{prefix}_{timestamp}.png"
            else:
                filename = f"{prefix}_{timestamp}_{i+1}.png"
            
            filepath = os.path.join(config.IMAGES_DIR, filename)
            
            try:
                # Save image
                img = Image.open(BytesIO(image_data))
                img.save(filepath, "PNG")
                saved_files.append(filepath)
                
            except Exception as e:
                print(f"Error saving image {i+1}: {e}")
        
        return saved_files
    
    def estimate_tokens(self, text: str) -> int:
        """Rough estimate of token count."""
        # Simple estimation: ~4 characters per token
        return len(text) // 4
    
    def validate_prompt(self, prompt: str) -> Tuple[bool, str]:
        """Validate prompt for length and content."""
        if not prompt.strip():
            return False, "Prompt cannot be empty"
        
        token_count = self.estimate_tokens(prompt)
        if token_count > 8000:  # Conservative limit
            return False, f"Prompt too long ({token_count} estimated tokens). Maximum ~8000 tokens allowed."
        
        return True, ""

# Global client instance (lazy initialization)
_client = None

def get_client() -> GeminiClient:
    """Get global Gemini client instance."""
    global _client
    if _client is None:
        _client = GeminiClient()
    return _client