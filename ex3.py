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

# contar_letras()

# reverter Array

def reverter_array():
    arr = [1, 2, 3, 4, 5]
    arr_2 = []
    for i in range(len(arr) - 1, -1, -1):
        arr_2.append(arr[i])
    print(arr_2)

# reverter_array()

def somar_valores():
    arr = [1, 2, 3, 4, 5]
    soma = 0
    for i in range(len(arr) - 1, -1, -1):
        soma += arr[i]
    print(soma)

# somar_valores()

def array_sem_repeticao():
    arr = [1, 1, 1, 2, 4, 5, 5, 6]
    arr2 = []
    for i in range(0, len(arr), 1):
        if not arr[i] in arr2:
            arr2.append(arr[i])
    print(arr2)

# array_sem_repeticao()

def string_to_capital():
    arr_string = ['arroz', 'batata', 'pão', 'python', 'estrogénio']
    resultado = [p.capitalize() for p in arr_string]
    # for i in range(0, len(arr_string)):
    #     resultado.append(arr_string[i].capitalize())

    print(resultado)

string_to_capital()