import numpy as np
from base64 import b64decode
import binascii
import os
from itertools import combinations


CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def get_edit_distance(string1, string2):
    '''
    This function is not useful in the answer as number of differing bits is required. However, the function is the correct way
    of calculating edit distance.
    Write a function to compute the edit distance/Hamming distance between two strings.
    The Hamming distance is just the number of differing bits.
    '''
    # initialize the matrix:
    length1 = len(string1)
    length2 = len(string2)
    matrix = np.zeros((length1+1, length2+1))
    # loop
    for i in range(0,length1+1):
        for j in range(0, length2+1):
            if i == 0:
                matrix[0][j] = j
            elif j == 0:
                matrix[i][0] = i
            else:
                if string1[i-1] == string2[j-1]:
                    matrix[i][j] = min([matrix[i-1][j], matrix[i][j-1],matrix[i-1][j-1]])
                else:
                    previous =  min([matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]])
                    matrix[i][j] = min([matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]]) + 1
                    now = matrix[i][j]
    print(matrix)
    return matrix[length1][length2]

def get_hamming_distance(string1, string2):
    return sum([bin(string1[i] ^ string2[i]).count('1') for i in range(len(string1))])

#string1 = b"this is a test"
#string2 = b"wokka wokka!!!"
# convert to string to bit
#print(get_hamming_distance(string1, string2))


def single_char_xor(input_bytes, key_value):
    output = b''
    for char in input_bytes:
        output += bytes([char ^ key_value])
    return output

def single_char_bruteforce(ciphertext):
    candidates = []
    for key in range(0,256):
        candidate = single_char_xor(ciphertext, key)
        candidate_score = 0
        for byte in candidate:
            candidate_score += CHARACTER_FREQ.get(chr(byte).lower(), 0)
        candidates.append([candidate_score, chr(key), candidate])
        candidates.sort(key=lambda x: x[0])
    return candidates[-1]

def repeating_key_XOR(plaintext, key):
    ciphertext = b""
    i = 0
    for byte in plaintext:
        ciphertext += bytes([byte ^ key[i]])
        i+=1
        if i == len(key):
            i = 0
    return ciphertext



if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(file_dir + '\\6.txt', 'r')
    content = b64decode(f.read())
    f.close()
    distances = {}
    # test the keysize
    for KEYSIZE in range(2,40):
        first_block = content[0:KEYSIZE]
        second_block = content[KEYSIZE:2*KEYSIZE]
        third_block = content[2*KEYSIZE:3*KEYSIZE]
        fourth_block = content[3*KEYSIZE:4*KEYSIZE]
        chunks = [first_block, second_block, third_block, fourth_block]
        pairs = combinations(chunks, 2)
        distance = 0.0
        for (x, y) in pairs:
            distance += get_hamming_distance(x, y)/KEYSIZE
        distances[KEYSIZE] = distance / 6

    # print(distances)
    real_KEYSIZE = min(distances, key=distances.get)
    # break the ciphertext
    content_list = [content[i:i+real_KEYSIZE] for i in range(0, len(content), real_KEYSIZE) ]

    # tranpose
    transposed_list = [b''] * real_KEYSIZE
    for i in range(0, real_KEYSIZE):
        for item in content_list:
            # take a look at this: https://stackoverflow.com/questions/34716876/how-to-get-a-single-byte-in-a-string-of-bytes-without-converting-to-int
            transposed_list[i] += item[i:i+1]

    final_key = ''

    # handle each chunk to get key char
    for chunk in transposed_list:
        result_list = single_char_bruteforce(chunk)
        # add to final_key
        final_key += result_list[1]

    # print(final_key)

    # decrypt the original message
    print(repeating_key_XOR(content, final_key.encode()))











        
