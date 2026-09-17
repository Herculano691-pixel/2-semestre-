"""x = 4
if x < 4:
    print(" O número é menor do que 4")
elif x == 4:
    print(" O número é igual a 4")    
elif x > 4:    
    print(" O número é maior do que 4")
"""


"""
try:
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        print("par")
    elif x % 2 != 0:
        print("impar")
except ValueError:
    print("Por favor, digite um número válido.")   
"""


"""
soma = 0

while True:
    x = int(input("Digite um número: "))
    soma += x
    if x == 0:
        break
print(soma)
"""

"""
x = [1, 2, "w", True, [["olá", "mundo"], 2]]
x[4][0][1] = "a"
print(x)
"""


"""
x = [["João", 23], ["Maria", 45], ["José", 67]]
for i in x:
    if i[1] > 40:
        print("Olá, meu nome é", i[0], "e eu tenho", i[1], "anos")
"""


"""
z = {"a": 5, "b": True, "c": [False, "unasp"]}
z["b"]= False
print(z.get("w", False))
"""


"""
produtos = {}

while True:
    nome = input("Digite o produto: ")
    valor = float(input("Digite o valor: "))
    produtos[nome] = valor

    print("\nLista de produtos:")
    for produto in produtos:
        print(produto, "- R$ %.2f" % produtos[produto])

    continuar = input("Quer adicionar mais? (s/n): ").lower

    if continuar == "n":
        break
"""


"""
A = list(set([1, 2, 3, 3]))
print(A)
"""
"""
A = {1, 2, 3, 3}
B = {1,4, 5, 6,} 
w = A | B
print(w)
"""


"""
def par(x):
    return x % 2 == 0

y = []
for i in [4, 7, 3, 9, 6]:
    y.append(par(i))
print(y)
"""


'''
def pesquisa_sequencial(lista, item):
  for i, j in enumerate(lista):
    if j == item:
      return i

y = pesquisa_sequencial([7, 9, 12, 15, 16, 18, 22], 15)
print(y)
'''


'''
def pesquisa_binaria(lista, item):
  baixo = 0
  alto = len(lista) - 1

  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    if chute == item:
      return meio
    elif chute > item:
      alto = meio - 1
    else:
      baixo = meio + 1
  return None

y = pesquisa_binaria([7, 9, 12, 15, 16, 18, 22], 22)
print(y)
'''

'''
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n + factorial(n - 1)

factorial(5)
print(factorial(5))
'''

'''
while True:
    x = 5
    soma = 0
    for i in range(x + 1):
        soma += i
    print(soma)
    break
'''
'''
import requests

# Função que fará requisição à API
def consulta_cep(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  res = requests.get(url)
  res = res.json()
  return (res['logradouro'], res['uf'])

# Lista de CEPs para consulta
lista_cep = ["13186642",
             "13178574",
             "13188020",
             "13184321",
             "20720293"]

y = [consulta_cep(cep) for cep in lista_cep if consulta_cep(cep)[1] == "SP"]
print(y)
'''

import requests
def cotar(data):
    url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
    res = requests.get(url)
    res = res.json()
    return res

cotacaoCompra = cotar("06-29-2007")['value'][0]['cotacaoCompra']
print(cotacaoCompra)
