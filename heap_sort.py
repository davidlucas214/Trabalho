# VANTAGENS:
#  - O(n log n) garantido em todos os casos.
#  - Não usa memória extra (ordena na própria lista).
# DESVANTAGENS:
#  - Mais difícil de entender (usa a ideia de "heap", uma árvore em lista).
#  - Não é estável.
#  - Na prática costuma ser mais lento que Quick Sort e Merge Sort.
import random
import time
def ajustar(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda
    if direita < n and lista[direita] > lista[maior]:
        maior = direita
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        ajustar(lista, n, maior)
def ordenar(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        ajustar(lista, n, i)
    for fim in range(n - 1, 0, -1):
        lista[0], lista[fim] = lista[fim], lista[0]
        ajustar(lista, fim, 0)
    return lista
TAMANHO = 100000
lista = [random.randint(0, 100000) for _ in range(TAMANHO)]
print("Primeiros 10 antes:  ", lista[:10])
inicio = time.time()
lista_ordenada = ordenar(lista)
fim = time.time()
print("Primeiros 10 depois: ", lista_ordenada[:10])
print("Está ordenada?", lista_ordenada == sorted(lista_ordenada))
print(f"Tempo: {fim - inicio:.2f} segundos")
