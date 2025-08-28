"""Conversational image generation module for NanoBanana Pro."""

import os
import re
from typing import Dict, List, Optional, Any, Tuple
from PIL import Image
from io import BytesIO

from .ui import ui
from .gemini_client import get_client
from .config import config

class ChatImageGenerator:
    """Handles conversational image generation and refinement."""
    
    def __init__(self):
        self.client = get_client()
        self.conversation_history = []
        self.current_images = []
        self.reference_images = {}  # Store referenced images by name
    
    def _parse_image_references(self, text: str) -> Tuple[str, List[str]]:
        """Parse image references in text and return clean text and image paths.
        
        Supported syntax:
        - @image:/path/to/image.jpg
        - @img:/path/to/image.jpg  
        - @/path/to/image.jpg
        """
        image_paths = []
        clean_text = text
        
        # Combined pattern that matches all formats in one pass
        # This ensures no overlapping matches
        pattern = r'@(?:image:|img:)?([^\s]+\.(?:jpg|jpeg|png|gif|bmp|tiff|heic))'
        
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        
        # Process matches in reverse order to maintain text positions
        for match in reversed(matches):
            path = match.group(1)
            image_paths.insert(0, path)  # Insert at beginning to maintain original order
            
            # Remove the full match from text
            start, end = match.span()
            clean_text = clean_text[:start] + clean_text[end:]
        
        # Clean up extra spaces
        clean_text = ' '.join(clean_text.split())
        
        return clean_text, image_paths
    
    def _load_reference_images(self, image_paths: List[str]) -> List[Image.Image]:
        """Load referenced images from file paths."""
        loaded_images = []
        
        for path in image_paths:
            try:
                # Expand user path and make absolute
                full_path = os.path.expanduser(path)
                if not os.path.isabs(full_path):
                    full_path = os.path.abspath(full_path)
                
                if not os.path.exists(full_path):
                    ui.show_warning(f"Image not found: {path}")
                    continue
                
                # Validate it's an image file
                try:
                    img = Image.open(full_path)
                    loaded_images.append(img)
                    
                    # Store in reference images for reuse
                    filename = os.path.basename(path)
                    self.reference_images[filename] = img
                    
                    ui.show_info(f"📸 Loaded reference image: {filename}")
                    
                except Exception as e:
                    ui.show_warning(f"Failed to load image {path}: {str(e)}")
                    continue
                    
            except Exception as e:
                ui.show_warning(f"Error processing image path {path}: {str(e)}")
                continue
        
        return loaded_images
    
    def run(self):
        """Run chat-image generation flow."""
        ui.console.print("\n[bold cyan]💬 Chat-Image Mode[/bold cyan]")
        ui.console.print("[dim]Start a conversation to generate and refine images iteratively.[/dim]")
        ui.console.print("[dim]Type 'quit' to exit, 'clear' to start new conversation, 'save' to save current images.[/dim]")
        ui.console.print("[dim]💡 Use @image:/path/to/file.jpg to reference local images in conversation![/dim]\n")
        
        self.conversation_history = []
        self.current_images = []
        
        while True:
            # Get user input
            user_input = ui.console.input("[bold green]You:[/bold green] ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() == 'clear':
                self._clear_conversation()
                continue
            elif user_input.lower() == 'save':
                self._save_current_images()
                continue
            elif user_input.lower() in ['help', '?']:
                self._show_chat_help()
                continue
            
            # Parse image references in user input
            clean_text, image_paths = self._parse_image_references(user_input)
            
            # Load referenced images
            reference_images = []
            if image_paths:
                reference_images = self._load_reference_images(image_paths)
            
            # Use clean text for the conversation
            conversation_text = clean_text if clean_text.strip() else "Please analyze the referenced image(s)"
            
            # Add user message to conversation history
            self.conversation_history.append({
                'type': 'text',
                'content': user_input,  # Keep original with references for history
                'role': 'user'
            })
            
            # Build message context for API
            messages = []
            
            # Add current generated images to conversation context if available
            if self.current_images:
                for img_data in self.current_images:
                    img = Image.open(BytesIO(img_data))
                    messages.append({
                        'type': 'image',
                        'content': img
                    })
            
            # Add referenced images
            for ref_img in reference_images:
                messages.append({
                    'type': 'image',
                    'content': ref_img
                })
            
            # Add the user's text message (cleaned)
            messages.append({
                'type': 'text',
                'content': conversation_text
            })
            
            # Generate response
            with ui.show_progress("🤖 Thinking...") as progress:
                task = progress.add_task("Processing...", total=None)
                
                success, response_text, new_images = self.client.chat_about_image(messages)
            
            if success:
                # Show response
                ui.console.print(f"[bold cyan]Assistant:[/bold cyan] {response_text}\n")
                
                # Update current images if new ones were generated
                if new_images:
                    self.current_images = new_images
                    ui.show_success(f"Generated {len(new_images)} new image(s)")
                    
                    # Ask if user wants to save immediately
                    if ui.console.input("Save images now? [Y/n]: ").lower() in ['', 'y', 'yes']:
                        self._save_current_images()
                
                # Add response to conversation history
                self.conversation_history.append({
                    'type': 'text',
                    'content': response_text,
                    'role': 'assistant'
                })
                
            else:
                ui.show_error("Chat failed", response_text)
        
        # Exit without asking to save images
    
    def _clear_conversation(self):
        """Clear conversation history and current images."""
        if self.current_images:
            save_current = ui.console.input("Save current images before clearing? [Y/n]: ").lower() in ['', 'y', 'yes']
            if save_current:
                self._save_current_images()
        
        self.conversation_history = []
        self.current_images = []
        self.reference_images = {}  # Clear reference images too
        ui.show_info("Conversation cleared. Starting fresh!")
    
    def _save_current_images(self):
        """Save current images to disk."""
        if not self.current_images:
            ui.show_warning("No images to save")
            return
        
        # Save images
        saved_files = self.client.save_images(self.current_images, "chat_image")
        
        ui.show_success(f"Saved {len(saved_files)} image(s)", saved_files)
        
        # Add to history
        conversation_summary = self._summarize_conversation()
        config.add_to_history({
            "mode": "chat-image",
            "theme_or_feature": "conversational",
            "prompt": conversation_summary,
            "generated_files": saved_files,
            "conversation_length": len(self.conversation_history)
        })
        
        # Ask if user wants to open images
        if config.get("auto_open_images") or \
           ui.console.input("Open saved images? [Y/n]: ").lower() in ['', 'y', 'yes']:
            self._open_images(saved_files)
    
    def _summarize_conversation(self) -> str:
        """Create a summary of the conversation for history."""
        user_messages = [msg['content'] for msg in self.conversation_history 
                        if msg.get('role') == 'user']
        
        if not user_messages:
            return "Empty conversation"
        
        if len(user_messages) == 1:
            return user_messages[0][:100]
        
        first_msg = user_messages[0][:50]
        last_msg = user_messages[-1][:50]
        return f"{first_msg}... [{len(user_messages)} messages] ...{last_msg}"
    
    def _show_chat_help(self):
        """Show help for chat mode."""
        help_text = """
[bold]💬 Chat-Image Mode Commands:[/bold]

[green]• Regular conversation:[/green] Just type naturally to generate and refine images
[green]• 'quit', 'exit', 'q':[/green] Exit chat mode
[green]• 'clear':[/green] Start a new conversation (saves current images first)
[green]• 'save':[/green] Save current images to disk
[green]• 'help', '?':[/green] Show this help

[bold]📸 Local Image References:[/bold]
[yellow]• @image:/path/to/photo.jpg[/yellow] - Reference a local image file
[yellow]• @img:/path/to/photo.jpg[/yellow] - Short form reference  
[yellow]• @/path/to/photo.jpg[/yellow] - Minimal reference (auto-detected by file extension)

[bold]Example conversations:[/bold]
• "Create a sunset landscape"
• "Make it more vibrant"
• "Add a mountain in the background" 
• "Change the time to midnight with stars"

[bold]Using image references:[/bold]
• "@image:/Users/john/Desktop/photo.jpg Analyze this photo"
• "Make the current image look like @img:style_ref.png"
• "@/path/to/portrait.jpg Change the background to a forest"
• "Combine the style from @style.jpg with @content.jpg"

[bold]Tips:[/bold]
• Be specific about what you want to change
• Use iterative refinement: "make it warmer", "add more contrast"
• Combine style and content changes: "make it more painterly and add clouds"
• Referenced images are loaded once and can be reused in the conversation
• Drag files into terminal on most systems to get the full path
        """
        
        ui.console.print(help_text)
    
    def _open_images(self, image_paths: List[str]):
        """Open generated images using system default application."""
        import subprocess
        import platform
        
        system = platform.system()
        
        for path in image_paths:
            try:
                if system == "Darwin":  # macOS
                    subprocess.run(["open", path])
                elif system == "Windows":
                    subprocess.run(["start", path], shell=True)
                else:  # Linux
                    subprocess.run(["xdg-open", path])
                ui.show_info(f"Opened: {path}")
            except Exception as e:
                ui.show_warning(f"Could not open {path}: {e}")

# Global instance
chat_image_generator = ChatImageGenerator()