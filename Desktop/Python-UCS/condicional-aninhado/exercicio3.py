altura=float(input('Informe a sua altura:'))
sexo=(input('Selecione o seu sexo:\n (M) Masculino \n (F) Feminino \n'))

idealMasculino=(72.7*altura) - 58
idealFeminino=(62.1*altura) - 44.7

if sexo == 'M' or sexo == 'm':
    pesoIdeal=idealMasculino
    print('O seu peso ideal é:',pesoIdeal)
elif sexo == 'F' or sexo == 'f':
    pesoIdeal=idealFeminino
    print('O seu peso ideal é:',pesoIdeal)
else:
    print('Você nos informou valores inválidos. Tente novamente!')
