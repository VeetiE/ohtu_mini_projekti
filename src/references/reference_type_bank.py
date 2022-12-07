

class ReferenceTypeBank:
    def __init__(self):
        #saves key=reference type, value = list of reference input fields, pairs
        self.reference_types = {}
    
    def add_new_reference_type(self, reference_type_name:str, reference_type_fields: list(str)):
        if reference_type_name not in self.reference_types:
            self.reference_types[reference_type_name] = list(reference_type_fields)
        




    