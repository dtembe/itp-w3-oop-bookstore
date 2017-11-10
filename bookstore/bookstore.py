class Bookstore(object):

    def __init__(self, store_name):
        self.name = store_name
        self.book_list = []

        self.response = []

    def add_book(self, book):
        self.book_list.append(book)

    def get_books(self):
        return self.book_list

    def search_books(self, title='', author=''):

        answer = []

        if title != '':
            for book in self.book_list:
                if title.lower() in book.title.lower():
                    answer.append(book)

        elif author != '':
            for book in self.book_list:
                if book.author == author:
                    answer.append(book)

        return answer


class Author(object):

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.book_list = []

    def get_books(self):
        return self.book_list


class Book(object):

    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.book_list.append(self)
