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