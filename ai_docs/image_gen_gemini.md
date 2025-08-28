::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .devsite-main-content role="main" has-book-nav="" has-sidebar=""}
:::: devsite-sidebar
::: devsite-sidebar-content
:::
::::

::::: {.devsite-banner .devsite-banner-announcement .nocontent background="google-blue"}
:::: devsite-banner-message
::: devsite-banner-message-text
Gemini 2.5 Flash Image Preview is now available in the Gemini API!
[Learn
more](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/){.button
.button-primary}
:::
::::
:::::

::: {.devsite-article-meta .nocontent role="navigation"}
- [Home](https://ai.google.dev/){.devsite-breadcrumb-link
  .gc-analytics-event category="Site-Wide Custom Events"
  data-label="Breadcrumbs" data-value="1" track-type="globalNav"
  track-name="breadcrumb" track-metadata-position="1"
  track-metadata-eventdetail=""}

- ::: {.devsite-breadcrumb-guillemet .material-icons aria-hidden="true"}
  :::

  [Gemini
  API](https://ai.google.dev/gemini-api){.devsite-breadcrumb-link
  .gc-analytics-event category="Site-Wide Custom Events"
  data-label="Breadcrumbs" data-value="2" track-type="globalNav"
  track-name="breadcrumb" track-metadata-position="2"
  track-metadata-eventdetail="Gemini API"}

- ::: {.devsite-breadcrumb-guillemet .material-icons aria-hidden="true"}
  :::

  [Gemini API
  docs](https://ai.google.dev/gemini-api/docs){.devsite-breadcrumb-link
  .gc-analytics-event category="Site-Wide Custom Events"
  data-label="Breadcrumbs" data-value="3" track-type="globalNav"
  track-name="breadcrumb" track-metadata-position="3"
  track-metadata-eventdetail=""}
:::

Send feedback

# Image generation with Gemini {#image-generation-with-gemini .devsite-page-title tabindex="-1"}

::: {.devsite-actions hidden="" nosnippet=""}
:::

::: devsite-page-title-meta
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.devsite-article-body .clearfix}
Gemini can generate and process images conversationally. You can prompt
Gemini with text, images, or a combination of both allowing you to
create, edit, and iterate on visuals with unprecedented control:

- **Text-to-Image:** Generate high-quality images from simple or complex
  text descriptions.
- **Image + Text-to-Image (Editing):** Provide an image and use text
  prompts to add, remove, or modify elements, change the style, or
  adjust the color grading.
- **Multi-Image to Image (Composition & Style Transfer):** Use multiple
  input images to compose a new scene or transfer the style from one
  image to another.
- **Iterative Refinement:** Engage in a conversation to progressively
  refine your image over multiple turns, making small adjustments until
  it\'s perfect.
- **High-Fidelity Text Rendering:** Accurately generate images that
  contain legible and well-placed text, ideal for logos, diagrams, and
  posters.

All generated images include a [SynthID
watermark](/responsible/docs/safeguards/synthid).

**Note:** You can also generate images with
[Imagen](/gemini-api/docs/imagen), our specialized image generation
model. See the [When to use Imagen](#choose-a-model) section for details
on how to choose between Gemini and Imagen.

## Image generation (text-to-image) {#image_generation_text-to-image data-text="Image generation (text-to-image)" tabindex="-1"}

The following code demonstrates how to generate an image based on a
descriptive prompt.

::::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Python {#python data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
```
::::

:::: section
### JavaScript {#javascript data-text="JavaScript" tabindex="-1"}

**Note:** We\'ve released the [Google SDK for TypeScript and
JavaScript](https://www.npmjs.com/package/@google/genai) in [preview
launch
stage](https://github.com/googleapis/js-genai?tab=readme-ov-file#preview-launch).
Use this SDK for image generation features.

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="JavaScript"}
import { GoogleGenAI, Modality } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const prompt =
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme";

  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image-preview",
    contents: prompt,
  });
  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
  }
}

main();
```
::::

:::: section
### Go {#go data-text="Go" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Go"}
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-2.5-flash-image-preview",
      genai.Text("Create a picture of a nano banana dish in a " +
                 " fancy restaurant with a Gemini theme"),
  )

  for _, part := range result.Candidates[0].Content.Parts {
      if part.Text != "" {
          fmt.Println(part.Text)
      } else if part.InlineData != nil {
          imageBytes := part.InlineData.Data
          outputFilename := "gemini_generated_image.png"
          _ = os.WriteFile(outputFilename, imageBytes, 0644)
      }
  }
}
```
::::

:::: section
### REST {#rest data-text="REST" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Bash"}
curl -s -X POST
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }]
  }' \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode > gemini-native-image.png
```
::::
:::::::::::

