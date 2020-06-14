'''
Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)
'''

import binascii
import os

def single_char_XOR(input_message, char_value):
    output = ""
    nums = binascii.unhexlify(input_message)
    for num in nums:
        output += chr(num ^ char_value)
    return output

file_dir =  os.path.dirname(os.path.realpath(__file__))
f = open(file_dir + "\\4.txt", 'r')
content = f.readlines()
f.close()

result_list = []
result_dic = {}


for line in content:
    hexed_message = line.replace("\n", '')
    for key in range(0,256):
        result_list.append(single_char_XOR(hexed_message, key))
        result_dic[single_char_XOR(hexed_message, key)] = [key, line]

possible_solution = sorted(result_list, key=lambda s: s.count(' '))[-1]
print(possible_solution,  result_list.index(possible_solution))
print(result_dic[possible_solution])

# [53, '7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f\n']
# So the solution is 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f

