#!/bin/bash
FILES=inputs/*_input.txt
#Loop through all files ending in _input.txt in input directory (Expected outputs are also in this directory ending in _output.txt)
for filename in $FILES; do
echo running test $filename
#Remove _index.txt and save it in testname so it is just the test name no input/output
TESTNAME=$(echo $filename | cut -d'_' -f 1 | cut -d '/' -f 2)
#Run the program with $filename (each file ending in _input.txt) and save its output in outputs (where all actual outputs are saved) with format testname_actualoutput.txt
python3.7 ../test_app.py $filename > outputs/$TESTNAME"_actualoutput.txt"
done
