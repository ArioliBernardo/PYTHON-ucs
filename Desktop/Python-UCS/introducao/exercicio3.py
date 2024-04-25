valorCasa=int(input('Informe o valor da casa:'))
salario=int(input('Informe o seu salário atual:'))
anos=int(input('Informe em quantos anos você vai pagar a casa:'))

porcentagemSalario=salario*0.3
    
if valorCasa / (15*12) > porcentagemSalario:
    print('Empréstimo negado')
else:
    print('Empréstimo aceito')
