# MD5
Hashes all files in a directory and searches for desired hash within all files.

# Requirements
* Python 3
* 'hashlib' library (should come with Python by default)

# Usage
1.  Clone this repository into the same folder containing the directory in question and navigate to the folder containing the script.
2.  Change "suspicious_files" to name of directory containing files to hash.
3.  Run the script with python3 hash_checker.py.
4.  When prompted, enter the hash you want to search for.

The script will then calculate the MD5 hash of every file in the specified directory and print the name of any file whose hash matches the input.
