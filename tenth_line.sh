# Read from the file file.txt and output the tenth line to stdout.
#!usr/bin/env bash

file="file.txt"
count=1
while [ $count -le 10 ]; do
    read -r line
    if [ $count -eq 10 ]; then
        echo -e "$line"
    fi
    ((count++))
# marks end of while loop
# tells the shell that the "read" command from while loop
# takes its input from $file
done <$file 

