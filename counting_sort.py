# VANTAGENS:
#  - Muito rápido: O(n + k), onde k é o maior valor da lista.
#  - Estável (nesta forma) e simples de entender.
# DESVANTAGENS:
#  - Só funciona com números inteiros (não negativos, nesta versão).
#  - Gasta muita memória se o maior valor for muito grande.
#  - Não é bom quando o intervalo de valores é enorme.
import random
import time
def ordenar(lista):
    maior = max(lista)
    contagem = [0] * (maior + 1)
    for numero in lista:
        contagem[numero] += 1
    resultado = []
    for valor in range(len(contagem)):
        resultado.extend([valor] * contagem[valor])
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
