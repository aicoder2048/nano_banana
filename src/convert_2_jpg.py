#!/usr/bin/env python3
"""
Image format conversion utility for NanoBanana Pro.
Converts HEIC or PNG images to JPEG format for optimal Gemini API compatibility.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Tuple, Optional

try:
    from PIL import Image
    from pillow_heif import register_heif_opener
    # Register HEIF opener to handle HEIC files
    register_heif_opener()
    HEIC_SUPPORT = True
except ImportError:
    from PIL import Image
    HEIC_SUPPORT = False
    print("Warning: pillow-heif not installed. HEIC conversion not available.")
    print("Install with: uv add pillow-heif")

def convert_image_to_jpeg(input_path: str, output_path: Optional[str] = None, quality: int = 90) -> Tuple[bool, str]:
    """
    Convert an image file to JPEG format.
    
    Args:
        input_path: Path to input image file
        output_path: Path for output JPEG file (optional)
        quality: JPEG quality (1-100, default 90)
    
    Returns:
        Tuple of (success, message)
    """
    try:
        input_file = Path(input_path)
        
        # Check if input file exists
        if not input_file.exists():
            return False, f"Input file not found: {input_path}"
        
        # Determine output path if not provided
        if output_path is None:
            output_file = input_file.with_suffix('.jpg')
        else:
            output_file = Path(output_path)
        
        # Check file format
        input_ext = input_file.suffix.lower()
        supported_formats = ['.png', '.heic', '.heif']
        
        if not HEIC_SUPPORT and input_ext in ['.heic', '.heif']:
            return False, f"HEIC format not supported. Install pillow-heif: uv add pillow-heif"
        
        if input_ext not in supported_formats:
            return False, f"Unsupported input format: {input_ext}. Supported: PNG, HEIC, HEIF"
        
        # Open and convert image
        with Image.open(input_file) as img:
            # Convert to RGB if necessary (PNG might have alpha channel, HEIC might be in different color space)
            if img.mode in ['RGBA', 'LA', 'P']:
                # Create white background for transparent images
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ['RGBA', 'LA'] else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as JPEG
            img.save(output_file, 'JPEG', quality=quality, optimize=True)
        
        # Get file sizes for comparison
        input_size = input_file.stat().st_size
        output_size = output_file.stat().st_size
        
        compression_ratio = (1 - output_size / input_size) * 100 if input_size > 0 else 0
        
        return True, f"Converted: {input_file.name} -> {output_file.name} (Quality: {quality}, Size: {input_size:,} -> {output_size:,} bytes, Compression: {compression_ratio:.1f}%)"
    
    except Exception as e:
        return False, f"Conversion failed: {str(e)}"

def batch_convert(input_dir: str, output_dir: Optional[str] = None, quality: int = 90) -> List[Tuple[str, bool, str]]:
    """
    Convert all supported images in a directory to JPEG.
    
    Args:
        input_dir: Directory containing input images
        output_dir: Directory for output images (optional, defaults to input_dir)
        quality: JPEG quality (1-100)
    
    Returns:
        List of (filename, success, message) tuples
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir) if output_dir else input_path
    
    if not input_path.exists():
        return [("", False, f"Input directory not found: {input_dir}")]
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all supported image files
    supported_extensions = ['.png', '.heic', '.heif']
    if not HEIC_SUPPORT:
        supported_extensions = ['.png']
    
    image_files = []
    for ext in supported_extensions:
        image_files.extend(input_path.glob(f"*{ext}"))
        image_files.extend(input_path.glob(f"*{ext.upper()}"))
    
    if not image_files:
        return [("", False, f"No supported image files found in {input_dir}")]
    
    results = []
    for image_file in image_files:
        output_file = output_path / f"{image_file.stem}.jpg"
        success, message = convert_image_to_jpeg(str(image_file), str(output_file), quality)
        results.append((image_file.name, success, message))
    
    return results

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Convert HEIC or PNG images to JPEG format for Gemini API compatibility"
    )
    parser.add_argument("input", help="Input image file or directory")
    parser.add_argument("-o", "--output", help="Output file or directory (optional)")
    parser.add_argument("-q", "--quality", type=int, default=90, 
                       help="JPEG quality (1-100, default: 90)")
    parser.add_argument("-b", "--batch", action="store_true",
                       help="Batch convert all images in directory")
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Verbose output")
    
    args = parser.parse_args()
    
    # Validate quality
    if not 1 <= args.quality <= 100:
        print("Error: Quality must be between 1 and 100")
        sys.exit(1)
    
    # Show HEIC support status
    if args.verbose:
        print(f"HEIC support: {'✓' if HEIC_SUPPORT else '✗'}")
        if not HEIC_SUPPORT:
            print("Install pillow-heif for HEIC support: uv add pillow-heif")
        print()
    
    try:
        if args.batch or os.path.isdir(args.input):
            # Batch conversion
            if args.verbose:
                print(f"Batch converting images in: {args.input}")
                print(f"Output directory: {args.output or args.input}")
                print(f"Quality: {args.quality}")
                print()
            
            results = batch_convert(args.input, args.output, args.quality)
            
            successful = 0
            failed = 0
            
            for filename, success, message in results:
                if success:
                    successful += 1
                    print(f"✓ {message}")
                else:
                    failed += 1
                    print(f"✗ {filename}: {message}")
            
            print(f"\nBatch conversion complete: {successful} successful, {failed} failed")
            
        else:
            # Single file conversion
            if args.verbose:
                print(f"Converting: {args.input}")
                print(f"Output: {args.output or 'auto-generated'}")
                print(f"Quality: {args.quality}")
                print()
            
            success, message = convert_image_to_jpeg(args.input, args.output, args.quality)
            
            if success:
                print(f"✓ {message}")
                sys.exit(0)
            else:
                print(f"✗ {message}")
                sys.exit(1)
    
    except KeyboardInterrupt:
        print("\nConversion interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def show_usage_examples():
    """Show usage examples."""
    examples = """
Usage Examples:

Convert single image:
  python convert_2_jpg.py photo.heic
  python convert_2_jpg.py image.png -o converted.jpg
  python convert_2_jpg.py photo.heic -q 95

Batch convert directory:
  python convert_2_jpg.py photos/ -b
  python convert_2_jpg.py input_dir/ -o output_dir/ -b -q 85

With NanoBanana Pro:
  # Convert then use with image editing
  python convert_2_jpg.py photo.heic
  python ../nanobanana_pro.py # then select image editing mode

Supported formats:
  Input:  PNG, HEIC, HEIF (HEIC requires pillow-heif)
  Output: JPEG (.jpg)

Quality settings:
  95-100: Highest quality, larger files
  85-94:  High quality (recommended)
  75-84:  Good quality, balanced size
  60-74:  Moderate quality, smaller files
  1-59:   Lower quality, smallest files
    """
    print(examples)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Image Format Conversion Utility for NanoBanana Pro")
        print("=" * 50)
        show_usage_examples()
    else:
        main()