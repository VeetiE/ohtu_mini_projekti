import unittest
from references.reference_type_bank import ReferenceTypeBank
class TestReferenceTypeBank(unittest.TestCase):
    def setUp(self):
        self.reference_type_bank = ReferenceTypeBank()
    
    def test_add_new_reference_type_saves_reference_to_dictionary(self):
        new_reference_type_name = "newReferenceType"
        new_reference_type_fields = ["published", "author"]
        self.reference_type_bank.add_new_reference_type(new_reference_type_name, new_reference_type_fields)

        self.assertEqual(new_reference_type_name in self.reference_type_bank.reference_types, True)
        self.assertEqual(self.reference_type_bank.reference_types[new_reference_type_name], new_reference_type_fields)

