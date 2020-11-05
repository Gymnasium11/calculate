import random


def main(level):
    oper = ["+", "-", "*", "/"]
    rndoper = random.choice(oper)

    # def sum(x,y):
    # def mult(x,y):
    # def sub(x,y):
    # def div(x,y):

    if level == "1":
        if rndoper in '+-':  # объявляю x и y если будут действия бычитания или сложения
            x, y = random.randint(1, 50), random.randint(1, 50)
        else:  # объявляю x и y если будут действия умножения или деления
            x, y = random.randint(1, 10), random.randint(1, 10)

        if rndoper == "+":
            pass
        elif rndoper == "-":
            pass
        elif rndoper == "*":
            pass
        elif rndoper == "/":
            """То же самое, как с вычитанием"""
            pass

    elif level == "2":
        if rndoper in '+-':  # объявляю x и y если будут действия бычитания или сложения
            x, y = random.randint(1, 100), random.randint(1, 100)
        else:  # объявляю x и y если будут действия умножения или деления
            x, y = random.randint(1, 30), random.randint(1, 30)

        if rndoper == "+":
            pass
        elif rndoper == "-":
            pass
        elif rndoper == "*":
            pass
        elif rndoper == "/":
            pass

    elif level == "3":
        if rndoper in '+-':  # объявляю x и y если будут действия бычитания или сложения
            x, y = random.randint(1, 100), random.randint(1, 100)
        else:  # объявляю x и y если будут действия умножения или деления
            x, y = random.randint(1, 50), random.randint(1, 50)

        if rndoper == "+":
            pass
        elif rndoper == "-":
            pass
        elif rndoper == "*":
            pass
        elif rndoper == "/":
            pass
