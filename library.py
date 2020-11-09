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


# def main(level):
#     oper = ["+", "-", "*", "/"]
#     rndoper = random.choice(oper)
#     if level == "1":
#         if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
#             x, y = random.randint(1, 50), random.randint(1, 50)
#         else:  # объявляю x и y, если будут действия умножения или деления
#             x, y = random.randint(1, 10), random.randint(1, 10)
#
#         if rndoper == "+":
#             return sum(x, y)
#         elif rndoper == "-":
#             return sub(x, y)
#         elif rndoper == "*":
#             return mult(x, y)
#         elif rndoper == "/":
#             return div(x, y)
#
#     elif level == "2":
#         if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
#             x, y = random.randint(50, 1000), random.randint(50, 100)
#         else:  # объявляю x и y, если будут действия умножения или деления
#             x, y = random.randint(10, 40), random.randint(10, 40)
#
#         if rndoper == "+":
#             return sum(x, y)
#         elif rndoper == "-":
#             return sub(x, y)
#         elif rndoper == "*":
#             return mult(x, y)
#         elif rndoper == "/":
#             return div(x, y)
#
#     elif level == "3":
#         if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
#             x, y = random.randint(1000, 10000), random.randint(1000, 10000)
#         else:  # объявляю x и y, если будут действия умножения или деления
#             x, y = random.randint(40, 50), random.randint(40, 50)
#
#         if rndoper == "+":
#             return sum(x, y)
#         elif rndoper == "-":
#             return sub(x, y)
#         elif rndoper == "*":
#             return mult(x, y)
#         elif rndoper == "/":
#             return div(x, y)

