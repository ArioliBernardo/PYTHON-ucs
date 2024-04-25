anoNascimento=int(input('Informe o seu ano de nascimento: '))

idade=2024-anoNascimento
situacao1=18-idade
situacao2=idade-18

if idade < 18:
    print('Ano de nascimento:',anoNascimento)
    print('Idade:',idade,'anos')
    print('Situação: Ainda não precisa se alistar. Faltam',situacao1,'ano(s) para o alistamento obrigatório')
else:
    print('Ano de nascimento:',anoNascimento)
    print('Idade:',idade,'anos')
    print('Situação: Já passou o prazo do alistamento. Está',situacao2,'ano(s) atrasado')
