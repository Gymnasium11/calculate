import random
def main(level):
    if level=="1":
        oper=["+","-","*","/"]
        rndoper=random.choice(oper)
        if rndoper=="+":
            def sum(x,y):
                x=random.randint(1,50)
                y=random.randint(1,50)
                res=x+y
                return res
        if rndoper=="-":
            def sub(x,y):
                """Вычитание, не могу понять как сделать так,
                уменьшаемое было всегда больше вычитаемого"""
                pass
        if rndoper=="*":
            def mult(x,y):
                x=random.randint(1,15)
                y=random.randint(1,15)
                multres=x*y
                return multres

        if rndoper=="/":
            """То же самое, как с вычитанием"""
            pass
    elif level=="2":
        oper = ["+", "-", "*", "/"]
        rndoper = random.choice(oper)
        if rndoper == "+":
            def sum(x, y):
                x = random.randint(1, 100)
                y = random.randint(1, 100)
                res = x + y
                return res
        if rndoper == "-":
            def sub(x, y):
                x = random.randint(1,100)
                y = random.randint(1,100)
                subres = x-y
                return subres
        if rndoper == "*":
            def mult(x, y):
                x = random.randint(1, 30)
                y = random.randint(1, 30)
                multres = x * y
                return multres

        if rndoper == "/":
            def div(x,y):
                """Здесь наверное нужно сделать так,
                 чтобы делилось без остатка"""
                pass
        elif level=="3":
            oper = ["+", "-", "*", "/"]
            rndoper = random.choice(oper)
            if rndoper == "+":
                def sum(x, y):
                    x = random.randint(1, 150)
                    y = random.randint(1, 150)
                    res = x + y
                    return res
            if rndoper == "-":
                def sub(x, y):
                    x = random.randint(1, 100)
                    y = random.randint(1, 100)
                    subres = x - y
                    return subres
            if rndoper == "*":
                def mult(x, y):
                    x = random.randint(1, 50)
                    y = random.randint(1, 50)
                    multres = x * y
                    return multres

            if rndoper == "/":
                def div(x,y):
                    x=random.randint(1,100)
                    y=random.randint(1,100)
                    divres=float(x/y)
                    return divres