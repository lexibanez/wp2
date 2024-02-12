import sys
from pathlib import Path
from encrypt import *


def get_files(original_text, encrypted_text):
    pass


def get_input():
    if len(sys.argv) != 5:
        print("Error. Usage: python wp2.py command file.txt file.txt key")

    elif len(sys.argv) == 5:
        command = sys.argv[1]
        original_text = sys.argv[2]
        encrypted_text = sys.argv[3]
        key = int(sys.argv[4])

        return command, original_text, encrypted_text, key
    
    else:
        print("Error. Usage: python wp2.py command file.txt file.txt key")

def main():
    command, original_text, encrypted_text, key = get_input()
    original_file, encrypted_file = get_files(original_text, encrypted_text)

    if command == '-e':
        encrypt_message(original_file, encrypted_file, key)

if __name__ == '__main__':
    main()