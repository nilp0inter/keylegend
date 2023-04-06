#!/bin/sh
make mykeyset.pdf
zathura mykeyset.pdf &
scalc mykeyset.csv &
find mykeyset.csv | entr make clean mykeyset.pdf
