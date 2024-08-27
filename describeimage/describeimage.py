import tkinter as tk
from tkinter import filedialog

import ollama

root = tk.Tk()
root.withdraw()


def getInput():
    image = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    return image


def describe(image_path):
    res = ollama.chat(
        model="llava",
        messages=[
            {
              'role': 'user',
              'content': "Describe this image in brazilian portuguese. This image will be used in apps and websites and this description will be in the alt text so can't be too long.",
              'images': [image_path]
            }
        ]
    )
    return res['message']['content']


def main():
    try:
        image_path = getInput()
    except Exception as e:
        print(f"{e}")

    description = describe(image_path)
    print(description)


if __name__ == "__main__":
    main()
    input()
