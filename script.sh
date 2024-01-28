#!/bin/bash
cd temp-images

mv upload**********.png original_image.png
python3 imageGenerate.py

rm *.png