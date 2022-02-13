# Feistel Oracle
Feistel Oracle is a Python project, modified from Munshi, A., 2021. Feistel Cipher -
GeeksforGeeks. [online] GeeksforGeeks. Available at:
<https://www.geeksforgeeks.org/feistel-cipher/> [Accessed 13 February 2022]., that has an
encryption and decryption scheme. This project was made for education purposes. This was
made as a way to better understand and test feistel ciphers for my intro to Cryptography class.

## Author
Austin Slade Getz

## Usage
The F rounding function in a feistel cipher does not need to be inversable and takes in a data block
that is half the size of the input and a subkey. My F function must output a string of 1's and 0's
the same length as a:

'''
def f(a, b):
  temp = ""
  # custom code
  # temp += "0" or "1" len(a) times
  return temp
'''

Key generation is fairly simple using the rand_key function (included) and the size of the key.
Below is an example to generate 16 random keys.

'''
KEYS = []
KEY_SIZE = 16
KEY_LENGTH = 128

for i in range(int(KEY_SIZE)):
    KEYS.append(rand_key(KEY_LENGTH))
'''
One can customize the character encoding by choosing the size CHAR_SIZE variable. Below shows an
example where each character is 8 bits long.

'''
CHAR_SIZE = 8 # modified original code to be able to choose char size
for i in range(0, len(bin_data), CHAR_SIZE):
    # slicing the bin_data from index range [0, CHAR_SIZE -1]
    # and storing it in temp_data
    temp_data = bin_data[i:i + CHAR_SIZE]

    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal(temp_data)

    # Decoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data

    str_data = str_data + chr(decimal_data)
'''

## Feistel Encryption
You can choose the number of rounds by modifying the ROUNDS variable. The below example shows how
the feistel encryption operates and the ROUNDS variable set to 16.

'''
ROUNDS = 16
for i in range(ROUNDS):
    F = f(R, KEYS[i]) # round function
    temp = exor(F, L) # exor F L
    L = R # swap L with old R
    R = temp

temp = L
L = R
R = temp
'''
