codigo=int(input('Qual o código do seu cargo? \n'))

if codigo < 101 and codigo < 104:
        print('ERRO: Você não é nosso funcionário.')
elif codigo == 101:
        salarioAtual=int(input('Preencha com o seu salário atual: \n'))
        cargo='Gerente'
        valorAumento=salarioAtual*0.1
        novoSalário=salarioAtual+valorAumento
        print('Cargo:',cargo)
        print('Salário Antigo: R$',salarioAtual)
        print('Novo Salário: R$',novoSalário)
        print('Valor do aumento: R$',valorAumento)
elif codigo == 102:
        salarioAtual=int(input('Preencha com o seu salário atual: \n'))
        cargo='Engenheiro'
        valorAumento=salarioAtual*0.2
        novoSalário=salarioAtual+valorAumento
        print('Cargo:',cargo)
        print('Salário Antigo: R$',salarioAtual)
        print('Novo Salário: R$',novoSalário)
        print('Valor do aumento: R$',valorAumento)
elif codigo == 103:
        salarioAtual=int(input('Preencha com o seu salário atual: \n'))
        cargo='Técnico'
        valorAumento=salarioAtual*0.3
        novoSalário=salarioAtual+valorAumento
        print('Cargo:',cargo)
        print('Salário Antigo: R$',salarioAtual)
        print('Novo Salário: R$',novoSalário)
        print('Valor do aumento: R$',valorAumento)
elif codigo == 104:
        salarioAtual=int(input('Preencha com o seu salário atual: \n'))
        cargo='Outros'
        valorAumento=salarioAtual*0.4
        novoSalário=salarioAtual+valorAumento
        print('Cargo:',cargo)
        print('Salário Antigo: R$',salarioAtual)
        print('Novo Salário: R$',novoSalário)
        print('Valor do aumento: R$',valorAumento)
else:
        print('ERRO: Você não trabalha aqui!')