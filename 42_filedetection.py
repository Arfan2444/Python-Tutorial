# Python file detection example

import os

file_path = "stuff/text.txt"

if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
    if os.path.isfile(file_path):
        print("That is a file.")
    elif os.path.isdir(file_path):
        print("That is a directory.")
else:
    print(f"That file does not exist.")