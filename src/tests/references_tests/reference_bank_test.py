import unittest
from references.book import Book
from references.reference_bank import ReferenceBank

class TestReferenceBank(unittest.TestCase):
    def setUp(self):
        self.ref = ReferenceBank()

    def test_generate_referenceString_correct(self):
        kirja = Book("Kirja","Borna","Sopranos", "publisher", "adress", 2020)
        ans = self.ref.generate_referenceString(kirja)

        self.assertEqual('borna2020',ans)


    def test_generate_referenceString_uncapitalized(self):
        kirja = Book("Kirja","Joe Biden","Sopranos","publisher", "adress",2020)
        ans = self.ref.generate_referenceString(kirja)
        
        self.assertEqual('joebi2020',ans)

    def test_generate_referenceString_no_spaces(self):
        kirja = Book("Kirja","Joe Biden","Sopranos","publisher", "adress",2020)
        ans = self.ref.generate_referenceString(kirja)
        
        self.assertEqual('joebi2020',ans)
    

    def test_get_correct_dictionary(self):

        kirja = Book("Kirja","MATTI","Breaking Bad", "publisher", "adress",2001)
        kirja2 = Book("Kirja","Matti","Bad", "publisher", "adress",2001)
        kirja3 = Book("Kirja","Matti2","Breaking Bad", "publisher", "adress",2001)

        self.ref.add_reference(kirja)
        self.ref.add_reference(kirja2)
        self.ref.add_reference(kirja3)

        ans = self.ref.get_reference_bank()

        self.assertEqual(ans['matti2001'],kirja)
        self.assertEqual(ans['matti2001(0)'],kirja2)
        self.assertEqual(ans['matti2001(1)'],kirja3)
        
            