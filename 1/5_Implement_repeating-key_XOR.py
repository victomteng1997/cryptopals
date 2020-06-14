message = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
import binascii

key = b"ICE"

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
    output = repeating_key_XOR(message, key)
    print(binascii.hexlify(output))
