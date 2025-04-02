my_dict = {}
my_dict['tuple'] = (1, 5, 6, 7, 8)
my_dict['list'] = [1, 2, 3, 4, 5]
my_dict['dict'] = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
my_dict['set'] = {1, 3, 4, 5, 6}
print(my_dict['tuple'][-1])
my_dict['list'].append(10)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'it is false'
del my_dict['dict'][5]
my_dict['set'].add(101)
my_dict['set'].discard(3)
print(my_dict)
