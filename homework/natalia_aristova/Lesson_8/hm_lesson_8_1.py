import random

salary = int(input('Wht salary do ypu have? '))
bonus = random.choice([True, False])
if bonus is True:
    new_salary = salary + random.randint(1, 1000000)
else:
    new_salary = salary
print(f'{salary}, {bonus} -"${new_salary}"')
