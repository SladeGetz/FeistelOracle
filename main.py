# Original code: Munshi, A., 2021. Feistel Cipher - GeeksforGeeks.
# [online] GeeksforGeeks. Available at: <https://www.geeksforgeeks.org/feistel-cipher/> [Accessed 13 February 2022].
# Python program to demonstrate
# Feistel Cipher Algorithm

# Author of modified code: Austin Slade Getz
# Purpose: Modify code from Geeks for Geeks to make a
# feistel cipher encryption oracle with custom and modifiable parameters

import binascii

# Random bits key generation
# AUTHOR: Ami Munshi
def rand_key(p):
    import random
    key1 = ""
    p = int(p)

    for i in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        key1 = key1 + temp

    return (key1)


# Function to implement bit exor
# AUTHOR: Ami Munshi
def exor(a, b):
    temp = ""

    for i in range(n):

        if (a[i] == b[i]):
            temp += "0"

        else:
            temp += "1"

    return temp


# F function - Round function of Feistel Cipher
# AUTHOR: Austin Slade Getz
def f(a, b):
    temp = ""

    for i in range(n):
        if (a[i] > b[i]):
            temp += "0"

        else:
            temp += "1"

    return temp

# Defining BinarytoDecimal() function
# AUTHOR: Ami Munshi
def BinaryToDecimal(binary):
    # Using int function to convert to
    # string
    string = int(binary, 2)

    return string


# Feistel Cipher
PT = "HelloWorldnSlade"

print("Plain Text is:", PT)

# Converting the plain text to
# ASCII
# AUTHOR: Ami Munshi
PT_Ascii = [ord(x) for x in PT]


# Converting the ASCII to
# 8-bit binary format
PT_Bin = [format(y, '08b') for y in PT_Ascii]
PT_Bin = "".join(PT_Bin)

n = int(len(PT_Bin) // 2)

L = PT_Bin[0:n] # left side
R = PT_Bin[n::] # right side


# Generate random keys
# AUTHOR: Austin Slade Getz
# KEY_SIZE ~ number of keys
# KEY_LENGTH ~ bit length of each key
KEYS = []
KEY_SIZE = 16
KEY_LENGTH = 128

# Ex. cyclic keys
for i in range(int(KEY_SIZE / 2)):
    KEYS.append(rand_key(KEY_LENGTH))
# Add reverse onto list
for i in range(int(KEY_SIZE / 2)):
    KEYS.append(KEYS[int(KEY_SIZE / 2) - 1 - i]);

# Choose number of rounds
ROUNDS = 16
for i in range(ROUNDS):
    F = f(R, KEYS[i]) # round function
    temp = exor(F, L) # exor F L
    L = R # swap L with old R
    R = temp

temp = L
L = R
R = temp

# Cipher text
# AUTHOR: Ami Munshi
bin_data = L + R
str_data = ''
print("Number of Bits:", len(bin_data)) # AUTHOR: Austin Slade Getz
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

print("Cipher Text:", str_data)
print("CT LEN:", len(str_data)) # AUTHOR: Austin Slade Getz

# Decryption
CT_Ascii = [ord(x) for x in str_data]
print("Ascii Values of CT:", CT_Ascii) # AUTHOR: Austin Slade Getz
# Converting the ASCII to
# 8-bit binary format
CT_Bin = [format(y, '08b') for y in CT_Ascii]
CT_Bin = "".join(CT_Bin)


# Decrypt using keys K_n to K_1
# AUTHOR: Austin Slade Getz
for i in range(ROUNDS-1, -1, -1):
    temp = R
    F = f(R, KEYS[len(KEYS) - 1 - i])
    R = exor(F, L)
    L = temp

temp = L
L = R
R = temp

# AUTHOR: Ami Munshi
PT1 = L + R
PT1 = int(PT1, 2)
RPT = binascii.unhexlify('%x' % PT1)
print("Retrieved Plain Text is: ", RPT)

