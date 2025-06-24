# lista=[1,3,5,7,8,0,2,4,6,8]

# def bubbleSort(lista):
#     for passnum in range(len(lista)-1,0,-1):
#         for i in range(passnum):
#             if lista[i]> lista[i+1]:
#                 temp=lista[i]
#                 lista[i]=lista[i+1]
#                 lista[i+1]= temp
# bubbleSort(lista)
# print(lista)
   
lista=[3,7,5,2,1]

for i in range(len(lista)-1,0,-1):
    indice=0
    for j in range(1,i+1):
        if lista[j]>lista[indice]:
            indice=j
        lista[i], lista[indice]= lista[indice],lista[i]
print(lista)


