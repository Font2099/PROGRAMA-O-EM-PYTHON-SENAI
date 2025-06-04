# loop for =  para


# range

#for variavel in range(10):
 #   print(variavel)
    
    
# lista
    
#ATIVIDADE 1

n = 0
while n <= 1000:
   print(n)
   n = n + 1 

# ATIVIDADE 1 - B

lista_nomes = []
for n in range(1, 11):
    nome = input('Digite seu nome:')
    lista_nomes.append(nome)
print(lista_nomes)



# ATIVIDADE 2
senha = '3031'
acesso = 'jorge'
p  =   0
lista_notas  = []

while p  <= 3:
    senha_user = input('Digite sua senha: ')
    login =  input('Digite seu login')
    p = p + 1
    if senha == senha_user and login == acesso:
        print('Sistema de notas')
        quantas_notas =  int(input('Quantiade notas: '))
        for n in range(quantas_notas):
            nota =  float(input('Digita a nota: '))
            lista_notas.append(nota)
            soma = sum(lista_notas)
            media  =  soma / quantas_notas
        print('Media - ', media)
        break
             
        
        
    else:
        print('Digitação incorreta! ')
else:
    print('Conta bloqueada!!')
    
    
