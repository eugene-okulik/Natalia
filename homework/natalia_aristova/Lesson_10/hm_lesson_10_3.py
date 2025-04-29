def my_dec(func):

    def wrapper(a, b):
        if a == b:
            func(a, b, '+')
        elif a > b:
            func(a, b, '-')
        elif a < 0 or b < 0:
            func(a, b, '*')
        else:
            func(a, b, '/')
    return wrapper


@my_dec
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return first / second


a = int(input('Type the first digit '))
b = int(input('Type the second digit '))
calc(a, b)
