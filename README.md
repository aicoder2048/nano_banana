# NanoBanana Pro - AI Image Generation CLI Application

A comprehensive, professional-grade CLI application for AI image generation and editing using Google's Gemini API. Built according to the complete PRD specification with an interactive menu system, professional templates, and advanced features.

## ✨ Features

### 🎨 **Three Major Operation Modes**

#### 1. **Text-to-Image Generation** (6 Professional Themes)
- **📸 Photorealistic Scenes** - Professional photography with detailed lighting and camera controls
- **🎨 Stylized Illustrations & Stickers** - Vector graphics, logos, and digital assets  
- **📝 Accurate Text in Images** - Logos, posters, and signage with perfect text rendering
- **📦 Product Mockups & Commercial Photography** - E-commerce and advertising imagery
- **⚪ Minimalist & Negative Space Design** - Clean designs perfect for text overlay
- **📚 Sequential Art (Comic/Storyboard)** - Comic panels and visual storytelling

#### 2. **Image Editing & Enhancement** (5 Advanced Features)
- **➕ Adding and Removing Elements** - Add/remove objects while preserving style
- **🎯 Inpainting (Semantic Masking)** - Edit specific parts without manual selection
- **🎭 Style Transfer** - Apply artistic styles to photographs
- **🖼️ Advanced Composition** - Combine elements from multiple images
- **🔍 High-Fidelity Detail Preservation** - Precise editing with critical detail protection

#### 3. **💬 Chat-Image (Conversational)**
- Multi-turn conversational refinement
- Iterative image improvement through natural language
- Context-aware modifications
- Progressive enhancement capabilities

### 🌟 **Additional Features**
- **Rich Terminal Interface** - Beautiful, colorful menus with emoji icons
- **Professional Templates** - Structured prompt templates with parameter guidance
- **Resolution Control** - 9 preset resolutions from mobile to desktop
- **History Management** - Complete generation history with search and export
- **Configuration System** - Customizable preferences and settings
- **Error Handling** - Comprehensive validation and recovery
- **Auto-open Images** - Optional automatic image viewing
- **Export/Import Settings** - Backup and restore configurations

## 🚀 Quick Start

### Installation
```bash
# Clone and setup
git clone <repository>
cd NanoBanana
uv sync

# Set up API key in .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Launch Application
```bash
# Start the interactive application
uv run python nanobanana_pro.py

# Or test with a simple demo
uv run python demo_simple.py

# Run component tests
uv run python test_basic.py
```

## 📖 Usage Guide

### Interactive Menu Navigation
The application features a beautiful Rich-based terminal interface:

```
🎨 NanoBanana Pro - AI Image Generation Studio
═══════════════════════════════════════════════

🖼️  [1] Text-to-Image Generation
🎭  [2] Image Editing & Enhancement  
💬  [3] Chat-Image (Conversational)
⚙️  [4] Settings & Configuration
📊  [5] View Generation History
❓  [6] Help & Templates
🚪  [Q] Quit

Select an option [1-6, Q]: 
```

### Template-Guided Generation
Each theme includes professional templates with structured parameters:

**Example - Photorealistic Scenes Template:**
```
A photorealistic {shot_type} of {subject}, {action_expression}, 
set in {environment}. The scene is illuminated by {lighting_description}, 
creating a {mood} atmosphere. Captured with a {camera_lens_details}, 
emphasizing {key_textures_details}. The image should be in a {aspect_ratio} format.
```

### Chat Mode Commands
```bash
# Start conversation
"Create a sunset landscape"

# Iterative refinement  
"Make it more vibrant"
"Add a mountain in the background"
"Change the time to midnight with stars"

# Special commands
'save' - Save current images
'clear' - Start new conversation  
'quit' - Exit chat mode
```

## 📁 Project Structure

```
NanoBanana/
├── src/                          # Source code
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main application entry point
│   ├── ui.py                    # Rich-based user interface
│   ├── config.py                # Configuration management
│   ├── templates.py             # Prompt templates system
│   ├── gemini_client.py         # Gemini API client
│   ├── text_to_image.py         # Text-to-image generation
│   ├── image_editing.py         # Image editing features
│   ├── chat_image.py            # Conversational generation
│   └── settings.py              # Settings management
├── images/                      # Generated images output
├── .nanobanana/                 # Application data
│   ├── config.json             # User preferences
│   └── history.json            # Generation history
├── specs/
│   └── prd.md                  # Complete PRD specification
├── nanobanana_pro.py           # Main executable script
├── demo_simple.py              # Simple demo script
├── test_basic.py               # Component tests
└── .env                        # Environment variables
```

## ⚙️ Configuration

### Resolution Presets
- `square-small` (512x512)
- `square-medium` (1024x1024) - Default
- `square-large` (2048x2048)
- `landscape-hd` (1920x1080)
- `landscape-macbook` (2880x1800)
- `landscape-macbook-xl` (3456x2234)
- `portrait-iphone` (1179x2556)
- `portrait-iphone-mini` (1080x2340)
- `portrait-social` (1080x1920)

### Settings Management
Access via Settings menu (option 4) to configure:
- Default resolution and theme
- History saving preferences
- Auto-open images
- Maximum history items
- Export/import settings

## 🎯 Examples

### Text-to-Image with Template
1. Select "Text-to-Image Generation" → "Photorealistic Scenes"
2. Choose template guidance
3. Fill parameters:
   - **shot_type**: "close-up portrait"
   - **subject**: "elderly Japanese ceramicist"
   - **environment**: "rustic workshop"
   - etc.
4. Select resolution and generate

### Image Editing
1. Select "Image Editing & Enhancement" → "Style Transfer"  
2. Provide input image path
3. Use template: "Transform into Van Gogh's Starry Night style"
4. Generate enhanced image

### Chat Mode
1. Select "Chat-Image (Conversational)"
2. Start with: "Create a futuristic cityscape"
3. Refine with: "Make it more neon-lit"
4. Continue: "Add flying cars in the sky"
5. Save final result

## 🔧 Image Format Conversion

For optimal compatibility with the Gemini API, convert HEIC or PNG images to JPEG:

```bash
# Convert single image
uv run python src/convert_2_jpg.py photo.heic

# Batch convert directory with custom quality
uv run python src/convert_2_jpg.py photos/ -b -q 85

# Convert with verbose output
uv run python src/convert_2_jpg.py image.png -o output.jpg -v
```

**Supported formats:**
- **Input**: PNG, HEIC, HEIF
- **Output**: JPEG with adjustable quality (1-100)
- **Features**: Single/batch conversion, compression statistics

## 🔧 Technical Details

### API Integration
- **Model**: `gemini-2.5-flash-image-preview`
- **Input**: Text prompts up to ~8K tokens
- **Image Input**: PNG, JPEG (up to 3 images simultaneously)
- **Output**: High-quality images with SynthID watermark

### Error Handling
- Input validation and sanitization
- Network error recovery with retries
- Graceful API limit handling
- Comprehensive user feedback

### Performance
- Efficient image processing
- Memory-optimized operations
- Configurable history limits
- Automatic cleanup features

## 📋 Requirements

- Python 3.13+
- Google Gemini API key
- Dependencies: `rich`, `google-generativeai`, `pillow`, `python-dotenv`

## 🤝 Contributing

This implementation follows the complete PRD specification in `specs/prd.md`. All features are fully implemented according to professional standards with proper error handling, user experience design, and modular architecture.

## 📄 License

Professional-grade AI image generation tool built with Google's Gemini API.