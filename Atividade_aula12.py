import random

# ATIVIDADE 1 

def num_ale():
    aleatorio = random.randint(5,10)
    print(aleatorio)
num_ale()

# ATIVIDADE 2

def num_ale3():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    n3 = random.randint(1,10)
    print(n1,n2,n3)
num_ale3()

# ATIVIDADE 3
def ran():
    var = random.randrange(10,31)
    print(var)
    
ran()



# ATIVIDADE 4

def contagem():
    for i in range(10,0,-1):
        print(i)
        
    print('Fogo !!!')
    
contagem()


# ATIVIDADE 5

def par():
    n = int(input('Digite um número:'))
    l = []
    for i in range(n):
        l.append(i)
        soma = sum(l)
    print(soma)
    
par()

# ATIVIDADE 6

def mult():
    n = int(input("digite o multiplicador da tabuada:"))
    for i in range (0,11):
        calculo = i * n
        print(n, "x",i,"=",calculo)
        
mult()

# ATIVIDADE 7

def impar():
    for i in range(99, 0, -2):
        print(i)
        
impar()