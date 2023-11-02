from uteis import Uteis


def subtrair(minu, subt) -> [int, float]:
    dife = minu - subt
    return dife


minuendo = Uteis.input_number('Digite o minuendo: ')
subtraendo = Uteis.input_number('Digite o subtraendo: ')

diferença = subtrair(minuendo, subtraendo)

print(diferença)
