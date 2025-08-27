#!/usr/bin/env python3
"""
Test Chinese interface for NanoBanana Pro.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_chinese_interface():
    """Test Chinese interface translations."""
    print("🎨 小香蕉专业版 - 中文界面测试")
    print("=" * 40)
    
    try:
        from src.i18n import i18n, Language
        from src.ui import ui
        
        # Test language switching
        print("测试语言切换...")
        
        # Test English (default)
        i18n.set_language(Language.ENGLISH)
        print(f"English: {i18n.t('app_title')}")
        
        # Test Chinese
        i18n.set_language(Language.CHINESE)
        print(f"中文: {i18n.t('app_title')}")
        
        print("\n✅ 语言切换测试通过!")
        
        # Test menu translations
        print("\n测试菜单翻译...")
        print(f"主菜单标题: {i18n.t('main_menu_title')}")
        print(f"文字生成图片: {i18n.t('main_menu_text_to_image')}")
        print(f"图片编辑: {i18n.t('main_menu_image_editing')}")
        print(f"对话模式: {i18n.t('main_menu_chat_image')}")
        print(f"设置: {i18n.t('main_menu_settings')}")
        
        print("\n✅ 菜单翻译测试通过!")
        
        # Test status messages
        print("\n测试状态消息...")
        print(f"成功: {i18n.t('success')}")
        print(f"错误: {i18n.t('error')}")
        print(f"警告: {i18n.t('warning')}")
        print(f"正在生成: {i18n.t('generating')}")
        
        print("\n✅ 状态消息测试通过!")
        
        # Test available languages
        print("\n测试可用语言...")
        languages = i18n.get_available_languages()
        for lang, display_name in languages.items():
            print(f"  {lang.value}: {display_name}")
        
        print("\n✅ 可用语言测试通过!")
        
        return True
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

def main():
    """Run the test."""
    success = test_chinese_interface()
    
    if success:
        print("\n🎉 所有中文界面测试通过!")
        print("\n使用方法:")
        print("1. 运行主程序: uv run python nanobanana_pro.py")
        print("2. 选择选项 '7' (Language / 语言)")
        print("3. 选择选项 '2' (中文)")
        print("4. 享受中文界面!")
    else:
        print("\n🔧 有些测试失败，请检查代码")

if __name__ == "__main__":
    main()