import json

def load_config():
    with open('./constants.json') as json_file:
        data = json.load(json_file)
    return data
