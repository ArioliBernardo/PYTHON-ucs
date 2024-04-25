sexo=(input('Qual seu sexo? \n'))
tempoTrabalho=int(input('Quanto tempo você está na empresa? \n'))
salarioAtual=int(input('Qual o seu salário atual? \n'))

bonus1=salarioAtual*0.2
bonus2=salarioAtual*0.25
bonus3=salarioAtual+1000

if sexo == 'M' or sexo == 'm' and tempoTrabalho > 15:
    print('R$',bonus1)
elif sexo == 'F' or sexo == 'f' and tempoTrabalho > 10:
    print('R$',bonus2)
else:
    print('R$',bonus3)

