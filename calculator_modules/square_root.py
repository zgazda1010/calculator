import math


def square_root(expression):
    try:
        total = str(math.sqrt(eval(expression)))
        expression = total
        return expression
    except ValueError:
        return " error "
