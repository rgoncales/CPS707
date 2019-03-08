#!/bin/bash
FILES=inputs/*_input.txt
#Loop through all files in inputs/ that end in input.txt (in order to only do each test once because expected outputs are in this directory too)
for filename in $FILES; do
echo checking test $filename
#change from testname_input.txt to testname_output.txt, save in variable testname
TESTNAME=$(echo $filename | cut -d'_' -f 1 | cut -d '/' -f 2)
#Inputs contains expected outputs, outputs contains actual outputs, so print the differences between them
diff inputs/$TESTNAME"_output.txt" outputs/$TESTNAME"_actualoutput.txt"
done
