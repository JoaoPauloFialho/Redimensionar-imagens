from PIL import Image
from time import sleep
import os


def redimensionar(caminho, new_whidt):

    '''
    :param caminho: caminho da imagem que você quer redimensionar
    :param new_whidt: nova largura da foto
    '''

    for raiz, dir, files in os.walk(caminho):
        for file in files:
            caminho_completo = os.path.join(raiz, file)
            tag_convertido = '_CONVERTIDA'
            nome_arquivo, extensao = os.path.splitext(file)
            new_path_file = caminho_completo + tag_convertido + extensao

            if tag_convertido in caminho_completo:
                print('Arquivo já convertido')
                continue

            imagem_pillow = Image.open(caminho_completo)
            whidt, height = imagem_pillow.size
            new_height = round((new_whidt * height)/whidt)
            new_image = imagem_pillow.resize((new_whidt, new_height))
            new_image.save(
                new_path_file,
                optimize=True,
                quality=70
            )

            print(f'{new_path_file} foi convertida')
            sleep(0.5)
            new_image.close()
            imagem_pillow.close()
            os.remove(caminho_completo)


def reverter(caminho, whidt, height):

    '''
    :param caminho: caminho da imagem que você quer reverter
    :param whidt: largura da imagem
    :param height:  altura da imagem
    '''

    for root, dir, files in os.walk(caminho):
        for file in files:
            caminho_completo = os.path.join(root, file)
            tag_original = '_ORIGINAL'
            nome_arquivo, extensao = os.path.splitext(file)
            novo_caminho = caminho_completo + tag_original + extensao

            if tag_original in caminho_completo:
                print(f'{novo_caminho} já está no seu tamanho original')
                continue

            imagem_original = Image.open(caminho_completo)
            nova_imagem = imagem_original.resize((whidt, height))
            nova_imagem.save(
                novo_caminho,
                optimize=True,
            )
            print(f'{caminho_completo} voltou ao tamanho original')
            sleep(1)
            imagem_original.close()
            nova_imagem.close()
            os.remove(caminho_completo)


if __name__ == '__main__':

    caminho_imagens = input('Digite o diretório da imagem (sub-pastas serão analisadas) -> ')
    escolha = input('As imagens estão reduzidas? ').upper()

    if escolha[0] == 'S':
        escolha = input('Deseja reverter? ').upper()
        if escolha[0] == 'S':
            largura = int(input('Largura -> '))
            altura = int(input('Altura -> '))
            reverter(caminho_imagens, largura, altura)

    else:
        largura = int(input('Qual largura da nova foto? '))
        redimensionar(caminho_imagens, largura)
