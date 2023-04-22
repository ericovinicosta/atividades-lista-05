'''
    10. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
from random import random, randrange, randint

def jogar_dados() -> int:
    jogada = randint(1,6)
    return jogada

def jogar() -> int:
    dado_1 = jogar_dados()
    dado_2 = jogar_dados()
    return dado_1 + dado_2

def jogo():
    jogada = jogar()

    ganhar = (7,11)
    craps = (2,3,12)

    if jogada in ganhar:
        print(f'{jogada} Parabéns, Ganhou!!')
    elif jogada in craps:
        print(f'{jogada} Sinto muito, CRAPS Perdeu!!')
    else:
        print(f'A jogada foi: {jogada}')
        while(True):
            resultado = jogar()
            if resultado == jogada:
                print(f'{resultado} Parabéns, Ganhou!!')
                break
            elif resultado == 7:
                print(f'{resultado} Sinto muito, Perdeu!!')
                break
            print(f'Jogadada: {resultado}')

if __name__ == '__main__':
    jogo()