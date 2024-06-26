﻿CONST_A_NAME = 'a'
CONST_B_NAME = 'b'
CONST_OP_NAME = 'op'


class Parser:
    def __init__(self, parsing_char=None):
        if parsing_char:
            self._parsing_char = parsing_char
        else:
            self._parsing_char = ' '

    @property
    def parsing_char(self):
        return self._parsing_char

    def parse(self, input_string):
        return input_string.split(self._parsing_char)


class CalculatorEngine:
    def __init__(self):
        self._parser = Parser()
        self._comands = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

    @staticmethod
    def transfer_type(value_str):
        if '.' in value_str:
            return float(value_str)
        return int(value_str)

    def collect_input(self, input_string):
        try:
            a, operator, b = self._parser.parse(input_string)
        except:
            print('Error')
            print("Use identation symbol: '%s'"
                  % self._parser.parsing_char())
            return {'a': 'No ',
                    'b': 'result',
                    'op': '+', }
        return {CONST_A_NAME: self.transfer_type(a),
                CONST_B_NAME: self.transfer_type(b),
                CONST_OP_NAME: operator}

    def execute(self, a, b, operator):
        if operator in self._comands:
            return self._comands.get(operator)(a, b)
        return None


class CalculatorInterface:
    def __init__(self):
        self._core = CalculatorEngine()

    def run(self):
        print('Start your input:')
        print('For example: 2 + 2 or exit to finish calculations')
        while True:
            input_string = input()
            if input_string == "exit":
                print('End')
                break
            input_data = self._core.collect_input(input_string)
            result = self._core.execute(a=input_data[CONST_A_NAME],
                                        b=input_data[CONST_B_NAME],
                                        operator=input_data[CONST_OP_NAME])
            print('Result: ', result, '\n')


interface = CalculatorInterface()
interface.run()
