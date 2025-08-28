"""Prompt templates for NanoBanana Pro based on Gemini best practices."""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass

@dataclass
class TemplateParameter:
    """Represents a template parameter."""
    name: str
    description: str
    example: str
    default: str = ""  # Smart default value
    required: bool = False  # Most parameters are optional now
    level: str = "optional"  # essential/optional/advanced
    suggestions: List[str] = None  # Quick selection options
    
    def __post_init__(self):
        if self.suggestions is None:
            self.suggestions = []
        # If no default provided, use example as default
        if not self.default:
            self.default = self.example

@dataclass 
class PromptTemplate:
    """Represents a prompt template."""
    name: str
    description: str
    template: str
    parameters: List[TemplateParameter]
    example: str

class TemplateManager:
    """Manages prompt templates for different themes and modes."""
    
    def __init__(self):
        self._text_to_image_templates = self._init_text_to_image_templates()
        self._image_editing_templates = self._init_image_editing_templates()
    
    def _init_text_to_image_templates(self) -> Dict[str, PromptTemplate]:
        """Initialize text-to-image templates."""
        return {
            "photorealistic": PromptTemplate(
                name="Photorealistic Scenes",
                description="Generate realistic photographs with professional quality",
                template="A photorealistic {shot_type} of {subject}, {action_expression}, set in {environment}. The scene is illuminated by {lighting_description}, creating a {mood} atmosphere. Captured with a {camera_lens_details}, emphasizing {key_textures_details}. The image should be in a {aspect_ratio} format.",
                parameters=[
                    TemplateParameter(
                        name="subject", 
                        description="Main subject of the photo", 
                        example="elderly Japanese ceramicist",
                        default="a person",
                        required=True,
                        level="essential",
                        suggestions=["person", "landscape", "object", "animal", "building"]
                    ),
                    TemplateParameter(
                        name="shot_type", 
                        description="Type of camera shot", 
                        example="close-up portrait",
                        default="medium shot",
                        level="optional",
                        suggestions=["close-up", "medium shot", "wide shot", "portrait", "full body"]
                    ),
                    TemplateParameter(
                        name="action_expression", 
                        description="Action or expression", 
                        example="carefully inspecting a freshly glazed tea bowl",
                        default="natural pose",
                        level="optional",
                        suggestions=["smiling", "working", "relaxed", "concentrated", "natural pose"]
                    ),
                    TemplateParameter(
                        name="environment", 
                        description="Setting/environment", 
                        example="rustic, sun-drenched workshop",
                        default="indoor setting",
                        level="optional",
                        suggestions=["indoor", "outdoor", "studio", "natural", "urban"]
                    ),
                    TemplateParameter(
                        name="lighting_description", 
                        description="Lighting setup", 
                        example="soft, golden hour light streaming through a window",
                        default="natural lighting",
                        level="advanced",
                        suggestions=["natural light", "soft lighting", "dramatic lighting", "golden hour", "studio lighting"]
                    ),
                    TemplateParameter(
                        name="mood", 
                        description="Overall mood", 
                        example="serene and masterful",
                        default="calm",
                        level="optional",
                        suggestions=["calm", "energetic", "mysterious", "warm", "professional"]
                    ),
                    TemplateParameter(
                        name="camera_lens_details", 
                        description="Camera/lens details", 
                        example="85mm portrait lens",
                        default="standard lens",
                        level="advanced",
                        suggestions=["standard lens", "portrait lens", "wide-angle lens", "telephoto lens", "macro lens"]
                    ),
                    TemplateParameter(
                        name="key_textures_details", 
                        description="Key textures and details", 
                        example="fine texture of the clay",
                        default="natural textures",
                        level="optional",
                        suggestions=["natural textures", "smooth surfaces", "detailed textures", "soft materials", "sharp details"]
                    ),
                    TemplateParameter(
                        name="aspect_ratio", 
                        description="Image format", 
                        example="vertical portrait orientation",
                        default="horizontal format",
                        level="advanced",
                        suggestions=["horizontal", "vertical", "square", "panoramic", "standard format"]
                    )
                ],
                example="A photorealistic close-up portrait of an elderly Japanese ceramicist with deep, sun-etched wrinkles and a warm, knowing smile, carefully inspecting a freshly glazed tea bowl, set in his rustic, sun-drenched workshop. The scene is illuminated by soft, golden hour light streaming through a window, creating a serene and masterful atmosphere. Captured with an 85mm portrait lens, emphasizing the fine texture of the clay. The image should be in a vertical portrait orientation format."
            ),
            
            "stylized": PromptTemplate(
                name="Stylized Illustrations & Stickers",
                description="Create vector-style graphics, logos, and digital assets",
                template="A {style} sticker of a {subject}, featuring {key_characteristics} and a {color_palette}. The design should have {line_style} and {shading_style}. The background must be {background_type}.",
                parameters=[
                    TemplateParameter(
                        name="subject",
                        description="Main subject to draw",
                        example="happy red panda wearing a tiny bamboo hat",
                        default="cute animal character",
                        required=True,
                        level="essential",
                        suggestions=["cute animal", "cartoon character", "logo icon", "food item", "plant/flower"]
                    ),
                    TemplateParameter(
                        name="style",
                        description="Art style",
                        example="kawaii-style",
                        default="cute cartoon style",
                        level="optional",
                        suggestions=["kawaii", "minimalist", "vintage", "modern", "hand-drawn"]
                    ),
                    TemplateParameter(
                        name="key_characteristics",
                        description="Key visual characteristics",
                        example="munching on a green bamboo leaf",
                        default="cheerful expression",
                        level="optional",
                        suggestions=["smiling", "playful pose", "colorful details", "simple design", "expressive eyes"]
                    ),
                    TemplateParameter(
                        name="color_palette",
                        description="Color scheme",
                        example="vibrant color palette",
                        default="bright colors",
                        level="optional",
                        suggestions=["vibrant colors", "pastel colors", "monochrome", "rainbow", "warm tones"]
                    ),
                    TemplateParameter(
                        name="line_style",
                        description="Line work style",
                        example="bold, clean outlines",
                        default="clean outlines",
                        level="advanced",
                        suggestions=["bold outlines", "thin lines", "no outlines", "sketchy lines", "smooth curves"]
                    ),
                    TemplateParameter(
                        name="shading_style",
                        description="Shading technique",
                        example="simple cel-shading",
                        default="flat colors",
                        level="advanced",
                        suggestions=["flat colors", "cel-shading", "gradient shading", "no shading", "soft shadows"]
                    ),
                    TemplateParameter(
                        name="background_type",
                        description="Background type",
                        example="transparent",
                        default="white background",
                        level="optional",
                        suggestions=["transparent", "white", "colored", "gradient", "pattern"]
                    )
                ],
                example="A kawaii-style sticker of a happy red panda wearing a tiny bamboo hat, featuring it munching on a green bamboo leaf and a vibrant color palette. The design should have bold, clean outlines and simple cel-shading. The background must be white."
            ),
            
            "text_in_images": PromptTemplate(
                name="Accurate Text in Images",
                description="Generate images with legible, well-placed text",
                template="Create a {image_type} for {brand_concept} with the text \"{text_to_render}\" in a {font_style}. The design should be {style_description}, with a {color_scheme}.",
                parameters=[
                    TemplateParameter(
                        name="text_to_render",
                        description="Text to include in image",
                        example="The Daily Grind",
                        default="Sample Text",
                        required=True,
                        level="essential",
                        suggestions=["Logo Name", "Brand Name", "Slogan", "Title", "Message"]
                    ),
                    TemplateParameter(
                        name="image_type",
                        description="Type of image",
                        example="modern, minimalist logo",
                        default="simple logo",
                        level="optional",
                        suggestions=["logo", "poster", "banner", "sign", "business card"]
                    ),
                    TemplateParameter(
                        name="brand_concept",
                        description="Brand or concept",
                        example="coffee shop called 'The Daily Grind'",
                        default="modern business",
                        level="optional",
                        suggestions=["coffee shop", "restaurant", "tech company", "store", "creative agency"]
                    ),
                    TemplateParameter(
                        name="font_style",
                        description="Font style",
                        example="clean, bold, sans-serif font",
                        default="clean font",
                        level="optional",
                        suggestions=["bold font", "elegant font", "modern font", "playful font", "classic font"]
                    ),
                    TemplateParameter(
                        name="style_description",
                        description="Style description",
                        example="featuring a simple, stylized coffee bean icon seamlessly integrated with the text",
                        default="clean and professional design",
                        level="optional",
                        suggestions=["with icon", "minimalist design", "decorative elements", "geometric shapes", "simple layout"]
                    ),
                    TemplateParameter(
                        name="color_scheme",
                        description="Color scheme",
                        example="black and white",
                        default="professional colors",
                        level="optional",
                        suggestions=["black and white", "colorful", "monochrome", "brand colors", "neutral tones"]
                    )
                ],
                example="Create a modern, minimalist logo for a coffee shop called 'The Daily Grind' with the text \"The Daily Grind\" in a clean, bold, sans-serif font. The design should be featuring a simple, stylized coffee bean icon seamlessly integrated with the text, with a black and white color scheme."
            ),
            
            "product_mockup": PromptTemplate(
                name="Product Mockups & Commercial Photography",
                description="Professional product photography and commercial imagery",
                template="A high-resolution, studio-lit product photograph of a {product_description} on a {background_surface}. The lighting is a {lighting_setup} to {lighting_purpose}. The camera angle is a {angle_type} to showcase {specific_feature}. Ultra-realistic, with sharp focus on {key_detail}. {aspect_ratio}.",
                parameters=[
                    TemplateParameter(
                        name="product_description",
                        description="Product to photograph",
                        example="minimalist ceramic coffee mug in matte black",
                        default="product item",
                        required=True,
                        level="essential",
                        suggestions=["coffee mug", "phone case", "skincare bottle", "book cover", "jewelry"]
                    ),
                    TemplateParameter(
                        name="background_surface",
                        description="Background/surface",
                        example="polished concrete surface",
                        default="clean white surface",
                        level="optional",
                        suggestions=["white background", "wooden table", "marble surface", "fabric backdrop", "concrete surface"]
                    ),
                    TemplateParameter(
                        name="lighting_setup",
                        description="Lighting setup",
                        example="three-point softbox setup",
                        default="professional lighting",
                        level="advanced",
                        suggestions=["soft lighting", "natural lighting", "studio lighting", "dramatic lighting", "even lighting"]
                    ),
                    TemplateParameter(
                        name="lighting_purpose",
                        description="Lighting purpose",
                        example="create soft, diffused highlights and eliminate harsh shadows",
                        default="create professional look",
                        level="advanced",
                        suggestions=["soft highlights", "even illumination", "dramatic effect", "natural look", "commercial appeal"]
                    ),
                    TemplateParameter(
                        name="angle_type",
                        description="Camera angle",
                        example="slightly elevated 45-degree shot",
                        default="straight-on view",
                        level="optional",
                        suggestions=["front view", "45-degree angle", "overhead shot", "side view", "close-up"]
                    ),
                    TemplateParameter(
                        name="specific_feature",
                        description="Feature to showcase",
                        example="clean lines",
                        default="product design",
                        level="optional",
                        suggestions=["clean lines", "texture details", "color", "shape", "quality"]
                    ),
                    TemplateParameter(
                        name="key_detail",
                        description="Key detail to focus on",
                        example="steam rising from the coffee",
                        default="product details",
                        level="optional",
                        suggestions=["texture", "surface finish", "branding", "craftsmanship", "material quality"]
                    ),
                    TemplateParameter(
                        name="aspect_ratio",
                        description="Image format",
                        example="Square image",
                        default="horizontal format",
                        level="advanced",
                        suggestions=["square", "horizontal", "vertical", "wide format", "standard ratio"]
                    )
                ],
                example="A high-resolution, studio-lit product photograph of a minimalist ceramic coffee mug in matte black on a polished concrete surface. The lighting is a three-point softbox setup to create soft, diffused highlights and eliminate harsh shadows. The camera angle is a slightly elevated 45-degree shot to showcase its clean lines. Ultra-realistic, with sharp focus on the steam rising from the coffee. Square image."
            ),
            
            "minimalist": PromptTemplate(
                name="Minimalist & Negative Space Design",
                description="Clean, spacious designs ideal for text overlay",
                template="A minimalist composition featuring a single {subject} positioned in the {position} of the frame. The background is a vast, empty {color} canvas, creating significant negative space. Soft, subtle lighting from {lighting_direction}. {aspect_ratio}.",
                parameters=[
                    TemplateParameter(
                        name="subject",
                        description="Single subject",
                        example="delicate red maple leaf",
                        default="simple object",
                        required=True,
                        level="essential",
                        suggestions=["leaf", "flower", "stone", "branch", "geometric shape"]
                    ),
                    TemplateParameter(
                        name="position",
                        description="Position in frame",
                        example="bottom-right",
                        default="center",
                        level="optional",
                        suggestions=["center", "bottom-right", "top-left", "left side", "right side"]
                    ),
                    TemplateParameter(
                        name="color",
                        description="Background color",
                        example="off-white",
                        default="white",
                        level="optional",
                        suggestions=["white", "off-white", "light gray", "cream", "soft beige"]
                    ),
                    TemplateParameter(
                        name="lighting_direction",
                        description="Lighting direction",
                        example="the top left",
                        default="above",
                        level="advanced",
                        suggestions=["above", "top left", "side", "diffused", "natural"]
                    ),
                    TemplateParameter(
                        name="aspect_ratio",
                        description="Image format",
                        example="Square image",
                        default="square format",
                        level="advanced",
                        suggestions=["square", "horizontal", "vertical", "wide", "portrait"]
                    )
                ],
                example="A minimalist composition featuring a single, delicate red maple leaf positioned in the bottom-right of the frame. The background is a vast, empty off-white canvas, creating significant negative space for text. Soft, diffused lighting from the top left. Square image."
            ),
            
            "sequential_art": PromptTemplate(
                name="Sequential Art (Comic Panel / Storyboard)",
                description="Comic-style panels and visual storytelling",
                template="A single comic book panel in a {art_style} style. In the foreground, {character_description_action}. In the background, {setting_details}. The panel has a {dialogue_caption_box} with the text \"{text_content}\". The lighting creates a {mood} mood. {aspect_ratio}.",
                parameters=[
                    TemplateParameter(
                        name="character_description_action",
                        description="Character and action",
                        example="a detective in a trench coat stands under a flickering streetlamp, rain soaking his shoulders",
                        default="a character in action",
                        required=True,
                        level="essential",
                        suggestions=["hero standing", "character running", "person talking", "figure walking", "character sitting"]
                    ),
                    TemplateParameter(
                        name="text_content",
                        description="Text content for speech/caption",
                        example="The city was a tough place to keep secrets.",
                        default="Sample dialogue",
                        level="optional",
                        suggestions=["Dialogue text", "Narration", "Thought bubble", "Sound effect", "Caption"]
                    ),
                    TemplateParameter(
                        name="art_style",
                        description="Art style",
                        example="gritty, noir art style with high-contrast black and white inks",
                        default="comic book style",
                        level="optional",
                        suggestions=["manga style", "superhero comic", "noir style", "cartoon style", "realistic art"]
                    ),
                    TemplateParameter(
                        name="setting_details",
                        description="Background setting",
                        example="the neon sign of a desolate bar reflects in a puddle",
                        default="simple background",
                        level="optional",
                        suggestions=["city street", "indoor room", "forest scene", "space setting", "school hallway"]
                    ),
                    TemplateParameter(
                        name="dialogue_caption_box",
                        description="Box type",
                        example="caption box at the top",
                        default="speech bubble",
                        level="optional",
                        suggestions=["speech bubble", "thought bubble", "caption box", "narration box", "no text box"]
                    ),
                    TemplateParameter(
                        name="mood",
                        description="Lighting mood",
                        example="dramatic, somber",
                        default="normal lighting",
                        level="advanced",
                        suggestions=["dramatic", "bright", "dark", "mysterious", "cheerful"]
                    ),
                    TemplateParameter(
                        name="aspect_ratio",
                        description="Image format",
                        example="Landscape",
                        default="landscape format",
                        level="advanced",
                        suggestions=["landscape", "square", "portrait", "wide panel", "tall panel"]
                    )
                ],
                example="A single comic book panel in a gritty, noir art style with high-contrast black and white inks. In the foreground, a detective in a trench coat stands under a flickering streetlamp, rain soaking his shoulders. In the background, the neon sign of a desolate bar reflects in a puddle. A caption box at the top reads \"The city was a tough place to keep secrets.\" The lighting is harsh, creating a dramatic, somber mood. Landscape."
            )
        }
    
    def _init_image_editing_templates(self) -> Dict[str, PromptTemplate]:
        """Initialize image editing templates."""
        return {
            "add_remove": PromptTemplate(
                name="Adding and Removing Elements",
                description="Add new objects or remove existing ones from images",
                template="Using the provided image of {subject}, please {action} {element} {preposition} the scene. Ensure the change is {integration_description}.",
                parameters=[
                    TemplateParameter(
                        name="subject",
                        description="Subject in image",
                        example="my cat",
                        default="the subject",
                        required=True,
                        level="essential",
                        suggestions=["person", "animal", "object", "landscape", "building"]
                    ),
                    TemplateParameter(
                        name="action",
                        description="Action to perform",
                        example="add",
                        default="add",
                        level="essential",
                        suggestions=["add", "remove", "replace", "modify", "enhance"]
                    ),
                    TemplateParameter(
                        name="element",
                        description="Element to add/remove",
                        example="a small, knitted wizard hat on its head",
                        default="something new",
                        required=True,
                        level="essential",
                        suggestions=["hat", "glasses", "background object", "decoration", "accessory"]
                    ),
                    TemplateParameter(
                        name="preposition",
                        description="Preposition (to/from)",
                        example="to",
                        default="to",
                        level="optional",
                        suggestions=["to", "from", "in", "on", "beside"]
                    ),
                    TemplateParameter(
                        name="integration_description",
                        description="How change should integrate",
                        example="sitting comfortably and matches the soft lighting of the photo",
                        default="naturally integrated",
                        level="optional",
                        suggestions=["naturally integrated", "seamlessly blended", "matching lighting", "realistic placement", "professional look"]
                    )
                ],
                example="Using the provided image of my cat, please add a small, knitted wizard hat on its head to the scene. Ensure the change is sitting comfortably and matches the soft lighting of the photo."
            ),
            
            "inpainting": PromptTemplate(
                name="Inpainting (Semantic Masking)",
                description="Edit specific parts of images while preserving the rest",
                template="Using the provided image, change only the {specific_element} to {new_element}. Keep everything else in the image exactly the same, preserving the original style, lighting, and composition.",
                parameters=[
                    TemplateParameter(
                        name="specific_element",
                        description="Element to change",
                        example="blue sofa",
                        default="object in image",
                        required=True,
                        level="essential",
                        suggestions=["sofa", "chair", "table", "wall color", "clothing"]
                    ),
                    TemplateParameter(
                        name="new_element",
                        description="New element description",
                        example="a vintage, brown leather chesterfield sofa",
                        default="different version",
                        required=True,
                        level="essential",
                        suggestions=["different color", "different style", "different material", "different design", "new object"]
                    )
                ],
                example="Using the provided image of a living room, change only the blue sofa to be a vintage, brown leather chesterfield sofa. Keep the rest of the room, including the pillows on the sofa and the lighting, unchanged."
            ),
            
            "style_transfer": PromptTemplate(
                name="Style Transfer",
                description="Apply artistic styles to existing photographs",
                template="Transform the provided photograph of {subject} into the artistic style of {artist_art_style}. Preserve the original composition but render it with {stylistic_elements}.",
                parameters=[
                    TemplateParameter(
                        name="subject",
                        description="Subject in photo",
                        example="a modern city street at night",
                        default="the scene",
                        level="optional",
                        suggestions=["cityscape", "portrait", "landscape", "building", "nature scene"]
                    ),
                    TemplateParameter(
                        name="artist_art_style",
                        description="Artist or art style",
                        example="Vincent van Gogh's 'Starry Night'",
                        default="artistic style",
                        required=True,
                        level="essential",
                        suggestions=["Van Gogh style", "Picasso style", "watercolor", "oil painting", "impressionist"]
                    ),
                    TemplateParameter(
                        name="stylistic_elements",
                        description="Stylistic elements",
                        example="swirling, impasto brushstrokes and a dramatic palette of deep blues and bright yellows",
                        default="artistic brushstrokes",
                        level="optional",
                        suggestions=["brushstrokes", "color palette", "texture", "artistic technique", "visual effects"]
                    )
                ],
                example="Transform the provided photograph of a modern city street at night into the artistic style of Vincent van Gogh's 'Starry Night'. Preserve the original composition of buildings and cars, but render all elements with swirling, impasto brushstrokes and a dramatic palette of deep blues and bright yellows."
            ),
            
            "composition": PromptTemplate(
                name="Advanced Composition (Combining Multiple Images)",
                description="Merge elements from multiple source images",
                template="Create a new image by combining the elements from the provided images. Take the {element_from_image1} and place it with/on the {element_from_image2}. The final image should be a {final_scene_description}.",
                parameters=[
                    TemplateParameter(
                        name="element_from_image1",
                        description="Element from first image",
                        example="blue floral dress from the first image",
                        default="element from first image",
                        required=True,
                        level="essential",
                        suggestions=["clothing item", "object", "person", "background", "accessory"]
                    ),
                    TemplateParameter(
                        name="element_from_image2",
                        description="Element from second image",
                        example="woman from the second image",
                        default="element from second image",
                        required=True,
                        level="essential",
                        suggestions=["person", "background scene", "object", "setting", "model"]
                    ),
                    TemplateParameter(
                        name="final_scene_description",
                        description="Final scene description",
                        example="realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment",
                        default="combined realistic scene",
                        level="optional",
                        suggestions=["professional photo", "realistic scene", "natural composition", "seamless blend", "studio quality"]
                    )
                ],
                example="Create a professional e-commerce fashion photo. Take the blue floral dress from the first image and let the woman from the second image wear it. Generate a realistic, full-body shot of the woman wearing the dress, with the lighting and shadows adjusted to match the outdoor environment."
            ),
            
            "detail_preservation": PromptTemplate(
                name="High-Fidelity Detail Preservation",
                description="Precise editing while maintaining critical details",
                template="Using the provided images, place {element_from_image2} onto {element_from_image1}. Ensure that the features of {element_from_image1} remain completely unchanged. The added element should {integration_description}.",
                parameters=[
                    TemplateParameter(
                        name="element_from_image2",
                        description="Element from second image",
                        example="the logo from the second image",
                        default="element to add",
                        required=True,
                        level="essential",
                        suggestions=["logo", "text", "pattern", "design", "graphic"]
                    ),
                    TemplateParameter(
                        name="element_from_image1",
                        description="Element from first image",
                        example="her black t-shirt",
                        default="target location",
                        required=True,
                        level="essential",
                        suggestions=["t-shirt", "wall", "surface", "background", "object"]
                    ),
                    TemplateParameter(
                        name="integration_description",
                        description="Integration description",
                        example="look like it's naturally printed on the fabric, following the folds of the shirt",
                        default="naturally integrated",
                        level="optional",
                        suggestions=["naturally printed", "seamlessly placed", "realistic integration", "following surface contours", "professional placement"]
                    )
                ],
                example="Take the first image of the woman with brown hair, blue eyes, and a neutral expression. Add the logo from the second image onto her black t-shirt. Ensure the woman's face and features remain completely unchanged. The logo should look like it's naturally printed on the fabric, following the folds of the shirt."
            )
        }
    
    def get_text_to_image_template(self, theme: str) -> Optional[PromptTemplate]:
        """Get text-to-image template by theme."""
        return self._text_to_image_templates.get(theme)
    
    def get_image_editing_template(self, feature: str) -> Optional[PromptTemplate]:
        """Get image editing template by feature."""
        return self._image_editing_templates.get(feature)
    
    def get_all_text_to_image_themes(self) -> List[str]:
        """Get all available text-to-image themes."""
        return list(self._text_to_image_templates.keys())
    
    def get_all_image_editing_features(self) -> List[str]:
        """Get all available image editing features."""
        return list(self._image_editing_templates.keys())
    
    def fill_template(self, template: PromptTemplate, parameters: Dict[str, str]) -> str:
        """Fill template with provided parameters."""
        filled = template.template
        
        # Create complete parameter dict with defaults for missing values
        complete_params = {}
        for param in template.parameters:
            if param.name in parameters:
                complete_params[param.name] = parameters[param.name]
            else:
                complete_params[param.name] = param.default or param.example
        
        # Replace all placeholders
        for param_name, param_value in complete_params.items():
            placeholder = "{" + param_name + "}"
            filled = filled.replace(placeholder, param_value)
        
        return filled

# Global template manager instance
template_manager = TemplateManager()