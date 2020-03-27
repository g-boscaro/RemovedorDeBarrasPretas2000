from PIL import Image, ImageFilter

#Abre a imagem indicada
im = Image.open("dispatch.png")

#Salva a imagem num arquivo temporário e 
#abre um programa(Paint, Visualizador do Windows) para mostrar a imagem
#im.show()

#Aplica o filtro SHARPEN a imagem
#im_sharp = im.filter(ImageFilter.SHARPEN)

#Salva a imagem com o filtro 
#im_sharp.save("img_sharpened.jpg", "JPEG")

#Separa os canais da imagem 
#r, g, b = im_sharp.split()
#r.show()

#Lê o tamanho da imagem
img_tamanho = im.size
print(img_tamanho)

#Pega o valor do pixel numa determinada posicao
valor_pixel = im.getpixel((0,0))
# e retorna o valor em uma tupla com os valores RGB
#print(valor_pixel)

valor_pixel_2 = im.getpixel((2559,0))
#print(valor_pixel_2)

area_corte = (100, 100, 400, 400)