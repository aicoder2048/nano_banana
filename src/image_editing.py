"""Image editing module for NanoBanana Pro."""

from typing import Dict, List, Optional
from .ui import ui
from .templates import template_manager
from .gemini_client import get_client
from .config import config

class ImageEditor:
    """Handles image editing with different features."""
    
    def __init__(self):
        self.client = get_client()
        self.feature_map = {
            "1": "add_remove",
            "2": "inpainting", 
            "3": "style_transfer",
            "4": "composition",
            "5": "detail_preservation"
        }
    
    def run(self):
        """Run image editing flow."""
        while True:
            choice = ui.show_image_editing_menu()
            
            if choice == "B":
                break
            
            if choice in self.feature_map:
                feature_key = self.feature_map[choice]
                self._edit_with_feature(feature_key)
            else:
                ui.show_error("Invalid selection")
    
    def _edit_with_feature(self, feature_key: str):
        """Edit images using specific feature."""
        template = template_manager.get_image_editing_template(feature_key)
        if not template:
            ui.show_error(f"Template not found for feature: {feature_key}")
            return
        
        ui.console.print()  # Add spacing
        
        # Get required number of images based on feature
        max_images = 3 if feature_key in ["composition", "detail_preservation"] else 1
        image_paths = ui.get_image_paths(max_images=max_images, required=True)
        
        if not image_paths:
            ui.show_error("At least one image is required for editing")
            return
        
        # Validate images
        is_valid, error_msg = self.client.validate_images(image_paths)
        if not is_valid:
            ui.show_error("Invalid images", error_msg)
            return
        
        # Ask if user wants to use template or custom prompt
        use_template = ui.console.input("Use template guide? [Y/n]: ").lower() in ['', 'y', 'yes']
        
        if use_template:
            # Show template guide
            ui.show_template_guide(template)
            
            # Ask if user wants to proceed with template or use custom prompt
            proceed = ui.console.input("Use this template? [Y/n]: ").lower() in ['', 'y', 'yes']
            
            if proceed:
                # Get template parameters
                parameters = ui.get_template_parameters(template)
                prompt = template_manager.fill_template(template, parameters)
            else:
                prompt = ui.get_custom_prompt("image editing")
        else:
            prompt = ui.get_custom_prompt("image editing")
        
        if not prompt.strip():
            ui.show_error("Prompt cannot be empty")
            return
        
        # Validate prompt
        is_valid, error_msg = self.client.validate_prompt(prompt)
        if not is_valid:
            ui.show_error("Invalid prompt", error_msg)
            return
        
        # Show prompt preview and image info
        ui.console.print("\n[bold]Final prompt:[/bold]")
        ui.console.print(f"[dim]{prompt}[/dim]\n")
        
        ui.console.print(f"[bold]Input images ({len(image_paths)}):[/bold]")
        for i, path in enumerate(image_paths, 1):
            ui.console.print(f"  {i}. {path}")
        ui.console.print()
        
        # Select resolution (optional for editing)
        use_custom_resolution = ui.console.input("Specify output resolution? [y/N]: ").lower() in ['y', 'yes']
        resolution = ui.select_resolution() if use_custom_resolution else None
        
        # Edit images
        with ui.show_progress("🎭 Editing images...") as progress:
            task = progress.add_task("Processing...", total=None)
            
            try:
                success, message, images = self.client.edit_image(prompt, image_paths, resolution)
            except Exception as e:
                success, message, images = False, f"Unexpected error: {str(e)}", None
        
        if success and images:
            # Save images
            try:
                saved_files = self.client.save_images(images, f"edited_{feature_key}")
                
                ui.show_success(message, saved_files)
                
                # Add to history
                config.add_to_history({
                    "mode": "image-editing",
                    "theme_or_feature": template.name,
                    "prompt": prompt,
                    "input_images": image_paths,
                    "resolution": resolution or "original",
                    "generated_files": saved_files
                })
                
                # Ask if user wants to open images
                if config.get("auto_open_images") or \
                   ui.console.input("Open edited images? [Y/n]: ").lower() in ['', 'y', 'yes']:
                    self._open_images(saved_files)
                    
            except Exception as e:
                ui.show_error("Failed to save images", f"Images were generated but couldn't be saved: {str(e)}")
        else:
            # Provide detailed error information
            ui.show_error("Editing failed", message)
            
            # Additional debugging info
            ui.console.print("\n[dim]Debugging information:[/dim]")
            ui.console.print(f"[dim]• Feature: {template.name}[/dim]")
            ui.console.print(f"[dim]• Input images: {len(image_paths)}[/dim]")
            ui.console.print(f"[dim]• Prompt length: {len(prompt)} characters[/dim]")
            ui.console.print(f"[dim]• Resolution: {resolution or 'original'}[/dim]")
            
            # Common solutions
            ui.console.print("\n[yellow]💡 Common solutions:[/yellow]")
            ui.console.print("• Check that image files exist and are readable")
            ui.console.print("• Ensure images are in supported formats (PNG, JPEG, JPG)")
            ui.console.print("• Verify your internet connection")
            ui.console.print("• Try with a simpler prompt or different images")
            ui.console.print("• Check if your API quota is exceeded")
        
        ui.pause()
    
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
image_editor = ImageEditor()