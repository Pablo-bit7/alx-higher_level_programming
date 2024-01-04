#!/bin/bash

# Iterate through each file in the current directory
for file in *; do
    # Check if the file is a regular file (not a directory)
    if [ -f "$file" ]; then
        # Run dos2unix on the file
        dos2unix "$file"
        echo "Converted $file to Unix line endings."
    fi
done
