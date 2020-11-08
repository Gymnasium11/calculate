import random
import eel
from lib import *


first_number, sign, second_number, result = 3, '+', 1, 4

def main(level):
    oper = ["+", "-", "*", "/"]
    rndoper = random.choice(oper)
    dic = {'1': {'-': (1, 50), '+': (1, 50), '*': (1, 10), '/': (1, 10)},
           '2': {'-': (50, 1000), '+': (50, 1000), '*': (10, 40), '/': (10, 40)},
           '3': {'-': (50, 1000), '+': (1000, 10000), '*': (40, 60), '/': (40, 60)}}
    x, y = dic[level][rndoper]
    x, y = random.randint(x, y), random.randint(x, y)
    d = {'+': sum(x, y), '-': sub(x, y), '*': mult(x, y), '/': div(x, y)}
    return d[rndoper]

@eel.expose
def get_level(level):
    global first_number, sign, second_number, result
    first_number, sign, second_number, result = main(level)


@eel.expose
def get_first_el():
    global first_number
    return first_number


@eel.expose
def get_znak():
    global sign
    return sign


@eel.expose
def get_second_el():
    global second
    return second_number


@eel.expose
def comp(res):
    global result
    if res == '':
        return False
    return int(res) == result


eel.init('web')
eel.start("main.html", size=(700, 400))
