import easygui
from PIL import Image

meu_path_arq = r"C:\Users\Fido\Documents\GitHub\CropImage\cropImage.py"
meu_path_img = r"C:\Users\Fido\Documents\GitHub\CropImage\Imagens teste\preto.png"

try:
    img = Image.open(meu_path_arq)
    img.verify()
    print("Imagem valida")
except:
    print("Imagem invalida")