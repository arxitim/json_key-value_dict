#!/usr/bin/python3

import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Key")
parser.add_argument("--value", nargs="*", help="value")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    a = open(storage_path, 'w')
    a.close()

# Запись пары ключ-значения
if args.key and args.value:
    if os.path.getsize(storage_path):
        with open(storage_path, 'r+', encoding='utf-8') as load_file:
            data = json.load(load_file)
        with open(storage_path, 'w', encoding='utf-8') as input_file:
            if args.key not in data:
                if isinstance(args.value, list):
                    data[args.key] = args.value
                else:
                    data[args.key] = [args.value]
            else:
                data[args.key] += args.value
            json.dump(data, input_file)
    else:
        data = {}
        data[args.key] = args.value
        with open(storage_path, 'w', encoding='utf-8') as input_file:
            json.dump(data, input_file)

# Вывод значения из хранилища
elif args.key:
    with open(storage_path, 'r') as output_file:
        try:
            data = json.load(output_file)
            print(', '.join(data[args.key]))
        except (KeyError, json.decoder.JSONDecodeError):
            print(None)
