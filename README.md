# MCP Image Generator

An MCP (Model Control Protocol) for generating images using Hugging Face models. This tool is designed to work both with Cursor IDE and as a global CLI tool.

## Features

- Generate images using Hugging Face's free models
- Local integration with Cursor IDE
- Global CLI tool functionality
- Easy to configure and use
- Support for multiple image generation models

## Installation

### Local Installation (Cursor IDE)

```bash
pip install -e .
```

### Global Installation

```bash
pip install -e . --user
```

## Usage

### As a Cursor MCP

The tool will be automatically available in Cursor IDE after installation.

### As a CLI Tool

```bash
mcp-image-gen --prompt "your image description" --model "model-name" --output "output-path"
```

## Configuration

Create a `.env` file in your project root:

```env
HUGGINGFACE_TOKEN=your_token_here
```

## Models

Currently supported models:
- Stable Diffusion
- More coming soon...

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT