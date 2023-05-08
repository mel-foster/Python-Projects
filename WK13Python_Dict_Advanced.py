#!/usr/bin/env python3.7

# Import the OS Module
import os

# Create empty list name "cwd_list"
cwd_files = []

# Define function to extract file info default cwd
def extract_info(path = '.'):
    cwd_files = []

# Recursively iterate over all files/directiories cwd
    for root, dirs, files in os.walk(path): 
        for file_name in files:
            file_dict = {} 
            
            # Get file path and size
            file_dict['path'] = os.path.join(root, file_name) 
            file_dict['size'] = os.path.getsize(os.path.join(root, file_name)) 
            
            # Appends file info dictionary to the list
            cwd_files.append(file_dict) 
            
        # Return List
        return cwd_files
        
exit = False

# Loop until User Chooses to Exit
while exit == False: 
    try:
        
        #User has option to input path or to exit the program
        path = input("Type in a path or press 'Enter' for CWD. (Type 'Exit' to exit the program): ") 
        
        if path.lower() == "exit": 
            exit =  True

        # Default to CWD if no path entered
        elif path == "": 
            info = extract_info()
            print(*info, sep="\n")

        # Pass custom path to function
        else:
            info = extract_info(path) 
            print(*info, sep="\n")
            
            
    # Unexpected Error Message         
    except: 
        print(" Error: Issue Processing Path. Please try again with a correct path.")    
        
        