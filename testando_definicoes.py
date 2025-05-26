compras = ["pao", "cafe","leite"]
print(compras)

#pode ser removido pelo nome do produto ou pelo indice.
#compras.remove("cafe").
compras.remove(compras[0])
print(compras)

#append adiciona um item de cada vez, ao final da lista.
compras.append("açucar")
print(compras)

#é preciso criar uma nova lista para receber os elementos ordenados da lista antiga
compras_ordenada = sorted(compras)
print(compras_ordenada)

#tanto faz o nome em que esta após o for, nesse caso "panela" é o identificador  dos itens de dentro da lista.
for panela in compras:
    print("-", panela)


