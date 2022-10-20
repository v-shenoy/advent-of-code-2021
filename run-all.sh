#!/usr/bin/env bash

for file in $(find . -name "day_*" | sort) 
do
    echo $file
    python "$file/a.py"
    python "$file/b.py"
done
