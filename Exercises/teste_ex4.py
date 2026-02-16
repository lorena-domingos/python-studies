from Exercises.ex4 import *

def test_palindrome():
    assert palindrome() == "É um palíndromo"

def test_bigger_word():
    assert bigger_word() == "JavaScript"

def test_words_count():
    assert words_count() == 3

def test_short_words():
    assert short_words(2) == ['BA', 'RJ']

def test_concatenar():
    assert concatenar_array() == [1, 2, 3, 4, 5, 6]