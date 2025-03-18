from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mcp-image-generator",
    version="0.1.0",
    author="TCyberChef",
    author_email="tcyberchef@github.com",
    description="An MCP for generating images using Hugging Face models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TCyberChef/mcp-image-generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "diffusers>=0.25.0",
        "transformers>=4.36.0",
        "torch>=2.0.0",
        "python-dotenv>=1.0.0",
        "pillow>=10.0.0",
        "click>=8.0.0"
    ],
    entry_points={
        'console_scripts': [
            'mcp-image-gen=mcp_image_generator.cli:main',
        ],
    },
)