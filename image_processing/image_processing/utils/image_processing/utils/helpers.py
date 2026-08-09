import os


def validate_image_path(image_path):
    """
    Verifica se o caminho da imagem existe.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    return True
