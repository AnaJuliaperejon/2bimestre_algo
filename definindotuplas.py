#tuplas se definem por parenteses(), diferente das listas que se definem por chaves []
numeros=(5, 8, 12, 8, 7, 8, 3)

#imprimindo a tupla original sem modificações
print("tupla original: ", numeros)

print("quantidade na tupla:", len(numeros))

print("acessando pelo indice:",numeros[2])

#o slicing mostra os valores dos indices selecionados
print("fazendo um slicing do 2 ao 5", numeros[2:5])

#count conta quantas vezes o numero repete
print("quantas vezes o número 8 repete:", numeros.count(8))

# index mostra em qual indice esta o numero específico
print("posição da primeira ocorrência do numero 7",numeros.index(7))

#maior valor da tupla
minimo_tupla=min(numeros)
print(minimo_tupla)

#menor valor da tupla
maximo_tupla=max(numeros)
print(maximo_tupla)

#soma os valores da tupla
soma_tupla=sum(numeros)
print(soma_tupla)

#sorted ordena os elemntos 
print("ordenando tuplas:",sorted(numeros))

#in serve para vereificar se um item está dentro da tupla
print("o numero 4 está na tupla?:", 4 in numeros)

numero2=(15,20)
#tuplas concatenadas junta as duas tuplas
tupla_concatenada=numeros+numero2
print(" a concatenação das duplas 1 e 2 resulta na nova tupla:",tupla_concatenada)

tupla_duplicada=numeros*2
print(tupla_duplicada)


