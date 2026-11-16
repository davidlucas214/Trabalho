# VANTAGENS:
#  - É o mais simples de todos, ótimo para aprender.
#  - Não usa memória extra e é estável.
#  - Se a lista já estiver ordenada, termina rápido (O(n)) com a flag 'trocou'.
# DESVANTAGENS:
#  - Muito lento: O(n²) no caso médio e no pior caso.
#  - Faz muitas trocas, o que o deixa o mais lento da lista.
#  - Não é indicado para listas grandes.
import random
import time
def ordenar(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
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
