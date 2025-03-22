

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
    

print(f'\nA maior temperatura foi {max(temperatura)}°C\nA menor temperatura foi {min(temperatura)}°C\nA média das temperaturas foi {(sum(temperatura)/len(temperatura)):.2f}°C\n')
print(f'A maior umidade foi {max(umidade)}\nA menor umidade foi {min(umidade)}\nA média das umidades foi {(sum(umidade)/len(umidade)):.2f}\n')
print(f'A maior pressão foi {max(pressao)}\nA menor pressão foi {min(pressao)}\nA média das pressão foi {(sum(pressao)/len(pressao)):.2f}')
