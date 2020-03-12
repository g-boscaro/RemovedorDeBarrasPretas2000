#Recortador de barras pretas

#Importa a biblioteca PIL
from PIL import Image

#Importa uma imagem
img_import = Image.open("preto.png")

#Pega o tamanho da imagem como uma tupla e o separa em duas variaveis
img_X_total, img_Y_total = img_import.size

#Define tupla com posição do primeiro pixel
prim_pixel = (0,0)

#Pega o valor da cor do pixel em RGB na posição 0,0
pix_ini = img_import.getpixel(prim_pixel)
pix_atual = img_import.getpixel(prim_pixel)

#Variáveis contadores
#cont_pix_alt = 0
pix_X = 0

#Função para montagem de tupla com as coordenadas passadas no loop
def montaTupla(larguraX,alturaY):
    coordenadasXY = (larguraX, alturaY)
    return coordenadasXY

#Loop para iterar sobre os pixels da imagem
while pix_atual == pix_ini:
    #Contador que define a posição do pixel X na horizontal
    pix_X += 1
    #print(pix_X)
    
    #Usa a função de montar tupla para definir as coordenadas
    coordenadas = montaTupla(pix_X,0)
    #print(coordenadas)
    
    #Pega o valor RGB da coordenada passada que será comparada com o valor do pixel 0,0
    pix_atual = img_import.getpixel(coordenadas)
    #print(pix_atual)

#Define as variaveis que serão usadas na área do corte
pos_esq_corte = pix_X
pos_cima_corte = 0
pos_dir_corte = img_X_total - pos_esq_corte - 1
pos_baixo_corte = img_Y_total

#Cria tupla para área
area_corte = (pos_esq_corte, pos_cima_corte, pos_dir_corte, pos_baixo_corte)

img_cortada = img_import.crop(area_corte)
#img_cortada.show()

img_cortada.save()
