# Tipo de Triângulo

def tipo_triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Inválido"

    elif a == b and b == c:
        return "Equilátero"
    elif a != b and b != c and c != a:
        return "Escaleno"
    elif a == b or b == c or c == a:
        return "Isósceles"

    return None

# Calculadora com operador String

def calculadora(valor1, operador, valor2):
    if valor1 < 0 or operador == "" or valor2 < 0:
        return "Inválido"

    if operador == "*":
        return valor1 * valor2
    elif operador == "/":
        return valor1 / valor2
    elif operador == "+":
        return valor1 + valor2
    elif operador == "-":
        return valor1 - valor2

    return None

# Retornar dia da semana com Match Case

def dia_semana(valor):
    match int(valor):
        case 1:
            return "Segunda"
        case 2:
            return "Terça"
        case 3:
            return "Quarta"
        case 4:
            return "Quinta"
        case 5:
            return "Sexta"

    return None

# Desafio FizzBuzz em Python

def fizz_buzz(valor):
    lista = []
    for i in range(1, valor + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append("TeAmo")
        elif i % 3 == 0:
            lista.append("Te")
        elif i % 5 == 0:
            lista.append("Amo")
        else:
            lista.append(i)

    return lista

# fizz_buzz(10)

# Nota Conceito

def nota_conceito(nota):
    if nota >= 9:
        return "A"
    elif nota >= 7:
        return "B"
    elif nota >= 5:
        return "C"
    else:
        return "D"

# Maior Valor

def maior_valor(a, b, c):
    return max(a, b, c)

# Tabuada

def tabuada(sequencia):
    tab = []
    contador = 0
    for i in range(1, 11):
        contador += 1
        tab.append(f"{sequencia} * {contador} = {sequencia * contador}")
    return tab

# tabuada(2)

