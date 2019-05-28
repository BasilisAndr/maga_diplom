## What it is
My Master's thesis code

## What is there
lexc files and Makefile for an automatic morpheme segmentation for Russian

## How to use it
- Install HFST (http://wiki.apertium.org/wiki/Installation)
- Clone the repositiory
- Run `make`
then
- Change the path CMD to your file in `corpus-stat.sh` (your file should be one word per line)
- Run `corpus-stat.sh`
or
- for one word lookup, run `echo "your_word" | hfst-lookup rus.hfstol | python post.py | python postpost.py `
