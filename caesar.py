def alphabet_position(letter):
    if letter.islower():
        return ord(letter) - 97
    elif letter.isupper:
        return ord(letter) - 65

def rotate_character(char, rot):
    if char.isalpha():
        if char.islower():
            newChar = (alphabet_position(char) + rot) % 26
            return chr(newChar + 97)
        else:
            newChar = (alphabet_position(char) + rot) % 26
            return chr(newChar + 65)
    else:
        return char

def encrypt(text, rot):
    encryptedText = ""
    for character in text:
        textChar = rotate_character(character, rot)
        encryptedText = encryptedText + textChar
    return encryptedText
