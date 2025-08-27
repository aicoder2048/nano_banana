"""User interface components for NanoBanana Pro using Rich."""

import os
from typing import Dict, List, Optional, Any, Tuple
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.columns import Columns
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.live import Live
from rich.layout import Layout

from .config import config
from .templates import template_manager, PromptTemplate
from .i18n import i18n, Language

class NanoBananaUI:
    """Rich-based UI for NanoBanana Pro."""
    
    def __init__(self):
        self.console = Console()
        self.history_shown = False
    
    def show_welcome(self):
        """Show welcome screen."""
        title = f"""
{i18n.t("app_title")}
{i18n.t("app_subtitle")}
        """
        
        welcome_panel = Panel(
            title.strip(),
            style="bold magenta",
            border_style="bright_magenta",
            padding=(1, 2)
        )
        
        self.console.print()
        self.console.print(welcome_panel)
        self.console.print()
        
        # Show version info
        version_info = i18n.t("version_info", 
                             version="2.0",
                             model="gemini-2.5-flash-image-preview",
                             images_dir=config.IMAGES_DIR)
        
        info_text = Text(version_info, style="dim")
        self.console.print(info_text)
        self.console.print()
    
    def show_main_menu(self) -> str:
        """Show main menu and get user choice."""
        menu_options = [
            ("1", i18n.t("main_menu_text_to_image"), i18n.t("main_menu_text_to_image_desc")),
            ("2", i18n.t("main_menu_image_editing"), i18n.t("main_menu_image_editing_desc")),
            ("3", i18n.t("main_menu_chat_image"), i18n.t("main_menu_chat_image_desc")),
            ("4", i18n.t("main_menu_settings"), i18n.t("main_menu_settings_desc")),
            ("5", i18n.t("main_menu_history"), i18n.t("main_menu_history_desc")),
            ("6", i18n.t("main_menu_help"), i18n.t("main_menu_help_desc")),
            ("7", i18n.t("main_menu_language"), i18n.t("main_menu_language_desc")),
            ("Q", i18n.t("main_menu_quit"), i18n.t("main_menu_quit_desc"))
        ]
        
        # Create table
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", style="bold cyan", width=3)
        table.add_column("Option", style="bold white", width=35)
        table.add_column("Description", style="dim", width=30)
        
        for key, option, desc in menu_options:
            table.add_row(f"[{key}]", option, desc)
        
        panel = Panel(
            table,
            title=f"[bold]{i18n.t('main_menu_title')}[/bold]",
            border_style="bright_blue",
            padding=(1, 2)
        )
        
        self.console.print(panel)
        self.console.print()
        
        choice = Prompt.ask(i18n.t("select_option"), choices=["1", "2", "3", "4", "5", "6", "7", "q", "Q"], default="1")
        return choice.upper()
    
    def show_text_to_image_menu(self) -> str:
        """Show text-to-image theme selection menu."""
        themes = [
            ("1", i18n.t("text_to_image_photorealistic"), i18n.t("text_to_image_photorealistic_desc")),
            ("2", i18n.t("text_to_image_stylized"), i18n.t("text_to_image_stylized_desc")),
            ("3", i18n.t("text_to_image_text_in_images"), i18n.t("text_to_image_text_in_images_desc")),
            ("4", i18n.t("text_to_image_product_mockup"), i18n.t("text_to_image_product_mockup_desc")),
            ("5", i18n.t("text_to_image_minimalist"), i18n.t("text_to_image_minimalist_desc")),
            ("6", i18n.t("text_to_image_sequential_art"), i18n.t("text_to_image_sequential_art_desc")),
            ("B", i18n.t("back_to_main"), i18n.t("back_to_main_desc"))
        ]
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", style="bold cyan", width=3)
        table.add_column("Theme", style="bold white", width=40)
        table.add_column("Description", style="dim", width=25)
        
        for key, theme, desc in themes:
            table.add_row(f"[{key}]", theme, desc)
        
        panel = Panel(
            table,
            title=f"[bold]{i18n.t('text_to_image_title')}[/bold]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        self.console.print(panel)
        self.console.print()
        
        choice = Prompt.ask(i18n.t("select_theme"), choices=["1", "2", "3", "4", "5", "6", "b", "B"], default="1")
        return choice.upper()
    
    def show_image_editing_menu(self) -> str:
        """Show image editing feature selection menu."""
        features = [
            ("1", i18n.t("image_editing_add_remove"), i18n.t("image_editing_add_remove_desc")),
            ("2", i18n.t("image_editing_inpainting"), i18n.t("image_editing_inpainting_desc")),
            ("3", i18n.t("image_editing_style_transfer"), i18n.t("image_editing_style_transfer_desc")),
            ("4", i18n.t("image_editing_composition"), i18n.t("image_editing_composition_desc")),
            ("5", i18n.t("image_editing_detail_preservation"), i18n.t("image_editing_detail_preservation_desc")),
            ("B", i18n.t("back_to_main"), i18n.t("back_to_main_desc"))
        ]
        
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", style="bold cyan", width=3)
        table.add_column("Feature", style="bold white", width=35)
        table.add_column("Description", style="dim", width=30)
        
        for key, feature, desc in features:
            table.add_row(f"[{key}]", feature, desc)
        
        panel = Panel(
            table,
            title=f"[bold]{i18n.t('image_editing_title')}[/bold]",
            border_style="bright_yellow",
            padding=(1, 2)
        )
        
        self.console.print(panel)
        self.console.print()
        
        choice = Prompt.ask(i18n.t("select_feature"), choices=["1", "2", "3", "4", "5", "b", "B"], default="1")
        return choice.upper()
    
    def show_template_guide(self, template: PromptTemplate):
        """Show template guide and help user fill parameters."""
        self.console.print(f"\n[bold green]📋 Template Guide: {template.name}[/bold green]")
        self.console.print(f"[dim]{template.description}[/dim]\n")
        
        # Show template structure
        template_panel = Panel(
            Syntax(template.template, "text", theme="monokai", line_numbers=False),
            title="Template Structure",
            border_style="blue"
        )
        self.console.print(template_panel)
        
        # Show example
        example_panel = Panel(
            template.example,
            title="Example Output",
            border_style="green"
        )
        self.console.print(example_panel)
        self.console.print()
    
    def get_template_parameters(self, template: PromptTemplate) -> Dict[str, str]:
        """Get parameters from user to fill template."""
        parameters = {}
        
        self.console.print("[bold cyan]📝 Fill Template Parameters[/bold cyan]\n")
        
        for param in template.parameters:
            prompt_text = f"[bold]{param.name}[/bold]"
            if param.description:
                prompt_text += f" ([dim]{param.description}[/dim])"
            
            prompt_text += f"\nExample: [green]{param.example}[/green]"
            
            if param.required:
                value = Prompt.ask(prompt_text)
                while not value.strip():
                    self.console.print("[red]This parameter is required.[/red]")
                    value = Prompt.ask(prompt_text)
            else:
                value = Prompt.ask(prompt_text, default=param.example)
            
            parameters[param.name] = value
            self.console.print()
        
        return parameters
    
    def get_custom_prompt(self, mode: str = "text-to-image") -> str:
        """Get custom prompt from user."""
        self.console.print(f"[bold cyan]✍️  Custom {mode.title()} Prompt[/bold cyan]\n")
        
        prompt = ""
        self.console.print("Enter your prompt (press Enter twice to finish):")
        
        while True:
            line = input()
            if line == "" and prompt:
                break
            prompt += line + "\n" if line else "\n"
        
        return prompt.strip()
    
    def select_resolution(self) -> str:
        """Let user select image resolution."""
        resolutions = list(config.RESOLUTION_PRESETS.keys())
        
        # Create columns for resolution display
        resolution_items = []
        for i, res in enumerate(resolutions):
            dimensions = config.RESOLUTION_PRESETS[res]
            item = f"[bold cyan][{i+1}][/bold cyan] {res}\n[dim]{dimensions}[/dim]"
            resolution_items.append(item)
        
        columns = Columns(resolution_items, equal=True, expand=True)
        
        panel = Panel(
            columns,
            title="[bold]📐 Select Resolution[/bold]",
            border_style="bright_cyan"
        )
        
        self.console.print(panel)
        self.console.print()
        
        choices = [str(i+1) for i in range(len(resolutions))]
        default_idx = resolutions.index(config.get("default_resolution", "square-medium")) + 1
        
        choice = Prompt.ask("Select resolution", choices=choices, default=str(default_idx))
        return resolutions[int(choice) - 1]
    
    def get_image_paths(self, max_images: int = 3, required: bool = True) -> List[str]:
        """Get image file paths from user."""
        images = []
        
        self.console.print(f"[bold cyan]📁 Select Images (max {max_images})[/bold cyan]\n")
        
        for i in range(max_images):
            if i == 0 and required:
                prompt_text = "Enter path to first image"
            else:
                prompt_text = f"Enter path to image {i+1} (or press Enter to skip)"
            
            path = Prompt.ask(prompt_text, default="" if i > 0 or not required else None)
            
            if not path:
                if i == 0 and required:
                    self.console.print("[red]At least one image is required.[/red]")
                    continue
                else:
                    break
            
            if not os.path.exists(path):
                self.console.print(f"[red]File not found: {path}[/red]")
                continue
            
            images.append(path)
            self.console.print(f"[green]✓ Added: {path}[/green]")
        
        return images
    
    def show_progress(self, message: str = "Generating..."):
        """Show progress spinner."""
        return Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True
        )
    
    def show_success(self, message: str, files: List[str] = None):
        """Show success message."""
        success_text = Text()
        success_text.append("✅ ", style="bold green")
        success_text.append(message, style="green")
        
        self.console.print(success_text)
        
        if files:
            self.console.print("\n[bold]Generated files:[/bold]")
            for file in files:
                self.console.print(f"  📄 {file}")
        
        self.console.print()
    
    def show_error(self, message: str, details: str = None):
        """Show error message."""
        error_text = Text()
        error_text.append("❌ ", style="bold red")
        error_text.append("Error: ", style="bold red")
        error_text.append(message, style="red")
        
        self.console.print(error_text)
        
        if details:
            self.console.print(f"[dim]Details: {details}[/dim]")
        
        self.console.print()
    
    def show_warning(self, message: str):
        """Show warning message."""
        warning_text = Text()
        warning_text.append("⚠️  ", style="bold yellow")
        warning_text.append("Warning: ", style="bold yellow")
        warning_text.append(message, style="yellow")
        
        self.console.print(warning_text)
        self.console.print()
    
    def show_info(self, message: str):
        """Show info message."""
        info_text = Text()
        info_text.append("ℹ️  ", style="bold blue")
        info_text.append(message, style="blue")
        
        self.console.print(info_text)
        self.console.print()
    
    def show_history(self, history: List[Dict[str, Any]]):
        """Show generation history."""
        if not history:
            self.show_info("No generation history found.")
            return
        
        table = Table(title="Generation History")
        table.add_column("Date", style="dim", width=20)
        table.add_column("Mode", style="cyan", width=15)
        table.add_column("Theme/Feature", style="green", width=20)
        table.add_column("Prompt", width=50)
        table.add_column("Files", style="yellow", width=15)
        
        for entry in history[:20]:  # Show last 20 entries
            timestamp = entry.get('timestamp', 'Unknown')
            if 'T' in timestamp:
                timestamp = timestamp.split('T')[0]  # Just date part
            
            mode = entry.get('mode', 'Unknown')
            theme = entry.get('theme_or_feature', 'Unknown')
            prompt = entry.get('prompt', '')[:45] + "..." if len(entry.get('prompt', '')) > 45 else entry.get('prompt', '')
            files = str(len(entry.get('generated_files', [])))
            
            table.add_row(timestamp, mode, theme, prompt, files)
        
        self.console.print(table)
        self.console.print()
    
    def show_settings(self):
        """Show current settings."""
        settings_table = Table(title="Current Settings")
        settings_table.add_column("Setting", style="cyan")
        settings_table.add_column("Value", style="green")
        settings_table.add_column("Description", style="dim")
        
        settings_info = [
            ("default_resolution", config.get("default_resolution"), "Default image resolution"),
            ("default_theme", config.get("default_theme"), "Default text-to-image theme"),
            ("save_history", config.get("save_history"), "Save generation history"),
            ("max_history_items", config.get("max_history_items"), "Maximum history entries"),
            ("auto_open_images", config.get("auto_open_images"), "Auto-open generated images")
        ]
        
        for setting, value, desc in settings_info:
            settings_table.add_row(setting, str(value), desc)
        
        self.console.print(settings_table)
        self.console.print()
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def pause(self, message: str = None):
        """Pause and wait for user input."""
        if message is None:
            message = i18n.t("press_enter")
        input(f"\n{message}")
    
    def show_language_menu(self) -> str:
        """Show language selection menu."""
        languages = i18n.get_available_languages()
        current_lang = i18n.get_language()
        
        language_options = []
        choices = []
        
        for i, (lang, display_name) in enumerate(languages.items(), 1):
            key = str(i)
            marker = "✓" if lang == current_lang else " "
            option = f"{marker} {display_name}"
            desc = i18n.t("current_language") if lang == current_lang else ""
            
            language_options.append((key, option, desc))
            choices.append(key)
        
        language_options.append(("B", i18n.t("back_to_main"), i18n.t("back_to_main_desc")))
        choices.extend(["b", "B"])
        
        # Create table
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", style="bold cyan", width=3)
        table.add_column("Language", style="bold white", width=20)
        table.add_column("Status", style="green", width=15)
        
        for key, option, desc in language_options:
            table.add_row(f"[{key}]", option, desc)
        
        panel = Panel(
            table,
            title=f"[bold]{i18n.t('language_selection_title')}[/bold]",
            border_style="bright_green",
            padding=(1, 2)
        )
        
        self.console.print(panel)
        self.console.print()
        
        choice = Prompt.ask(i18n.t("select_language"), choices=choices, default="1")
        return choice.upper()
    
    def switch_language(self, language: Language):
        """Switch to a different language."""
        i18n.set_language(language)
        # Update config to save language preference
        from .config import config
        config.set("language", language.value)

# Global UI instance
ui = NanoBananaUI()