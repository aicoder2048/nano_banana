# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**NanoBanana Pro** is a comprehensive, professional-grade AI image generation and editing CLI application using Google's Gemini API. Built according to a complete PRD specification with an interactive menu system, professional templates, and advanced features.

## Development Commands

### Package Management
- `uv sync` - Install/sync all dependencies
- `uv add <package>` - Add new dependency
- `uv run <script>` - Execute Python scripts

### Running the Application
- `uv run python nanobanana_pro.py` - **Main interactive application**
- `uv run python demo_simple.py` - Simple generation demo
- `uv run python test_basic.py` - Component testing suite
- `uv run python src/convert_2_jpg.py` - Image format conversion utility

### Project Structure
```
src/                          # Source code modules
├── main.py                  # Main application entry point
├── ui.py                    # Rich-based colorful interface  
├── config.py                # Configuration management
├── templates.py             # Professional prompt templates
├── gemini_client.py         # Gemini API client
├── text_to_image.py         # Text-to-image generation (6 themes)
├── image_editing.py         # Image editing features (5 modes)
├── chat_image.py            # Conversational generation
├── settings.py              # Settings management
└── convert_2_jpg.py         # Image format conversion utility

nanobanana_pro.py           # Main executable script
specs/prd.md                # Complete PRD specification  
images/                     # Generated images output
.nanobanana/                # Application data (config, history)
.env                        # Environment variables (not tracked)
```

## Configuration Requirements

The application requires:
1. `GEMINI_API_KEY` environment variable (stored in `.env` file)
2. Uses Gemini's "gemini-2.5-flash-image-preview" model for image generation
3. Images saved as PNG files with timestamp format: `generated_image_YYYYMMDD_HHMMSS.png`
4. Rich library for colorful terminal interface
5. pillow-heif for HEIC image conversion support

## Architecture Notes

**NanoBanana Pro** features a modular architecture with three major operation modes:

### 1. Text-to-Image Generation (6 Professional Themes)
- Photorealistic Scenes, Stylized Illustrations, Text in Images
- Product Mockups, Minimalist Design, Sequential Art
- Each theme includes structured templates with parameter guidance

### 2. Image Editing & Enhancement (5 Advanced Features)  
- Adding/Removing Elements, Inpainting, Style Transfer
- Advanced Composition, High-Fidelity Detail Preservation
- Support for up to 3 input images simultaneously

### 3. Chat-Image (Conversational Mode)
- Multi-turn conversational refinement
- Context-aware image modifications
- Progressive enhancement capabilities

### Key Components
- **Rich Terminal UI**: Beautiful, colorful menus with emoji icons
- **Template System**: Professional prompt templates with 70+ parameters
- **Configuration Management**: Persistent settings and generation history
- **Error Handling**: Comprehensive validation and user feedback
- **Format Conversion**: HEIC/PNG to JPEG utility for API compatibility

The application follows professional software development practices with proper error handling, modular design, and comprehensive documentation.