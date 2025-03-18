from .generator import ImageGenerator
from .config import Config

def generate_image(prompt: str, model: str = None, output_path: str = None):
    """MCP function to generate images"""
    config = Config()
    generator = ImageGenerator(config)

    if model:
        generator.load_model(model)

    return generator.generate(prompt, output_path)