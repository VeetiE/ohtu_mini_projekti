
class BibtexGenerator():

    '''
    Create a list of bibtex strings from a list of reference objects
    '''

    def __init__(self, reference_dict):
        self.reference_dict = reference_dict

    def make_bibtex_list(self):
        bibtex_list = []
        for reference in self.reference_dict:
            current = self.reference_dict[reference]
            reference_type = current["reference_type"]
            string = f"@{reference_type}"
            string += "{"
            string += f"{reference},"

            for key in current.keys():
                string += f"{key}=\"{current[key]}\","

            string += "}"
            bibtex_list.append(string)
        print(bibtex_list)
        return bibtex_list
