"""
LAÇOS DE REPETIÇÃO
"""

condicao = True

while condicao:
    x = input('Digite uma palavra: ')
    print(x)

# ----------------------------------------

contador = 0

while contador < 10:
    print(contador)
    contador += 1
print('Acabou!')

# ----------------------------------------

contador = 0

while contador < 10:

    print(contador)
    contador += 1

    if contador == 4:
        break

print('Acabou!')

# ----------------------------------------

contador = 0

while contador < 10:

    if contador == 4:
        contador += 1  
        continue

    print(contador)
    contador += 1

print('Acabou!')

# ----------------------------------------

texto = 'Python'
novo_texto = ''

for letra in texto:  
    print(letra)
    novo_texto += letra
print(novo_texto)

# ----------------------------------------

#           start, stop, step

numeros = range(0, 10, 2)

for numero in numeros:
    print(numero)
print('Fim')