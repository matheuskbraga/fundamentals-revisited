"""
FUNÇÕES

Podem recerber parametros e argumentos e retornar valores especificos

Por padrao as funcoes retornam None
"""

def saudacao():
    return 'Ola Matheus, seja bem-vindo!'

saudacao()

# ------------------------------------------

def minha_funcao(a, b, c): # 'a' 'b' e 'c' sao os parametros
    return a + b + c

print(minha_funcao(1, 2, 3)) # '1' '2' e '3' sao os argumentos que serao passados para a funcao

# ------------------------------------------

"""
Argumento nomeado
"""

def soma(x, y):
    print(x+y)

soma(1, 2)
soma(y=2, x=30)

# ------------------------------------------

"""
Valores padrao para parametro, se nao for enviado valores para os parametros da funcao pelos argumentos.

Ex: z = None

"""

def funcao_soma(x, y, z=None):
    if z:
        print(x + y + z)
    else:
        print(x + y)

funcao_soma(6, 2, 3)
funcao_soma(6, 3)

# ------------------------------------------

"""
Escopo de funcoes
"""

def escopo():
    variavel_da_funcao = 1
    print(variavel_da_funcao)

escopo()
# print(variavel_da_funcao) # da erro pois o escopo deixa a variavel 'variavel_da_funcao' apenas dentro da funcao

x = 2

def minha_outra_funcao():
    x = 10
    print(x)

minha_outra_funcao() # altera o valor de 'x' apenas dentro da funcao
print(x) # permanece 2, pois eh uma variavel global

# ------------------------------------------

"""
Retorno das funcoes
"""

def multiplicar(x, y):
    if (x * y) >= 10:
        return x * y
    else:
        return 10

print(multiplicar(20, 10)) # retorna um 'int'

# ------------------------------------------

"""
args - argumentos nao nomeados

* - *args (empacotamento e desempacotamento)

"""

variavel_1, variavel_2, *resto_variaveis = 1, 2, 3, 4, 5

print(variavel_1, variavel_2, resto_variaveis)


def somando(*args): # '*args' empacota todos os argumentos que eu mandar para a funcao, tornando 'args' uma tupla
    #print(args)
    total = 0
    for numero in args:
        print(numero)
        total += numero
    print('TOTAL:', total)
    return total

somando(1, 2, 3, 4, 5)