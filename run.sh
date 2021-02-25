#!/bin/bash
FILE=$1

if [ -z "$FILE" ]; then
	echo "USE: ./run.sh INPUT_FILE"
else
	python main.py "$FILE"
fi

