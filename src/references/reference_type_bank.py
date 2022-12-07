

class ReferenceTypeBank:
    def __init__(self):
        #saves key=reference type, value = list of reference input fields, pairs
        self.reference_types = {
               'book':["author","title","publisher","address","published"],
               'article':["author","title","journal","year"],
               'booklet':["title"],
               'conference':["author","title","journal","year"],
               'inbook':["author","title","chapter","publisher","published"],
               'incollection':["author","title","booktitle","publisher","published"],
               'inproceedings':["author","title","booktitle","published"],
               'manual':["title"],
               'mastersthesis':["author","title","school","published"],
               'misc':[],
               'phdhesis':["author","title","school","published"],
               'proceedings':["title","published"],
               'techreport':["author","title","institution","published"],
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
        if reference_type_name not in self.reference_types:
            self.reference_types[reference_type_name] = list(reference_type_fields)
        




    