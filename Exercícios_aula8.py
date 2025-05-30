# EXERCÍCOS 1
numero = int(input('Digite um número: '))
if numero >= 0:
     print('o número é positivo')
else:
    print('O número é negativo')

print()
# EXERCÍCIO  2
idade = int(input('Digite sua idade: '))

if idade >= 16:
    print('Você pode votar')
else:
    print('Você não tem idade para votar')
    
print()
# EXERCÍCIO 3
numero = int(input('Digite um número de 0 a 10'))

if numero % 2 == 0:
    print(' par')
else:
    print('Impar')

print()
#EXERCÍCIO 4
tr1 = int(input('Digite um lado do triângulo'))
tr2 = int(input('Digite outro lado do triângulo'))
tr3 = int(input('Digite o último lado do triângulo'))

if tr1 == tr2 == tr3:
    print('É um triângulo equilátero')
elif tr1 == tr2 != tr3:
    print('É um triângulo isóceles')
elif tr1 != tr2 != tr1  == tr3:
    print('É um triângulo isóceles')
elif tr1 != tr2 != tr3:
    print('É um triângulo escaleno')
elif tr1 != tr2 == tr3:
    print('É um triâmgulo isóceles')
    
print()
# EXERCÍCIO 5
n1 = int(input(' Escreva um número:'))
if n1 % 7 == 0 or n1 % 5 == 0 :
    print( ' Seu número é múltiplo de 7 e 5 ')
else:
    print('Seu número não é múltiplo de 7 e 5')

print()
# EXERCÍCIO 6
nmr = int(input('Digite um número para verificar se ele é positivo e maior que dez'))

if nmr >= 10:
    print('O número é positivo e maior que dez')
else:
    print('Seu número precisa ser maior que 10 e positivo')

print()
# EXERCÍCIO 7
n1 = int(input('Digite um número'))
if n1 % 3 == 0 or n1 % 5 == 0:
    print('Seu número é divisível por 3 ou por 5 ')
else:
    print('Seu número não é divisivel nem por 3 nem por 5')

