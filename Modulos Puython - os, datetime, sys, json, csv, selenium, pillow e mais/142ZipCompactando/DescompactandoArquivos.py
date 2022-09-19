from zipfile import ZipFile
import os

caminho = r''
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo, in os.listdir(caminho):
        caminhoCompleto = os.path.join(caminho, arquivo)
        zip._writwe(caminhoCompleto, arquivo)
        print(caminhoCompleto)

with ZipFile ('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactando')

