from ex2 import *

def testando_triangulo():
    assert tipo_triangulo(2, 3, 4) == "Escaleno"
    assert tipo_triangulo(0, 0, 0) == "Inválido"
    assert tipo_triangulo(1, 1, 1) == "Equilátero"
    assert tipo_triangulo(1, 2, 2) == "Isósceles"

def testando_calculadora():
    assert calculadora(2, "*", 2) == 4
    assert calculadora(2, "+", 2) == 4
    assert calculadora(2, "-", 2) == 0
    assert calculadora(2, "/", 2) == 1
    assert calculadora(2, "", 2) == "Inválido"
