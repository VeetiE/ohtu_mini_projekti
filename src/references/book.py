
class Book:

    '''
    Create a book object
    '''

    def __init__(self, type: str, author: str, title: str, publisher: str, address: str, year: int):
        self.type = type
        self.author = author
        self.title = title
        self.publisher = publisher
        self.address = address
        self.year = year

    def __str__(self):
        return f"{self.type}, {self.author}, {self.title}, {self.publisher}, {self.address}, {self.year}"
