import json
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
        for r in self.reference_dict:
            s = "@book{"
            s += f"{r},"
            s += f"author=\"{self.reference_dict[r].author}\","
            s += f"title=\"{self.reference_dict[r].title}\","
            s += f"publisher=\"{self.reference_dict[r].publisher}\","
            s += f"address=\"{self.reference_dict[r].address}\","
            s += f"year=\"{self.reference_dict[r].year}\""
            s += "}"
            bibtex_list.append(s)
        return bibtex_list
