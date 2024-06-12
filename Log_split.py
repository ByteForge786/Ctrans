#!/bin/bash

# Set the source and destination directories
src_dir="./logs"
dest_dir="./history_logs"

# Get the current date in the format YYYY-MM-DD
current_date=$(date '+%Y-%m-%d')

# Create the destination directory if it doesn't exist
mkdir -p "$dest_dir"

# Create a temporary directory for moving log files
temp_dir=$(mktemp -d)

# List of log file names to move (update this as needed)
log_files=("app.log" "error.log" "server.log")

# Move the specified log files to the temporary directory
for file in "${log_files[@]}"
do
    src_file="$src_dir/$file"
    if [ -f "$src_file" ]
    then
        mv "$src_file" "$temp_dir"
    else
        echo "File $file not found in $src_dir"
    fi
done

echo "Specified log files have been moved to $temp_dir"

# Zip the temporary directory
zip_file="$dest_dir/$current_date.zip"
zip -r "$zip_file" "$temp_dir"

echo "Temporary directory has been zipped to $zip_file"

# Remove the temporary directory
rm -rf "$temp_dir"

echo "Temporary directory has been removed"

# Create new empty files at the source path for the moved log files
for file in "${log_files[@]}"
do
    src_file="$src_dir/$file"
    touch "$src_file"
done

echo "New empty files have been created at $src_dir"
