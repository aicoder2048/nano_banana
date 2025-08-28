#!/usr/bin/env python3
"""
获取图片分辨率的脚本
支持常见的图片格式：PNG, JPEG, GIF, BMP, TIFF, WebP等
"""

import argparse
import sys
from pathlib import Path
from PIL import Image


def get_image_size(image_path: str) -> tuple[int, int]:
    """
    获取图片的分辨率
    
    Args:
        image_path: 图片文件路径
        
    Returns:
        tuple[int, int]: (宽度, 高度)
        
    Raises:
        FileNotFoundError: 文件不存在
        PIL.UnidentifiedImageError: 不是有效的图片格式
    """
    path = Path(image_path)
    
    if not path.exists():
        raise FileNotFoundError(f"图片文件不存在: {image_path}")
    
    if not path.is_file():
        raise ValueError(f"路径不是文件: {image_path}")
    
    with Image.open(path) as img:
        return img.size


def main():
    parser = argparse.ArgumentParser(description="获取图片分辨率")
    parser.add_argument("image_path", help="图片文件路径")
    
    args = parser.parse_args()
    
    try:
        width, height = get_image_size(args.image_path)
        print(f"{width}x{height}")
    except FileNotFoundError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"错误: 无法读取图片 '{args.image_path}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()