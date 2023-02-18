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

def vigerene_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def vigerene_text(string, key):
    vigereneText = []
    for i in range(len(string)):
        x = (ord(string[i]) +ord(key[i])) % 26
        x += ord('A')
        vigereneText.append(chr(x))
    return ("".join(vigereneText))


#print(phonetic(s))