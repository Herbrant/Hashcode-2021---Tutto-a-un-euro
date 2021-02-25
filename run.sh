#!/bin/bash
FILE=$1

if [ -z "$FILE" ]; then
	echo "USE: ./run.sh INPUT_FILE"
else
	python3 main.py "$FILE"

	[ -f "code.zip" ] && rm code.zip
	zip code.zip *.py
fi

