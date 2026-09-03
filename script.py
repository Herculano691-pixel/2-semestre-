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


"""
def pesquisa_sequencial(lista, item):
  for i, j in enumerate(lista):
    if j == item:
      return i

y = pesquisa_sequencial([7, 9, 12, 15, 16, 18, 22], 15)
print(y)
"""



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