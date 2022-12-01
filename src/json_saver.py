import json
from json import JSONEncoder


class converter(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def save_array_to_json(list):
    jsonBooksList = []
    for book in list:
        jsonBooksList.append(book.__dict__)

    json_obj = json.dumps(jsonBooksList, indent=4)

    with open("testi.json", "w") as file:
        file.write(json_obj)
        file.close()

    with open("testi.json", "r") as openFile:
        data = json.load(openFile)
        openFile.close()
    print(data)


def save_dictionary_to_json(dictionary):
    json_obj = json.dumps(dictionary, indent=4, cls=converter)

    with open("testi.json", "w") as file:
        file.write(json_obj)
        file.close()

    with open("testi.json", "r") as openFile:
        data = json.load(openFile)
        openFile.close()
    print(data)
