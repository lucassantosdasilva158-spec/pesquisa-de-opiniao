# Exibe o título da pesquisa

print ("PESQUISA DE OPINIÃO")

# Aqui é o contador da opinião dos entrevistados, onde cada variável será incrementada de acordo com a opinião do entrevistado

ruim = 0
bom = 0
excelente = 0

# Aqui é onde será realizado a pesquisa, onde o loop será realizado até os 50 entrevistados responderem a pesquisa

for entrevistado in range (1, 51):
    entrevistado = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opinião = input("Digite a opinião desejada (ruim, bom ou excelente) a opinião deve ser digitada em letras minusculas: ")
    print ("O entrevistado", entrevistado, "tem", idade, "anos e sua opinião é", opinião)

    # Incrementa o contador de acordo com a opinião do entrevistado

    if opinião == "ruim":
        ruim += 1
    elif opinião == "bom":
        bom += 1
    elif opinião == "excelente":
        excelente += 1

# Exibe os resultados da pesquisa

print ("Resultados da pesquisa:")
print ("Ruim:", ruim)
print ("Bom:", bom)
print ("Excelente:", excelente)