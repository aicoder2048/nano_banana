#!/usr/bin/env python3
"""
Test startup and menu display for NanoBanana Pro with i18n.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_startup():
    """Test application startup with i18n."""
    print("🎨 NanoBanana Pro - Startup Test")
    print("=" * 40)
    
    try:
        from src.i18n import i18n, Language
        from src.ui import ui
        from src.config import config
        
        # Test English interface
        print("Testing English interface...")
        i18n.set_language(Language.ENGLISH)
        ui.show_welcome()
        
        print("\n" + "="*50 + "\n")
        
        # Test Chinese interface
        print("Testing Chinese interface...")
        i18n.set_language(Language.CHINESE)
        ui.show_welcome()
        
        print("\n✅ Both interfaces work correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_startup()