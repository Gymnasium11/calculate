import random


def create_x_y_plus(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
    elif level == 3:
        x = random.randint(0, 999)
        y = random.randint(0, 999)
    return x, y


def create_x_y_mult(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(0, 20)
        y = random.randint(0, 10)
    elif level == 3:
        x = random.randint(0, 40)
        y = random.randint(0, 20)
    return x, y
list=[" + "," - "," * "," / "]
oper=random.choice(list)

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



