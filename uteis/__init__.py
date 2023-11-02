class Uteis:

    @staticmethod
    def input_number(txt='Digite: ', style='blue', format_number=0) -> [int, float]:
        """
        Solicita e converte um número (inteiro ou flutuante) com estilo de texto colorido.

        :param txt: (str) Mensagem exibida para o usuário.
        :param style: (str) Estilo de cor do texto (default: 'blue').
        :param format_number: (int) Casas decimais para formatação (default: 0).
        :return: (int ou float): Número inserido pelo usuário.
        """

        style = style.upper()
        if style == 'RED':
            id_color = 31
        elif style == 'GREEN':
            id_color = 32
        elif style == 'YELLOW':
            id_color = 33
        elif style == 'BLUE':
            id_color = 34
        elif style == 'MAGENTA':
            id_color = 35
        elif style == 'CYAN':
            id_color = 36
        else:
            id_color = 34  # default: blue

        result = None
        while not isinstance(result, int) or not isinstance(result, float):
            result = input(f'\33[1;{id_color}m{txt}\33[m')

            if '.' in result:  # flutuante
                try:
                    result = float(result)
                    if format_number:
                        result = f'{result:,.{format_number}f}'
                    break
                except ValueError:
                    pass

            else:  # inteiro
                try:
                    result = int(result)
                    break
                except ValueError:
                    pass

        return result


if __name__ == '__main__':
    uteis = Uteis()
    resposta = uteis.input_number(format_number=2)
    print(resposta)
