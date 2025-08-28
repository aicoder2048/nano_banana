"""User interface components for NanoBanana Pro using Rich."""

import os
import glob
from pathlib import Path
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
from .enhanced_image_browser import create_enhanced_browser
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
        
        # Show template structure with proper text wrapping
        from rich.text import Text
        template_text = Text(template.template)
        template_panel = Panel(
            template_text,
            title="Template Structure",
            border_style="blue",
            expand=False,
            padding=(1, 2)
        )
        self.console.print(template_panel)
        
        # Show example with proper text wrapping
        example_text = Text(template.example)
        example_panel = Panel(
            example_text,
            title="Example Output",
            border_style="green",
            expand=False,
            padding=(1, 2)
        )
        self.console.print(example_panel)
        self.console.print()
    
    def get_template_parameters(self, template: PromptTemplate) -> Dict[str, str]:
        """Get parameters from user to fill template (legacy method, uses detailed mode)."""
        return self.get_template_parameters_detailed(template)
    
    def get_template_parameters_quick(self, template: PromptTemplate) -> Dict[str, str]:
        """Get only essential parameters from user."""
        parameters = {}
        
        # Get essential parameters only
        essential_params = [p for p in template.parameters if p.level == "essential" or p.required]
        
        if not essential_params:
            self.console.print("[yellow]No essential parameters found. Using all parameters.[/yellow]")
            return self.get_template_parameters_detailed(template)
        
        self.console.print(f"[bold cyan]⚡ Quick Mode - {len(essential_params)} Essential Parameters[/bold cyan]\n")
        
        for param in essential_params:
            prompt_text = f"[bold]{param.name}[/bold]"
            if param.description:
                prompt_text += f" ([dim]{param.description}[/dim])"
            
            prompt_text += f"\nExample: [green]{param.example}[/green]"
            
            # Show suggestions if available
            if param.suggestions:
                prompt_text += f"\nSuggestions: [blue]{', '.join(param.suggestions[:3])}...[/blue]"
            
            if param.required:
                value = Prompt.ask(prompt_text)
                while not value.strip():
                    self.console.print("[red]This parameter is required.[/red]")
                    value = Prompt.ask(prompt_text)
            else:
                value = Prompt.ask(prompt_text, default=param.default or param.example)
            
            parameters[param.name] = value
            self.console.print()
        
        # Fill non-essential parameters with defaults
        for param in template.parameters:
            if param.name not in parameters:
                parameters[param.name] = param.default or param.example
        
        return parameters
    
    def get_template_parameters_detailed(self, template: PromptTemplate) -> Dict[str, str]:
        """Get all parameters from user with full interface."""
        parameters = {}
        
        self.console.print(f"[bold cyan]🔍 Detailed Mode - All {len(template.parameters)} Parameters[/bold cyan]\n")
        
        for param in template.parameters:
            # Show parameter level
            level_color = {"essential": "red", "optional": "yellow", "advanced": "blue"}.get(param.level, "white")
            level_badge = f"[{level_color}]({param.level.upper()})[/{level_color}]"
            
            prompt_text = f"{level_badge} [bold]{param.name}[/bold]"
            if param.description:
                prompt_text += f" ([dim]{param.description}[/dim])"
            
            prompt_text += f"\nExample: [green]{param.example}[/green]"
            
            # Show suggestions
            if param.suggestions:
                prompt_text += f"\nSuggestions: [blue]{', '.join(param.suggestions[:5])}[/blue]"
            
            if param.required:
                value = Prompt.ask(prompt_text)
                while not value.strip():
                    self.console.print("[red]This parameter is required.[/red]")
                    value = Prompt.ask(prompt_text)
            else:
                default_value = param.default or param.example
                value = Prompt.ask(prompt_text, default=default_value)
            
            parameters[param.name] = value
            self.console.print()
        
        return parameters
    
    def get_template_parameters_custom(self, template: PromptTemplate) -> Dict[str, str]:
        """Let user choose which parameters to customize."""
        parameters = {}
        
        self.console.print(f"[bold cyan]🎯 Custom Mode - Choose Parameters to Fill[/bold cyan]\n")
        
        # Show all parameters with levels
        self.console.print("Available parameters:")
        for i, param in enumerate(template.parameters, 1):
            level_color = {"essential": "red", "optional": "yellow", "advanced": "blue"}.get(param.level, "white")
            required_mark = " [red]*[/red]" if param.required else ""
            self.console.print(f"  [{level_color}]{i:2d}[/{level_color}]. {param.name}{required_mark} - {param.description}")
        
        self.console.print(f"\n[dim]* = required parameter[/dim]")
        self.console.print("[dim]Enter parameter numbers separated by commas (e.g., 1,3,5)[/dim]")
        self.console.print("[dim]Or press Enter to fill only essential/required parameters[/dim]\n")
        
        # Get user choice
        choice = self.console.input("Select parameters to fill: ").strip()
        
        if choice:
            try:
                selected_indices = [int(x.strip()) - 1 for x in choice.split(",")]
                selected_params = [template.parameters[i] for i in selected_indices 
                                if 0 <= i < len(template.parameters)]
            except (ValueError, IndexError):
                self.console.print("[yellow]Invalid selection. Using essential/required parameters only.[/yellow]")
                selected_params = [p for p in template.parameters if p.level == "essential" or p.required]
        else:
            # Default to essential/required parameters
            selected_params = [p for p in template.parameters if p.level == "essential" or p.required]
        
        if not selected_params:
            selected_params = template.parameters  # Fallback to all parameters
        
        self.console.print(f"\nFilling {len(selected_params)} selected parameters:\n")
        
        # Fill selected parameters
        for param in selected_params:
            level_color = {"essential": "red", "optional": "yellow", "advanced": "blue"}.get(param.level, "white")
            level_badge = f"[{level_color}]({param.level.upper()})[/{level_color}]"
            
            prompt_text = f"{level_badge} [bold]{param.name}[/bold]"
            if param.description:
                prompt_text += f" ([dim]{param.description}[/dim])"
            
            prompt_text += f"\nExample: [green]{param.example}[/green]"
            
            if param.suggestions:
                prompt_text += f"\nSuggestions: [blue]{', '.join(param.suggestions[:5])}[/blue]"
            
            if param.required:
                value = Prompt.ask(prompt_text)
                while not value.strip():
                    self.console.print("[red]This parameter is required.[/red]")
                    value = Prompt.ask(prompt_text)
            else:
                default_value = param.default or param.example
                value = Prompt.ask(prompt_text, default=default_value)
            
            parameters[param.name] = value
            self.console.print()
        
        # Fill unselected parameters with defaults
        for param in template.parameters:
            if param.name not in parameters:
                parameters[param.name] = param.default or param.example
        
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
    
    def _scan_for_images(self, directory: str = ".", recursive: bool = True) -> List[str]:
        """Scan directory for image files."""
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.webp'}
        images = []
        
        try:
            if recursive:
                # Search current directory and subdirectories
                for ext in image_extensions:
                    pattern = os.path.join(directory, "**", f"*{ext}")
                    images.extend(glob.glob(pattern, recursive=True))
                    pattern = os.path.join(directory, "**", f"*{ext.upper()}")
                    images.extend(glob.glob(pattern, recursive=True))
            else:
                # Search only current directory
                for ext in image_extensions:
                    pattern = os.path.join(directory, f"*{ext}")
                    images.extend(glob.glob(pattern))
                    pattern = os.path.join(directory, f"*{ext.upper()}")
                    images.extend(glob.glob(pattern))
            
            # Remove duplicates and sort
            images = sorted(list(set(images)))
            
            # Convert to relative paths for better display
            current_dir = os.getcwd()
            relative_images = []
            for img in images:
                try:
                    rel_path = os.path.relpath(img, current_dir)
                    if len(rel_path) < len(img):
                        relative_images.append(rel_path)
                    else:
                        relative_images.append(img)
                except ValueError:
                    # Can't make relative path, use absolute
                    relative_images.append(img)
            
            return relative_images[:50]  # Limit to 50 images for performance
            
        except Exception as e:
            self.console.print(f"[red]Error scanning for images: {e}[/red]")
            return []
    
    def _show_image_selection_menu(self, images: List[str], title: str = "Select Image") -> Optional[str]:
        """Show interactive menu to select an image."""
        if not images:
            self.console.print("[yellow]No images found in current directory and subdirectories.[/yellow]")
            return None
        
        self.console.print(f"\n[bold cyan]📸 {title}[/bold cyan]")
        self.console.print(f"[dim]Found {len(images)} image(s) in current directory and subdirectories[/dim]\n")
        
        # Show images in a table format
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("#", style="bold green", width=4)
        table.add_column("Image Path", style="white")
        table.add_column("Size", style="dim", width=10)
        
        # Add images to table (show first 20, then paginate if needed)
        display_images = images[:20]
        for i, img_path in enumerate(display_images, 1):
            try:
                # Get file size
                size = os.path.getsize(img_path)
                size_str = self._format_file_size(size)
            except:
                size_str = "Unknown"
            
            # Truncate long paths for display
            display_path = img_path
            if len(display_path) > 60:
                display_path = "..." + display_path[-57:]
            
            table.add_row(str(i), display_path, size_str)
        
        if len(images) > 20:
            table.add_row("...", f"[dim](and {len(images) - 20} more)[/dim]", "")
        
        self.console.print(table)
        
        # Show options
        self.console.print(f"\n[bold]Options:[/bold]")
        self.console.print(f"[green]1-{min(20, len(images))}[/green]: Select image by number")
        if len(images) > 20:
            self.console.print("[yellow]'more'[/yellow]: Show all images")
        self.console.print("[yellow]'manual'[/yellow]: Enter path manually")
        self.console.print("[yellow]'scan'[/yellow]: Scan different directory")
        self.console.print("[red]'skip'[/red]: Skip this image")
        
        while True:
            choice = self.console.input("\nSelect option: ").strip().lower()
            
            if choice == 'skip':
                return None
            elif choice == 'manual':
                return self._get_manual_image_path()
            elif choice == 'scan':
                return self._scan_different_directory()
            elif choice == 'more' and len(images) > 20:
                return self._show_all_images_menu(images, title)
            else:
                # Try to parse as number
                try:
                    choice_num = int(choice)
                    if 1 <= choice_num <= min(20, len(images)):
                        selected_path = images[choice_num - 1]
                        if os.path.exists(selected_path):
                            return selected_path
                        else:
                            self.console.print(f"[red]File no longer exists: {selected_path}[/red]")
                            continue
                    else:
                        self.console.print(f"[red]Please enter a number between 1 and {min(20, len(images))}[/red]")
                        continue
                except ValueError:
                    self.console.print("[red]Invalid choice. Please try again.[/red]")
                    continue
    
    def _show_all_images_menu(self, images: List[str], title: str) -> Optional[str]:
        """Show all images with pagination."""
        page_size = 20
        total_pages = (len(images) + page_size - 1) // page_size
        current_page = 0
        
        while True:
            start_idx = current_page * page_size
            end_idx = min(start_idx + page_size, len(images))
            page_images = images[start_idx:end_idx]
            
            self.console.clear()
            self.console.print(f"\n[bold cyan]📸 {title} - Page {current_page + 1}/{total_pages}[/bold cyan]")
            
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("#", style="bold green", width=4)
            table.add_column("Image Path", style="white")
            table.add_column("Size", style="dim", width=10)
            
            for i, img_path in enumerate(page_images, start_idx + 1):
                try:
                    size = os.path.getsize(img_path)
                    size_str = self._format_file_size(size)
                except:
                    size_str = "Unknown"
                
                display_path = img_path
                if len(display_path) > 60:
                    display_path = "..." + display_path[-57:]
                
                table.add_row(str(i), display_path, size_str)
            
            self.console.print(table)
            
            # Navigation options
            options = []
            options.append(f"[green]{start_idx + 1}-{end_idx}[/green]: Select image")
            if current_page > 0:
                options.append("[yellow]'prev'[/yellow]: Previous page")
            if current_page < total_pages - 1:
                options.append("[yellow]'next'[/yellow]: Next page")
            options.append("[yellow]'manual'[/yellow]: Enter path manually")
            options.append("[red]'back'[/red]: Go back")
            
            self.console.print(f"\n[bold]Options:[/bold] {' | '.join(options)}")
            
            choice = self.console.input("\nSelect option: ").strip().lower()
            
            if choice == 'back':
                return None
            elif choice == 'prev' and current_page > 0:
                current_page -= 1
            elif choice == 'next' and current_page < total_pages - 1:
                current_page += 1
            elif choice == 'manual':
                return self._get_manual_image_path()
            else:
                try:
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(images):
                        selected_path = images[choice_num - 1]
                        if os.path.exists(selected_path):
                            return selected_path
                        else:
                            self.console.print(f"[red]File no longer exists: {selected_path}[/red]")
                            self.console.input("Press Enter to continue...")
                    else:
                        self.console.print(f"[red]Please enter a number between 1 and {len(images)}[/red]")
                        self.console.input("Press Enter to continue...")
                except ValueError:
                    self.console.print("[red]Invalid choice. Please try again.[/red]")
                    self.console.input("Press Enter to continue...")
    
    def _get_manual_image_path(self) -> Optional[str]:
        """Get image path manually from user input."""
        self.console.print("\n[bold cyan]📝 Manual Path Entry[/bold cyan]")
        self.console.print("[dim]Tip: You can drag and drop files into the terminal on most systems[/dim]")
        
        path = Prompt.ask("Enter image path").strip()
        
        if not path:
            return None
        
        # Clean up the path (remove quotes if present)
        path = path.strip('\'"')
        
        if os.path.exists(path):
            return path
        else:
            self.console.print(f"[red]File not found: {path}[/red]")
            return None
    
    def _scan_different_directory(self) -> Optional[str]:
        """Scan a different directory for images."""
        self.console.print("\n[bold cyan]📁 Scan Different Directory[/bold cyan]")
        directory = Prompt.ask("Enter directory path", default=".")
        
        if not os.path.isdir(directory):
            self.console.print(f"[red]Directory not found: {directory}[/red]")
            return None
        
        images = self._scan_for_images(directory)
        if images:
            return self._show_image_selection_menu(images, f"Select from {directory}")
        else:
            self.console.print(f"[yellow]No images found in {directory}[/yellow]")
            return None
    
    def _format_file_size(self, size_bytes: int) -> str:
        """Format file size in human readable format."""
        if size_bytes < 1024:
            return f"{size_bytes}B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f}KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f}MB"
    
    def get_image_paths(self, max_images: int = 3, required: bool = True) -> List[str]:
        """Get image file paths from user with enhanced interactive browser."""
        self.console.print(f"[bold cyan]🖼️  图片选择器[/bold cyan]")
        self.console.print(f"[dim]多列布局 • 目录导航 • 批量选择 (最多 {max_images} 张)[/dim]\\n")
        
        # 询问用户选择方式
        self.console.print("[bold]选择方式:[/bold]")
        self.console.print("[green]1.[/green] 🚀 增强版浏览器 (推荐) - 多列布局、目录导航")
        self.console.print("[green]2.[/green] 📝 手动输入路径")
        
        method = Prompt.ask("选择方式", choices=["1", "2"], default="1")
        
        if method == "1":
            # 使用增强版浏览器
            try:
                browser = create_enhanced_browser(self.console)
                selected_paths = browser.browse_and_select_images(max_images=max_images)
                
                if selected_paths:
                    self.console.print(f"\\n[bold green]✅ 已选择 {len(selected_paths)} 张图片:[/bold green]")
                    for i, path in enumerate(selected_paths, 1):
                        self.console.print(f"  {i}. [blue]{os.path.basename(path)}[/blue]")
                    return selected_paths
                elif required:
                    self.console.print("[red]需要至少选择一张图片[/red]")
                    # 回退到手动输入
                    return self._get_manual_image_paths_fallback(max_images)
                else:
                    return []
                    
            except Exception as e:
                self.console.print(f"[red]浏览器错误: {e}[/red]")
                self.console.print("[yellow]回退到手动输入模式[/yellow]")
                return self._get_manual_image_paths_fallback(max_images)
        else:
            # 手动输入路径
            return self._get_manual_image_paths_fallback(max_images)
    
    def _get_manual_image_paths_fallback(self, max_images: int) -> List[str]:
        """手动输入图片路径的后备方法"""
        images = []
        
        self.console.print(f"\\n[bold yellow]📝 手动输入图片路径 (最多 {max_images} 张)[/bold yellow]")
        
        for i in range(max_images):
            while True:
                if i == 0:
                    prompt = "请输入第一张图片路径"
                else:
                    prompt = f"请输入第 {i+1} 张图片路径 (直接回车跳过)"
                
                path = self.console.input(f"{prompt}: ").strip()
                
                if not path:
                    if i == 0:
                        self.console.print("[red]至少需要输入一张图片路径[/red]")
                        continue
                    else:
                        break  # 跳过后续图片
                
                # 展开用户路径
                expanded_path = os.path.expanduser(path)
                
                if not os.path.exists(expanded_path):
                    self.console.print(f"[red]文件不存在: {path}[/red]")
                    continue
                
                if not os.path.isfile(expanded_path):
                    self.console.print(f"[red]不是有效的文件: {path}[/red]")
                    continue
                
                # 检查文件扩展名
                ext = os.path.splitext(expanded_path)[1].lower()
                supported_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.webp'}
                if ext not in supported_formats:
                    self.console.print(f"[yellow]警告: 可能不支持的图片格式: {ext}[/yellow]")
                    if not Confirm.ask("继续使用此文件?", default=False):
                        continue
                
                if expanded_path in images:
                    self.console.print(f"[yellow]图片已选择: {path}[/yellow]")
                    continue
                
                images.append(expanded_path)
                self.console.print(f"[green]✓ 已添加: {os.path.basename(expanded_path)}[/green]")
                break
        
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