import random


def main(level):
    oper = ["+", "-", "*", "/"]
    rndoper = random.choice(oper)

    def sum(x,y):
        res=x+y
        return res
    def mult(x,y):
        res=x*y
        return res
    def sub(x,y):
        """Не понимаю как сделать так,
         чтобы был неотрицательный результат"""
    def div(x,y):
        res=x/y
        return res
    if level == "1":
        if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
            x, y = random.randint(1, 50), random.randint(1, 50)
        else:  # объявляю x и y, если будут действия умножения или деления
            x, y = random.randint(1, 10), random.randint(1, 10)

        if rndoper == "+":
            return sum(x,y)
        elif rndoper == "-":
            return sub(x,y)
        elif rndoper == "*":
            return mult(x,y)
        elif rndoper == "/":
            return div(x,y)

    elif level == "2":
        if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
            x, y = random.randint(1, 100), random.randint(1, 100)
        else:  # объявляю x и y, если будут действия умножения или деления
            x, y = random.randint(1, 30), random.randint(1, 30)

        if rndoper == "+":
            return sum(x, y)
        elif rndoper == "-":
            return sub(x,y)
        elif rndoper == "*":
            return mult(x,y)
        elif rndoper == "/":
            return div(x,y)

    elif level == "3":
        if rndoper in '+-':  # объявляю x и y, если будут действия вычитания или сложения
            x, y = random.randint(1, 100), random.randint(1, 100)
        else:  # объявляю x и y, если будут действия умножения или деления
            x, y = random.randint(1, 50), random.randint(1, 50)

        if rndoper == "+":
            return sum(x,y)
        elif rndoper == "-":
            return sub(x,y)
        elif rndoper == "*":
            return mult(x,y)
        elif rndoper == "/":
            return div(x,y)
