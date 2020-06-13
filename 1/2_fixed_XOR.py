import codecs

def HEX(string):
    return int(string, 16)

def XOR(buffer1, buffer2):
    if len(str(buffer1)) != len(str(buffer2)):
        return False
    hex_buffer1 = HEX(buffer1)
    hex_buffer2 = HEX(buffer2)
    result = hex_buffer1 ^ hex_buffer2
    return hex(result)

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
print(XOR(string1, string2))
