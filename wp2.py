import sys
from pathlib import Path
from encrypt import *
from keyvalidate import _validate_key, InvalidKeyException


def load_files(file1_txt, file2_txt):
    file1 = Path(file1_txt)
    file2 = Path(file2_txt)
    file2.touch()

    if file1.exists():
        return file1, file2
    else:
        print("Error. File does not exist.")


def get_input():
    if len(sys.argv) != 5:
        print("Error. Usage: python wp2.py command file.txt file.txt key")

    elif len(sys.argv) == 5:
        try:
            command = sys.argv[1]
            original_text = sys.argv[2]
            encrypted_text = sys.argv[3]
            key = int(sys.argv[4])
        except ValueError:
            print("Error. Key must be an integer.")

        return command, original_text, encrypted_text, key

    else:
        print("Error. Usage: python wp2.py command file.txt file.txt key")


def main():
    try:
        command, file1_txt, file2_txt, key = get_input()
        file1, file2 = load_files(file1_txt, file2_txt)

        test_key = _validate_key(key, file1)

        if command == '-e':
            encrypted_file = encrypt_message(file1, file2, key)

        elif command == '-d':
            decrypted_file = decrypt_message(file1, file2, key)

    except InvalidKeyException as e:
        print(e)
    except UnboundLocalError:
        pass
    except TypeError:
        pass


if __name__ == '__main__':
    main()
