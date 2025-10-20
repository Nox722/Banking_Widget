import json
import os


def get_data_from_json_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    file_path = os.path.join(root_dir, 'data', 'test_empty.json')

    data = get_data_from_json_file(file_path)
    print(data)