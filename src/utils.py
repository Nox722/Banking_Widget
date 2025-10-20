import json


def get_data_from_json_file(path):
    with open(path) as f:
        data = json.load(f)
        return data
