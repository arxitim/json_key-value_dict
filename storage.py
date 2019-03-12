#!/usr/bin/python3

import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Key")
parser.add_argument("--value", nargs="+", help="value")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


# Запись пары ключ-значения
if args.key and args.value:
    if os.path.exists(storage_path) and os.path.getsize(storage_path):
        with open(storage_path, 'r+', encoding='utf-8') as load_file:
            data = json.load(load_file)
        with open(storage_path, 'w', encoding='utf-8') as input_file:
            data[args.key] = args.value
            json.dump(data, input_file)
    else:
        data = {}
        data[args.key] = args.value
        with open(storage_path, 'w', encoding='utf-8') as input_file:
            json.dump(data, input_file)

# Вывод значения из хранилища
elif args.key:
    with open(storage_path, 'r') as output_file:
        data = json.load(output_file)
        try:
            print(', '.join(data[args.key]))
        except KeyError:
            print(None)
