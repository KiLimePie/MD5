# import OS module and library of hashing algorithms
import os
import hashlib
from hashlib import md5

# creates list of all files in suspicious_files directory
dir=os.listdir("suspicious_files")

# places desired hash into search variable
search=input("Enter the hash here: ")

# creates loop to search every file in directory
for file in dir:

    # checks if path provided is an existing regular file or not
    if os.path.isfile("suspicious_files/" + file):

        # opens the file in binary format for reading as variable f
        with open("suspicious_files/" + file, 'rb') as f:

            # read each line in file as buf variable
            buf = f.read()
            # md5 hashes each line in file as hash variable
            hash = md5(buf).hexdigest()

        # tests if search variable exists in hash variable
        if search in hash:

            # prints the file name that contains the search string
            print("The file that matches the given hash is: %s" % file)