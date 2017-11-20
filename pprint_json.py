import json
import argparse


def parse_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('path', help='path to file')
    args = arg_parser.parse_args()
    return args


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = file.read()
        return data


def pretty_print_json(data):
    json_obj = json.loads(data, encoding='utf-8')
    json_pretty_string = json.dumps(json_obj,
                                    ensure_ascii=False,
                                    sort_keys=True,
                                    indent=4)
    return json_pretty_string


if __name__ == '__main__':
    arguments = parse_arguments()
    path_to_file = arguments.path
    data = load_data(path_to_file)
    json_pretty_string = pretty_print_json(data)
    print(json_pretty_string)

