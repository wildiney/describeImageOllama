# Image Describer with Ollama

This code use Ollama LLaVa to recognize and describe images. The output will be in brazilian portuguese, but you can change the prompt.

## Installation

Yout can run the python script directly after install the dependencies

```python
poetry shell 
poetry install
poetry run python describeimage/describeimage.py
```

It's possible to generata an executable file running

```python
pyinstaller --onefile describeimage/describeimage.py
```

After generating the file is available at dist folder.
