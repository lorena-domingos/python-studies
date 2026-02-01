def soma (a, b):
    return a + b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    return a / b

def subtrair (a, b):
    return a - b

def impar_par (a):
    if a % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def maior (a, b):
    if a > b:
        return "Maior"
    else:
        return "Menor"

# 6 aqui.

def maior_idade (a):
    if a >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

def nota (a):
    if a >= 7:
        return "Aprovado"
    elif a >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def desconto(valor, desconto):
    valor_desconto = (desconto / 100) * valor
    valor_final = valor - valor_desconto
    return valor_final

def valor_dobro(a):
    if a > 0:
        return a * 2
    else:
        return None

def multiplo_de_cinco(a):
    if a % 5 == 0:
        return True
    else:
        return False

def fahrenheit(a):
    if a > 0:
        return (a * 9 / 5) + 32
    else:
        return None

def sequencia_de_dez():
    lista = [i for i in range(1, 11)]
    return lista

# sequencia_de_dez()

