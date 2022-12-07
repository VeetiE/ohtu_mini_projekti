import unittest
from json_saver import save_dictionary_to_json
import json


class TestJsonSaver(unittest.TestCase):

    def test_dictionary_with_one_element_saves_correctly(self):
        test_dictionary = {
            "Key1": ["value1", "value2"]
        }

        save_dictionary_to_json(test_dictionary, "unittest.json")

        with open("unittest.json", encoding="utf-8") as open_file:
            saved_dictionary = json.load(open_file)

            open_file.close()
        
        self.assertDictEqual(saved_dictionary, test_dictionary)
    
    def test_dictionary_with_many_elements_saves_correctly(self):
        test_dictionary = {
            "Key1": ["value1", "value2"],
            "Key2": ["value1", "value2"],
            "Key3": ["value1", "value2"],
        }

        save_dictionary_to_json(test_dictionary, "unittest.json")

        with open("unittest.json", encoding="utf-8") as open_file:
            saved_dictionary = json.load(open_file)

            open_file.close()
        
        self.assertDictEqual(saved_dictionary, test_dictionary)


