import re

s = "Papa Yankee Hotel"

def morse(text):
    encrypt  = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
                'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--', 'Q':'--.-', 'R':'.-.',
                'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ':'.....'}

    decrypt  = {value: key for key, value in encrypt. items()}

    if re.match('(\s|-|\.)+', text):
        return ''.join(decrypt[i] for i in text.split())
    return ' '.join(encrypt[i] for i in text.upper())

def phonetic(text):
    encrypt = {'A':'Alpha', 'B':'Bravo', 'C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel',
               'I':'India','J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa',
               'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey',
               'X':'Xray', 'Y':'Yankee', 'Z':'Zulu', ' ':'     '}

    decrypt = {value: key for key, value in encrypt.items()}

    if re.match('(\s|-|\.)+', text):
        return ''.join(decrypt[i] for i in text.split())
    return ' '.join(encrypt[i] for i in text.upper())

def vigenere_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def vigenere_text(string, key):
    vigenereText = []
    for i in range(len(string)):
        x = (ord(string[i]) +ord(key[i])) % 26
        x += ord('A')
        vigenereText.append(chr(x))
    return ("".join(vigenereText))

def vigenere():
    if __name__ == "__main__":
        string = input("Text: ").upper()
        string = string.replace(" ", "")
        keyword = input("Key: ").upper()
        key = vigenere_key(string, keyword)
        vigenereText = vigenere_text(string, key)
        print("Vigerene Code:", vigenereText)

def binary(text):
    encrypt = {'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110',
               'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100',
               'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010',
               'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000',
               'Y': '01011001', 'Z': '01011010', ' ': '.....'}

    decrypt = {value: key for key, value in encrypt.items()}


#print(phonetic(s))

