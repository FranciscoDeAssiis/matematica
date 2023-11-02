# Divisibilidade por 2:
# São todos os números pares -> terminados em 2, 4, 6, 8
# Ex:
#   368 é divisível sim! porque:
#     8 = par
#   4560 é divisível sim! porque:
#      0 = par
#   37 não! porque:
#    7 = impar



# Divisibilidade por 3:
# É quando a soma dos algarismos for divisível por 3.
# Ex:
#   3471 é divisível sim! porque:
#   3 + 4 + 7 + 1 = 15
#   (é divisível por 3? Sim!) 15 / 3 = 5
#
#   12937 não!
#   1 + 2 + 9 + 3 + 7 = 22
#   (é divisível por 3? Não!) 22 / 3 = 7.333...



# Divisibilidade por 4:
# Quando os dois últimos algarismos formarem um número divisível por 4.
# Ex:
#   578428 é divisível sim! porque:
#       28 / 4 = 7
#
#   3748900 é divisível sim! porque:
#        00 / 4 = 0
#
#   3750742 não!
#        42 / 4 = 10.5



# Divisibilidade por 5:
# Quando o último algarismo for um número divisível por 0 ou 5.
# Ex:
#   37418935 é divisível sim! porque:
#          5
#
#   37914703 não!
#          3



# Divisibilidade por 6:
# Quando o número é divisível por 2 E 3.
# Ex:
# 53427 não!
#     7 = impar (primeiro critério de divisibilidade por 2 não satisfeito)
#     5 + 3 + 4 + 2 + 7 = 21 / 3 = 7 (segundo critério de divisibilidade por 3 satisfeito)
#
# 106424 sim!
#      4 = par (primeiro critério de divisibilidade por 2 satisfeito)
#      1 + 0 + 6 + 4 + 2 + 4 = 17 / 3 = 5.666666666666667 (segundo critério de divisibilidade por 3 não satisfeito)
#
# 812472 não!
#      2 = par (primeiro critério de divisibilidade por 2 satisfeito)
#      8 + 1 + 2 + 4 + 7 + 2 = 24 / 3 = 8 (segundo critério de divisibilidade por 3 satisfeito)



# Divisibilidade por 7:
# Ex:
# 22389651536 é divisível sim! porque:
# (22) (389) (651) (536) -> grupos a cada 3
# restos da divisão: 1 4 0 4
# sinais alternados: +1 -4 +0 -4 = -7 (é divisível por 7? sim!)



# Divisibilidade por 8:
# Quando os três últimos algarismos formarem um número divisível por 8
# Ex:
#   3958743328 é divisível sim! porque:
#          328 / 8 = 41



# Divisibilidade por 9:
# Ex:
#   4901067 é divisível sim! porque:
#   soma: 4 + 9 + 0 + 1 + 6 + 7 = 27
#                                 27 / 9 = 3
#
#   307410541 não! porque:
#   soma: 3 + 0 + 7 + 4 + 1 + 0 + 5 + 4 + 1 = 25
#                                             25 / 9 = 10.555...



# Divisibilidade por 10:
# Quando o último algarismo for 0.
# Ex:
#   930 sim!
#   540 sim!
#   680 sim!



# Divisibilidade por 11:
# Ex: Fazer soma alternada
#                 10832041 é divisão exata! porque:
# soma alternada: 1 8 2 4 = 15
# soma alternada:  0 3 0 1 = 4
#                           15 - 4 = 11 (é divisível por 11? sim!)
#                                    11 / 11 = 1
#
#                 2357014982 não! porque:
# soma alternada: 2 5 0 4 8 = 19
# soma alternada:  3 7 1 9 2 = 22
#                             19 - 22 = -3 (é divisível por 11? Não!)
#                                       -3 / 11 = -0.2727272727272727



# Divisibilidade por 12, 13, 14, ...:
# Quando a multiplicação de dois números resultarem no divisor.
# Ex:
#   213145
#   3 * 4 = 12
#   é divisível por 12 se:
#       12 / 3 = 4 (divisão exata)
#       E
#       12 / 4 = 3 (divisão exata)
#   porque 3 vezes 4 é igual a 12


def divisibilidade_por_2(num, exi=False) -> bool:
    if int(str(num)[-1]) in [0, 2, 4, 6, 8]:
        if exi:
            print(f'Sim! {num} é divisível por 2.')
        return True
    else:
        if exi:
            print(f'Não! {num} não é divisão exata por 2.')
        return False


def divisibilidade_por_3(num, exi=False) -> bool:
    soma = 0
    for n in str(num):
        soma += int(n)
    if soma % 3 == 0:
        if exi:
            print(f'Sim! {num} é divisível por 3. Soma: {soma}')
        return True
    else:
        if exi:
            print(f'Não! {num} não é divisão exata por 3. Soma: {soma}')
        return False


def divisibilidade_por_4(num, exi=False) -> bool:
    n = int(str(num)[-1])
    if n % 4 == 0:
        if exi:
            print(f'Sim! {num} é divisível por 4. Final: {n}')
        return True
    else:
        if exi:
            print(f'Não! {num} não é divisão exata por 4. Final: {n}')
        return False


