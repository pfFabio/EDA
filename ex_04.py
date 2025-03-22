

temperatura = []
umidade = []
pressao = []

dados = open("EDA\dadosclimaticos.txt", "r")
for linha in dados:
    linha_dividida =  linha.split(':', 1)
    ciclo = int(linha_dividida[0].split()[1])
    linha_valores = linha_dividida[1].strip()
    #cada ciclo dura 10mins logo 6 ciclos duram 1hr, 6*24 = 144 ciclos em 1 dia
    #144*19 = 2736 ciclo inicial
    #144*20 = 2880 ciclo final
    if ciclo > 2736 and ciclo < 2881:
        informacao = eval(linha_valores)
        temperatura.append(informacao['Temperatura'])
        umidade.append(informacao['Umidade'])
        pressao.append(informacao['Pressao'])
        print(ciclo)
    

print(f' a maior temperatura foi {max(temperatura)}°C\na menor temperatura foi {min(temperatura)}°C\na média das temperaturas foi {sum(temperatura)/len(temperatura)}°C')
print(f' a maior umidade foi {max(umidade)}°C\na menor umidade foi {min(umidade)}°C\na média das umidades foi {sum(umidade)/len(umidade)}°C')
