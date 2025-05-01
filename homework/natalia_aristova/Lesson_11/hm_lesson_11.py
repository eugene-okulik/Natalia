
class Book:
    page_material = 'paper'
    text = True


    def __init__(self, title, author, number_of_pages, isbn, reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved


    def info(self):
        if self.reserved == True:
            print(f' Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' материал: {self.page_material}, зарезервирована' )
        else:
            print(f' Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' материал: {self.page_material}')


book_1 = Book('Idiot', 'Dostoevsky', 500, 123, False)
book_2 = Book('War and Peace', 'Tolstoy', 5000, 1234, False)
book_3 = Book('Fathers and sons', 'Turgenev', 333, 1236, False)
book_4 = Book('The Master and Margarita', 'Bulgakov', 872, 5123, False)
book_5 = Book('Brothers Karamazov', 'Dostoevsky', 999, 9123, False)

book_1.reserved = True

book_1.info()
book_2.info()
book_3.info()
book_4.info()
book_5.info()


class Schoolbook(Book):


    def __init__(self, title, author, number_of_pages, isbn, reserved, subject, grade, tasks ):
        super().__init__(title, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.tasks = tasks


    def info1(self):
        if self.reserved == True:
            print(f' Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' предмет: {self.subject}, класс: {self.grade},  зарезервирована' )
        else:
            print(f' Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},'
                  f' предмет: {self.subject}, класс: {self.grade}')


schoolbook1 = Schoolbook('Algebra', 'Vilenkin', 500, 666, False, 'Maths',
                         4, False)
schoolbook2 = Schoolbook('History', 'Ivanov', 466, 6661, False, 'History',
                         5, True)
schoolbook3 = Schoolbook('English', 'Smith', 426, 6662, False, 'English',
                         5, True)
schoolbook4 = Schoolbook('Russian', 'Petrov', 421, 66692, False,
                         'Russian',5, True)

schoolbook1.reserved = True

schoolbook1.info1()
schoolbook2.info1()
schoolbook3.info1()
schoolbook4.info1()
