ecommerce = {
    
    'livros' :{
        
        'a' : 50.0,
        'b': 70.0,
        'c' : 100.0,
        
        },
    
    "eletronicos" : {
        'tablets' : 3000,
        'fone' : 150,
        }
    
    
    
    
}

secao1 = input('Digite o seção 1 ')
secao2 = input('Digite o seção 2 ')

produto1 = input('Digite o produto 1 ')
produto2= input('Digite o produto 2 ')


carrinho = [produto1, produto2]
valores = [ecommerce[secao1][produto1], ecommerce[secao2][produto2]]
soma = sum(valores)

print(carrinho)
print('R$', soma)