import json

INPUT_JSON_FILE = 'test_input.json'


def main():
    print("Loading data from {}...".format(INPUT_JSON_FILE))
    with open(INPUT_JSON_FILE, 'r') as file_handle:
        json_data = json.load(file_handle)
        print(json_data['hotels'][0]['city']) # Should print Chicago


if __name__ == '__main__':
    main()