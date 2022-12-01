import unittest
from bibtex_generator import BibtexGenerator
from references.book import Book
from references.reference_bank import ReferenceBank


class TestBibtexGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_library = ReferenceBank()
        self.test_library.add_reference(Book("book", "Kaapo Kivioja", "Cooking with Kaapo", "University of Helsinki", "Helsinki, Finland", 2015))

    def test_bibtex_generator(self):
        generator = BibtexGenerator(self.test_library.reference_bank)
        bibtex = generator.make_bibtex_list()

        self.assertAlmostEqual(bibtex[0], "@book{kaapo2015,author=\"Kaapo Kivioja\",title=\"Cooking with Kaapo\",publisher=\"University of Helsinki\",address=\"Helsinki, Finland\",year=\"2015\"}")
