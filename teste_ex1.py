from ex1 import *

def teste_soma():
    assert soma(2, 3) == 5

def teste_multiplicar():
    assert multiplicar(2, 3) == 6

def teste_dividir():
    assert dividir(6, 3) == 2

def teste_subtrair():
    assert subtrair(3, 2) == 1

def teste_impar_par():
    assert impar_par(3) == "Ímpar"

def teste_maior_numero():
    assert maior(4, 2) == "Menor"

def teste_idade():
    assert maior_idade(10) == "Maior de idade"

def teste_desconto():
    assert desconto(100, 10) == 90

def teste_dobro():
    assert valor_dobro(2) == 4

def teste_multiplo_cinco():
    assert multiplo_de_cinco(25) == True

def teste_fahrenheit():
    assert fahrenheit(30) == 86

def teste_sequencia():
    assert sequencia_de_dez() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]