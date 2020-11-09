import eel
from main import main

n=0

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