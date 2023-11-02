from uteis import Uteis


def multiplicar(fator1, fator2) -> [int, float]:
    produto = fator1 * fator2


fator1 = Uteis.input_number('Digite o primeiro fator: ')
fator2 = Uteis.input_number('Digite o segundo fato: ')

produto = multiplicar(fator1, fator2)

print(produto)

