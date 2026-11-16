# VANTAGENS:
#  - Muito rápido na prática: O(n log n) em média.
#  - Um dos mais usados no mundo real.
# DESVANTAGENS:
#  - Pior caso é O(n²) (quando o pivô é sempre ruim).
#  - Não é estável.
#  - Esta versão simples cria listas novas (usa mais memória).
#  - Usa recursão.
import random
import time
def ordenar(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return ordenar(menores) + iguais + ordenar(maiores)
TAMANHO = 100000
lista = [random.randint(0, 100000) for _ in range(TAMANHO)]
print("Primeiros 10 antes:  ", lista[:10])
inicio = time.time()
lista_ordenada = ordenar(lista)
fim = time.time()
print("Primeiros 10 depois: ", lista_ordenada[:10])
print("Está ordenada?", lista_ordenada == sorted(lista_ordenada))
print(f"Tempo: {fim - inicio:.2f} segundos")
