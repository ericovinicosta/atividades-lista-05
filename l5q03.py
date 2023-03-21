'''
3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma_tres(a, b, c):
    return a+b+c

numero1 = int(input('Digite o 1º valor inteiro:'))
numero2 = int(input('Digite o 2º valor inteiro:'))
numero3 = int(input('Digite o 3º valor inteiro:'))

print(soma_tres(numero1, numero2, numero3))