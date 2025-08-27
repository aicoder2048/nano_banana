import os
import argparse
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
from io import BytesIO

# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate images using Gemini AI")
parser.add_argument("-p", "--prompt", 
                   help="Text prompt for image generation",
                   default="A futuristic AI agent walking in downtown San Francisco at night, neon lights everywhere")
args = parser.parse_args()

# Load environment variables from .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Use prompt from CLI args or default
prompt = args.prompt
print(f"Generating image with prompt: {prompt}")

# Ensure the images directory exists
images_dir = "images"
os.makedirs(images_dir, exist_ok=True)

# Generate image
model = genai.GenerativeModel("gemini-2.5-flash-image-preview")
response = model.generate_content(prompt)

# Debug: Examine response structure
print(f"Response type: {type(response)}")
print(f"Response candidates: {len(response.candidates)}")
print(f"First candidate parts: {len(response.candidates[0].content.parts)}")

# Check if response contains text or image data
try:
    print(f"Response text: {response.text}")
except ValueError as e:
    print(f"Response contains non-text data: {e}")

# Parse and save the image
for i, part in enumerate(response.candidates[0].content.parts):
    print(f"\nPart {i}:")
    print(f"  Type: {type(part)}")
    print(f"  Has text: {hasattr(part, 'text')}")
    print(f"  Has inline_data: {hasattr(part, 'inline_data')}")
    print(f"  Text content: {part.text if part.text else 'None'}")
    print(f"  Inline data exists: {part.inline_data is not None}")
    
    if part.text:
        print(f"  Text: {part.text}")
    
    if part.inline_data:
        img = Image.open(BytesIO(part.inline_data.data))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        img_filename = os.path.join(images_dir, f"generated_image_{timestamp}.png")
        img.save(img_filename)
        print(f"Image saved as {img_filename}")

    # Inside your for-loop, save to the images/ folder
