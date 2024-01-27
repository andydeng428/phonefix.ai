#!/bin/bash

cd temp-images
FILENAME=$(ls)x
cd ..
cd output-images
python imageGenerate.py $FILENAME

cd ..
cd temp-images
rm $FILENAME


