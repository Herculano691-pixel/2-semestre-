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

'''
from datetime import datetime, timedelta
import requests
def cotar(data):
    url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
    res = requests.get(url)
    res = res.json()
    if res['value']:
        return res ['value'][0]['cotacaoCompra']
    else:
        anterior = datetime.strptime(data, "%d-%m-%Y") - timedelta(1)
        anterior = datetime.strftime(anterior, "%d-%m-%Y")
        return cotar(anterior)
'''
'''
import os
import webbrowser
import requests
from folium import Map, Marker

API_URL = "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2506"
LOGIN_URL = "http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar"
TOKEN = "23abdd7ee1166cd0d31304207382aa62023527836f4643f4dd2fbd3c7969859d"


def buscar_paradas():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json",
    }

    try:
        resposta = requests.get(API_URL, headers=headers, timeout=20)
        print(f"Status da API: {resposta.status_code}")

        if resposta.status_code != 200:
            raise RuntimeError(f"Erro na API: {resposta.status_code} - {resposta.text[:200]}")

        dados = resposta.json()
        paradas = dados.get("vs") or dados.get("paradas") or []

        if not paradas:
            raise ValueError("A API não retornou paradas para a linha 2506.")

        return paradas
    except Exception as erro:
        print(f"Não foi possível consultar a API: {erro}")
        return [
            {"np": "UNASP", "py": -22.8773542, "px": -47.2280647},
            {"np": "Parada 1", "py": -22.8768000, "px": -47.2269000},
            {"np": "Parada 2", "py": -22.8783000, "px": -47.2292000},
        ]


paradas = buscar_paradas()

m = Map(location=[paradas[0]["py"], paradas[0]["px"]], zoom_start=14)
for ponto in paradas:
    nome = ponto.get("np") or ponto.get("nome") or "Parada"
    lat = ponto.get("py") or ponto.get("latitude")
    lon = ponto.get("px") or ponto.get("longitude")

    if lat is None or lon is None:
        continue

    Marker(location=[lat, lon], popup=nome).add_to(m)

arquivo = os.path.join(os.getcwd(), "unasp.html")
m.save(arquivo)
print(f"Arquivo gerado: {arquivo}")
webbrowser.open(f"file://{arquivo}")

        

cotacaoCompra = cotar("09-07-2026")
print(cotacaoCompra)
'''

M = [[1,3], [5,6]]
N = [[2,8], [9,5]]

for i in range(2):
    for j in range(2):
        print(M[i][j] + N[i][j])
    print()
