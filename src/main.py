"""Main application entry point for NanoBanana Pro."""

import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from .ui import ui
from .config import config
from .text_to_image import text_to_image_generator
from .image_editing import image_editor
from .chat_image import chat_image_generator
from .settings import settings_manager
from .i18n import i18n, Language

class NanoBananaApp:
    """Main application class for NanoBanana Pro."""
    
    def __init__(self):
        self.running = True
    
    def run(self):
        """Run the main application."""
        try:
            # Load saved language preference
            saved_language = config.get("language", "en")
            if saved_language == "zh":
                i18n.set_language(Language.CHINESE)
            else:
                i18n.set_language(Language.ENGLISH)
            
            # Check for API key
            if not config.get_api_key():
                ui.show_error(
                    "GEMINI_API_KEY environment variable is required",
                    "Please set your Gemini API key in the .env file"
                )
                return
            
            # Show welcome screen
            ui.show_welcome()
            
            # Main application loop
            while self.running:
                try:
                    choice = ui.show_main_menu()
                    self._handle_menu_choice(choice)
                except KeyboardInterrupt:
                    ui.console.print("\n\n[yellow]Interrupted by user[/yellow]")
                    if self._confirm_quit():
                        break
                except Exception as e:
                    ui.show_error("Unexpected error occurred", str(e))
                    ui.console.print("\n[dim]Please report this issue if it persists.[/dim]")
                    ui.pause()
        
        except Exception as e:
            ui.show_error("Fatal error", str(e))
            sys.exit(1)
        
        finally:
            self._cleanup()
    
    def _handle_menu_choice(self, choice: str):
        """Handle main menu choice."""
        if choice == "1":
            # Text-to-Image Generation
            text_to_image_generator.run()
        
        elif choice == "2":
            # Image Editing & Enhancement
            image_editor.run()
        
        elif choice == "3":
            # Chat-Image (Conversational)
            chat_image_generator.run()
        
        elif choice == "4":
            # Settings & Configuration
            settings_manager.run()
        
        elif choice == "5":
            # View Generation History
            self._show_history()
        
        elif choice == "6":
            # Help & Templates
            self._show_help()
        
        elif choice == "7":
            # Language Selection
            self._show_language_selection()
        
        elif choice == "Q":
            # Quit
            if self._confirm_quit():
                self.running = False
        
        else:
            ui.show_error("Invalid menu choice")
    
    def _show_history(self):
        """Show generation history."""
        ui.console.print("\n[bold cyan]📊 Generation History[/bold cyan]\n")
        
        history = config.get_history()
        
        if not history:
            ui.show_info("No generation history found.")
            ui.pause()
            return
        
        # Show history with pagination
        page_size = 10
        total_pages = (len(history) + page_size - 1) // page_size
        current_page = 0
        
        while True:
            start_idx = current_page * page_size
            end_idx = min(start_idx + page_size, len(history))
            page_history = history[start_idx:end_idx]
            
            ui.show_history(page_history)
            
            if total_pages > 1:
                ui.console.print(f"[dim]Page {current_page + 1} of {total_pages}[/dim]")
                ui.console.print("[dim]Commands: [n]ext, [p]revious, [q]uit[/dim]\n")
                
                from rich.prompt import Prompt
                nav = Prompt.ask("Navigation", 
                               choices=["n", "p", "q"], 
                               default="q" if current_page == total_pages - 1 else "n")
                
                if nav == "n" and current_page < total_pages - 1:
                    current_page += 1
                elif nav == "p" and current_page > 0:
                    current_page -= 1
                elif nav == "q":
                    break
            else:
                ui.pause()
                break
    
    def _show_help(self):
        """Show help and templates."""
        help_menu = [
            ("1", "📋  View Text-to-Image Templates", "See all available templates"),
            ("2", "🎭  View Image Editing Templates", "See editing templates"),
            ("3", "💡  Best Practices Guide", "Tips for better prompts"),
            ("4", "🔗  API Documentation", "Gemini API reference"),
            ("5", "❓  Keyboard Shortcuts", "Quick reference"),
            ("B", "🔙  Back to Main Menu", "Return to main menu")
        ]
        
        while True:
            from rich.table import Table, Panel
            table = Table(show_header=False, box=None, padding=(0, 2))
            table.add_column("Key", style="bold cyan", width=3)
            table.add_column("Option", style="bold white", width=35)
            table.add_column("Description", style="dim", width=25)
            
            for key, option, desc in help_menu:
                table.add_row(f"[{key}]", option, desc)
            
            panel = Panel(
                table,
                title="[bold]❓ Help & Templates[/bold]",
                border_style="bright_white",
                padding=(1, 2)
            )
            
            ui.console.print(panel)
            ui.console.print()
            
            from rich.prompt import Prompt
            choice = Prompt.ask("Select option", 
                               choices=["1", "2", "3", "4", "5", "b", "B"], 
                               default="1")
            
            if choice.upper() == "B":
                break
            elif choice == "1":
                self._show_text_templates()
            elif choice == "2":
                self._show_editing_templates()
            elif choice == "3":
                self._show_best_practices()
            elif choice == "4":
                self._show_api_docs()
            elif choice == "5":
                self._show_shortcuts()
    
    def _show_text_templates(self):
        """Show text-to-image templates."""
        from .templates import template_manager
        
        ui.console.print("\n[bold cyan]📋 Text-to-Image Templates[/bold cyan]\n")
        
        themes = template_manager.get_all_text_to_image_themes()
        
        for theme in themes:
            template = template_manager.get_text_to_image_template(theme)
            if template:
                ui.console.print(f"[bold green]{template.name}[/bold green]")
                ui.console.print(f"[dim]{template.description}[/dim]")
                ui.console.print(f"[yellow]Template:[/yellow] {template.template}")
                ui.console.print(f"[blue]Example:[/blue] {template.example[:100]}...")
                ui.console.print()
        
        ui.pause()
    
    def _show_editing_templates(self):
        """Show image editing templates."""
        from .templates import template_manager
        
        ui.console.print("\n[bold cyan]🎭 Image Editing Templates[/bold cyan]\n")
        
        features = template_manager.get_all_image_editing_features()
        
        for feature in features:
            template = template_manager.get_image_editing_template(feature)
            if template:
                ui.console.print(f"[bold green]{template.name}[/bold green]")
                ui.console.print(f"[dim]{template.description}[/dim]")
                ui.console.print(f"[yellow]Template:[/yellow] {template.template}")
                ui.console.print(f"[blue]Example:[/blue] {template.example[:100]}...")
                ui.console.print()
        
        ui.pause()
    
    def _show_best_practices(self):
        """Show best practices guide."""
        best_practices = """
[bold cyan]💡 Best Practices for AI Image Generation[/bold cyan]

[bold green]1. Be Hyper-Specific[/bold green]
• Instead of "fantasy armor," use "ornate elven plate armor, etched with silver leaf patterns"
• Include details about textures, materials, lighting, and atmosphere
• Use photography terms for realistic images (aperture, lens type, lighting setup)

[bold green]2. Provide Context and Intent[/bold green]
• Explain the purpose: "Create a logo for a high-end, minimalist skincare brand"
• Context influences the final output significantly
• Include the intended use case when relevant

[bold green]3. Use Step-by-Step Instructions[/bold green]
• Break complex scenes into layers
• "First, create a background... Then, add... Finally, place..."
• This helps with compositional control

[bold green]4. Control the Camera[/bold green]
• Use terms like: wide-angle shot, macro shot, low-angle perspective
• Specify depth of field: shallow depth of field, bokeh effect
• Include aspect ratio requirements

[bold green]5. Iterative Refinement[/bold green]
• Start with a base image, then refine iteratively
• Use specific modification requests: "make the lighting warmer", "add more contrast"
• Build up complexity gradually

[bold green]6. Semantic Negative Prompts[/bold green]
• Instead of "no cars," use "empty, deserted street with no signs of traffic"
• Describe what you want positively rather than what you don't want
        """
        
        ui.console.print(best_practices)
        ui.pause()
    
    def _show_api_docs(self):
        """Show API documentation reference."""
        api_info = """
[bold cyan]🔗 Gemini API Documentation[/bold cyan]

[bold green]Model Information[/bold green]
• Primary Model: gemini-2.5-flash-image-preview
• Input: Text prompts up to ~8K tokens
• Image Input: PNG, JPEG (up to 3 images simultaneously)
• Output: High-quality images with SynthID watermark

[bold green]Key Features[/bold green]
• Text-to-Image Generation
• Image + Text-to-Image (Editing)
• Multi-Image to Image (Composition & Style Transfer)
• Iterative Refinement
• High-Fidelity Text Rendering

[bold green]Limitations[/bold green]
• Best performance with EN, es-MX, ja-JP, zh-CN, hi-IN
• Works best with up to 3 input images
• All generated images include SynthID watermark
• No audio or video inputs supported

[bold green]External Resources[/bold green]
• Full API Documentation: https://ai.google.dev/gemini-api/docs/image-understanding
• Cookbook Examples: https://colab.sandbox.google.com/github/google-gemini/cookbook/
• Best Practices: https://ai.google.dev/gemini-api/docs/prompting
        """
        
        ui.console.print(api_info)
        ui.pause()
    
    def _show_shortcuts(self):
        """Show keyboard shortcuts and quick reference."""
        shortcuts = """
[bold cyan]❓ Keyboard Shortcuts & Quick Reference[/bold cyan]

[bold green]General Navigation[/bold green]
• Ctrl+C: Interrupt current operation
• Enter: Accept default option
• Numbers: Select menu items
• Q: Quit from most menus
• B: Back to previous menu

[bold green]Chat Mode Commands[/bold green]
• 'quit', 'exit', 'q': Exit chat mode
• 'clear': Start new conversation
• 'save': Save current images
• 'help', '?': Show chat help

[bold green]Template Mode[/bold green]
• Y/Enter: Use template guide
• N: Skip to custom prompt
• Empty parameter: Use example value (if optional)

[bold green]File Paths[/bold green]
• Absolute paths work best
• Drag and drop files in terminal (most systems)
• Relative paths from project directory
• Supported formats: PNG, JPEG, JPG
        """
        
        ui.console.print(shortcuts)
        ui.pause()
    
    def _confirm_quit(self) -> bool:
        """Confirm quit action."""
        from rich.prompt import Confirm
        return Confirm.ask("Are you sure you want to quit?", default=False)
    
    def _show_language_selection(self):
        """Show language selection menu."""
        while True:
            choice = ui.show_language_menu()
            
            if choice == "B":
                break
            elif choice == "1":
                # English
                ui.switch_language(Language.ENGLISH)
                ui.show_info("Language changed to English")
                ui.pause()
                break
            elif choice == "2":
                # Chinese
                ui.switch_language(Language.CHINESE)
                ui.show_info("语言已切换为中文")
                ui.pause()
                break
    
    def _cleanup(self):
        """Cleanup before exit."""
        ui.console.print(f"\n[bold green]{i18n.t('goodbye')}[/bold green]")
        ui.console.print(f"[dim]{i18n.t('images_saved_info')}[/dim]\n")

def main():
    """Main entry point."""
    app = NanoBananaApp()
    app.run()

if __name__ == "__main__":
    main()