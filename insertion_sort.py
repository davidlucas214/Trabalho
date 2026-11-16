# VANTAGENS:
#  - Simples e rápido para listas pequenas ou quase ordenadas (O(n)).
#  - Estável e não usa memória extra.
#  - Funciona bem "ao vivo", conforme novos elementos chegam.
# DESVANTAGENS:
#  - Lento para listas grandes e desordenadas: O(n²).
#  - Faz muitos deslocamentos de elementos.
import random
import time
def ordenar(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual
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
