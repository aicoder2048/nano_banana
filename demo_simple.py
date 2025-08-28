#!/usr/bin/env python3
"""
Simple demo script for NanoBanana Pro - generate one image directly.
"""

import sys
import os
from datetime import datetime

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def demo_text_to_image():
    """Demo text-to-image generation."""
    print("🎨 NanoBanana Pro - Simple Demo")
    print("=" * 40)
    
    try:
        # Import modules
        from src.gemini_client import get_client
        from src.config import config
        
        # Create client
        client = get_client()
        print("✓ Gemini client initialized")
        
        # Simple prompt
        prompt = "A photorealistic close-up of a small, perfectly ripe banana on a wooden table, soft natural lighting, shallow depth of field, food photography style"
        
        print(f"🖼️  Generating image with prompt:")
        print(f"   {prompt}")
        print()
        
        # Generate image
        print("⏳ Generating... (this may take 10-30 seconds)")
        success, message, images = client.generate_text_to_image(prompt, "square-medium")
        
        if success and images:
            # Save image
            saved_files = client.save_images(images, "demo_simple")
            
            print("✅ Success!")
            print(f"   Response: {message}")
            print(f"   Generated {len(saved_files)} image(s):")
            
            for file in saved_files:
                print(f"     📄 {file}")
                
                # Try to get file size
                try:
                    size = os.path.getsize(file)
                    print(f"        Size: {size:,} bytes")
                except:
                    pass
            
            print()
            print("🎉 Demo completed successfully!")
            print("   You can find the generated image in the images/ directory")
            
            return True
        else:
            print(f"❌ Generation failed: {message}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run the demo."""
    success = demo_text_to_image()
    
    if success:
        print("\n📋 Next steps:")
        print("   • Run 'uv run python nanobanana_pro.py' for the full interactive experience")
        print("   • Try different themes and templates")
        print("   • Experiment with image editing features")
        print("   • Use chat mode for iterative refinement")
    else:
        print("\n🔧 Troubleshooting:")
        print("   • Check your GEMINI_API_KEY in .env")
        print("   • Ensure you have internet connection") 
        print("   • Run 'python test_basic.py' to diagnose issues")

if __name__ == "__main__":
    main()