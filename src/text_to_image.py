"""Text-to-image generation module for NanoBanana Pro."""

from typing import Dict, List, Optional
from .ui import ui
from .templates import template_manager
from .gemini_client import get_client
from .config import config

class TextToImageGenerator:
    """Handles text-to-image generation with different themes."""
    
    def __init__(self):
        self.client = get_client()
        self.theme_map = {
            "1": "photorealistic",
            "2": "stylized", 
            "3": "text_in_images",
            "4": "product_mockup",
            "5": "minimalist",
            "6": "sequential_art"
        }
    
    def run(self):
        """Run text-to-image generation flow."""
        while True:
            choice = ui.show_text_to_image_menu()
            
            if choice == "B":
                break
            
            if choice in self.theme_map:
                theme_key = self.theme_map[choice]
                self._generate_with_theme(theme_key)
            else:
                ui.show_error("Invalid selection")
    
    def _generate_with_theme(self, theme_key: str):
        """Generate image using specific theme."""
        template = template_manager.get_text_to_image_template(theme_key)
        if not template:
            ui.show_error(f"Template not found for theme: {theme_key}")
            return
        
        ui.console.print()  # Add spacing
        
        # Ask if user wants to use template or custom prompt
        use_template = ui.console.input("Use template guide? [Y/n]: ").lower() in ['', 'y', 'yes']
        
        if use_template:
            # Show template guide
            ui.show_template_guide(template)
            
            # Ask if user wants to proceed with template or use custom prompt
            proceed = ui.console.input("Use this template? [Y/n]: ").lower() in ['', 'y', 'yes']
            
            if proceed:
                # Ask for mode selection
                ui.console.print("\n[bold cyan]📋 Template Mode Selection[/bold cyan]")
                ui.console.print("[bold green][1][/bold green] Quick Mode - Only essential parameters")
                ui.console.print("[bold green][2][/bold green] Detailed Mode - All available parameters")
                ui.console.print("[bold green][3][/bold green] Custom Mode - Choose which parameters to fill")
                
                from rich.prompt import Prompt
                mode_choice = Prompt.ask("Select mode", choices=["1", "2", "3"], default="1")
                
                if mode_choice == "1":
                    # Quick mode - only essential parameters
                    parameters = ui.get_template_parameters_quick(template)
                elif mode_choice == "2":
                    # Detailed mode - all parameters
                    parameters = ui.get_template_parameters_detailed(template)
                else:
                    # Custom mode - let user choose
                    parameters = ui.get_template_parameters_custom(template)
                
                prompt = template_manager.fill_template(template, parameters)
            else:
                prompt = ui.get_custom_prompt("text-to-image")
        else:
            prompt = ui.get_custom_prompt("text-to-image")
        
        if not prompt.strip():
            ui.show_error("Prompt cannot be empty")
            return
        
        # Validate prompt
        is_valid, error_msg = self.client.validate_prompt(prompt)
        if not is_valid:
            ui.show_error("Invalid prompt", error_msg)
            return
        
        # Show prompt preview
        ui.console.print("\n[bold]Final prompt:[/bold]")
        ui.console.print(f"[dim]{prompt}[/dim]\n")
        
        # Confirm generation
        if not ui.console.input("Generate image? [Y/n]: ").lower() in ['', 'y', 'yes']:
            return
        
        # Select resolution
        resolution = ui.select_resolution()
        
        # Generate image
        with ui.show_progress("🎨 Generating image...") as progress:
            task = progress.add_task("Generating...", total=None)
            
            success, message, images = self.client.generate_text_to_image(prompt, resolution)
        
        if success and images:
            # Save images
            saved_files = self.client.save_images(images, f"text2img_{theme_key}")
            
            ui.show_success(message, saved_files)
            
            # Add to history
            config.add_to_history({
                "mode": "text-to-image",
                "theme_or_feature": template.name if use_template else "custom",
                "prompt": prompt,
                "resolution": resolution,
                "generated_files": saved_files
            })
            
            # Ask if user wants to open images
            if config.get("auto_open_images") or \
               ui.console.input("Open generated images? [Y/n]: ").lower() in ['', 'y', 'yes']:
                self._open_images(saved_files)
        else:
            ui.show_error("Generation failed", message)
        
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
text_to_image_generator = TextToImageGenerator()