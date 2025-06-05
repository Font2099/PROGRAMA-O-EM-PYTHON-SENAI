#ATIVIDADE 1
print('Par ou ímpar')
def impar_par():
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        print('Número é par')
    else:
        print('Número é impar')
        
impar_par()
print()
# ATIVIDADE 2
def num_mult():
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite outro número:"))
    n3 = int(input("Digite o último número:"))
    print('=', n1 * n2 *n3)
    
num_mult()
print()
# ATIVIDADE 3
print('Exponenciação')
def expt():
    n1 = int(input("Digíte um número:"))
    n2 = int(input('Digite outro número:'))
    print('=', n1 ** n2)
    
expt()
print()

# ATIVIDADE 4
print('Habilitação')
def idade():
    ida = int(input('Digite sua idade'))
    if ida >= 18:
        print('Você pode dirigir')
    else:
        print('Você não pode dirigir')
             
idade()
print()

# ATIVIDADE 5
print('Vou descobrir sua idade')
def qual():
    n1 = int(input('Digite o ano que você nasceu:'))
    n2 = int(input('Em que anos estamos?'))
    print('sua idade é:',n2 - n1)
    
qual()
print()
# ATIVIDADE 6
def copa():
    copas = [1958, 1962, 1970, 1994, 2002]
    ano = int(input('Digite um ano que o Brasil foi campeão do mundo'))
    if ano in copas:
        print('O Brasil ganhou')
    else:
        print('O Brasil não ganhou esse ano')
    
copa()
print()

# ATIVIDADE 7
print('Restaurante')
def rest():
    cardapio = [ 'salada', ' macarronada', ' sanduiche', ' sorvete']
    print(cardapio)
    escolha = int(input("Digite o ID do produto"))
    print('Escolha', cardapio[escolha])
    
while True:
    rest()