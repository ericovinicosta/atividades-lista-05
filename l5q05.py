"""
5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
“altera” o valor de custo para incluir o imposto sobre vendas.
"""
def soma_imposto(taxa_imposto, custo):
    return custo * (1+taxa_imposto/100)

custo_principal = float(input('Entre com o valor do custo: '))
taxa = float(input('Entre com a a taxa aplicada: '))

custo_principal = soma_imposto(taxa, custo_principal)

print(f'O valor após a taxa é: R$ {custo_principal:.2f}')