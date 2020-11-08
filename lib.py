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


