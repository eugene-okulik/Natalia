class Flower:
    def __init__(self, name, freshness, color, stem_length, price, life):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length    # длина стебля
        self.price = price
        self.life = life    # время жизни цветка

    def __str__(self):
            return (f' Flower name = {self.name}, freshmess = {self.freshness} days, color = {self.color},'
                    f' stem length = {self.stem_length}, price = {self.price} euro, life = {self.life} days')

    def __repr__(self):
            return (f' Flower name = {self.name}, freshmess = {self.freshness} days, color = {self.color},'
                    f' stem length = {self.stem_length}, price = {self.price} euro, life = {self.life} days')


class Tulip(Flower):

    def __init__(self, name, freshness, color, stem_length, price, life, country_of_origin):
        super().__init__(name, freshness, color, stem_length, price,  life)
        self.country_of_origin = country_of_origin


class Rose(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life, thorn ):
        super().__init__(name, freshness, color, stem_length, price, life)
        self.thorn = thorn


class Forget_me_not(Flower):
    def __init__(self, name, freshness, color, stem_length, price, life, wild_flowers ):
        super().__init__(name, freshness, color, stem_length, price, life)
        self.wild_flowers = wild_flowers


tulip = Tulip ('Tulip', 2, 'red', 7, 8, 5, 'Holland')
rose = Rose('Rose', 1, 'white', 15, 10, 6, True)
forget_me_not = Forget_me_not('Forget-me-not', 1, 'purple', 6, 15, 2,
                              'True')


class  Buket:
    def __init__(self, flowers):
        self.flowers = flowers

    def average_life(self):
        return round(sum(i.life for i in self.flowers) / len(self.flowers), 2)

    def sort_by(self, attribute):                                 # начиная отсюда  совсем не понимаю( взято из gpt
        self.flowers.sort(key=lambda f: getattr(f, attribute))

    def find_by_lifes(self, min_days):                           # взято из gpt, но я это понимаю
        return [f for f in self.flowers if f.life >= min_days]


    print(tulip)
    print(rose)
    print(forget_me_not)

bouquet = Buket([tulip, rose, forget_me_not])
print(bouquet.sort_by('freshness'))
print(bouquet.find_by_lifes(1))
print(bouquet.average_life())



