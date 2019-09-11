def getAlphbetialOrder(keyString):
    import string
    alphabet = list(string.ascii_lowercase)
    itera = 0
    charChange = False
    word = list(keyString.lower())
    for letter in alphabet:
        for index, char in enumerate(word):
            if char == letter:
                word[index] = itera
                charChange = True
        if charChange:
            itera += 1
            charChange = False

    return word


print(getAlphbetialOrder("boolean"))