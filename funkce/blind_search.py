
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

class BindAlg:
    def __init__(self, function):
        self.function = function
    # tmax - maximální počet iterací
    # width - délka jednoho grayova čísla
    # params_of_fn - počet grayových čísel -> alfa = (a1,a2,....,an)
    # f_min - minimum funkce
    # alfa - vektor kodovaný v grayove kodu
    def run(self, tmax, width, params_of_fn):
        print("Slepý algoritmus")
        f_min = math.inf
        alfa_min = ''
        center = (2 ** width) / 20
        array_of_points = []
        for i in range(tmax):
            alfa = self.random_seq(width * params_of_fn)
            alfa_splited = re.findall('.' * width, alfa)
            alfa_decimal = []
            for j in range(params_of_fn):
                alfa_decimal.append((Koder.gray_do_dec(alfa_splited[j]) / 10) - center)
            fun = self.function(*alfa_decimal)
            array_of_points.append([fun,*alfa_decimal,False])
            if(fun < f_min):
                f_min = fun
                alfa_min = alfa
                print(f'počet: {i}')
                print(f'f({alfa_decimal})')
                print('výsledek funkce:',f_min)
                array_of_points[i][3] = True

        return array_of_points

    def random_seq(self,kn):
        new_alfa = []
        for i in range(kn):
            new_alfa.append(str(random.randint(0, 1)))
        return ''.join(new_alfa)






