from references.book import Book
from json_saver import  save_dictionary_to_json


class ReferenceBank:
    '''
    Save references
    '''

    def __init__(self):
        self.reference_bank = {}
        self.running_number = 0

    def add_reference(self, book: Book):

        ref_string = self.generate_reference_string(book)
        self.reference_bank[ref_string] = book
        save_dictionary_to_json(self.reference_bank)

    def generate_reference_string(self, book: Book):

        name = book.author.replace(" ", "")
        published = book.year

        first_five_letters = name[0:5].lower()
        generated = first_five_letters+str(published)

        if generated in self.reference_bank.keys():
            generated += f"({self.running_number})"
            self.running_number += 1

        return generated

    def get_reference_bank(self):
        return self.reference_bank
