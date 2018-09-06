a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = float(input('Введите третье число: '))


def func(a, b, c):
    return a+b+c
print('Сумма введенных чисел: ', round(func(a, b, c)))


def funce(a, b, c):
    return a*b*c
print('Произведение введенных чисел: ', round(funce(a, b, c)))