# VANTAGENS:
#  - Muito rápido quando os valores estão bem distribuídos: O(n) em média.
#  - Fácil de dividir o trabalho em partes.
# DESVANTAGENS:
#  - Depende da distribuição dos dados (se todos caírem em um balde, vira O(n²)).
#  - Usa memória extra para os baldes.
#  - Precisa escolher bem a quantidade de baldes.
import random
import time
def ordenar_balde(balde):
    for i in range(1, len(balde)):
        atual = balde[i]
        j = i - 1
        while j >= 0 and balde[j] > atual:
            balde[j + 1] = balde[j]
            j -= 1
        balde[j + 1] = atual
    return balde
def ordenar(lista):
    quantidade = 1000
    maior = max(lista)
    baldes = [[] for _ in range(quantidade)]
    for numero in lista:
        indice = numero * quantidade // (maior + 1)
        baldes[indice].append(numero)
    resultado = []
    for balde in baldes:
        resultado.extend(ordenar_balde(balde))
    return resultado
TAMANHO = 100000
lista = [random.randint(0, 100000) for _ in range(TAMANHO)]
print("Primeiros 10 antes:  ", lista[:10])
inicio = time.time()
lista_ordenada = ordenar(lista)
fim = time.time()
print("Primeiros 10 depois: ", lista_ordenada[:10])
print("Está ordenada?", lista_ordenada == sorted(lista_ordenada))
print(f"Tempo: {fim - inicio:.2f} segundos")
