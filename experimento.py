from sorteadores.quick_sort_recursivo import quick_sort_recursivo_wapper
from sorteadores.quick_sort_random import quick_sort_recursivo_random_wapper
from sorteadores.merge_sort_interativo import Merge_Sort_interativo_wapper
from sorteadores.merge_sort_recursivo import merge_sort__recursivo_wapper
from sorteadores.merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from sorteadores.select_sort_recursivo import select_sort_recursivo_wapper
from sorteadores.select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sorteadores.shellSort_base_line import shellSort_Wapper
from sorteadores.heap_sort_recursivo import heapSort
from sorteadores.insertion_sort import insertionSort

from gerador import gerar_dados_crescente, gerar_dados_random, gerar_dados_decrescente, agora, dif_time

import pandas as pd

# ----------------------------------------------------------
#               DEMONSTRAÇÂO DA EXECUÇÂO
# ----------------------------------------------------------
# X = [58, 30, 97, 21, 81, 35, 48, 59, 24, 2, -1]
# print(f'X : {X}')

# QS1 = quick_sort_recursivo_wapper(X.copy())
# QS2 = quick_sort_recursivo_random_wapper(X.copy())
# print(f'Quick sort recursivo: {QS1}')
# print(f'Quick sort recursivo randomizado: {QS2}')

# MS1 = Merge_Sort_interativo_wapper(X.copy())
# MS2 = merge_sort__recursivo_wapper(X.copy())
# MS3 = merge_sort_recursivo_random_wapper(X.copy())
# print(f'Merge sort interativo: {MS1}')
# print(f'Merge sort recursivo: {MS2}')
# print(f'Merge sort recursivo randomizado: {MS3}')

# SS1 = select_sort_recursivo_wapper(X.copy())
# SS2 = select_sort_recursivo_random_wapper(X.copy())
# print(f'Select sort recursivo: {SS1}')
# print(f'Select sort recursivo randomizado: {SS2}')

# BASE_LINE = shellSort_Wapper(X.copy())
# print(f'Sell Sort [Baseline]: {BASE_LINE}')

# ----------------------------------------------------------
#                    FUNÇÂO DE EXECUÇÂO
# ----------------------------------------------------------

def execucao(X):
    # Criando o dicionario para armazenar os tempos
    temposExec = []

    # Rodando quick sort recursivo e salvando o tempo no dicionario
    a = agora()
    QS1 = quick_sort_recursivo_wapper(X.copy())
    b = agora()
    temposExec.append(dif_time(b,a))

    # Rodando o quick sort random e salvando o tempo no dicionario
    a = agora()
    QS2 = quick_sort_recursivo_random_wapper(X.copy())
    b = agora()
    temposExec.append(dif_time(b,a))

    # Rodando o merge sort interativo e salvando o tempo no dicionario
    # a = agora()
    # MS1 = Merge_Sort_interativo_wapper(X.copy())
    # b = agora()
    # temposExec.append(dif_time(b,a))

    # Rodando o merge sort recursivo e salvando o tempo no dicionario
    a = agora()
    MS2 = merge_sort__recursivo_wapper(X.copy())
    b = agora()
    temposExec.append(dif_time(b,a))

    # Rodando o merge sort recursivo e salvando o tempo no dicionario
    a = agora()
    MS3 = merge_sort_recursivo_random_wapper(X.copy())
    b = agora()
    temposExec.append(dif_time(b,a))

    # Rodando o select sort recursivo e salvando o tempo no dicionario
    a = agora()
    SS1 = select_sort_recursivo_wapper(X.copy())
    b = agora()
    temposExec.append(dif_time(b,a))

    # Rodando o select sort recursivo e salvando o tempo no dicionario
    a = agora()
    SS2 = select_sort_recursivo_random_wapper(X.copy())
    b = agora()
    temposExec.append(dif_time(b,a))

    # Rodando o shell sort e salvando o tempo no dicionario
    # a = agora()
    # BASE_LINE = shellSort_Wapper(X.copy())
    # b = agora()
    # temposExec.append(dif_time(b,a))

    # Rodando o heap sort e salvando o tempo no dicionario
    # a = agora()
    # HP = heapSort(X.copy())
    # b = agora()
    # temposExec.append(dif_time(b,a))

    # Rodando o insertion sort e salvando o tempo no dicionario
    # a = agora()
    # IS = insertionSort(X.copy())
    # b = agora()
    # temposExec.append(dif_time(b,a))

    return temposExec


def testes(numExec=10, tamanhoArray=100, tipo="DSC"):
    execucoes = []
    tamExecucoes = []

    # Caso seja para gerar dados crescentes
    if tipo == "ASC":
        for i in range(1, numExec, 1):
           tamanho = i*tamanhoArray
           X = gerar_dados_decrescente(tamanhoArray)
           execucoes.append(execucao(X))
           tamExecucoes.append(tamanho)
    # Caso seja para gerar dados decrescentes
    elif tipo == "DSC":
        for i in range(1, numExec, 1):
           tamanho = i*tamanhoArray
           X = gerar_dados_crescente(tamanhoArray)
           execucoes.append(execucao(X))
           tamExecucoes.append(tamanho)
    # Caso seja para gerar dados aleatórios
    elif tipo =="RNG":
        for i in range(1, numExec, 1):
           tamanho = i*tamanhoArray
           X = gerar_dados_random(tamanhoArray)
           execucoes.append(execucao(X))
           tamExecucoes.append(tamanho)
    # Caso o tipo seja diferente
    else:
        return
    
    # criando tabela unificada de tamanho + tempo
    listaCompleta = []
    for i, lista in enumerate(execucoes):
        print(lista)
        listaCompleta.append(lista + [tamExecucoes[i]])

    # Criando o dataframe do pandas
    df = pd.DataFrame(listaCompleta, columns=['QS1', 'QS2', 'MS2', 'MS3', 'SS1', 'SS2', 'TAMANHO'])

    # salvando o dataframe
    df.to_excel(f'./output/dados_{tipo}_{tamanhoArray}.xlsx', index=False)

# Testando
testes(tamanhoArray=100, tipo="DSC")
testes(tamanhoArray=100, tipo="ASC")
testes(tamanhoArray=100, tipo="RNG")
    

