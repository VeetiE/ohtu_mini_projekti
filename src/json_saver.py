import json


class Converter(json.JSONEncoder):
    def default(self, o):
        return o.__dict__

def save_dictionary_to_json(dictionary, filename):
    json_obj = json.dumps(dictionary, indent=4, cls=Converter)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_obj)
        file.close()


def read_dictionary_from_json(filename):
    data = {}
    try:
        with open(filename, "a", encoding="utf-8") as open_file:
            data = json.load(open_file)
            open_file.close()
            return data
    except:
        return data
