import random
import time
def insertion_sort(lista):
    comparacoes = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        #a chave é o elemento q era movido para outra posição
        #e j é index do elemento anterior a chave
        #e lista[j] que é o elemento antes ta chave
        while j >= 0 and lista[j] > chave:
            comparacoes += 1
            #quando a chave for menor que o elemento anterior a lista[j] era movido pra frente
            lista[j + 1] = lista[j]
            j -= 1
        #quando a chave for maior que o elemento anterior a lista[j] era movido pra frente
        lista[j + 1] = chave
        if j >= 0:

            comparacoes += 1
    return comparacoes

# Caso 1 – Melhor caso (lista já ordenada)
numeros_pequenos = [1, 2, 3, 4, 5]
inicio1 = time.perf_counter()
operacoes1 = insertion_sort(numeros_pequenos[:])
fim1 = time.perf_counter()
tempo_execucao1 = fim1 - inicio1
print()

# Caso 2 – Caso médio
numeros_medios = list(range(50, 0, -1))  
inicio2 = time.perf_counter()
operacoes2 = insertion_sort(numeros_medios[:])
fim2 = time.perf_counter()
tempo_execucao2 = fim2 - inicio2
print()

# Caso 3 – Pior caso (lista decrescente grande)
numeros_grandes = list(range(100, 0, -1))  
inicio3 = time.perf_counter()
operacoes3 = insertion_sort(numeros_grandes[:])
fim3 = time.perf_counter()
tempo_execucao3 = fim3 - inicio3
print()

# Visualização dos dados
import matplotlib.pyplot as plt
casos = ['Melhor Caso', 'Caso Médio', 'Pior Caso']
tempos = [tempo_execucao1, tempo_execucao2, tempo_execucao3]
operacoes = [operacoes1, operacoes2, operacoes3]
plt.figure(figsize=(10, 5))
# Gráfico de tempo
plt.subplot(1, 2, 1)
plt.bar(casos, tempos, color='skyblue')
plt.title('Tempo de Execução - Insertion Sort')
plt.ylabel('Tempo (segundos)')
# Gráfico de operações
plt.subplot(1, 2, 2)
plt.bar(casos, operacoes, color='orange')
plt.title('Número de Operações - Insertion Sort')
plt.ylabel('Número de Operações')
plt.show()