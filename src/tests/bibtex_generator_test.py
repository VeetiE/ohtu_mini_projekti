import unittest
from bibtex_generator import BibtexGenerator
from references.book import Book


class TestBibtexGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_book = Book("book", "Kaapo Kivioja", "Cooking with Kaapo", "University of Helsinki", "Helsinki, Finland", 2015)

    def test_bibtex_generator(self):
        generator = BibtexGenerator(self.test_book)
        bibtex = generator.make_bibtex()

        self.assertAlmostEqual(bibtex, "@book{CitekeyBook,author=\"Kaapo Kivioja\",title=\"Cooking with Kaapo\",publisher=\"University of Helsinki\",address=\"Helsinki, Finland\",year=\"2015\"}")
