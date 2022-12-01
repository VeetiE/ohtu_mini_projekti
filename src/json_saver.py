import json
from json import JSONEncoder


class Converter(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def save_array_to_json(in_list):
    json_books_list = []
    for book in in_list:
        json_books_list.append(book.__dict__)

    json_obj = json.dumps(json_books_list, indent=4)

    with open("testi.json", "w", encoding="utf-8") as file:
        file.write(json_obj)
        file.close()

    with open("testi.json", "r", encoding="utf-8") as openFile:
        data = json.load(openFile)
        openFile.close()
    print(data)


def save_dictionary_to_json(dictionary):
    json_obj = json.dumps(dictionary, indent=4, cls=Converter)

    with open("testi.json", "w", encoding="utf-8") as file:
        file.write(json_obj)
        file.close()

    with open("testi.json", "r", encoding="utf-8") as openFile:
        data = json.load(openFile)
        openFile.close()
    print(data)
