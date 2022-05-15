
#převodníky
from sympy.combinatorics.graycode import gray_to_bin
from sympy.combinatorics.graycode import bin_to_gray

import math
import random
#regex
import re

import numpy as np

class Koder:
    @staticmethod
    def gray_do_dec(n):
        n = gray_to_bin(n)
        return int(n, 2)

    @staticmethod
    def dec_do_gray(n):
        n = "{0:b}".format(n)
        return bin_to_gray(n)

class ClimberAlg:
    def __init__(self, function, params_of_fn):
        self.function = function
        self.params_of_fn = params_of_fn
        self.array_of_points = []
        self.center = 0

    # tmax - počet iterací
    # width - délka jednoho grayova čísla
    # params_of_fn - počet grayových čísel -> alfa = (a1,a2,....,an)
    # c0 - počet vygenerovaných potomků
    # f_min - minimum funkce
    # alfa - vektor kodovaný v grayove kodu
    def run(self, tmax, width , mutate_koef, number_of_childs):
        alfa_min = '1' * width * self.params_of_fn
        alfa_decimal_array = self.get_alfa_decimal_array(width, alfa_min)
        f_min = self.function(*alfa_decimal_array)
        self.center = (2 ** width) / 20
        for i in range(tmax):
            alfa = self.choose_best_child(alfa_min, number_of_childs, mutate_koef, width, f_min)
            alfa_decimal_array = self.get_alfa_decimal_array(width,alfa)
            fun = self.function(*alfa_decimal_array)
            if(fun < f_min):
                f_min = fun
                alfa_min = alfa
                print(f'počet: {i}')
                print(f'f({alfa_decimal_array})')
                print('výsledek funkce:',f_min)

        return self.array_of_points

    def get_alfa_decimal_array(self,width,alfa):
        alfa_splited = re.findall('.' * width, alfa)
        alfa_decimal = []
        for j in range(self.params_of_fn):
            alfa_decimal.append((Koder.gray_do_dec(alfa_splited[j]) / 10) - self.center ) # můžu ovlivnit desetinná čísla
        return alfa_decimal

    def choose_best_child(self, alfa, number_of_childs, mutate_koef, width, f_min):
        best = alfa
        best_alfa_decimal = self.get_alfa_decimal_array(width, best)
        fun_min = f_min
        self.array_of_points.append([fun_min, *best_alfa_decimal, True])
        for i in range(number_of_childs):
            new_alfa = self.mutate(alfa, mutate_koef)
            alfa_decimal_array = self.get_alfa_decimal_array(width, new_alfa)
            fun = self.function(*alfa_decimal_array)
            self.array_of_points.append([fun, *alfa_decimal_array, False])
            if (fun < fun_min):
                best = new_alfa
                fun_min = fun
        return best

    def mutate(self, alfa, mutate_koef):
        new_alfa = []
        for a in alfa:
            new_alfa.append(('0' if a else '1') if mutate_koef >= random.randint(1, 101) else a)
        return ''.join(new_alfa)


