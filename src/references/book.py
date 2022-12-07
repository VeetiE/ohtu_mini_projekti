
class Book:

    '''
    DON'T USE THIS
    '''

    def __init__(self, ref_type, author: str, title: str, publisher: str, address: str, year: int):
        self.ref_type = ref_type
        self.author = author
        self.title = title
        self.publisher = publisher
        self.address = address
        self.year = year

    def __str__(self):
        return f"{self.ref_type}, {self.author}, {self.title}, {self.publisher}, {self.address}, {self.year}"
