import time
import matplotlib.pyplot as plt

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    operacoes = 0
    #o gap é matade da lista
    while gap > 0:
        for i in range(gap, n):
            #o temp é o elemento que vai ser movido
            #e o j é o index do é msm index de i
            temp = arr[i]
            j = i
            #arr[j-gap] se for maior que o temp o elemento arr[j-arr] é movido para lugar do temp 
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                #aqui o j fica menor que o gap, para que o loop não continue
                j -= gap
                operacoes += 1
            #aqui o temp é movido para a posição do index j, a qual é o index do elemento que era maior que o temp
            arr[j] = temp
            operacoes += 1
        gap //= 2
    return operacoes

# Caso 1 – Melhor caso (lista já ordenada)
numeros_pequenos = [1, 2, 3, 4, 5]
inicio1 = time.perf_counter()
operacoes1 = shell_sort(numeros_pequenos[:])
fim1 = time.perf_counter()
tempo_execucao1 = fim1 - inicio1

# Caso 2 – Caso médio
numeros_medios = list(range(50, 0, -1))  # Lista reversa de 50 a 1
inicio2 = time.perf_counter()
operacoes2 = shell_sort(numeros_medios[:])
fim2 = time.perf_counter()
tempo_execucao2 = fim2 - inicio2

# Caso 3 – Pior caso (lista decrescente grande)
numeros_grandes = list(range(100, 0, -1))  
inicio3 = time.perf_counter()
operacoes3 = shell_sort(numeros_grandes[:])
fim3 = time.perf_counter()
tempo_execucao3 = fim3 - inicio3

# Visualização dos dados
casos = ['Melhor Caso', 'Caso Médio', 'Pior Caso']
tempos = [tempo_execucao1, tempo_execucao2, tempo_execucao3]
operacoes = [operacoes1, operacoes2, operacoes3]

plt.figure(figsize=(10, 5))

# Gráfico de tempo
plt.subplot(1, 2, 1)
plt.bar(casos, tempos, color='skyblue')
plt.title('Tempo de Execução - Shell Sort')
plt.ylabel('Tempo (segundos)')

# Gráfico de operações
plt.subplot(1, 2, 2)
plt.bar(casos, operacoes, color='orange')
plt.title('Número de Operações - Shell Sort')
plt.ylabel('Operações')

plt.tight_layout()
plt.show()

# Exemplo visual de ordenação
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("\nExemplo prático:")
print("Antes:", lista)
shell_sort(lista)
print("Depois:", lista)




