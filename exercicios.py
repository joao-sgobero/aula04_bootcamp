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

# from datetime import datetime


# def hora_certa():
#     agora = datetime.now()
#     return f"{agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}"


# hora = hora_certa()
# print(f"{hora}")

# ----------------------------------------------------------------------------

#Função com parametro e com retorno
def conta_com_gorgerta(valor_conta, percentual_gorgeta):
    valor_gorgeta = valor_conta * percentual_gorgeta
    return valor_conta + valor_gorgeta

valor_total = conta_com_gorgerta(485, 0.08)
print(f"O valor final da conta é R${valor_total}")