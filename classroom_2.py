"""
OPERAÇÕES CONDICIONAIS
"""

# if /   elif        / else
# se /   se não se   / se não


entrada = input('Voce quer "entrar" ou "sair": ')


if entrada == "entrar":
    print('Voce entrou!')
elif entrada == "sair":
    print('Voce saiu!')
else:
    print('Comando nao reconhecido.')


print('Continuacao do sistema...')

print('')
print('')
print('')

# ----------------------------------------------------

condicao = True

if condicao:
    print('Condicao verdadeira!')
else:
    print('Condicao nao verdadeira!')

print('')
print('')
print('')

# ----------------------------------------------------

"""
OPERADORES RELACIONAIS

>   maior            2 > 1
>=  maior ou igual   2 >= 2
<   menor            1 < 2
<=  menor ou igual   2 <= 2
==  igual            'a' == 'a'
!=  diferente        'a' > 'b'
"""

comparacao = 5>= 5

if comparacao:
    print('Condicao verdadeira!')
else:
    print('Condicao nao verdadeira!')

print('')
print('')
print('')

# ----------------------------------------------------

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

if condicao1:
    print('Condicao 1 verdadeira!')
elif condicao2:
    print('Condicao 2 verdadeira!')
elif condicao3:
    print('Condicao 3 verdadeira!')
elif condicao4:
    print('Condicao 4 verdadeira!')
else:
    print('Nenhuma condicao verdadeira')

print('')
print('')
print('')

# ----------------------------------------------------

"""
Utilizar 'and' para verificar 2 condicoes para acessar algo.
"""

condicao_1 = True
condicao_2 = True

if condicao_1 and condicao_2:
    print('Condicoes 1 e 2 verdadeiras!')
else:
    print('Uma ou Nenhuma condicao verdadeira')

print('')
print('')
print('')

# ----------------------------------------------------

"""
Utilizar 'or' para verificar 2 condicoes e aceitar uma ou outra.
"""

entrada_1 = True
entrada_2 = False

if condicao_1 or condicao_2:
    print('Voce entrou!')
else:
    print('Voce nao entrou!')

senha = input('Digite sua senha: ') or 'Sem senha'
print(senha)

print('')
print('')
print('')

# ----------------------------------------------------

"""
Operador 'not', inverte a expressao do 'if'
"""

nova_senha = input("Senha: ")

if not nova_senha:
    print('Voce nao digitou nada!')

print('')
print('')
print('')

# ----------------------------------------------------

"""
Operadore 'in' e 'not in' -> 'Entre' e 'Nao Entre'
"""

lista_numeros = [1, 2, 3, 4, 5]
numero_escolhido = 5

if numero_escolhido in lista_numeros:
    print('O numero escolhido esta na lista!')
elif numero_escolhido not in lista_numeros:
    print('O numero escolhido NAO esta na lista!')