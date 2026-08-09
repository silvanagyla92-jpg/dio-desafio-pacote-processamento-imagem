from PIL import Image


def redimensionar_imagem(caminho_imagem, largura, altura, caminho_saida):
    """
    Redimensiona uma imagem e salva o resultado.
    """
    imagem = Image.open(caminho_imagem)
    imagem_redimensionada = imagem.resize((largura, altura))
    imagem_redimensionada.save(caminho_saida)

    return imagem_redimensionada
