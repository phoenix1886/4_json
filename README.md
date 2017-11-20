# Prettify JSON

This script reads JSON from file and prints it in user friendly manner.

It takes 1 positional arguments:
* path: path to file.

Requirements:
* file should be encoded in UTF-8.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to file>
[
    {
        "geoData": {
            "coordinates": [
                37.58803599964753,
                55.89020100016689
            ],
            "type": "Point"
        },
        "global_id": 14937274  
    }     
]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
