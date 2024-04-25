valorProduto=int(input('Informe o valor do produto: R$'))
condicaoPagamento=int(input('Qual vai ser a forma de pagamento?\n (1) À vista em inheiro/cheque \n (2) À vista no cartão de crédito \n (3) Em até 2x no cartão de crédito \n (4) 3x ou mais no cartão de crédito \n'))

dinheiroCheque=valorProduto-(valorProduto*0.1)

credito_A_Vista=valorProduto-(valorProduto*0.05)

credito_Duas_Vezes=valorProduto

credito_Tres_ou_Mais=valorProduto+(valorProduto*0.1)

if condicaoPagamento == 1:
    print('À vista em dinheiro ou cheque: R$',dinheiroCheque)
elif condicaoPagamento == 2:
    print('À vista no cartão de crédito: R$',credito_A_Vista)
elif condicaoPagamento == 3:
    print('Em até 2x no cartão de crédito: R$',credito_Duas_Vezes)
elif condicaoPagamento == 4:
    print('3x ou mais no cartão de crédito: R$',credito_Tres_ou_Mais)
else:
    print('Não trabalhamos com essas condições!')

