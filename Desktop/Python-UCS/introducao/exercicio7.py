codigo=int(input('Qual o código do seu pedido? \n'))
if codigo < 100 or codigo > 105:
    print('ERRO: Código inválido')
elif codigo == 100:
    quantidade=int(input('Quantos desse você vai querer? \n'))
    valorFinal=10*quantidade
    print('Valor total do pedido: R$',valorFinal)
elif codigo == 101:
    quantidade=int(input('Quantos desse você vai querer? \n'))
    valorFinal=18*quantidade
    print('Valor total do pedido: R$',valorFinal)
elif codigo == 102:
    quantidade=int(input('Quantos desse você vai querer? \n'))
    valorFinal=20*quantidade
    print('Valor total do pedido: R$',valorFinal)
elif codigo == 103:
    quantidade=int(input('Quantos desse você vai querer? \n'))
    valorFinal=5*quantidade
    print('Valor total do pedido: R$',valorFinal)
elif codigo == 104:
    quantidade=int(input('Quantos desse você vai querer? \n'))
    valorFinal=15*quantidade
    print('Valor total do pedido: R$',valorFinal)
else:
    codigo == 105
    quantidade=int(input('Quantos desse você vai querer? \n'))
    valorFinal=4*quantidade
    print('Valor total do pedido: R$',valorFinal)
