import unittest
from references.reference_bank import ReferenceBank


class TestReferenceBank(unittest.TestCase):
    def setUp(self):
        self.ref = ReferenceBank()
        self.book = {
            "reference_type": "book",
            "title": "Sopranos",
            "author": "Joe Biden",
            "publisher": "University of Helsinki",
            "adress": "Helsinki, Finland",
            "year": 2001
            }

    def test_generate_reference_string_correct(self):
        ans = self.ref._generate_reference_string(self.book)

        self.assertEqual('joebi2001', ans)

    def test_get_correct_dictionary(self):
        self.ref.add_reference(self.book)
        self.ref.add_reference(self.book)
        self.ref.add_reference(self.book)

        ans = self.ref.get_reference_bank()

        self.assertEqual(ans['joebi2001'], self.book)
        self.assertEqual(ans['joebi2001(0)'], self.book)
        self.assertEqual(ans['joebi2001(1)'], self.book)

