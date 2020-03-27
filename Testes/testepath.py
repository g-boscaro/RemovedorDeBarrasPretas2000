import os

meu_path = r"C:\Users\Fido\Documents\GitHub\CropImage\Imagens teste\corruption.png"

def criaNovoDir(caminho):
    #Pega o nome do diretorio
    nome_dir = os.path.dirname(caminho)
    print(nome_dir)

    nome_arq = os.path.basename(caminho)
    print("Arquivo:", nome_arq)
    arquivo, extensao = os.path.splitext(nome_arq)
    print("Nome arquivo:",arquivo)
    print("Extensão:",extensao)

    #Cria caminho com o final \No_bars
    novo_path = nome_dir + "\\No_bars\\"
    #print(novo_path)

    #Verifica a existencia do novo caminho
    check_existe = os.path.exists(novo_path)
    #print(check_existe)

    #Checa 
    if check_existe == False:
        os.mkdir(novo_path)
    else:
        return novo_path

print(criaNovoDir(meu_path))