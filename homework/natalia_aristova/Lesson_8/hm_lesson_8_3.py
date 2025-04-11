fibo_n_1 = 1
fibo_n_2 = 0
fibo = 0
for i in range(0, 10):
    fibo = fibo_n_1 + fibo_n_2
    fibo_n_2 = fibo_n_1
    fibo_n_1 = fibo
    print(fibo)