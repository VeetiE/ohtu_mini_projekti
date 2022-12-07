import json
from json import JSONEncoder


class Converter(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def save_dictionary_to_json(dictionary, filename):
    json_obj = json.dumps(dictionary, indent=4, cls=Converter)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_obj)
        file.close()

    with open(filename, "r", encoding="utf-8") as openFile:
        data = json.load(openFile)
        openFile.close()
    print(data)
