PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list = PRICE_LIST.split()
items = [x for x in list if int(list.index(x)) % 2 ==0]
prices = [int(x[:-1]) for x in list if int(list.index(x)) % 2 != 0]
my_dict = dict(zip(items, prices))
print(my_dict)
