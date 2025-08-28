#!/usr/bin/env python3
"""
Basic test script for NanoBanana Pro components.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        from src.config import config
        print("✓ Config module imported")
        
        from src.templates import template_manager
        print("✓ Templates module imported")
        
        from src.gemini_client import get_client
        print("✓ Gemini client module imported")
        
        from src.ui import ui
        print("✓ UI module imported")
        
        from src.text_to_image import text_to_image_generator
        print("✓ Text-to-image module imported")
        
        from src.image_editing import image_editor
        print("✓ Image editing module imported")
        
        from src.chat_image import chat_image_generator
        print("✓ Chat-image module imported")
        
        from src.settings import settings_manager
        print("✓ Settings module imported")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_config():
    """Test configuration system."""
    print("\nTesting configuration...")
    
    try:
        from src.config import config
        
        # Test API key
        api_key = config.get_api_key()
        if api_key:
            print("✓ API key found")
        else:
            print("✗ API key not found")
            return False
        
        # Test resolution presets
        resolutions = config.RESOLUTION_PRESETS
        print(f"✓ Found {len(resolutions)} resolution presets")
        
        # Test settings
        default_res = config.get("default_resolution")
        print(f"✓ Default resolution: {default_res}")
        
        return True
    except Exception as e:
        print(f"✗ Config error: {e}")
        return False

def test_templates():
    """Test template system."""
    print("\nTesting templates...")
    
    try:
        from src.templates import template_manager
        
        # Test text-to-image templates
        text_themes = template_manager.get_all_text_to_image_themes()
        print(f"✓ Found {len(text_themes)} text-to-image themes")
        
        # Test image editing templates
        editing_features = template_manager.get_all_image_editing_features()
        print(f"✓ Found {len(editing_features)} image editing features")
        
        # Test specific template
        photorealistic = template_manager.get_text_to_image_template("photorealistic")
        if photorealistic:
            print("✓ Photorealistic template loaded")
            print(f"  Parameters: {len(photorealistic.parameters)}")
        else:
            print("✗ Photorealistic template not found")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Template error: {e}")
        return False

def test_client():
    """Test Gemini client (without making API calls)."""
    print("\nTesting Gemini client...")
    
    try:
        from src.gemini_client import get_client
        
        client = get_client()
        print("✓ Gemini client created")
        
        # Test prompt validation
        valid, msg = client.validate_prompt("Test prompt")
        if valid:
            print("✓ Prompt validation works")
        else:
            print(f"✗ Prompt validation failed: {msg}")
        
        # Test image validation (with non-existent file)
        valid, msg = client.validate_images(["nonexistent.png"])
        if not valid:
            print("✓ Image validation correctly rejects invalid files")
        else:
            print("✗ Image validation should reject non-existent files")
        
        return True
    except Exception as e:
        print(f"✗ Client error: {e}")
        return False

def main():
    """Run basic tests."""
    print("NanoBanana Pro - Basic Component Tests")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_config,
        test_templates,
        test_client
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All tests passed! NanoBanana Pro is ready to use.")
        print("\nTo start the application, run:")
        print("  uv run python nanobanana_pro.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()