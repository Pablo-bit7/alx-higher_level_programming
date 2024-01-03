#!/bin/bash

# Create the directory "1." if it doesn't exist
mkdir -p "1."

# Create the directory "dx" if it doesn't exist
mkdir -p "dx"

# Exclude files and directories from being moved
exclude=("README.md" "move_files.sh" "1.")

# Move all files (not directories) to "1." excluding specified files
for file in *; do
    if [[ ! " ${exclude[@]} " =~ " ${file} " ]]; then
        mv "$file" "1."
    fi
done

# Move files starting with "dx" to "dx" directory
mv dx* "dx"

echo "Files moved to '1.' and 'dx' directories."