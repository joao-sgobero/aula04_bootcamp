# 1)  Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# # Atualizar o preço do produto com id 2 para 90
# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90

# print(produtos)

#===============================================

#2) Dados dois dicionários, fundi-los em um único dicionário.

# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}

# dicionario_fundido = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

#===============================================

# 3) Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

# estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

# print(estoque_positivo)

#===============================================

# 04) Dado um dicionário, criar listas separadas para suas chaves e valores.

# dicionario = {"a": 1, "b": 2, "c": 3}
# lista_chave = dicionario.keys()
# lista_valor = dicionario.values()

# print(
#     lista_chave,
#     lista_valor
# )


#===============================================

# 5) Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

for i in texto:
    if i not in frequencia:
        frequencia[i] = 1
    else: 
        frequencia[i] += 1
        
print(frequencia)