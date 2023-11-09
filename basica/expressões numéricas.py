#########################################################
# Expressões Numéricas
#
#     Prioridade de Símbolos:
#         1º parênteses ()
#         2º colchetes []
#         3º chaves {}
#
#     Prioridade nas Operações:
#         1º potências ou raízes
#         2º multiplicação ou divisão
#         3º adição ou subtração
#
#     Exemplos de Expressões:
#         7 + {20 + [30 - (11 + 5) + 2]}
#         7 * {25 - [(12 + 9) - 14] + 3 + 0}
#         1453 - { 6 * (9 + 4) + [50 * 24 + 3] - 80} - 6
# 
#########################################################


def expressão_numérica(exp: str):
    parênteses = colchetes = chaves = ''

    print(exp)

    # Parênteses:
    if '(' in exp:
        ini = exp.find('(')
        fin = exp.find(')')
        parênteses = exp[ini: fin+1]
        exp = exp[:ini] + str(eval(parênteses)) + exp[fin+1:]
        print(exp)

    # Colchetes:
    if '[' in exp:
        ini = exp.find('[')
        fin = exp.find(']')
        colchetes = exp[ini+1: fin]
        exp = exp[:ini] + str(eval(colchetes)) + exp[fin+1:]
        print(exp)

    # # Chaves:
    if '{' in exp:
        ini = exp.find('{')
        fin = exp.find('}')
        chaves = exp[ini+1: fin]
        exp = exp[:ini] + str(eval(chaves)) + exp[fin+1:]
        print(exp)

    print(eval(exp))


expressão = str(input('\33[1;34mDigite a expressão numérica(max uma de cada na expressão): \33[m'))
expressão_numérica(expressão)
