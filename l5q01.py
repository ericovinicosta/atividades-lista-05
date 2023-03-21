''' 1. Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.'''

def repetir_vezes(numero):
    for n in range(numero):
        print(f'{numero:4}', end='')
    print()

numero = int(input('Digite a quantidade de vezes: '))
for n in range(1,numero+1):
    repetir_vezes(n)