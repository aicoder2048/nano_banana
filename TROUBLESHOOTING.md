# 🔧 NanoBanana Pro - Troubleshooting Guide

When you encounter errors in NanoBanana Pro, this guide will help you understand and resolve common issues.

## 🎭 Image Editing Errors

### Error: "Editing failed"

This generic error can have several causes. The improved error handling now provides detailed information:

#### 📁 **File-Related Issues**

**Error**: `Image file not found: /path/to/image.jpg`
- **Cause**: The specified image file doesn't exist
- **Solution**: 
  - Check the file path is correct
  - Ensure the file hasn't been moved or deleted
  - Use absolute paths or drag-and-drop files in terminal

**Error**: `Permission denied accessing image file`
- **Cause**: No permission to read the image file
- **Solution**: 
  - Check file permissions: `ls -la /path/to/image.jpg`
  - Use `chmod 644 /path/to/image.jpg` to fix permissions

**Error**: `Invalid image file: [Errno 21] Is a directory`
- **Cause**: You specified a directory instead of an image file
- **Solution**: Provide the full path to the image file, not just the folder

#### 🌐 **Network Issues**

**Error**: `Network connection error`
- **Cause**: No internet connection or connectivity issues
- **Solution**: 
  - Check your internet connection
  - Try again in a few moments
  - Check if your firewall is blocking the connection

#### 🔑 **API Issues**

**Error**: `API authentication failed`
- **Cause**: Invalid or missing API key
- **Solution**: 
  - Check your `.env` file has `GEMINI_API_KEY=your_key_here`
  - Verify your API key is valid at [Google AI Studio](https://aistudio.google.com/)
  - Make sure there are no spaces or quotes around the key

**Error**: `API quota exceeded or rate limit hit`
- **Cause**: You've exceeded your API usage limits
- **Solution**: 
  - Wait before trying again (rate limits reset over time)
  - Check your quota at [Google AI Studio](https://aistudio.google.com/)
  - Consider upgrading your API plan if needed

#### 🛡️ **Content Safety Issues**

**Error**: `Content blocked by safety filters`
- **Cause**: The image or prompt violates content policies
- **Solution**: 
  - Use appropriate, non-harmful content
  - Try a different image or modify your prompt
  - Avoid potentially sensitive content

#### 🖼️ **Image Format Issues**

**Error**: `Invalid image format` or similar PIL errors
- **Cause**: Unsupported image format or corrupted file
- **Solution**: 
  - Convert images to JPEG or PNG: `uv run python src/convert_2_jpg.py your_image.heic`
  - Supported formats: PNG, JPEG, JPG
  - Try opening the image in another program to verify it's not corrupted

## 🖼️ Text-to-Image Errors

### Error: "Generation failed"

Similar causes as image editing, but common specific issues:

**Error**: `Prompt cannot be empty`
- **Solution**: Provide a descriptive text prompt

**Error**: `No images generated in response`
- **Cause**: API didn't return image data
- **Solution**: 
  - Try a different prompt
  - Check your internet connection
  - Wait a moment and try again

## 💬 Chat-Image Errors

### Connection Issues

**Error**: `Failed to initialize chat`
- **Solution**: Same as API authentication issues above

## 🔍 Debugging Information

When errors occur, NanoBanana Pro now shows debugging information:

```
Debugging information:
• Feature: Adding and Removing Elements
• Input images: 1
• Prompt length: 45 characters  
• Resolution: original
```

This helps identify the issue:
- **Feature**: Which template/feature was being used
- **Input images**: How many images were provided
- **Prompt length**: Very long prompts might cause issues
- **Resolution**: Whether custom resolution was requested

## 🚨 Common Quick Fixes

1. **Check file paths**: Use absolute paths or drag-and-drop files
2. **Verify API key**: Ensure `GEMINI_API_KEY` is set in `.env`
3. **Test connectivity**: Try generating a simple text-to-image first
4. **Check file formats**: Convert HEIC files to JPEG if needed
5. **Restart the app**: Sometimes helps with connection issues

## 📊 Getting More Help

If you continue experiencing issues:

1. **Check the error message carefully** - The improved error handling provides specific details
2. **Note the debugging information** shown after errors
3. **Try with a simple test case** - Single image, simple prompt
4. **Check your internet connection** and API quota
5. **Verify image files** are readable and in supported formats

## 🔄 Image Conversion Utility

For image format issues, use the built-in converter:

```bash
# Convert single image
uv run python src/convert_2_jpg.py image.heic

# Batch convert with custom quality
uv run python src/convert_2_jpg.py photos/ -b -q 90

# Verbose output for debugging
uv run python src/convert_2_jpg.py image.png -v
```

## 🌐 Supported Formats

- **Input Images**: PNG, JPEG, JPG, HEIC (convert to JPEG)
- **Output Images**: PNG (with transparency support)
- **Maximum Images**: Up to 3 images for composition features

## 📞 Still Need Help?

If none of these solutions work:
1. Note the exact error message
2. Check what you were trying to do
3. Verify your setup meets the requirements
4. Consider filing an issue with detailed information about the error