#vazia
lista = []

#lista preenchia

lista_teste = [1,2,3,4,5,10,11]
#              0 1 2 3 4  5  6

print(lista_teste[-3])


lista_teste[5] = 100
print(lista_teste)

#funções:

lista = []

#alteram a estrutura da lista:
#append() extend() +=()
# append vai adicionar apenas 1 dado

lista.append(10)

print(lista)

#varios dados no final da lista -> extend() +=()
lista.extend([10,20,30,40,50,100, ' teste', True])
print(lista)

lista += ('a','b')
print(lista)

# add dado em um indice especifico

lista.insert(0,200)

print(lista)

#deltar dado del remove pop

lista.pop()

lista.pop(0)

print(lista)

lista.remove('a')

del lista[0]

print(lista)