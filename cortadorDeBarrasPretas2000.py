#Recortador de barras pretas

#PIL para tratar a imagem
from PIL import Image
#easygui para abrir a caixa de diálogo para selecionar o arquivo
import easygui
#os para faciliar o tratamento de paths e extensoes
import os

from time import sleep

#Funcao que pega o caminho da imagem que sera tratada e separa a extensao do arquivo
def pegaCaminho():
    #Caminho da imagem
    #Abre uma caixa de diálogo que permite selecionar um arquivo ou mais
    lista_caminho = easygui.fileopenbox(
        msg = "Escolha um ou mais arquivos", 
        filetypes = ["*.jpg", "*.png", "*.bmp"],
        multiple = True)

    return lista_caminho

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
        coordenadas = (pix_X,0)
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
    lista_caminho = pegaCaminho()
    #print(caminho_img, exten_img)

    #Condicionamento dependendo da quantidade de arquivos na lista
    if lista_caminho == None:
        print("Nenhum arquivo selecionado")
        print("Encerrando...")
        sleep(2.5)
        exit()
    
    elif len(lista_caminho) > 1:
        for arquivo in lista_caminho:
            print("Tratando aquivo:", arquivo)
            sleep(0.5)

            #Separa o caminho e a extensao do arquivo em duas variaveis
            caminho_img, exten_img = os.path.splitext(arquivo)
            #print(caminho_img)
            #print(exten_img)

            #Abre a imagem
            img_import = Image.open(caminho_img + exten_img)

            #Trata a imagem
            imagem_tratada = trataImagem(img_import)

            #Salva a imagem
            imagem_tratada.save(caminho_img + "_noBars" + exten_img)
            print("Finalizado")
            
    else:
        print("Tratando aquivo:", lista_caminho)
        #Separa o caminho e a extensao do arquivo em duas variaveis
        caminho_img, exten_img = os.path.splitext(lista_caminho[0])
        #print(caminho_img)
        #print(exten_img)

        #Abre a imagem
        img_import = Image.open(caminho_img + exten_img)

        #Trata a imagem
        imagem_tratada = trataImagem(img_import)

        #Salva a imagem no caminho passado pelo usuario utilizando a caixa de dialogo do easygui
        imagem_tratada.save(easygui.filesavebox(default=caminho_img + "_noBars" + exten_img))
#        imagem_tratada.save(caminho_img + "_noBars" + exten_img)
        
        print("Finalizado")

if __name__ == "__main__":
    main()