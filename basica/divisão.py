from uteis import Uteis


def divisor(D, d) -> tuple:
    q = int(D / d)
    r = D % d if D else 0
    return (q, r)


def dividendo(d, q, r):
    D = d * q + r
    return D


dividendo_ = Uteis.input_number('Digite o dividendo: ')
divisor_ = Uteis.input_number('Digite o divisor: ')
resultado = divisor(dividendo_, divisor_)
print(f"Quociente: {resultado[0]}")
print(f"Resto: {resultado[1]}\n")

divisor = Uteis.input_number('Digite o divisor: ', style='cyan')
quociente = Uteis.input_number('Digite o quociente: ', style='cyan')
resto = Uteis.input_number('Digite o resto: ', style='cyan')
dividendo = dividendo(divisor, quociente, resto)
print('[Dividendo = divisor * quociente + resto]')
print(f'{dividendo} = {divisor} * {quociente} + {resto}')
