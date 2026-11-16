# VANTAGENS:
#  - Rápido e previsível: O(n log n) em todos os casos.
#  - Estável (mantém a ordem de elementos iguais).
#  - Ótimo para listas grandes.
# DESVANTAGENS:
#  - Usa memória extra (O(n)) para as listas auxiliares.
#  - Um pouco mais difícil de entender (usa recursão).
#  - Mais lento que o Quick Sort na prática em listas pequenas.
import random
import time
def ordenar(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = ordenar(lista[:meio])
    direita = ordenar(lista[meio:])
    return intercalar(esquerda, direita)
def intercalar(esquerda, direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
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
