# ALUNO: PEDRO NEGREIROS ANDRADE


def separar_pares_impares(valores):
    pares = [valor for valor in valores if valor % 2 == 0]
    impares = [valor for valor in valores if valor % 2 != 0]
    return pares, impares

def calcular_soma(valores):
    return sum(valores)

valores = []
for _ in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

pares, impares = separar_pares_impares(valores)

print("Números pares:", pares)

print("Números ímpares:", tuple(impares))

print("Quantidade de números pares:", len(pares))
print("Quantidade de números ímpares:", len(impares))

soma_pares = calcular_soma(pares)
soma_impares = calcular_soma(impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
