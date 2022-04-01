from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    description="A small package for Which Bollywood Celebrity You look like? Deep Learning Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'mtcnn==0.1.0',
        'tensorflow',
        'keras',
        'keras-vggface==0.6',
        'keras_applications==1.0.8',
        'PyYAML',
        'tqdm',
        'scikit-learn',
        'streamlit',
        'bing-image-downloader'
    ]
)