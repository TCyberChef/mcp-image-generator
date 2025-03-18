from diffusers import StableDiffusionPipeline
import torch
from pathlib import Path
from .config import Config

class ImageGenerator:
    def __init__(self, config: Config):
        self.config = config
        self.model = None

    def load_model(self, model_id="stabilityai/stable-diffusion-2-1"):
        """Load the specified model"""
        self.model = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")

    def generate(self, prompt: str, output_path: str = None, **kwargs):
        """Generate an image from the prompt"""
        if self.model is None:
            self.load_model()

        image = self.model(prompt, **kwargs).images[0]
        
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            image.save(output_path)

        return image