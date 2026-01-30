"""
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.

"""

# cigarros = int(input("Quantos cigarros você fuma por dia?\n"))
# anos_fumando = int(input("Quantos anos fuma?\n"))
#
# minutos = (cigarros * 10) * (anos_fumando * 365)
#
# resultado = minutos / 1440 # Quantidade de minutos de um dia.
#
# print(f"Total de dias de vida que o fumante perderá: {round(resultado, 2)} dias")

"""
25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
de cada lado deve ser menor que a soma dos outros dois.
"""

# a = int(input("Digite um valor númerico:\n"))
# b = int(input("Digite outro valor númerico:\n"))
# c = int(input("Digite mais um valor númerico:\n"))
#
# if a < b + c and b < a + c and c < a + b:
#     print("É um triângulo!")
# else:
#     print("Não é um triângulo!")

"""
30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
"""

# a = int(input("Digite um valor númerico:\n"))
# b = int(input("Digite outro valor númerico:\n"))
# c = int(input("Digite mais um valor númerico:\n"))
#
# if a < b + c and b < a + c and c < a + b:
#     if a == b and b == c and c == a:
#         print("Equilátero")
#
#     elif a != b and b != c and c != a:
#         print("Escaleno")
#
#     elif a == b or b == c or c == a:
#         print("Isósceles")
#
#     print("É um triângulo!")
# else:
#     print("Não é um triângulo!")


"""
[DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
"""

import random

computador = random.randint(1, 3)
usuario = int(input("Digite 1 para Pedra, 2 para Papel e 3 para Tesoura\n"))

if computador == 1:
    resultado = "Pedra"
elif computador == 2:
    resultado = "Papel"
elif computador == 3:
    resultado = "Tesoura"

if usuario in [1, 2, 3]:
    if usuario == computador:
        print("Empate")
    elif (usuario == 1 and computador == 2) or (usuario == 2 and computador == 3) or (usuario == 3 and computador == 1):
        print(f"O computador escolheu: {resultado}")
        print("Computador Vence!")
    else:
        print(f"O computador escolheu: {resultado}")
        print("Usuário Vence!")
else:
    print("Digite um valor válido")


