def square(expression):
    try:
        total = str(eval(expression) ** 2)
        expression = total
        return expression
    except ValueError:
        return " error "
