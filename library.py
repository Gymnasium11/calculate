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


#функции для кнопок
def start(*args):
    global point, count
    point = count = 0


def new(*args):
    x1.set(rnd(0,50))
    x2.set(rnd(0,50))
    result.set(" ")
    status.set('')
    equil['state'] = 'instate'
    equil.delete(0, 'end')
    equil.focus()


def calc(*args):
    global point, count
    user = int(answer.get())
    summa = int(x1.get())+int(x2.get())
    if user == summa:
        result.set('Отлично')
        point += 1
    else:
        result.set('Плохо')
    count += 1
    equil['state'] = 'readonly'


def stop(*args):
    global point, count
    status.set('Верных ответов: '+str(point)+' Неверных ответов: '+str(count-point))
    point = 0
    count = 0
    result.set("Ваш результат)")
    equil['state'] = 'instate'
    x1.set(0)
    x2.set(0)
    answer.set(0)