def divisibilidade_por_5(num, exi=False) -> bool:
    n = int(str(num)[-1])
    if n % 5 == 0 or n == 0:
        if exi:
            if n:
                print(f'Sim! {num} é divisível por 5. Final: {n}')
            else:
                print(f'Sim! {num} é divisível por 5, tem final 0.')
        return True
    else:
        if exi:
            print(f'Não! {num} não é divisão exata por 5. Final: {n}')
        return False


def divisibilidade_por_6(num, exi=False) -> bool:
    if divisibilidade_por_2(num) and divisibilidade_por_3(num):
        if exi:
            print(f'Sim! {num} É divisível por 6, porque {str(num)[-1]} é par e {num} é divisível por 3.')
        return True
    else:
        if exi:
            print(f'Não! {num} não é divisível por 6, porque não atende ao critério de divisão por 2 ou por 3.')
        return False


def divisibilidade_por_7(num, exi=False) -> bool:

    # sinais alternados: +1 -4 +0 -4 = -7 (é divisível por 7? sim!)
    lista = []
    n = str(num)[::-1]  # inverte a ordem dos números

    for x in range(0, len(n), 3):
        r = n[x:x+3][::-1]  # grupos de 3 em 3.
        lista.append(r)

    # Resto:
    restos = []
    for n in lista:
        restos.insert(0, int(n) % 7)  # adicionando na primeira posição corrigindo a ordem.

    sinal = '+'
    soma = 0
    for r in restos:  # Alternando sinais:
        if sinal == '+':
            soma += +r
            sinal = '-'
        elif sinal == '-':
            soma += -r
            sinal = '+'

    # Soma é divisível por 7?
    if soma % 7 == 0:
        if exi:
            print(f'{num} é divisível por 7. Divisão da soma dos restos por 7 deu exata: {soma} / 7 = {soma / 7}')
            return True
    else:
        if exi:
            print(f'{num} não é divisível por 7. Divisão da soma dos restos por 7 não foi exata: {soma} / 7 = {soma / 7}')
            return False


def divisibilidade_por_8(num, exi=False) -> bool:
    n = int(str(num)[-3:])
    if n % 8 == 0:
        if exi:
            print(f'Sim! {num} É divisível por 8, porque {n} / 8 = {n / 8} é divisão exata.')
        return True
    else:
        if exi:
            print(f'Não! {num} não é divisível por 8, porque {n} / 8 = {n / 8} não é divisão exata.')
        return False


def divisibilidade_por_9(num, exi=False) -> bool:
    soma = 0
    for n in str(num):
        soma += int(n)

    if soma % 9 == 0:
        if exi:
            print(f'{num} é divisível por 9, Soma dos algarismos {soma} / 9 = {soma / 9} é exata')
        return True
    else:
        if exi:
            print(f'{num} não é divisível por 9, Soma dos algarismos {soma} / 9 = {soma / 9} não é exata')
        return False


def divisibilidade_por_10(num, exi=True) -> bool:
    if str(num)[-1] == 0:
        if exi:
            print(f'{num} é divisível por 10, porque termina com 0.')
        return True
    else:
        if exi:
            print(f'{num} não é divisível por 10, porque não termina com 0')
        return False


def divisibilidade_por_11(num, exi=True) -> bool:
    soma1 = soma2 = 0
    for n, x in enumerate(str(num)):
        x = int(x)
        if n % 2 == 0:
            soma1 += x
        else:
            soma2 += x

    sub = soma1 - soma2

    if sub % 11 == 0:
        if exi:
            print(f'Sim! {num} é divisível por 11, porque a subtração dos números alternados é {sub} / 11 = {sub / 11} é divisão exata.')
        return True
    else:
        if exi:
            print(f'Não! {num} não divisível por 11, porque a subtração dos números alternados é {sub} / 11 = {sub / 11} não é divisão exata.')
        return False


def divisibilidade_por_numero(dividendo, divisor, exi=True):
    if dividendo % divisor == 0:
        if exi:
            print(f'{dividendo} é divisível por {divisor}!')
        return True
    else:
        if exi:
            print(f'{dividendo} não é divisível por {divisor}!')
        return False


# divisibilidade_por_2(368, True)
# divisibilidade_por_2(4560, True)
# divisibilidade_por_2(37, True)

# divisibilidade_por_3(3471, True)
# divisibilidade_por_3(12937, True)

# divisibilidade_por_4(578428, True)
# divisibilidade_por_4(3748900, True)
# divisibilidade_por_4(3750742, True)

# divisibilidade_por_5(37418935, True)
# divisibilidade_por_5(37914470, True)
# divisibilidade_por_5(37914703, True)

# divisibilidade_por_6(53427, True)
# divisibilidade_por_6(106424, True)
# divisibilidade_por_6(812472, True)

# divisibilidade_por_7(22389651536, True)
# divisibilidade_por_7(2323566, True)
# divisibilidade_por_7(2664434, True)

# divisibilidade_por_8(3958743328, True)
# divisibilidade_por_8(250023847, True)

# divisibilidade_por_9(4901067, True)
# divisibilidade_por_9(307410541, True)

# divisibilidade_por_10(2353637, True)
# divisibilidade_por_10(3443453450, True)

# divisibilidade_por_11(10832041, True)

# divisibilidade_por_numero(307410541, 9, True)
