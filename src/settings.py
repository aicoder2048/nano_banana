"""Settings management for NanoBanana Pro."""

from typing import Dict, Any
from .ui import ui
from .config import config

class SettingsManager:
    """Manages application settings and preferences."""
    
    def __init__(self):
        pass
    
    def run(self):
        """Run settings management interface."""
        while True:
            choice = self._show_settings_menu()
            
            if choice == "1":
                self._change_default_resolution()
            elif choice == "2":
                self._change_default_theme()
            elif choice == "3":
                self._toggle_save_history()
            elif choice == "4":
                self._change_max_history()
            elif choice == "5":
                self._toggle_auto_open()
            elif choice == "6":
                self._view_current_settings()
            elif choice == "7":
                self._clear_history()
            elif choice == "8":
                self._export_settings()
            elif choice == "9":
                self._import_settings()
            elif choice.upper() == "B":
                break
            else:
                ui.show_error("Invalid selection")
    
    def _show_settings_menu(self) -> str:
        """Show settings menu."""
        menu_options = [
            ("1", "🖼️  Change Default Resolution", "Set default image resolution"),
            ("2", "🎨  Change Default Theme", "Set default text-to-image theme"),
            ("3", "📝  Toggle History Saving", "Enable/disable generation history"),
            ("4", "📊  Change Max History Items", "Set maximum history entries"),
            ("5", "👀  Toggle Auto-Open Images", "Enable/disable auto-opening images"),
            ("6", "⚙️  View Current Settings", "Display all current settings"),
            ("7", "🗑️  Clear History", "Delete all generation history"),
            ("8", "📤  Export Settings", "Export settings to file"),
            ("9", "📥  Import Settings", "Import settings from file"),
            ("B", "🔙  Back to Main Menu", "Return to main menu")
        ]
        
        from rich.table import Table
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", style="bold cyan", width=3)
        table.add_column("Option", style="bold white", width=35)
        table.add_column("Description", style="dim", width=30)
        
        for key, option, desc in menu_options:
            table.add_row(f"[{key}]", option, desc)
        
        from rich.panel import Panel
        panel = Panel(
            table,
            title="[bold]⚙️ Settings & Configuration[/bold]",
            border_style="bright_magenta",
            padding=(1, 2)
        )
        
        ui.console.print(panel)
        ui.console.print()
        
        from rich.prompt import Prompt
        choice = Prompt.ask("Select an option", 
                           choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "b", "B"], 
                           default="6")
        return choice
    
    def _change_default_resolution(self):
        """Change default resolution setting."""
        ui.console.print("\n[bold cyan]🖼️  Change Default Resolution[/bold cyan]\n")
        
        current = config.get("default_resolution")
        ui.console.print(f"Current default: [green]{current}[/green]")
        
        # Show resolution options
        resolutions = list(config.RESOLUTION_PRESETS.keys())
        
        from rich.columns import Columns
        resolution_items = []
        for i, res in enumerate(resolutions):
            dimensions = config.RESOLUTION_PRESETS[res]
            marker = "[green]✓[/green]" if res == current else " "
            item = f"{marker} [{i+1}] {res}\n[dim]{dimensions}[/dim]"
            resolution_items.append(item)
        
        columns = Columns(resolution_items, equal=True, expand=True)
        ui.console.print(columns)
        ui.console.print()
        
        choices = [str(i+1) for i in range(len(resolutions))]
        current_idx = resolutions.index(current) + 1
        
        from rich.prompt import Prompt
        choice = Prompt.ask("Select new default resolution", 
                           choices=choices, 
                           default=str(current_idx))
        
        new_resolution = resolutions[int(choice) - 1]
        config.set("default_resolution", new_resolution)
        
        ui.show_success(f"Default resolution changed to: {new_resolution}")
        ui.pause()
    
    def _change_default_theme(self):
        """Change default theme setting."""
        ui.console.print("\n[bold cyan]🎨  Change Default Theme[/bold cyan]\n")
        
        current = config.get("default_theme")
        ui.console.print(f"Current default: [green]{current}[/green]\n")
        
        themes = {
            "photorealistic": "📸  Photorealistic Scenes",
            "stylized": "🎨  Stylized Illustrations & Stickers", 
            "text_in_images": "📝  Accurate Text in Images",
            "product_mockup": "📦  Product Mockups & Commercial Photography",
            "minimalist": "⚪  Minimalist & Negative Space Design",
            "sequential_art": "📚  Sequential Art (Comic/Storyboard)"
        }
        
        from rich.table import Table
        table = Table(show_header=False, box=None)
        table.add_column("Key", style="bold cyan", width=3)
        table.add_column("Theme", style="bold white", width=40)
        table.add_column("Current", style="green", width=8)
        
        theme_keys = list(themes.keys())
        for i, (key, name) in enumerate(themes.items(), 1):
            marker = "✓" if key == current else ""
            table.add_row(f"[{i}]", name, marker)
        
        ui.console.print(table)
        ui.console.print()
        
        choices = [str(i+1) for i in range(len(themes))]
        current_idx = theme_keys.index(current) + 1 if current in theme_keys else 1
        
        from rich.prompt import Prompt
        choice = Prompt.ask("Select new default theme", 
                           choices=choices, 
                           default=str(current_idx))
        
        new_theme = theme_keys[int(choice) - 1]
        config.set("default_theme", new_theme)
        
        ui.show_success(f"Default theme changed to: {themes[new_theme]}")
        ui.pause()
    
    def _toggle_save_history(self):
        """Toggle history saving setting."""
        current = config.get("save_history", True)
        new_value = not current
        
        config.set("save_history", new_value)
        
        status = "enabled" if new_value else "disabled"
        ui.show_success(f"History saving {status}")
        ui.pause()
    
    def _change_max_history(self):
        """Change maximum history items setting."""
        current = config.get("max_history_items", 100)
        ui.console.print(f"\nCurrent maximum history items: [green]{current}[/green]")
        
        from rich.prompt import IntPrompt
        new_value = IntPrompt.ask("Enter new maximum (1-1000)", 
                                 default=current, 
                                 show_default=True)
        
        if 1 <= new_value <= 1000:
            config.set("max_history_items", new_value)
            ui.show_success(f"Maximum history items changed to: {new_value}")
        else:
            ui.show_error("Value must be between 1 and 1000")
        
        ui.pause()
    
    def _toggle_auto_open(self):
        """Toggle auto-open images setting."""
        current = config.get("auto_open_images", False)
        new_value = not current
        
        config.set("auto_open_images", new_value)
        
        status = "enabled" if new_value else "disabled"
        ui.show_success(f"Auto-open images {status}")
        ui.pause()
    
    def _view_current_settings(self):
        """Display current settings."""
        ui.console.print("\n[bold cyan]⚙️  Current Settings[/bold cyan]\n")
        ui.show_settings()
        ui.pause()
    
    def _clear_history(self):
        """Clear all generation history."""
        from rich.prompt import Confirm
        if Confirm.ask("Are you sure you want to clear all history?", default=False):
            config.clear_history()
            ui.show_success("History cleared successfully")
        else:
            ui.show_info("History not cleared")
        
        ui.pause()
    
    def _export_settings(self):
        """Export settings to file."""
        import json
        from pathlib import Path
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_file = f"nanobanana_settings_{timestamp}.json"
        
        try:
            export_data = {
                "version": "2.0",
                "exported_at": datetime.now().isoformat(),
                "settings": config.settings
            }
            
            with open(export_file, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            ui.show_success(f"Settings exported to: {export_file}")
        except Exception as e:
            ui.show_error("Export failed", str(e))
        
        ui.pause()
    
    def _import_settings(self):
        """Import settings from file."""
        import json
        from rich.prompt import Prompt
        
        ui.console.print("\nEnter path to settings file:")
        file_path = Prompt.ask("File path")
        
        try:
            with open(file_path, 'r') as f:
                import_data = json.load(f)
            
            if 'settings' in import_data:
                # Merge imported settings with current settings
                for key, value in import_data['settings'].items():
                    config.set(key, value)
                
                ui.show_success("Settings imported successfully")
            else:
                ui.show_error("Invalid settings file format")
        
        except FileNotFoundError:
            ui.show_error("File not found", file_path)
        except json.JSONDecodeError:
            ui.show_error("Invalid JSON file")
        except Exception as e:
            ui.show_error("Import failed", str(e))
        
        ui.pause()

# Global instance
settings_manager = SettingsManager()