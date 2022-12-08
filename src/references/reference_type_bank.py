

class ReferenceTypeBank:
    def __init__(self):
        #saves key=reference type, value = list of reference input fields, pairs
        self.reference_types = {
               'book':["author","title","publisher","address","year"],
               'article':["author","title","journal","year"],
               'booklet':["title"],
               'conference':["author","title","journal","year"],
               'inbook':["author","title","chapter","publisher","year"],
               'incollection':["author","title","booktitle","publisher","year"],
               'inproceedings':["author","title","booktitle","year"],
               'manual':["title"],
               'mastersthesis':["author","title","school","year"],
               'phdhesis':["author","title","school","year"],
               'proceedings':["title","year"],
               'techreport':["author","title","institution","year"],
               'unpublished':["author","title"]
               }
        self.all_possible_types = [
            "address", "author", "booktitle", "chapter",
            "crossref", "edition", "editor", "howpublished",
            "institution", "journal", "key", "month",
            "note", "number", "organization", "pages",
            "publisher", "school", "series", "title",
            "type", "volume", "year"
            ]
    def add_new_reference_type(self, reference_type_name:str, reference_type_fields):
        print(reference_type_name)
        print(reference_type_fields)
        if len(reference_type_name) == 0 or len(reference_type_fields) == 0:
            print("INVALID")
            return False


        if reference_type_name not in self.reference_types:
            self.reference_types[reference_type_name] = list(reference_type_fields)
            print(self.reference_types)
            return True
        
        
        return False
