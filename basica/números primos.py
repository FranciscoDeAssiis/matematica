# IN = {0, 1, 2, 3, 4, ...}

# Nª Primo: Quando for divisível somente por 1 E ele mesmo.
# Ex:
#   2, 3, 5, 7, 11, 13, 17, ...
#   2 é o único primo par, todos os outros são ímpares.

# Nª Composto: Quando possuir outros divisores além do número 1 e ele mesmo.
# Ex:
#   12 - 1, 12, 4, 6
#   21 - 1, 21, 3, 7
#   25 - 1, 25, 5
#   ...
# Obs: Todos os números compostos podem ser transformados em fatores primos.


# Como saber se um número natural é primo?
# Regra:
#   O Nª é primo se as divisões sucessivas
#   por números primos resultarem resto
#   diferente de zero até o divisor ser
#   maior ou igual ao quociente.


# Ex:
#   143 é primo(divisível por 1 e ele mesmo)? Não, porque é divisível por 11
#       143 / 2 = 71 (resto 1)
#       143 / 3 = 47 (resto 2)
#       143 / 5 = 28 (resto 3)
#       143 / 7 = 20 (resto 3)
#       143 / 11 = 13 (resto 0) (143 é divisível por 1, 11 e 143, por tanto é composto)
#
#   127 é primo?
#       126 / 2 = 63 (resto 1)
#       126 / 3 = 42 (resto 1)
#       127 / 5 = 22 (resto 2)
#       127 / 7 = 18 (resto 1)
#       127 / 11 = 11 (resto 6) ⇾ Divisor igual ou maior ao quociente, por tanto, é primo.
#
#   Se p e q são números primos, tais que p - q = 41, então o valor de p + q é:
#       a) 91.
#       b) 79.
#       c) 73.
#       d) 45.
#       e) 43.
#
#       p - q = 41
#       p - 2 = 41
#       p = 41 + 2
#       p = 43//
#
#       p + q = 45//


def is_primo(n: int, exibir_print=True):
    # Se número for divisível por 1 e por ele mesmo:
    compostos = []
    primo_ou_composto = 0

    for x in range(1, n):
        if n % x == 0:  # Resto igual a 0:
            if exibir_print:
                print('Primo!: ', x)
            primo_ou_composto += 1
            compostos.append(x)

        else:  # Resto diferente de 0:
            if exibir_print:
                print('Não Primo!: ', x)

    if primo_ou_composto == 1:  # Primo:
        return f'   \33[1;36mPRIMO! \33[m'

    elif primo_ou_composto > 1:  # Composto:
        compostos.append(n)
        return f'   \33[34mCOMPOSTO! \33[1;32m{len(compostos)}\33[34m - {compostos}\33[m'

    else:
        return f'\33[31mError!\33[m'


print('\33[1;33m--- PRIMO OU COMPOSTO ---\33[m')
while True:
    num = int(input("\33[1;32mNÚMERO NATURAL: \33[m"))
    result = is_primo(num, False)
    print(result, end=f'\n\n{"-"*60}\n')
