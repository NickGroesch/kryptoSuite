plaintext = input("enter a message to encode: ")
keyLength = int(input("enter an interger key length"))


def encodeColTransCy(message, key):
    ciphertext = [''] * key
    for column in range(key):
        index = column
        while index < len(message):
            ciphertext[column] += message[index]

            index += key
    return "".join(ciphertext)

def decodeColTransCy(message, key)
    plaintext=['']*key



encodeColTransCy(plaintext, keyLength)