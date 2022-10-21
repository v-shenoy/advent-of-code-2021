#!/usr/bin/env bash

for file in $(find . -name "*.py" | sort) 
do
    echo $file
    python $file
done
