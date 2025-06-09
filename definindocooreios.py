pacotes=(("ABC123"), ("XYZ789"),("DEF456"), ("JKL321"), ("MNO654"),("PQR987"), ("STU741"),)
rastreio=(("Enviado"),("Recebido"),("Em Trânsito"),("Enviado"),("Recebido"),("Em Trânsito"),("Enviado"))

Enviado=rastreio.count("Enviado")
print("quantos pedidos enviados:",Enviado)
Recebido=rastreio.count("Recebido")
print("quantos pedidos Recebidos:",Recebido)
Em_transito=rastreio.count("Em Trânsito")
print("quantos pedidos em trânsito:",Em_transito)

print("os pacotes em transito são:", pacotes[2], pacotes[5])

codigo= input("insira o codigo do pacote")
print("o pacote esta no indice",pacotes.index(codigo), "status", rastreio[pacotes.index(codigo)])

def buscar_status(codigo_rastreamento):
    if codigo_rastreamento in pacotes:
        indice = pacotes.index(codigo_rastreamento)
        return f"O pacote {codigo_rastreamento} está '{rastreio[indice]}'."
    return "Pacote não cadastrado."

pacote_ordenado= sorted(pacotes, rastreio)

print("os pacotes ordenados",pacote_ordenado)