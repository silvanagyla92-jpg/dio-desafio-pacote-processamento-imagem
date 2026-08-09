from PIL import Image


def resize_image(image_path, width, height, output_path):
    """
    Resizes an image and saves the result.
    """
    image = Image.open(image_path)
    resized = image.resize((width, height))
    resized.save(output_path)

    return resized
