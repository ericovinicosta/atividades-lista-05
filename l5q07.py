"""Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso."""


def valor_pagamento(valor: float, dias_em_atraso: int) -> float:
    multa = 0.03
    juro_diario = 0.01
    valor_multa = valor * multa
    valor_juros = valor * dias_em_atraso * juro_diario
    return float(f'{valor_juros + valor_multa + valor:.2f}')


def armazena_lista(lista_calculos: list, valor: float) -> None:
    lista_calculos.append(valor)


def principal():
    lista_de_valores = []
    while (True):
        valor_original = float(input('Digite o valor da prestação: '))
        if valor_original == 0:
            return lista_de_valores
        dias_atraso = int(input('Informe quantos dias em atraso: '))
        valor_atual = valor_pagamento(valor_original, dias_atraso)
        print(f'O valor atual para pagamento é: R$ {valor_atual}')
        armazena_lista(lista_de_valores, valor_atual)
        print()


def soma(lista_calc):
    soma = 0
    for pag in lista_calc:
        soma += pag
    return soma


lista_calc = principal()
print(f'Quantidade de pagamento: {len(lista_calc)}')

print(f'O Valor total é: {soma(lista_calc)}')
