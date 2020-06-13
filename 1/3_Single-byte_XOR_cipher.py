import binascii

def single_char_XOR(input_message, char_value):
    output = ""
    nums = binascii.unhexlify(input_message)
    for num in nums:
        output += chr(num ^ char_value)
    return output


hexed_message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

for key in range(0,256):
    print(single_char_XOR(hexed_message, key))

# Cooking MC's like a pound of bacon