#Recortador de barras pretas

#PIL para tratar a imagem
from PIL import Image
#easygui para abrir a caixa de diálogo para selecionar o arquivo
import easygui
#os para faciliar o tratamento de paths e extensoes
import os
#Importa a funcao de sleep para controlar o tempo que as mensagens ficam em exibicao
from time import sleep

#Funcao que pega o caminho da imagem que sera tratada e separa a extensao do arquivo
def pegaCaminho():
    #Caminho da imagem
    #Abre uma caixa de diálogo que permite selecionar um arquivo ou mais
    lista_arquivos = easygui.fileopenbox(
        msg = "Escolha um ou mais arquivos", 
        filetypes = ["*.jpg", "*.png", "*.bmp"],
        multiple = True)

    return lista_arquivos

#Funcao de tratamento da imagem
def trataImagem(imagem_tratamento):
    #Pega as dimensões da imagem como uma tupla e separa em duas variaveis
    img_X_total, img_Y_total = imagem_tratamento.size

    #Define tupla com posição do primeiro pixel
    prim_pixel = (0,0)

    #Pega o valor da cor do pixel em RGB(R, G, B) na posição 0,0
    pix_ini = imagem_tratamento.getpixel(prim_pixel)
    pix_atual = imagem_tratamento.getpixel(prim_pixel)

    #Variáveis contadores
    #cont_pix_alt = 0
    pix_X = 0

    #Loop para iterar sobre os pixels da imagem
    while pix_atual == pix_ini:
        #Contador que define a posição do pixel X, na horizontal
        pix_X += 1
        #print(pix_X)

        #Usa a função de montar tupla para definir as coordenadas na primeira linha de pixels da imagem
        coordenadas = (pix_X,0)
        #print(coordenadas)

        #Pega o valor RGB da coordenada passada que será comparada com o valor RGB do pixel 0,0
        pix_atual = imagem_tratamento.getpixel(coordenadas)
        #print(pix_atual)

    #Define as variaveis que serão usadas na área do corte da imagem
    pos_esq_corte = pix_X
    pos_cima_corte = 0
    pos_dir_corte = img_X_total - pos_esq_corte
    pos_baixo_corte = img_Y_total

    #Cria tupla para área do corte
    area_corte = (pos_esq_corte, pos_cima_corte, pos_dir_corte, pos_baixo_corte)

    img_cortada = imagem_tratamento.crop(area_corte)
    #img_cortada.show()

    return img_cortada

#Função que cria novo diretorio, extrai nome e extensão do arquivo
def manipulaArq(caminho):
    #Pega o nome do diretorio
    nome_dir = os.path.dirname(caminho)

    #Extrai somento o nome do arquivo com extensão
    arquivo_completo = os.path.basename(caminho)
    #Separa o nome do arquivo da extensão
    nome_arquivo, extensao = os.path.splitext(arquivo_completo)

    #Cria caminho com o final \No_bars
    novo_path = nome_dir + "\\Sem_barras\\"
    #print(novo_path)

    #Verifica a existencia do novo caminho
    check_dir = os.path.exists(novo_path)
    #print(check_dir)

    #Trata a existencia do novo caminho
    #Se não existir cria o diretorio e retorna o caminho
    if check_dir == False:
        os.mkdir(novo_path)
        return novo_path, nome_arquivo, extensao
    #Se existir só retorna o caminho
    else:
        return novo_path, nome_arquivo, extensao

#Funcao principal
def main():
    #-----Importa uma imagem
    print("Selecione o/os arquivo/os que será/serão tratado/os.")
    sleep(0.5)
    lista_arquivos = pegaCaminho()
    #print(caminho_img, exten_img)

    #-----Condicionamento dependendo da quantidade de arquivos na lista
    #Se nenhum arquivo, fecha o programa
    if lista_arquivos == None:
        print("Nenhum arquivo selecionado.")
        print("Encerrando programa...")
        sleep(1)
        exit()
    
    #-----Tratamento de multiplos arquivos
    #Se mais de um arquivo, trata cada arquivo da lista
    elif len(lista_arquivos) > 1:
        print ("Foram selecionados:", len(lista_arquivos), "arquivos.")

        for arquivo in lista_arquivos:
            print("Tratando aquivo:", arquivo)
            sleep(0.5)

            #-----Trata se o arquivo enviado é uma imagem, se sim, o abre, se não, pula para o próximo item da lista
            try:
                #Abre imagem
                img_import = Image.open(arquivo)
                #Verifica se é uma imagem
                img_import.verify()
                #Abre novamente a imagem
                img_import = Image.open(arquivo)
            except:
                print("Arquivo invalido.")
                continue

            #-----Trata a imagem
            imagem_tratada = trataImagem(img_import)

            #-----Cria novo diretorio onde irão as imagens, extrai o nome e a extensao dos arquivos originais
            novo_caminho, nome_arq, ext_arq = manipulaArq(arquivo)

            #-----Salva a imagem
            imagem_tratada.save(novo_caminho + nome_arq + ext_arq)
            print("Arquivo processado.")
            sleep(0.5)

    #-----Tratamento para apenas um arquivo
    else:
        print("Tratando aquivo:", lista_arquivos[0])

        #-----Trata se o arquivo enviado é uma imagem, se sim, o abre, se não, encerra o programa
        try:
            img_import = Image.open(lista_arquivos[0])
            img_import.verify()
            #Arquivo deve ser reaberto para que o PIL consiga tratar a imagem
            img_import = Image.open(lista_arquivos[0])
        except:
            print("Arquivo invalido.")
            print("Encerrando programa...")
            sleep(1)
            exit()

        #-----Trata a imagem
        imagem_tratada = trataImagem(img_import)

        #-----Cria novo diretorio onde irá a imagem tratada, extrai o nome e a extensao do arquivo original
        novo_caminho, nome_arq, ext_arq = manipulaArq(lista_arquivos[0])

        #-----Salva a imagem no novo caminho, com a 
        imagem_tratada.save(novo_caminho + nome_arq + ext_arq)
        
        print("Arquivo processado.")
        sleep(0.5)
        print("Encerrando programa.")
        sleep(1)

if __name__ == "__main__":
    main()