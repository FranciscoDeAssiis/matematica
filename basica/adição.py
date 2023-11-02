from uteis import Uteis


def soma(parcela_1, parcela_2):
    total = parcela_1 + parcela_2
    return total


while True:
    parcela1 = Uteis.input_number('Primeira parcela: ')
    parcela2 = Uteis.input_number('Segunda parcela: ')
    soma = soma(parcela1, parcela2)
    print(soma)
