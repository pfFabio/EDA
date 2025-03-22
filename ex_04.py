

temperatura = []
umidade = []
pressao = []

with open("EDA\dadosclimaticos.txt", "r") as dados:
    for linha in dados:
        linha_dividida =  linha.split(':', 1)
        linha_valores = linha_dividida[1].strip()
        informacao = eval(linha_valores)
        temperatura.append(informacao['Temperatura'])
        umidade.append(informacao['Umidade'])
        pressao.append(informacao['Pressao'])
    
    print(pressao)
    print(umidade)
    print(temperatura)


"""
for i in informação:
    print(i)
    
    temperatura.append(i["Temperatura"])
    umidade.append(i['Umidade'])
    pressao.append(i['pressao'])"""

