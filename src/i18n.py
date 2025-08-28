"""
Internationalization (i18n) support for NanoBanana Pro.
Supports English and Chinese languages.
"""

import os
from typing import Dict, Any
from enum import Enum

class Language(Enum):
    """Supported languages."""
    ENGLISH = "en"
    CHINESE = "zh"

class I18n:
    """Internationalization manager."""
    
    def __init__(self):
        self.current_language = Language.CHINESE
        self.translations = self._load_translations()
    
    def _load_translations(self) -> Dict[Language, Dict[str, str]]:
        """Load translation dictionaries."""
        return {
            Language.ENGLISH: {
                # Application Title
                "app_title": "🎨 NanoBanana Pro - AI Image Generation Studio",
                "app_subtitle": "═══════════════════════════════════════════════",
                "version_info": "Version: {version} | Model: {model} | Images: {images_dir}/",
                
                # Main Menu
                "main_menu_title": "Main Menu",
                "main_menu_text_to_image": "🖼️  Text-to-Image Generation",
                "main_menu_text_to_image_desc": "Create images from text prompts",
                "main_menu_image_editing": "🎭  Image Editing & Enhancement",
                "main_menu_image_editing_desc": "Edit existing images",
                "main_menu_chat_image": "💬  Chat-Image (Conversational)",
                "main_menu_chat_image_desc": "Interactive image refinement",
                "main_menu_settings": "⚙️  Settings & Configuration",
                "main_menu_settings_desc": "Manage preferences",
                "main_menu_history": "📊  View Generation History",
                "main_menu_history_desc": "See previous generations",
                "main_menu_help": "❓  Help & Templates",
                "main_menu_help_desc": "View templates and help",
                "main_menu_quit": "🚪  Quit",
                "main_menu_quit_desc": "Exit the application",
                "main_menu_language": "🌐  Language / 语言",
                "main_menu_language_desc": "Switch language",
                "select_option": "Select an option",
                
                # Text-to-Image Menu
                "text_to_image_title": "🖼️ Text-to-Image Generation Modes",
                "text_to_image_photorealistic": "📸  Photorealistic Scenes",
                "text_to_image_photorealistic_desc": "Professional photography",
                "text_to_image_stylized": "🎨  Stylized Illustrations & Stickers",
                "text_to_image_stylized_desc": "Vector graphics and logos",
                "text_to_image_text_in_images": "📝  Accurate Text in Images",
                "text_to_image_text_in_images_desc": "Logos and signage",
                "text_to_image_product_mockup": "📦  Product Mockups & Commercial Photography",
                "text_to_image_product_mockup_desc": "E-commerce imagery",
                "text_to_image_minimalist": "⚪  Minimalist & Negative Space Design",
                "text_to_image_minimalist_desc": "Clean, spacious designs",
                "text_to_image_sequential_art": "📚  Sequential Art (Comic/Storyboard)",
                "text_to_image_sequential_art_desc": "Comic panels and storytelling",
                "back_to_main": "🔙  Back to Main Menu",
                "back_to_main_desc": "Return to previous menu",
                "select_theme": "Select a theme",
                
                # Image Editing Menu  
                "image_editing_title": "🎭 Image Editing & Enhancement",
                "image_editing_add_remove": "➕  Adding and Removing Elements",
                "image_editing_add_remove_desc": "Add/remove objects from images",
                "image_editing_inpainting": "🎯  Inpainting (Semantic Masking)",
                "image_editing_inpainting_desc": "Edit specific parts only",
                "image_editing_style_transfer": "🎭  Style Transfer",
                "image_editing_style_transfer_desc": "Apply artistic styles",
                "image_editing_composition": "🖼️  Advanced Composition",
                "image_editing_composition_desc": "Combine multiple images",
                "image_editing_detail_preservation": "🔍  High-Fidelity Detail Preservation",
                "image_editing_detail_preservation_desc": "Precise editing with detail protection",
                "select_feature": "Select a feature",
                
                # Settings Menu
                "settings_title": "⚙️ Settings & Configuration",
                "settings_default_resolution": "🖼️  Change Default Resolution",
                "settings_default_resolution_desc": "Set default image resolution",
                "settings_default_theme": "🎨  Change Default Theme",
                "settings_default_theme_desc": "Set default text-to-image theme",
                "settings_toggle_history": "📝  Toggle History Saving",
                "settings_toggle_history_desc": "Enable/disable generation history",
                "settings_max_history": "📊  Change Max History Items",
                "settings_max_history_desc": "Set maximum history entries",
                "settings_toggle_auto_open": "👀  Toggle Auto-Open Images",
                "settings_toggle_auto_open_desc": "Enable/disable auto-opening images",
                "settings_view_current": "⚙️  View Current Settings",
                "settings_view_current_desc": "Display all current settings",
                "settings_clear_history": "🗑️  Clear History",
                "settings_clear_history_desc": "Delete all generation history",
                "settings_export": "📤  Export Settings",
                "settings_export_desc": "Export settings to file",
                "settings_import": "📥  Import Settings",
                "settings_import_desc": "Import settings from file",
                
                # Help Menu
                "help_title": "❓ Help & Templates",
                "help_text_templates": "📋  View Text-to-Image Templates",
                "help_text_templates_desc": "See all available templates",
                "help_editing_templates": "🎭  View Image Editing Templates", 
                "help_editing_templates_desc": "See editing templates",
                "help_best_practices": "💡  Best Practices Guide",
                "help_best_practices_desc": "Tips for better prompts",
                "help_api_docs": "🔗  API Documentation",
                "help_api_docs_desc": "Gemini API reference",
                "help_shortcuts": "❓  Keyboard Shortcuts",
                "help_shortcuts_desc": "Quick reference",
                
                # Common Actions
                "use_template_guide": "Use template guide? [Y/n]",
                "use_this_template": "Use this template? [Y/n]",
                "generate_image": "Generate image? [Y/n]",
                "edit_images": "Edit images? [Y/n]",
                "open_images": "Open generated images? [Y/n]",
                "save_images": "Save images now? [Y/n]",
                "specify_resolution": "Specify output resolution? [y/N]",
                "confirm_quit": "Are you sure you want to quit?",
                "press_enter": "Press Enter to continue...",
                
                # Status Messages
                "generating": "🎨 Generating image...",
                "editing": "🎭 Editing images...",
                "processing": "🤖 Processing...",
                "thinking": "🤖 Thinking...",
                "success": "✅ Success!",
                "error": "❌ Error:",
                "warning": "⚠️  Warning:",
                "info": "ℹ️  ",
                "generated_files": "Generated files:",
                "input_images": "Input images",
                "final_prompt": "Final prompt:",
                
                # Chat Mode
                "chat_mode_title": "💬 Chat-Image Mode",
                "chat_mode_desc": "Start a conversation to generate and refine images iteratively.",
                "chat_mode_commands": "Type 'quit' to exit, 'clear' to start new conversation, 'save' to save current images.",
                "you": "You:",
                "assistant": "Assistant:",
                
                # File Operations
                "select_images": "📁 Select Images (max {max_images})",
                "enter_image_path": "Enter path to {ordinal} image",
                "enter_custom_prompt": "✍️  Custom {mode} Prompt",
                "enter_prompt_instructions": "Enter your prompt ([green]press Enter twice to finish[/green]):",
                "enter_once_more": "[yellow]Press Enter once more to complete input[/yellow]",
                
                # Resolution Selection
                "select_resolution": "📐 Select Resolution",
                
                # Language Selection
                "language_selection_title": "🌐 Language Selection / 语言选择",
                "current_language": "Current language",
                "select_language": "Select language",
                
                # Goodbye
                "goodbye": "👋 Thank you for using NanoBanana Pro!",
                "images_saved_info": "Generated images are saved in the images/ directory."
            },
            
            Language.CHINESE: {
                # 应用程序标题
                "app_title": "🎨 小香蕉专业版 - AI 图像生成工作室",
                "app_subtitle": "═══════════════════════════════════════════════",
                "version_info": "版本: {version} | 模型: {model} | 图片目录: {images_dir}/",
                
                # 主菜单
                "main_menu_title": "主菜单",
                "main_menu_text_to_image": "🖼️  文字生成图片",
                "main_menu_text_to_image_desc": "从文字提示创建图片",
                "main_menu_image_editing": "🎭  图片编辑与增强",
                "main_menu_image_editing_desc": "编辑现有图片",
                "main_menu_chat_image": "💬  对话式图片生成",
                "main_menu_chat_image_desc": "交互式图片优化",
                "main_menu_settings": "⚙️  设置与配置",
                "main_menu_settings_desc": "管理偏好设置",
                "main_menu_history": "📊  查看生成历史",
                "main_menu_history_desc": "查看之前的生成记录",
                "main_menu_help": "❓  帮助与模板",
                "main_menu_help_desc": "查看模板和帮助",
                "main_menu_quit": "🚪  退出",
                "main_menu_quit_desc": "退出应用程序",
                "main_menu_language": "🌐  Language / 语言",
                "main_menu_language_desc": "切换语言",
                "select_option": "选择选项",
                
                # 文字生成图片菜单
                "text_to_image_title": "🖼️ 文字生成图片模式",
                "text_to_image_photorealistic": "📸  逼真场景",
                "text_to_image_photorealistic_desc": "专业摄影风格",
                "text_to_image_stylized": "🎨  风格化插画与贴纸",
                "text_to_image_stylized_desc": "矢量图形和标志",
                "text_to_image_text_in_images": "📝  图片中的精确文字",
                "text_to_image_text_in_images_desc": "标志和标牌",
                "text_to_image_product_mockup": "📦  产品样机与商业摄影",
                "text_to_image_product_mockup_desc": "电商图片",
                "text_to_image_minimalist": "⚪  简约与留白设计",
                "text_to_image_minimalist_desc": "简洁、宽敞的设计",
                "text_to_image_sequential_art": "📚  连环画（漫画/故事板）",
                "text_to_image_sequential_art_desc": "漫画面板和故事叙述",
                "back_to_main": "🔙  返回主菜单",
                "back_to_main_desc": "返回上一级菜单",
                "select_theme": "选择主题",
                
                # 图片编辑菜单
                "image_editing_title": "🎭 图片编辑与增强",
                "image_editing_add_remove": "➕  添加和移除元素",
                "image_editing_add_remove_desc": "从图片中添加/移除对象",
                "image_editing_inpainting": "🎯  修复绘制（语义遮罩）",
                "image_editing_inpainting_desc": "仅编辑特定部分",
                "image_editing_style_transfer": "🎭  风格迁移",
                "image_editing_style_transfer_desc": "应用艺术风格",
                "image_editing_composition": "🖼️  高级合成",
                "image_editing_composition_desc": "组合多张图片",
                "image_editing_detail_preservation": "🔍  高保真细节保护",
                "image_editing_detail_preservation_desc": "精确编辑并保护细节",
                "select_feature": "选择功能",
                
                # 设置菜单
                "settings_title": "⚙️ 设置与配置",
                "settings_default_resolution": "🖼️  更改默认分辨率",
                "settings_default_resolution_desc": "设置默认图片分辨率",
                "settings_default_theme": "🎨  更改默认主题",
                "settings_default_theme_desc": "设置默认文字生成图片主题",
                "settings_toggle_history": "📝  切换历史记录保存",
                "settings_toggle_history_desc": "启用/禁用生成历史记录",
                "settings_max_history": "📊  更改最大历史记录数",
                "settings_max_history_desc": "设置最大历史记录条目数",
                "settings_toggle_auto_open": "👀  切换自动打开图片",
                "settings_toggle_auto_open_desc": "启用/禁用自动打开图片",
                "settings_view_current": "⚙️  查看当前设置",
                "settings_view_current_desc": "显示所有当前设置",
                "settings_clear_history": "🗑️  清除历史记录",
                "settings_clear_history_desc": "删除所有生成历史记录",
                "settings_export": "📤  导出设置",
                "settings_export_desc": "将设置导出到文件",
                "settings_import": "📥  导入设置",
                "settings_import_desc": "从文件导入设置",
                
                # 帮助菜单
                "help_title": "❓ 帮助与模板",
                "help_text_templates": "📋  查看文字生成图片模板",
                "help_text_templates_desc": "查看所有可用模板",
                "help_editing_templates": "🎭  查看图片编辑模板",
                "help_editing_templates_desc": "查看编辑模板",
                "help_best_practices": "💡  最佳实践指南",
                "help_best_practices_desc": "更好提示词的技巧",
                "help_api_docs": "🔗  API 文档",
                "help_api_docs_desc": "Gemini API 参考",
                "help_shortcuts": "❓  键盘快捷键",
                "help_shortcuts_desc": "快速参考",
                
                # 常用操作
                "use_template_guide": "使用模板指导？ [Y/n]",
                "use_this_template": "使用这个模板？ [Y/n]",
                "generate_image": "生成图片？ [Y/n]",
                "edit_images": "编辑图片？ [Y/n]",
                "open_images": "打开生成的图片？ [Y/n]",
                "save_images": "现在保存图片？ [Y/n]",
                "specify_resolution": "指定输出分辨率？ [y/N]",
                "confirm_quit": "确定要退出吗？",
                "press_enter": "按回车键继续...",
                
                # 状态消息
                "generating": "🎨 正在生成图片...",
                "editing": "🎭 正在编辑图片...",
                "processing": "🤖 正在处理...",
                "thinking": "🤖 正在思考...",
                "success": "✅ 成功！",
                "error": "❌ 错误：",
                "warning": "⚠️  警告：",
                "info": "ℹ️  ",
                "generated_files": "生成的文件：",
                "input_images": "输入图片",
                "final_prompt": "最终提示词：",
                
                # 对话模式
                "chat_mode_title": "💬 对话式图片模式",
                "chat_mode_desc": "开始对话来迭代生成和优化图片。",
                "chat_mode_commands": "输入 'quit' 退出，'clear' 开始新对话，'save' 保存当前图片。",
                "you": "你：",
                "assistant": "助手：",
                
                # 文件操作
                "select_images": "📁 选择图片（最多 {max_images} 张）",
                "enter_image_path": "输入第 {ordinal} 张图片的路径",
                "enter_custom_prompt": "✍️  自定义 {mode} 提示词",
                "enter_prompt_instructions": "输入您的提示词（[green]按两次 Enter 键完成输入[/green]）：",
                "enter_once_more": "[yellow]已输入一次 Enter，再按一次 Enter 完成输入[/yellow]",
                
                # 分辨率选择
                "select_resolution": "📐 选择分辨率",
                
                # 语言选择
                "language_selection_title": "🌐 Language Selection / 语言选择",
                "current_language": "当前语言",
                "select_language": "选择语言",
                
                # 告别
                "goodbye": "👋 感谢使用小香蕉专业版！",
                "images_saved_info": "生成的图片保存在 images/ 目录中。"
            }
        }
    
    def set_language(self, language: Language):
        """Set the current language."""
        self.current_language = language
    
    def get_language(self) -> Language:
        """Get the current language."""
        return self.current_language
    
    def t(self, key: str, **kwargs) -> str:
        """
        Translate a key to the current language.
        
        Args:
            key: Translation key
            **kwargs: Format parameters
            
        Returns:
            Translated string
        """
        translations = self.translations.get(self.current_language, {})
        text = translations.get(key, key)
        
        if kwargs:
            try:
                return text.format(**kwargs)
            except (KeyError, ValueError):
                return text
        
        return text
    
    def get_available_languages(self) -> Dict[Language, str]:
        """Get available languages with display names."""
        return {
            Language.ENGLISH: "English",
            Language.CHINESE: "中文"
        }

# Global i18n instance
i18n = I18n()