import unittest
from bibtex_generator import BibtexGenerator
from references.reference_bank import ReferenceBank


class TestBibtexGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_library = ReferenceBank()
        self.book = {
            "reference_type": "book",
            "title": "Sopranos",
            "author": "Joe Biden",
            "publisher": "University of Helsinki",
            "address": "Helsinki, Finland",
            "year": 2001
            }
        self.test_library.add_reference(self.book)

    def test_bibtex_generator(self):
        generator = BibtexGenerator(self.test_library.get_reference_bank())
        bibtex = generator.make_bibtex_list()
        print(bibtex)

        self.assertEqual(
            bibtex[0], "@book{joebi2001,reference_type=\"book\",title=\"Sopranos\",author=\"Joe Biden\",publisher=\"University of Helsinki\",address=\"Helsinki, Finland\",year=\"2001\",}")
