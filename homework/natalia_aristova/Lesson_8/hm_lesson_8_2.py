import sys

def progression(limit=100):
    count = 0
    fibo_n_1 = 1
    fibo_n_2 = 0
    fibo = 0
    while count < limit:
        yield fibo
        fibo = fibo_n_1 + fibo_n_2
        fibo_n_2 = fibo_n_1
        fibo_n_1 = fibo
        count += 1

sys.set_int_max_str_digits(100000)
count2 = 0
for number in progression(100000):
    if count2 == 3:  #это 5-ое число, т.к. вычисление начинается с 3-го числа и до 5-го числа нам надо сделать 3 шага
        print(f'Пятое число {number}')
    elif count2 == 198:
        print(f'Двухсотое число {number}')
    elif count2 == 998:
        print(f'Тысячное число {number}')
    elif count2 == 99998:
        print(f'Стотысячное число {number}')
        break
    count2 +=1

