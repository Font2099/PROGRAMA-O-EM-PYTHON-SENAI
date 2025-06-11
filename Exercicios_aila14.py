#ATIVIDADE 3

str = input('Digite uma letra:' )

match str:
    case '':
        print('Você não digitou nada')
    case _:
        print('Você digitou algo')

print()
#ATIVIDADE 4
num = int(input('Digite um número: '))

match num:
    case 10:
        print('Seu número é 10')
    case  x if x > 10:
        print('O número é maior que dez')
    case _:
        print('O número é menor que dez')

print()
#ATIVIDADE 5 

idade = int(input('Digite sua idade:'))

match idade:
    case x if x <= 12:
        print('Você é uma criança')
    case x if x > 12 and x  <= 17:
        print('Você é um adolecente')
    case  x if x > 17 and x <= 35:
        print('Você é um(a) jovem')
    case x if x > 35 and x <=64:
        print('Você é um(a) adulto(a)')
    case _:
        print('Você é idoso')
