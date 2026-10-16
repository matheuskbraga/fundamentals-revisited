"""
LISTAS
"""

lista = ['Matheus', 2, 3.14, True, []]

print(lista)

#-----------------------------------------

"""
CRUD da lista- Criar, le, alterar, pagar
"""

lista_nomes = ['Matheus', 'Luiz', 'Paulo', 'Maurício', 'Bitas']
lista_nomes[0] = 'Braga'
del lista_nomes[3]
lista_nomes.append('Johnson')
ultimo_valor = lista_nomes.pop()
print(lista_nomes)
print('Item removido:', ultimo_valor)