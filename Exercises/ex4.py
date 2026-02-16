import re

# Palindrome

def palindrome():
    word = "ovo".lower()
    reversed_word = word[::-1]
    if word == reversed_word:
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"

# palindrome()

# Bigger Word

def bigger_word():
    word = "Eu prefiro JavaScript"
    word_list = word.split()
    bigger_one = ""
    for i in word_list:
        if len(i) > len(bigger_one):
            bigger_one = i
    return bigger_one

# bigger_word()

# Words Count

def words_count():
    word = "Eu prefiro JavaScript"
    word_list = word.split()
    qtd = len(word_list)
    return qtd
    # print(qtd)

# words_count()

# Short Words

def short_words(valor):
    palavras = "BA, RJ, Ame, Lore, Japão"
    lista_palavras = palavras.split(",")
    palavras_curtas = []
    for i in lista_palavras:
        i = i.strip()
        if len(i) <= valor:
            palavras_curtas.append(i)
    return palavras_curtas

# short_words(2)

# concatenar array

def concatenar_array():
    arr = [1, 2, 3]
    arr_2 = [4, 5, 6]
    arr_final = [*arr, *arr_2]
    # for i in arr:
    #     arr_final.append(i)
    #
    # for j in arr_2:
    #     arr_final.append(j)

    return arr_final

# concatenar_array()

def intersecao_arr():
    a = ["arroz", "batata", "naruto"]
    b = ["arroz", "sasuke", "naruto"]
    c = []
    for i in a:
        if i in b:
            c.append(i)
    print(c)

# intersecao_arr()

def remover_vogais():
    frase = "É 4 da manhã e cá estou eu descobrindo como usar regex no Python"
    nova_frase = re.sub(r'[aeiouáéíóúãõ]', '', frase, flags=re.IGNORECASE)
    print(nova_frase)

remover_vogais()

