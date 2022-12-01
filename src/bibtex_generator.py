import json
#from references import reference_types


#reftypes = json.loads(reference_types)

class BibtexGenerator():

    '''
    Create bibtex string from a reference object
    '''

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
        return "@book{CitekeyBook," + f"author=\"{self.reference.author}\",title=\"{self.reference.title}\",publisher=\"{self.reference.publisher}\",address=\"{self.reference.address}\",year=\"{self.reference.year}\"" + "}"
