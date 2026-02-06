# parâmetro padrão

def oi_mundo(name ="Lorena"):
    return f'Olá {name}!'

def media_arr():
    arr = [1, 2, 3, 4, 5, 6]
    return sum(arr) / len(arr)

def filtrar_pares():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = []
    for i in arr:
        if i % 2 == 0:
            pares.append(i)
    return pares

# filtrar_pares()

def maior_menor_numero():
    arr = [1, 2, 3, 4, 5, 6, 7]
    max_value = max(arr)
    min_value = min(arr)
    return f'{max_value}/{min_value}'

def contar_letras():
    palavra = "banana"
    obj = {}
    for i in palavra:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    print(obj)

contar_letras()