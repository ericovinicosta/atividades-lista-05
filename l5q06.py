"""_summary_
6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor 'A' para A.M. e 'P' para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""
from datetime import datetime


def converte_hora_24_12(hora_str):
    hora = int(hora_str)
    if int(hora) > 12:
        hora -= 12
    return hora


def mostrar(hora_str):
    hora = hora_str.split(':')
    if int(hora[0]) < 12:
        am_pm = 'A'
    else:
        am_pm = 'P'

    return f'{converte_hora_24_12(hora[0]):2}:{hora[1]:2} {am_pm}'


hoje = datetime.today()
hora = hoje.strftime("%H:%M")

print(mostrar(hora))
