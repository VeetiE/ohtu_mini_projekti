
class Book:

    '''
    Create a book object
    '''

    def __init__(self,type,author,title,year):
        self.type = type
        self.author = author
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.type}, {self.author}, {self.title}, {self.year}"