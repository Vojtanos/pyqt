#převodníky
from sympy.combinatorics.graycode import gray_to_bin
from sympy.combinatorics.graycode import bin_to_gray

import math
import random
#regex
import re

import collections
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


class TabuAlg:

    def __init__(self, function, params_of_fn):
        self.function = function
        self.params_of_fn = params_of_fn
        self.best_i = 0
        self.array_of_points = []
        self.center = 0

    # tmax - počet iterací
    # width - délka jednoho grayova čísla
    # params_of_fn - počet grayových čísel -> alfa = (a1,a2,....,an)
    # c0 - počet vygenerovaných potomků
    # f_min - minimum funkce
    # alfa - vektor kodovaný v grayove kodu
    def run(self, tmax, width, max_tabu):
        tabu_list = collections.deque(maxlen=int(max_tabu))
        alfa_min = '1' * width * self.params_of_fn
        alfa_decimal_array = self.get_alfa_decimal_array(width, alfa_min)
        f_min = self.function(*alfa_decimal_array)
        self.center = (2 ** width) / 20
        for i in range(tmax):
            alfa = self.choose_best_transformation(alfa_min, width, tabu_list,f_min)
            alfa_decimal_array = self.get_alfa_decimal_array(width,alfa)
            fun = self.function(*alfa_decimal_array)
            if(fun < f_min):
                f_min = fun
                alfa_min = alfa
                tabu_list.append(self.best_i)
                print(f'počet: {i}')
                print(f'f({alfa_decimal_array})')
                print('výsledek funkce:',f_min)
                print(tabu_list)

        return self.array_of_points

    # vrací alfu jako pole parametrů funkce v desítkové soustavě
    def get_alfa_decimal_array(self,width,alfa):
        alfa_splited = re.findall('.' * width, alfa)
        alfa_decimal = []
        for j in range(self.params_of_fn):
            alfa_decimal.append((Koder.gray_do_dec(alfa_splited[j]) / 10) - self.center) # můžu ovlivnit desetiná čísla
        return alfa_decimal

    def choose_best_transformation(self, alfa, width, tabu_list, f_min):
        best_i = 0
        best = alfa
        best_alfa_decimal = self.get_alfa_decimal_array(width, best)
        fun_min = f_min
        self.array_of_points.append([fun_min, *best_alfa_decimal, 0])
        for i in range(len(alfa)):
            new_alfa = self.change_in_index(alfa, i)
            alfa_decimal_array = self.get_alfa_decimal_array(width, new_alfa)
            fun = self.function(*alfa_decimal_array)
            if i not in tabu_list:
                self.array_of_points.append([fun, *alfa_decimal_array, 1])
                if fun < fun_min:
                    best = new_alfa
                    fun_min = fun
                    best_i = i
            else:
                self.array_of_points.append([fun, *alfa_decimal_array, 2])

        self.best_i = best_i
        return best

    def change_in_index(self, alfa, i):
        list_alfa = list(alfa)
        list_alfa[i] =  '0' if list_alfa[i] else '1'
        new_alfa = "".join(list_alfa)
        return new_alfa