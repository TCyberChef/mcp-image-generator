import click
from .generator import ImageGenerator
from .config import Config
from pathlib import Path

@click.command()
@click.option('--prompt', required=True, help='The prompt to generate an image from')
@click.option('--model', default=None, help='The model to use for generation')
@click.option('--output', default=None, help='Output path for the generated image')
def main(prompt, model, output):
    """Generate images using Hugging Face models"""
    config = Config()
    generator = ImageGenerator(config)

    if model:
        generator.load_model(model)

    if not output:
        output = Path(config.output_dir) / f"{prompt[:30].replace(' ', '_')}.png"

    try:
        image = generator.generate(prompt, str(output))
        click.echo(f"Image generated successfully at: {output}")
    except Exception as e:
        click.echo(f"Error generating image: {str(e)}", err=True)

if __name__ == '__main__':
    main()