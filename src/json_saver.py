import json
from json import JSONEncoder


class Converter(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def save_dictionary_to_json(dictionary):
    json_obj = json.dumps(dictionary, indent=4, cls=Converter)

    with open("testi.json", "w", encoding="utf-8") as file:
        file.write(json_obj)
        file.close()

    with open("testi.json", "r", encoding="utf-8") as openFile:
        data = json.load(openFile)
        openFile.close()
    print(data)
