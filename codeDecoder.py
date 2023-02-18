import re

s = "python"

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

    if text.isalpha():
        return ''.join(decrypt[i] for i in text.split())
    return ' '.join(encrypt[i] for i in text.upper())


#print(morse(s))