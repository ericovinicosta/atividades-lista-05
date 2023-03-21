'''2. Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
       para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''
def repetir_vezes(numero):
    for n in range(numero):
        print(f'{n+1:3}', end=' ')
    print()

numero = int(input('Digite a quantidade de vezes: '))
for n in range(1,numero+1):
    repetir_vezes(n)