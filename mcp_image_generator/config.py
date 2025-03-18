import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.huggingface_token = os.getenv('HUGGINGFACE_TOKEN')
        self.default_model = os.getenv('DEFAULT_MODEL', 'stabilityai/stable-diffusion-2-1')
        self.output_dir = os.getenv('OUTPUT_DIR', 'generated_images')