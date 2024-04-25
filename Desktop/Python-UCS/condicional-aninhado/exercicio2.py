codigo=int(input('Escolha um código (1),(2),(3) ou (4)'))
num1=int(input('Informe o primeiro número: '))
num2=int(input('Informe o segundo número: '))
num3=int(input('Informe o terceiro número: '))

soma = num1 + num2 + num3
subtracao = num1 - num2 - num3
multiplicacao = num1 * num2 * num3
somaCubo = num1 ** 3 + num2 ** 3 + num3 ** 3

if codigo == 1:
    print('A multiplicação dos valores é:',multiplicacao)
elif codigo == 2:
    print('A soma dos valores é:',soma)
elif codigo == 3:
    print('A subtração dos valores é:',subtracao)
elif codigo == 4:
    print('A soma dos cubos é:',somaCubo)
else:
    print('Valor(es) inválido(s)')
