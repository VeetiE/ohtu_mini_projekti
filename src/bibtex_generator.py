import json
#from references import reference_types


#reftypes = json.loads(reference_types)

class BibtexGenerator():
    def __init__(self, reference):
        self.reference = reference

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


    def make_bibtex(self):
        return "@book{CitekeyBook,\n" + f"  author = \"{self.reference.author}\",\n" + f"  title = \"{self.reference.title}\",\n" + f"  publisher = \"{self.reference.publisher}\",\n" + f"  address = \"{self.reference.address}\",\n" + f"  year = \"{self.reference.year}\"" + "}"
