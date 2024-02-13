wp2.py

This program is a transposition encryption and decryption
function. The program takes input from the command line
in the form of:

python wp2.py -e originaltext.txt encryptedtext.txt key
python wp2.py -d encryptedtext.txt decryptedtext.txt key

commands:
The -e command encrypts the originaltext.txt file
The -d command decrypts the encryptedtext.txt file

key:
The key is an integer greater than 1 and less than the 
length of the file to be encrypted or decrypted.
During encryption, the contents of the file
are converted into a matrix with amount of columns "key".
The matrix is then transposed and then the rows are concatenated
to take the form of an encrypted message. The process works the
same in reverse during decryption, however blank spaces in the
matrix are reintroduced so that the decryption produces the right
message. The product of the encryption/decryption are then written
to the second file provided in the command line.