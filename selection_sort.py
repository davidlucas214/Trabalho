# VANTAGENS:
#  - Muito simples de entender e de implementar.
#  - Faz poucas trocas (no máximo n trocas).
#  - Não usa memória extra (ordena na própria lista).
# DESVANTAGENS:
#  - Lento para listas grandes: complexidade O(n²) sempre.
#  - Não fica mais rápido mesmo se a lista já estiver quase ordenada.
#  - Não é estável (pode mudar a ordem de elementos iguais).
import random
import time
def ordenar(lista):
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
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
