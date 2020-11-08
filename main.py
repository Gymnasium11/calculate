import random
import eel


def sum(x, y):
    res = x + y
    return (x, "+", y, res)


def mult(x, y):
    res = x * y
    return (x, "*", y, res)


def sub(y, res):
    x = y + res
    return (x, "-", y, res)


def div(y, res):
    x = y * res
    return (x, "/", y, res)



def main(level):
    oper = ["+", "-", "*", "/"]
    rndoper = random.choice(oper)
    if level == "1":
        if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
            x, y = random.randint(1, 50), random.randint(1, 50)
        else:  # объявляю x и y, если будут действия умножения или деления
            x, y = random.randint(1, 10), random.randint(1, 10)

        if rndoper == "+":
            return sum(x, y)
        elif rndoper == "-":
            return sub(x, y)
        elif rndoper == "*":
            return mult(x, y)
        elif rndoper == "/":
            return div(x, y)

    elif level == "2":
        if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
            x, y = random.randint(50, 1000), random.randint(50, 100)
        else:  # объявляю x и y, если будут действия умножения или деления
            x, y = random.randint(10, 40), random.randint(10, 40)

        if rndoper == "+":
            return sum(x, y)
        elif rndoper == "-":
            return sub(x, y)
        elif rndoper == "*":
            return mult(x, y)
        elif rndoper == "/":
            return div(x, y)

    elif level == "3":
        if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
            x, y = random.randint(1000, 10000), random.randint(1000, 10000)
        else:  # объявляю x и y, если будут действия умножения или деления
            x, y = random.randint(40, 50), random.randint(40, 50)

        if rndoper == "+":
            return sum(x, y)
        elif rndoper == "-":
            return sub(x, y)
        elif rndoper == "*":
            return mult(x, y)
        elif rndoper == "/":
            return div(x, y)


a = 3
b = '+'
c = 1
d = 4

@eel.expose
def get_level(level):
    global a, b, c, d
    a, b, c, d = main(level)

@eel.expose
def get_first_el():
    global a
    return a

@eel.expose
def get_znak():
    global b
    return b

@eel.expose
def get_second_el():
    global c
    return c

@eel.expose
def get_result():
    global d
    return d


@eel.expose
def comp(b):
    global d
    if b=='':
        return False
    return int(b) == d



eel.init('web')
eel.start("main.html", size=(700, 400))
