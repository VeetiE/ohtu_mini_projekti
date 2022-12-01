
#from references import reference_types


#reftypes = json.loads(reference_types)

class BibtexGenerator():

    '''
    Create bibtex string from a reference object
    '''

    def __init__(self, reference_dict):
        self.reference_dict = reference_dict

#    def _extract_attributes(self, type):
#        return [i for i in reftypes(type)]

#    def _string_generator(self, type, attr):
#        output = ""
#        longest = 0
#        for i in attr:
#            if len(i) > longest:
#                longest = len(i)
#
#        for i in attr:
#            output.join(f"  {i:longest}")

    def make_bibtex_list(self):
        bibtex_list = []
        for reference in self.reference_dict:
            string = "@book{"
            string += f"{reference},"
            string += f"author=\"{self.reference_dict[reference].author}\","
            string += f"title=\"{self.reference_dict[reference].title}\","
            string += f"publisher=\"{self.reference_dict[reference].publisher}\","
            string += f"address=\"{self.reference_dict[reference].address}\","
            string += f"year=\"{self.reference_dict[reference].year}\""
            string += "}"
            bibtex_list.append(string)
        return bibtex_list
