i=int(input('Informe o código'))

a=float(input('Primeiro valor real:'))
b=float(input('Segundo valor real:'))
c=float(input('Terceiro valor real:'))

maior=a
if a > b and b > a:
    intermediario=b
    menor=c

intermediario=a
if a < b and a > c:
    maior=b
    menor=c

menor=a
if a < b and b < c:
    intermediario=b
    maior=c

if i == 1:
    print('Valores em ordem crescente',menor,intermediario,maior)
elif i == 2:
    print('Valores em ordem descrescente',maior,intermediario,menor)
elif i == 3:
    print('Valores misturados',intermediario,maior,menor)
else:
    print('Valores inválidos')

