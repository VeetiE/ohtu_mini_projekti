from json_saver import  save_dictionary_to_json, read_dictionary_from_json


class ReferenceBank:
    '''
    Save references
    '''

    def __init__(self, references={},  file_to_save_to="testi.json"):
        #WARINING:: running number WILL BE broken if there are duplicated in references
        self.reference_bank = references
        self.running_number = 0
        self.file_to_save = file_to_save_to
    def _make_normal_dictionary(self, reference):
        #flask returns an "ImmutableMultiDict" (ew), this makes it a regular dict
        new_dict = {}
        for element in reference:
            new_dict[element] = reference[element]
        return new_dict

    def _generate_reference_string(self, reference):

        print(str(reference["year"]))
        if reference["author"]:
            name = reference["author"].replace(" ", "")
        elif reference["title"]:
            name = reference["title"].replace(" ", "")
        else:
            name = "misc"
        
        generated = name[0:5].lower()

        if reference["year"]:
            generated += str(reference["year"])

        if generated in self.reference_bank.keys():
            generated += f"({self.running_number})"
            self.running_number += 1

        return generated

    def add_reference(self, reference):
        reference = self._make_normal_dictionary(reference)
        ref_string = self._generate_reference_string(reference)
        self.reference_bank[ref_string] = reference
        save_dictionary_to_json(self.reference_bank, self.file_to_save)

    def get_reference_bank(self):
        return self.reference_bank
