#Label the program written in problem 4 with comments.

import os

# Set the directory you want to list (use '.' for current directory)
directory = '/'

# Get the list of files and directories
contents = os.listdir(directory)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
