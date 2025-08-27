"""Configuration management for NanoBanana Pro."""

import os
from typing import Dict, Any, Optional
from datetime import datetime
import json
from pathlib import Path

class Config:
    """Configuration manager for NanoBanana Pro."""
    
    # Resolution presets from PRD
    RESOLUTION_PRESETS = {
        "square-small": "512x512",
        "square-medium": "1024x1024", 
        "square-large": "2048x2048",
        "landscape-hd": "1920x1080",
        "landscape-macbook": "2880x1800",
        "landscape-macbook-xl": "3456x2234",
        "portrait-iphone": "1179x2556",
        "portrait-iphone-mini": "1080x2340",
        "portrait-social": "1080x1920"
    }
    
    # Gemini model settings
    GEMINI_IMAGE_MODEL = "gemini-2.5-flash-image-preview"
    GEMINI_TEXT_MODEL = "gemini-2.5-flash"
    
    # Directory settings
    IMAGES_DIR = "images"
    CONFIG_DIR = ".nanobanana"
    
    def __init__(self):
        self.config_dir = Path(self.CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.history_file = self.config_dir / "history.json"
        
        # Ensure images directory exists
        Path(self.IMAGES_DIR).mkdir(exist_ok=True)
        
        self.settings = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file."""
        default_config = {
            "default_resolution": "square-medium",
            "default_theme": "photorealistic",
            "save_history": True,
            "max_history_items": 100,
            "auto_open_images": False,
            "language": "en"
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    return {**default_config, **config}
            except (json.JSONDecodeError, IOError):
                return default_config
        
        return default_config
    
    def save_config(self):
        """Save current configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except IOError as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value."""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value."""
        self.settings[key] = value
        self.save_config()
    
    def get_api_key(self) -> Optional[str]:
        """Get Gemini API key from environment."""
        return os.environ.get("GEMINI_API_KEY")
    
    def add_to_history(self, entry: Dict[str, Any]):
        """Add entry to generation history."""
        if not self.get("save_history"):
            return
            
        history = self.get_history()
        entry["timestamp"] = datetime.now().isoformat()
        history.insert(0, entry)  # Add to beginning
        
        # Keep only max_history_items
        max_items = self.get("max_history_items", 100)
        history = history[:max_items]
        
        try:
            with open(self.history_file, 'w') as f:
                json.dump(history, f, indent=2)
        except IOError as e:
            print(f"Error saving history: {e}")
    
    def get_history(self) -> list:
        """Get generation history."""
        if not self.history_file.exists():
            return []
            
        try:
            with open(self.history_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    
    def clear_history(self):
        """Clear generation history."""
        try:
            if self.history_file.exists():
                self.history_file.unlink()
        except IOError as e:
            print(f"Error clearing history: {e}")

# Global config instance
config = Config()