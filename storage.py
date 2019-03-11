#!/usr/bin/python3

import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Key")
parser.add_argument("--value", help="value")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.json')


# Запись пары ключ-значения
if args.key and args.value:
    with open(storage_path, 'w') as f:
        data = {args.key:args.value}
        f.write(json.dumps(data, ensure_ascii=False))

# Вывод значения из хранилища
elif args.key:
    with open(storage_path, 'r') as f:
        data = json.load(f)
        try:
            print(", ".join(data[args.key]))
        except KeyError:
            print(None)


