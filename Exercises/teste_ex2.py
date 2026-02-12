from Exercises.ex2 import *

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

def testando_semana():
    assert dia_semana(1) == "Segunda"
    assert dia_semana(2) == "Terça"
    assert dia_semana(3) == "Sábado"

def testando_fizz():
    assert fizz_buzz(10) == [1, 2, "Te", 4, "Amo", "Te", 7, 8, "Te", "Amo"]

def testando_nota_conceitual():
    assert nota_conceito(2) == "D"
    assert nota_conceito(6) == "C"
    assert nota_conceito(8) == "B"
    assert nota_conceito(10) == "A"

def testando_maior_valor():
    assert maior_valor(1, 2, 3) == 3
    # assert maior_valor(1, 2, 3) == 2

def testando_tabuada():
    assert tabuada(2) == ['2 * 1 = 2', '2 * 2 = 4', '2 * 3 = 6', '2 * 4 = 8', '2 * 5 = 10', '2 * 6 = 12', '2 * 7 = 14', '2 * 8 = 16', '2 * 9 = 18', '2 * 10 = 20']

def test_ano_bissexto():
    assert ano_bissexto(2000) == "Bissexto"
    assert ano_bissexto(1900) == "Não é um ano bissexto"
    assert ano_bissexto(2024) == "Bissexto"
    assert ano_bissexto(2023) == "Não é um ano bissexto"

def test_numero_primo():
    assert numero_primo(10) == "Não é primo"
    assert numero_primo(11) == "É primo"

def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(1) == 1
    assert fatorial(0) == 1