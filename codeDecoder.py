s = "python"

def morse(text):
    encrypt  = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
                'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--', 'Q':'--.-', 'R':'.-.',
                'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ':'.....'}

    decrypt  = {value: key for key, value in encrypt. items()}

    if '-' in text:
        return ''.join(decrypt[i] for i in text.split())

