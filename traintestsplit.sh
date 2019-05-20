#! /bin/bash

cat nkrya_res.csv | grep '1800' | sort --random-sort | head -n 1000 > 1800.txt
cat nkrya_res.csv | grep '1900' | sort --random-sort | head -n 1000 > 1900.txt
cat nkrya_res.csv | grep '1950' | sort --random-sort | head -n 1000 > 1950.txt
cat 1800.txt | head -n500 > 1800_train.txt
cat 1800.txt | tail -n500 > 1800_test.txt
cat 1900.txt | head -n500 > 1900_train.txt
cat 1900.txt | tail -n500 > 1900_test.txt
cat 1950.txt | head -n500 > 1950_train.txt
cat 1950.txt | tail -n500 > 1950_test.txt
cat 1800_train.txt 1900_train.txt 1950_train.txt > train.txt
cat 1800_test.txt 1900_test.txt 1950_test.txt > test.txt
cat train.txt | cut -d'_' -f1 > train_for_run.txt
