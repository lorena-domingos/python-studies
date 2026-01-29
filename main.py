"""
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.

"""

cigarros = int(input("Quantos cigarros você fuma por dia?\n"))
anos_fumando = int(input("Quantos anos fuma?\n"))

minutos = (cigarros * 10) * (anos_fumando * 365)

resultado = minutos / 1440 # Quantidade de minutos de um dia.

print(f"Total de dias de vida que o fumante perderá: {round(resultado, 2)} dias")