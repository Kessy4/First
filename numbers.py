from random import randint

a = randint(0, 101)

while True:
    b = input('Угадай число или набери "Выход": ')
    if b == 'Выход':
        print("Выход из программы!")
        break
    b = int(b)
    if b > 100:
        print('От 1 до 100!')
    elif b == a:
        print("Угадал!")
    elif b < a:
        print('Мало!')
    elif b > a:
        print('Много!')
