#!/usr/bin/env python3.7

# Import the OS Module
import os

# Create empty list name "cwd_files"
cwd_files = []

# Define the working directory as "cwd" variable
my_cwd = os.getcwd()

# Loop through all files in the current working directory
for file in os.listdir():

# Join the file name with the current working directory path
    file_path = os.path.join(file)
    
# Get file stats (path and size of file)
    file_stats = os.stat(file_path)

# Append a new dictionary to 'cwd_files' with path and size
    cwd_files.append({'my_cwd':my_cwd+'/' +file, 'size': file_stats.st_size})
    
# using a "for" loop with range() function to print the files pretty 
for i in range(len(cwd_files)):
    print(cwd_files[i])