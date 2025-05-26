compras=[]
resposta=""

while resposta.upper() !="SAIR":
    resposta=input("deseja inserir mais itens a lista? Caso não, Insira 'SAIR': \n")
    if resposta.upper() =="SIM":
        mais_item= input("insira o item: \n")
        compras.append(mais_item)
        print(compras)
    elif resposta.upper() =="NÃO" or resposta.upper() == "NAO":
        remove=input("insira o item que deseja remover: \n")
        compras.remove(remove)
        print(compras)

