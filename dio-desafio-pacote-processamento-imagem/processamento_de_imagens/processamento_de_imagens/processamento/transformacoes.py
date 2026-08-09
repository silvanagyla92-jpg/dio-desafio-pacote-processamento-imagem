from PIL import Image


def resize_image(image_path, width, height, output_path):
    """
    Redimensiona uma imagem e salva o resultado.
    """
    image = Image.open(image_path)
    resized = image.resize((width, height))
    resized.save(output_path)

    return resized

