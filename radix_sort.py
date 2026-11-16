# VANTAGENS:
#  - Muito rápido para inteiros: O(d * (n + b)), d = nº de dígitos.
#  - Não compara elementos entre si.
#  - Estável.
# DESVANTAGENS:
#  - Só funciona bem com inteiros (ou dados que viram dígitos).
#  - Usa memória extra para os baldes.
#  - Mais complexo que os algoritmos simples.
import random
import time
def ordenar(lista):
    maior = max(lista)
    casa = 1
    while maior // casa > 0:
        baldes = [[] for _ in range(10)]
        for numero in lista:
            digito = (numero // casa) % 10
            baldes[digito].append(numero)
        lista = []
        for balde in baldes:
            lista.extend(balde)
        casa *= 10
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
