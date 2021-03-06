import json
import argparse


def parse_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('path', help='path to file')
    args = arg_parser.parse_args()
    return args


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        raw_data = file.read()
        return raw_data


def get_json_pretty_string(raw_data):
    decoded_json = json.loads(raw_data)
    json_pretty_string = json.dumps(decoded_json,
                                    ensure_ascii=False,
                                    sort_keys=True,
                                    indent=4)
    return json_pretty_string


if __name__ == '__main__':
    arguments = parse_arguments()
    path_to_file = arguments.path
    raw_data = load_data(path_to_file)
    json_pretty_string = get_json_pretty_string(raw_data)
    print(json_pretty_string)

