#Recortador de barras pretas

#Importa a biblioteca PIL
from PIL import Image
import easygui
import os

#Funcao que pega o caminho da imagem que sera tratada e separa a extensao do arquivo
def pegaCaminho():
    #Caminho da imagem
    #Abre uma caixa de diálogo que permite selecionar um arquivo ou mais
    caminho = easygui.fileopenbox(multiple=False)

    img_caminho, img_ext = os.path.splitext(caminho)

    return img_caminho, img_ext

#Função para montagem de tupla com as coordenadas passadas no loop
def montaTupla(larguraX,alturaY):
    coordenadasXY = (larguraX, alturaY)
    return coordenadasXY

#Funcao de tratamento da imagem
def trataImagem(imagem_tratamento):
    #Pega o tamanho da imagem como uma tupla e o separa em duas variaveis
    img_X_total, img_Y_total = imagem_tratamento.size

    #Define tupla com posição do primeiro pixel
    prim_pixel = (0,0)

    #Pega o valor da cor do pixel em RGB na posição 0,0
    pix_ini = imagem_tratamento.getpixel(prim_pixel)
    pix_atual = imagem_tratamento.getpixel(prim_pixel)

    #Variáveis contadores
    #cont_pix_alt = 0
    pix_X = 0

    #Loop para iterar sobre os pixels da imagem
    while pix_atual == pix_ini:
        #Contador que define a posição do pixel X na horizontal
        pix_X += 1
        #print(pix_X)

        #Usa a função de montar tupla para definir as coordenadas
        coordenadas = montaTupla(pix_X,0)
        #print(coordenadas)

        #Pega o valor RGB da coordenada passada que será comparada com o valor do pixel 0,0
        pix_atual = imagem_tratamento.getpixel(coordenadas)
        #print(pix_atual)

    #Define as variaveis que serão usadas na área do corte
    pos_esq_corte = pix_X
    pos_cima_corte = 0
    pos_dir_corte = img_X_total - pos_esq_corte
    pos_baixo_corte = img_Y_total

    #Cria tupla para área
    area_corte = (pos_esq_corte, pos_cima_corte, pos_dir_corte, pos_baixo_corte)

    img_cortada = imagem_tratamento.crop(area_corte)
    #img_cortada.show()

    return img_cortada

#Funcao principal
def main():
    #Importa uma imagem
    caminho_img, exten_img = pegaCaminho()
    #print(caminho_img, exten_img)

    #Abre a imagem
    img_import = Image.open(caminho_img + exten_img)

    imagem_tratada = trataImagem(img_import)

    #Salva a imagem
    imagem_tratada.save(caminho_img + "_alt" + exten_img)

if __name__ == "__main__":
    main()