<figure>
<img src="/static/gemini-api/docs/images/nano-banana.png"
class="screenshot" alt="AI-generated image of a nano banana dish" />
<figcaption>AI-generated image of a nano banana dish in a Gemini-themed
restaurant</figcaption>
</figure>

## Image editing (text-and-image-to-image) {#gemini-image-editing data-text="Image editing (text-and-image-to-image)" tabindex="-1"}

**Reminder**: Make sure you have the necessary rights to any images you
upload. Don\'t generate content that infringe on others\' rights,
including videos or images that deceive, harass, or harm. Your use of
this generative AI service is subject to our [Prohibited Use
Policy](https://policies.google.com/terms/generative-ai/use-policy).

To perform image editing, add an image as input. The following example
demonstrates uploading base64 encoded images. For multiple images,
larger payloads, and supported MIME types, check the [Image
understanding](/gemini-api/docs/image-understanding) page.

::::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Python {#python_1 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = (
    "Create a picture of my cat eating a nano-banana in a "
    "fancy restaurant under the Gemini constellation",
)

image = Image.open("/path/to/cat_image.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt, image],
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
```
::::

:::: section
### JavaScript {#javascript_1 data-text="JavaScript" tabindex="-1"}

**Note:** We\'ve released the [Google SDK for TypeScript and
JavaScript](https://www.npmjs.com/package/@google/genai) in [preview
launch
stage](https://github.com/googleapis/js-genai?tab=readme-ov-file#preview-launch).
Use this SDK for image generation features.

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="JavaScript"}
import { GoogleGenAI, Modality } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const imagePath = "path/to/cat_image.png";
  const imageData = fs.readFileSync(imagePath);
  const base64Image = imageData.toString("base64");

  const prompt = [
    { text: "Create a picture of my cat eating a nano-banana in a" +
            "fancy restaurant under the Gemini constellation" },
    {
      inlineData: {
        mimeType: "image/png",
        data: base64Image,
      },
    },
  ];

  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image-preview",
    contents: prompt,
  });
  for (const part of response.candidates[0].content.parts) {
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
  }
}

main();
```
::::

:::: section
### Go {#go_1 data-text="Go" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Go"}
package main

import (
 "context"
 "fmt"
 "os"
 "google.golang.org/genai"
)

func main() {

 ctx := context.Background()
 client, err := genai.NewClient(ctx, nil)
 if err != nil {
     log.Fatal(err)
 }

 imagePath := "/path/to/cat_image.png"
 imgData, _ := os.ReadFile(imagePath)

 parts := []*genai.Part{
   genai.NewPartFromText("Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation"),
   &genai.Part{
     InlineData: &genai.Blob{
       MIMEType: "image/png",
       Data:     imgData,
     },
   },
 }

 contents := []*genai.Content{
   genai.NewContentFromParts(parts, genai.RoleUser),
 }

 result, _ := client.Models.GenerateContent(
     ctx,
     "gemini-2.5-flash-image-preview",
     contents,
 )

 for _, part := range result.Candidates[0].Content.Parts {
     if part.Text != "" {
         fmt.Println(part.Text)
     } else if part.InlineData != nil {
         imageBytes := part.InlineData.Data
         outputFilename := "gemini_generated_image.png"
         _ = os.WriteFile(outputFilename, imageBytes, 0644)
     }
 }
}
```
::::

:::: section
### REST {#rest_1 data-text="REST" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Bash"}
IMG_PATH=/path/to/cat_image.jpeg

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

IMG_BASE64=$(base64 "$B64FLAGS" "$IMG_PATH" 2>&1)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d "{
      \"contents\": [{
        \"parts\":[
            {\"text\": \"'Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation\"},
            {
              \"inline_data\": {
                \"mime_type\":\"image/jpeg\",
                \"data\": \"$IMG_BASE64\"
              }
            }
        ]
      }]
    }"  \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode > gemini-edited-image.png
```
::::
:::::::::::

<figure>
<img src="/static/gemini-api/docs/images/cat-banana.png"
class="screenshot"
alt="AI-generated image of a cat eating anano banana" />
<figcaption>AI-generated image of a cat eating a nano
banana</figcaption>
</figure>

## Other image generation modes {#other_image_generation_modes data-text="Other image generation modes" tabindex="-1"}

Gemini supports other image interaction modes based on prompt structure
and context, including:

- **Text to image(s) and text (interleaved):** Outputs images with
  related text.
  - Example prompt: \"Generate an illustrated recipe for a paella.\"
- **Image(s) and text to image(s) and text (interleaved)**: Uses input
  images and text to create new related images and text.
  - Example prompt: (With an image of a furnished room) \"What other
    color sofas would work in my space? can you update the image?\"
- **Multi-turn image editing (chat):** Keep generating and editing
  images conversationally.
  - Example prompts: \[upload an image of a blue car.\] , \"Turn this
    car into a convertible.\", \"Now change the color to yellow.\"

## Prompting guide and strategies {#prompt-guide data-text="Prompting guide and strategies" tabindex="-1"}

Mastering Gemini 2.5 Flash Image Generation starts with one fundamental
principle:

> **Describe the scene, don\'t just list keywords.** The model\'s core
> strength is its deep language understanding. A narrative, descriptive
> paragraph will almost always produce a better, more coherent image
> than a list of disconnected words.

### Prompts for generating images {#image-generation-prompts data-text="Prompts for generating images" tabindex="-1"}

The following strategies will help you create effective prompts to
generate exactly the images you\'re looking for.

#### 1. Photorealistic scenes {#1_photorealistic_scenes data-text="1. Photorealistic scenes" tabindex="-1"}

For realistic images, use photography terms. Mention camera angles, lens
types, lighting, and fine details to guide the model toward a
photorealistic result.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A photorealistic [shot type] of [subject], [action or expression], set in
[environment]. The scene is illuminated by [lighting description], creating
a [mood] atmosphere. Captured with a [camera/lens details], emphasizing
[key textures and details]. The image should be in a [aspect ratio] format.
```
::::

:::: section
### Prompt {#prompt data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A photorealistic close-up portrait of an elderly Japanese ceramicist with
deep, sun-etched wrinkles and a warm, knowing smile. He is carefully
inspecting a freshly glazed tea bowl. The setting is his rustic,
sun-drenched workshop. The scene is illuminated by soft, golden hour light
streaming through a window, highlighting the fine texture of the clay.
Captured with an 85mm portrait lens, resulting in a soft, blurred background
(bokeh). The overall mood is serene and masterful. Vertical portrait
orientation.
```
::::

:::: section
### Python {#python_2 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="A photorealistic close-up portrait of an elderly Japanese ceramicist with deep, sun-etched wrinkles and a warm, knowing smile. He is carefully inspecting a freshly glazed tea bowl. The setting is his rustic, sun-drenched workshop with pottery wheels and shelves of clay pots in the background. The scene is illuminated by soft, golden hour light streaming through a window, highlighting the fine texture of the clay and the fabric of his apron. Captured with an 85mm portrait lens, resulting in a soft, blurred background (bokeh). The overall mood is serene and masterful.",
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('photorealistic_example.png')
    image.show()
```
::::
:::::::::

![A photorealistic close-up portrait of an elderly Japanese
ceramicist\...](/static/gemini-api/docs/images/photorealistic_example.png){.screenshot
width="450"}

#### 2. Stylized illustrations & stickers {#2_stylized_illustrations_stickers data-text="2. Stylized illustrations & stickers" tabindex="-1"}

To create stickers, icons, or assets, be explicit about the style and
request a transparent background.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_1 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A [style] sticker of a [subject], featuring [key characteristics] and a
[color palette]. The design should have [line style] and [shading style].
The background must be transparent.
```
::::

:::: section
### Prompt {#prompt_1 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A kawaii-style sticker of a happy red panda wearing a tiny bamboo hat. It's
munching on a green bamboo leaf. The design features bold, clean outlines,
simple cel-shading, and a vibrant color palette. The background must be white.
```
::::

:::: section
### Python {#python_3 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="A kawaii-style sticker of a happy red panda wearing a tiny bamboo hat. It's munching on a green bamboo leaf. The design features bold, clean outlines, simple cel-shading, and a vibrant color palette. The background must be white.",
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('red_panda_sticker.png')
    image.show()
```
::::
:::::::::

<figure>
<img src="/static/gemini-api/docs/images/red_panda_sticker.png"
class="screenshot" width="450"
alt="A kawaii-style sticker of a happy red..." />
<figcaption>A kawaii-style sticker of a happy red panda...</figcaption>
</figure>

#### 3. Accurate text in images {#3_accurate_text_in_images data-text="3. Accurate text in images" tabindex="-1"}

Gemini excels at rendering text. Be clear about the text, the font style
(descriptively), and the overall design.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_2 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Create a [image type] for [brand/concept] with the text "[text to render]"
in a [font style]. The design should be [style description], with a
[color scheme].
```
::::

:::: section
### Prompt {#prompt_2 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Create a modern, minimalist logo for a coffee shop called 'The Daily Grind'.
The text should be in a clean, bold, sans-serif font. The design should
feature a simple, stylized icon of a a coffee bean seamlessly integrated
with the text. The color scheme is black and white.
```
::::

:::: section
### Python {#python_4 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="Create a modern, minimalist logo for a coffee shop called 'The Daily Grind'. The text should be in a clean, bold, sans-serif font. The design should feature a simple, stylized icon of a a coffee bean seamlessly integrated with the text. The color scheme is black and white.",
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('logo_example.png')
    image.show()
```
::::
:::::::::

![Create a modern, minimalist logo for a coffee shop called \'The Daily
Grind\'\...](/static/gemini-api/docs/images/logo_example.png){.screenshot
width="450"}

#### 4. Product mockups & commercial photography {#4_product_mockups_commercial_photography data-text="4. Product mockups & commercial photography" tabindex="-1"}

Perfect for creating clean, professional product shots for e-commerce,
advertising, or branding.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_3 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A high-resolution, studio-lit product photograph of a [product description]
on a [background surface/description]. The lighting is a [lighting setup,
e.g., three-point softbox setup] to [lighting purpose]. The camera angle is
a [angle type] to showcase [specific feature]. Ultra-realistic, with sharp
focus on [key detail]. [Aspect ratio].
```
::::

:::: section
### Prompt {#prompt_3 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A high-resolution, studio-lit product photograph of a minimalist ceramic
coffee mug in matte black, presented on a polished concrete surface. The
lighting is a three-point softbox setup designed to create soft, diffused
highlights and eliminate harsh shadows. The camera angle is a slightly
elevated 45-degree shot to showcase its clean lines. Ultra-realistic, with
sharp focus on the steam rising from the coffee. Square image.
```
::::

:::: section
### Python {#python_5 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="A high-resolution, studio-lit product photograph of a minimalist ceramic coffee mug in matte black, presented on a polished concrete surface. The lighting is a three-point softbox setup designed to create soft, diffused highlights and eliminate harsh shadows. The camera angle is a slightly elevated 45-degree shot to showcase its clean lines. Ultra-realistic, with sharp focus on the steam rising from the coffee. Square image.",
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('product_mockup.png')
    image.show()
```
::::
:::::::::

![A high-resolution, studio-lit product photograph of a minimalist
ceramic coffee
mug\...](/static/gemini-api/docs/images/product_mockup.png){.screenshot
width="450"}

#### 5. Minimalist & negative space design {#5_minimalist_negative_space_design data-text="5. Minimalist & negative space design" tabindex="-1"}

Excellent for creating backgrounds for websites, presentations, or
marketing materials where text will be overlaid.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_4 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A minimalist composition featuring a single [subject] positioned in the
[bottom-right/top-left/etc.] of the frame. The background is a vast, empty
[color] canvas, creating significant negative space. Soft, subtle lighting.
[Aspect ratio].
```
::::

:::: section
### Prompt {#prompt_4 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A minimalist composition featuring a single, delicate red maple leaf
positioned in the bottom-right of the frame. The background is a vast, empty
off-white canvas, creating significant negative space for text. Soft,
diffused lighting from the top left. Square image.
```
::::

:::: section
### Python {#python_6 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="A minimalist composition featuring a single, delicate red maple leaf positioned in the bottom-right of the frame. The background is a vast, empty off-white canvas, creating significant negative space for text. Soft, diffused lighting from the top left. Square image.",
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('minimalist_design.png')
    image.show()
```
::::
:::::::::

![A minimalist composition featuring a single, delicate red maple
leaf\...](/static/gemini-api/docs/images/minimalist_design.png){.screenshot
width="450"}

#### 6. Sequential art (Comic panel / Storyboard) {#6_sequential_art_comic_panel_storyboard data-text="6. Sequential art (Comic panel / Storyboard)" tabindex="-1"}

Builds on character consistency and scene description to create panels
for visual storytelling.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_5 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A single comic book panel in a [art style] style. In the foreground,
[character description and action]. In the background, [setting details].
The panel has a [dialogue/caption box] with the text "[Text]". The lighting
creates a [mood] mood. [Aspect ratio].
```
::::

:::: section
### Prompt {#prompt_5 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
A single comic book panel in a gritty, noir art style with high-contrast
black and white inks. In the foreground, a detective in a trench coat stands
under a flickering streetlamp, rain soaking his shoulders. In the
background, the neon sign of a desolate bar reflects in a puddle. A caption
box at the top reads "The city was a tough place to keep secrets." The
lighting is harsh, creating a dramatic, somber mood. Landscape.
```
::::

:::: section
### Python {#python_7 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents="A single comic book panel in a gritty, noir art style with high-contrast black and white inks. In the foreground, a detective in a trench coat stands under a flickering streetlamp, rain soaking his shoulders. In the background, the neon sign of a desolate bar reflects in a puddle. A caption box at the top reads \"The city was a tough place to keep secrets.\" The lighting is harsh, creating a dramatic, somber mood. Landscape.",
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('comic_panel.png')
    image.show()
```
::::
:::::::::

![A single comic book panel in a gritty, noir art
style\...](/static/gemini-api/docs/images/comic_panel.png){.screenshot
width="450"}

### Prompts for editing images {#image-editing-prompts data-text="Prompts for editing images" tabindex="-1"}

These examples show how to provide images alongside your text prompts
for editing, composition, and style transfer.

#### 1. Adding and removing elements {#1_adding_and_removing_elements data-text="1. Adding and removing elements" tabindex="-1"}

Provide an image and describe your change. The model will match the
original image\'s style, lighting, and perspective.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_6 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Using the provided image of [subject], please [add/remove/modify] [element]
to/from the scene. Ensure the change is [description of how the change should
integrate].
```
::::

:::: section
### Prompt {#prompt_6 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
"Using the provided image of my cat, please add a small, knitted wizard hat
on its head. Make it look like it's sitting comfortably and matches the soft
lighting of the photo."
```
::::

:::: section
### Python {#python_8 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Base image prompt: "A photorealistic picture of a fluffy ginger cat sitting on a wooden floor, looking directly at the camera. Soft, natural light from a window."
image_input = Image.open('/path/to/your/cat_photo.png')
text_input = """Using the provided image of my cat, please add a small, knitted wizard hat on its head. Make it look like it's sitting comfortably and not falling off."""

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[text_input, image_input],
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('cat_with_hat.png')
    image.show()
```
::::
:::::::::

+------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Input                                                                  | Output                                                                |
+------------------------------------------------------------------------+-----------------------------------------------------------------------+
| <figure>                                                               | ![Using the provided image of my cat, please add a small, knitted     |
| <img src="/static/gemini-api/docs/images/cat.png" class="screenshot"   | wizard                                                                |
| width="450" alt="A photorealistic picture of a fluffy ginger cat.." /> | hat\...](/static/gemini-api/docs/images/cat_with_hat.png){.screenshot |
| <figcaption>A photorealistic picture of a fluffy ginger                | width="450"}                                                          |
| cat...</figcaption>                                                    |                                                                       |
| </figure>                                                              |                                                                       |
+------------------------------------------------------------------------+-----------------------------------------------------------------------+

#### 2. Inpainting (Semantic masking) {#2_inpainting_semantic_masking data-text="2. Inpainting (Semantic masking)" tabindex="-1"}

Conversationally define a \"mask\" to edit a specific part of an image
while leaving the rest untouched.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_7 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Using the provided image, change only the [specific element] to [new
element/description]. Keep everything else in the image exactly the same,
preserving the original style, lighting, and composition.
```
::::

:::: section
### Prompt {#prompt_7 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
"Using the provided image of a living room, change only the blue sofa to be
a vintage, brown leather chesterfield sofa. Keep the rest of the room,
including the pillows on the sofa and the lighting, unchanged."
```
::::

:::: section
### Python {#python_9 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Base image prompt: "A wide shot of a modern, well-lit living room with a prominent blue sofa in the center. A coffee table is in front of it and a large window is in the background."
living_room_image = Image.open('/path/to/your/living_room.png')
text_input = """Using the provided image of a living room, change only the blue sofa to be a vintage, brown leather chesterfield sofa. Keep the rest of the room, including the pillows on the sofa and the lighting, unchanged."""

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[living_room_image, text_input],
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('living_room_edited.png')
    image.show()
```
::::
:::::::::

+-----------------------------------------------------------------------+------------------------------------------------------------------------------+
| Input                                                                 | Output                                                                       |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------+
| ![A wide shot of a modern, well-lit living                            | ![Using the provided image of a living room, change only the blue sofa to be |
| room\...](/static/gemini-api/docs/images/living_room.png){.screenshot | a vintage, brown leather chesterfield                                        |
| width="450"}                                                          | sofa\...](/static/gemini-api/docs/images/living_room_edited.png){.screenshot |
|                                                                       | width="450"}                                                                 |
+-----------------------------------------------------------------------+------------------------------------------------------------------------------+

#### 3. Style transfer {#3_style_transfer data-text="3. Style transfer" tabindex="-1"}

Provide an image and ask the model to recreate its content in a
different artistic style.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_8 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Transform the provided photograph of [subject] into the artistic style of [artist/art style]. Preserve the original composition but render it with [description of stylistic elements].
```
::::

:::: section
### Prompt {#prompt_8 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
"Transform the provided photograph of a modern city street at night into the artistic style of Vincent van Gogh's 'Starry Night'. Preserve the original composition of buildings and cars, but render all elements with swirling, impasto brushstrokes and a dramatic palette of deep blues and bright yellows."
```
::::

:::: section
### Python {#python_10 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Base image prompt: "A photorealistic, high-resolution photograph of a busy city street in New York at night, with bright neon signs, yellow taxis, and tall skyscrapers."
city_image = Image.open('/path/to/your/city.png')
text_input = """Transform the provided photograph of a modern city street at night into the artistic style of Vincent van Gogh's 'Starry Night'. Preserve the original composition of buildings and cars, but render all elements with swirling, impasto brushstrokes and a dramatic palette of deep blues and bright yellows."""

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[city_image, text_input],
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('city_style_transfer.png')
    image.show()
```
::::
:::::::::

+------------------------------------------------------------------+--------------------------------------------------------------------------------+
| Input                                                            | Output                                                                         |
+------------------------------------------------------------------+--------------------------------------------------------------------------------+
| ![A photorealistic, high-resolution photograph of a busy city    | ![Transform the provided photograph of a modern city street at                 |
| street\...](/static/gemini-api/docs/images/city.png){.screenshot | night\...](/static/gemini-api/docs/images/city_style_transfer.png){.screenshot |
| width="450"}                                                     | width="450"}                                                                   |
+------------------------------------------------------------------+--------------------------------------------------------------------------------+

#### 4. Advanced composition: Combining multiple images {#4_advanced_composition_combining_multiple_images data-text="4. Advanced composition: Combining multiple images" tabindex="-1"}

Provide multiple images as context to create a new, composite scene.
This is perfect for product mockups or creative collages.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_9 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Create a new image by combining the elements from the provided images. Take
the [element from image 1] and place it with/on the [element from image 2].
The final image should be a [description of the final scene].
```
::::

:::: section
### Prompt {#prompt_9 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
"Create a professional e-commerce fashion photo. Take the blue floral dress
from the first image and let the woman from the second image wear it.
Generate a realistic, full-body shot of the woman wearing the dress, with
the lighting and shadows adjusted to match the outdoor environment."
```
::::

:::: section
### Python {#python_11 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Base image prompts:
# 1. Dress: "A professionally shot photo of a blue floral summer dress on a plain white background, ghost mannequin style."
# 2. Model: "Full-body shot of a woman with her hair in a bun, smiling, standing against a neutral grey studio background."
dress_image = Image.open('/path/to/your/dress.png')
model_image = Image.open('/path/to/your/model.png')

text_input = """Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."""

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[dress_image, model_image, text_input],
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('fashion_ecommerce_shot.png')
    image.show()
```
::::
:::::::::

+------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Input 1                                                          | Input 2                                                        | Output                                                                            |
+------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ![A professionally shot photo of a blue floral summer            | ![Full-body shot of a woman with her hair in a                 | ![Create a professional e-commerce fashion                                        |
| dress\...](/static/gemini-api/docs/images/dress.png){.screenshot | bun\...](/static/gemini-api/docs/images/model.png){.screenshot | photo\...](/static/gemini-api/docs/images/fashion_ecommerce_shot.png){.screenshot |
| width="450"}                                                     | width="450"}                                                   | width="450"}                                                                      |
+------------------------------------------------------------------+----------------------------------------------------------------+-----------------------------------------------------------------------------------+

#### 5. High-fidelity detail preservation {#5_high-fidelity_detail_preservation data-text="5. High-fidelity detail preservation" tabindex="-1"}

To ensure critical details (like a face or logo) are preserved during an
edit, describe them in great detail along with your edit request.

::::::::: {.ds-selector-tabs ds-scope="code-sample"}
:::: section
### Template {#template_10 data-text="Template" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
Using the provided images, place [element from image 2] onto [element from
image 1]. Ensure that the features of [element from image 1] remain
completely unchanged. The added element should [description of how the
element should integrate].
```
::::

:::: section
### Prompt {#prompt_10 data-text="Prompt" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded=""}
"Take the first image of the woman with brown hair, blue eyes, and a neutral
expression. Add the logo from the second image onto her black t-shirt.
Ensure the woman's face and features remain completely unchanged. The logo
should look like it's naturally printed on the fabric, following the folds
of the shirt."
```
::::

:::: section
### Python {#python_12 data-text="Python" tabindex="-1"}

<div>

</div>

``` {.devsite-click-to-copy translate="no" dir="ltr" is-upgraded="" syntax="Python"}
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# Base image prompts:
# 1. Woman: "A professional headshot of a woman with brown hair and blue eyes, wearing a plain black t-shirt, against a neutral studio background."
# 2. Logo: "A simple, modern logo with the letters 'G' and 'A' in a white circle."
woman_image = Image.open('/path/to/your/woman.png')
logo_image = Image.open('/path/to/your/logo.png')
text_input = """Take the first image of the woman with brown hair, blue eyes, and a neutral expression. Add the logo from the second image onto her black t-shirt. Ensure the woman's face and features remain completely unchanged. The logo should look like it's naturally printed on the fabric, following the folds of the shirt."""

# Generate an image from a text prompt
response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[woman_image, logo_image, text_input],
)

image_parts = [
    part.inline_data.data
    for part in response.candidates[0].content.parts
    if part.inline_data
]

if image_parts:
    image = Image.open(BytesIO(image_parts[0]))
    image.save('woman_with_logo.png')
    image.show()
```
::::
:::::::::

+-----------------------------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------+
| Input 1                                                         | Input 2                                                         | Output                                                                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------+
| ![A professional headshot of a woman with brown hair and blue   | ![A simple, modern logo with the letters \'G\' and              | ![Take the first image of the woman with brown hair, blue eyes, and a neutral   |
| eyes\...](/static/gemini-api/docs/images/woman.png){.screenshot | \'A\'\...](/static/gemini-api/docs/images/logo.png){.screenshot | expression\...](/static/gemini-api/docs/images/woman_with_logo.png){.screenshot |
| width="450"}                                                    | width="450"}                                                    | width="450"}                                                                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------+

### Best Practices {#best-practices data-text="Best Practices" tabindex="-1"}

To elevate your results from good to great, incorporate these
professional strategies into your workflow.

- **Be Hyper-Specific:** The more detail you provide, the more control
  you have. Instead of \"fantasy armor,\" describe it: \"ornate elven
  plate armor, etched with silver leaf patterns, with a high collar and
  pauldrons shaped like falcon wings.\"
- **Provide Context and Intent:** Explain the *purpose* of the image.
  The model\'s understanding of context will influence the final output.
  For example, \"Create a logo for a high-end, minimalist skincare
  brand\" will yield better results than just \"Create a logo.\"
- **Iterate and Refine:** Don\'t expect a perfect image on the first
  try. Use the conversational nature of the model to make small changes.
  Follow up with prompts like, \"That\'s great, but can you make the
  lighting a bit warmer?\" or \"Keep everything the same, but change the
  character\'s expression to be more serious.\"
- **Use Step-by-Step Instructions:** For complex scenes with many
  elements, break your prompt into steps. \"First, create a background
  of a serene, misty forest at dawn. Then, in the foreground, add a
  moss-covered ancient stone altar. Finally, place a single, glowing
  sword on top of the altar.\"
- **Use \"Semantic Negative Prompts\":** Instead of saying \"no cars,\"
  describe the desired scene positively: \"an empty, deserted street
  with no signs of traffic.\"
- **Control the Camera:** Use photographic and cinematic language to
  control the composition. Terms like `wide-angle shot`{translate="no"
  dir="ltr"}, `macro shot`{translate="no" dir="ltr"},
  `low-angle perspective`{translate="no" dir="ltr"}.

## Limitations {#limitations data-text="Limitations" tabindex="-1"}

- For best performance, use the following languages: EN, es-MX, ja-JP,
  zh-CN, hi-IN.
- Image generation does not support audio or video inputs.
- The model won\'t always follow the exact number of image outputs that
  the user explicitly asked for.
- The model works best with up to 3 images as an input.
- When generating text for an image, Gemini works best if you first
  generate the text and then ask for an image with the text.
- Uploading images of children is not currently supported in EEA, CH,
  and UK.
- All generated images include a [SynthID
  watermark](/responsible/docs/safeguards/synthid).

## When to use Imagen {#choose-a-model data-text="When to use Imagen" tabindex="-1"}

In addition to using Gemini\'s built-in image generation capabilities,
you can also access [Imagen](/gemini-api/docs/imagen), our specialized
image generation model, through the Gemini API.

+-------------------+------------------------+------------------------+
| Attribute         | Imagen                 | Gemini Native Image    |
+===================+========================+========================+
| Strengths         | Most capable image     | **Default              |
|                   | generation model to    | recommendation.**\     |
|                   | date. Recommended for  | Unparalleled           |
|                   | photorealistic images, | flexibility,           |
|                   | sharper clarity,       | contextual             |
|                   | improved spelling and  | understanding, and     |
|                   | typography.            | simple, mask-free      |
|                   |                        | editing. Uniquely      |
|                   |                        | capable of multi-turn  |
|                   |                        | conversational         |
|                   |                        | editing.               |
+-------------------+------------------------+------------------------+
| Availability      | Generally available    | Preview (Production    |
|                   |                        | usage allowed)         |
+-------------------+------------------------+------------------------+
| Latency           | **Low**. Optimized for | Higher. More           |
|                   | near-real-time         | computation is         |
|                   | performance.           | required for its       |
|                   |                        | advanced capabilities. |
+-------------------+------------------------+------------------------+
| Cost              | Cost-effective for     | Token-based pricing.   |
|                   | specialized tasks.     | \$30 per 1 million     |
|                   | \$0.02/image to        | tokens for image       |
|                   | \$0.12/image           | output (image output   |
|                   |                        | tokenized at 1290      |
|                   |                        | tokens per image flat, |
|                   |                        | up to 1024x1024px)     |
+-------------------+------------------------+------------------------+
| Recommended tasks | - Image quality,       | - Interleaved text and |
|                   |   photorealism,        |   image generation to  |
|                   |   artistic detail, or  |   seamlessly blend     |
|                   |   specific styles      |   text and images.     |
|                   |   (e.g.,               | - Combine creative     |
|                   |   impressionism,       |   elements from        |
|                   |   anime) are top       |   multiple images with |
|                   |   priorities.          |   a single prompt.     |
|                   | - Infusing branding,   | - Make highly specific |
|                   |   style, or generating |   edits to images,     |
|                   |   logos and product    |   modify individual    |
|                   |   designs.             |   elements with simple |
|                   | - Generating advanced  |   language commands,   |
|                   |   spelling or          |   and iteratively work |
|                   |   typography.          |   on an image.         |
|                   |                        | - Apply a specific     |
|                   |                        |   design or texture    |
|                   |                        |   from one image to    |
|                   |                        |   another while        |
|                   |                        |   preserving the       |
|                   |                        |   original subject\'s  |
|                   |                        |   form and details.    |
+-------------------+------------------------+------------------------+

Imagen 4 should be your go-to model starting to generate images with
Imagen. Choose Imagen 4 Ultra for advanced use-cases or when you need
the best image quality (note that can only generate one image at a
time).

## What\'s next {#what-is-next data-text="What's next" tabindex="-1"}

- Find more examples and code samples in the [cookbook
  guide](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Image_out.ipynb).
- Check out the [Veo guide](/gemini-api/docs/video) to learn how to
  generate videos with the Gemini API.
- To learn more about Gemini models, see [Gemini
  models](/gemini-api/docs/models/gemini).
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Send feedback

::: devsite-floating-action-buttons
:::

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/), and code samples
are licensed under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0). For details, see
the [Google Developers Site
Policies](https://developers.google.com/site-policies). Java is a
registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-26 UTC.

::: devsite-content-data
Need to tell us more?

\[\[\[\"Easy to
understand\",\"easyToUnderstand\",\"thumb-up\"\],\[\"Solved my
problem\",\"solvedMyProblem\",\"thumb-up\"\],\[\"Other\",\"otherUp\",\"thumb-up\"\]\],\[\[\"Missing
the information I
need\",\"missingTheInformationINeed\",\"thumb-down\"\],\[\"Too
complicated / too many
steps\",\"tooComplicatedTooManySteps\",\"thumb-down\"\],\[\"Out of
date\",\"outOfDate\",\"thumb-down\"\],\[\"Samples / code
issue\",\"samplesCodeIssue\",\"thumb-down\"\],\[\"Other\",\"otherDown\",\"thumb-down\"\]\],\[\"Last
updated 2025-08-26 UTC.\"\],\[\],\[\],null,\[\]\]
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
