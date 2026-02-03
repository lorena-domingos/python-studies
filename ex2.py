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