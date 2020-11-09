from random import randint as rnd


def create_x_y_plus(level):
    if level == 1:
        x = rnd(0, 9)
        y = rnd(0, 9)
    elif level == 2:
        x = rnd(0, 99)
        y = rnd(0, 99)
    elif level == 3:
        x = rnd(0, 999)
        y = rnd(0, 999)
    return x, y


def create_x_y_mult(level):
    if level == 1:
        x = rnd(0, 9)
        y = rnd(0, 9)
    elif level == 2:
        x = rnd(0, 20)
        y = rnd(0, 10)
    elif level == 3:
        x = rnd(0, 40)
        y = rnd(0, 20)
    return x, y

#Функции для кнопок
def plus(x, y):
    res = x + y
    return res


def multiply(x, y):
    res = x * y
    return res


def minus(y, res):
    x = y + res
    return res


def div(y, res):
    x = y * res
    return res
