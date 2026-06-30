#Função sem parametro e sem retorno:

# def diga_oi():
#     print("Oi")
#     # poderia usar algo como pass também
    
# diga_oi()

# ----------------------------------------------------------------------------

#Função com parametro mas sem retorno:

# def saudacao(nome_visitante):
#     print(f"Seja bem vindo(a), {nome_visitante}")
    

# saudacao("João")
# saudacao("Paula")

# ----------------------------------------------------------------------------

#Função sem parametro e com retorno

from datetime import datetime


def hora_certa():
    agora = datetime.now()
    return f"{agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}"


hora = hora_certa()
print(f"{hora}")