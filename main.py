from threading import Timer
from time import sleep
import numpy as np

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def function1(MF, MH, MK):
    try:
        temp = np.dot(MH, MK)
        MG = (MF - temp)
        print('-' * 30)
        print('\nПолученная матрица MG\n')
        print(MG)
        print()
        print('-' * 30)
        print()
    except Exception:
        print('Ошибка полученных данных в первую функцию')
        quit()


def function2(B, C, MA, ME):
    try:
        temp = np.dot(MA, ME)
        temp1 = np.dot(B, C)
        MD = np.dot(temp1, temp)
        print('-' * 30)
        print('\nПолученная матрица MD\n')
        print(MD)
        print()
        print('-' * 30)
        print()
    except Exception:
        print('Ошибка полученных данных во вторую функцию')
        quit()


try:
    print('Starting')
    b = np.array(input('Задайте вектор B\n').split(), dtype=float)
    c = np.array(input('Задайте вектор C\n').split(), dtype=float)
    MF = []
    print('Задайте матрицу MF')
    for i in range(len(b)):
        temp = input().split()
        if len(temp) != len(b):
            print(f'Не верное количество значений, ваша текущая размерность ={len(b)}')
            quit()
        MF.append(temp)
    #  print(MF)
    MF = np.array(MF, dtype=float)

    MH = []
    print('Задайте матрицу MH')
    for i in range(len(b)):
        temp = input().split()
        if len(temp) != len(b):
            print(f'Не верное количество значений, ваша текущая размерность ={len(b)}')
            quit()
        MH.append(temp)
    MH = np.array(MH, dtype=float)

    MK = []
    print('Задайте матрицу MK')
    for i in range(len(b)):
        temp = input().split()
        if len(temp) != len(b):
            print(f'Не верное количество значений, ваша текущая размерность ={len(b)}')
            quit()
        MK.append(temp)

    MK = np.array(MK, dtype=float)

    MA = []
    print('Задайте матрицу MA')
    for i in range(len(b)):
        temp = input().split()
        if len(temp) != len(b):
            print(f'Не верное количество значений, ваша текущая размерность ={len(b)}')
            quit()
        MA.append(temp)

    MA = np.array(MA, dtype=float)

    ME = []
    print('Задайте матрицу ME')
    for i in range(len(b)):
        temp = input().split()
        if len(temp) != len(b):
            print(f'Не верное количество значений, ваша текущая размерность ={len(b)}')
            quit()
        ME.append(temp)

    ME = np.array(ME, dtype=float)
    print('\nВсе стартовые данные получены. Идет запуск потоков\n')

    rt1 = RepeatedTimer(3, function1, MF, MH, MK)
    rt2 = RepeatedTimer(5, function2, b, c, MA, ME)

except Exception:
    print('Ошибка стартовых данных')
    quit()