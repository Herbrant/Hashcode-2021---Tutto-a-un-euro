#!/bin/bash

python3 main.py a
python3 main.py b
python3 main.py c
python3 main.py d
python3 main.py e
python3 main.py f


[ -f "code.zip" ] && rm code.zip
zip code.zip *.py


