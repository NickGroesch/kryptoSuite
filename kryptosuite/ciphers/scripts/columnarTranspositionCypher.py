#plaintext = input("enter a message to encode: ")
#keyLength = input("enter a key (sort by length and alphabetical order): ")

#there once was a man from nantucket
#artfully
#tc mkrwna os frtuhem ee antea nnaoc
#['tc mk', 'rwna', ' os frtu', 'hem e', 'e ant', 'ea n', 'naoc']


def encodeColTransCy(
        message, key):  # TODO: actually we should allow a scrambled alphabet
    keynum = getAlphabetialOrder(key)
    length = max(keynum) + 1
    ciphertext = [''] * length
    #need to get this sorted in alpabetical
    for index, letter in enumerate(message):
        column = index % len(keynum)
        ciphertext[keynum[column]] += letter
    print(ciphertext)
    return "".join(ciphertext)


def decodeColTransCy(message, key):  #TODO: obviously
    keynum = getAlphabetialOrder(key)
    length = max(keynum) + 1
    mesLen = len(message)
    print(length, len(keynum), keynum, mesLen)
    columns = [''] * len(keynum)
    column = 0
    row = 0
    for index, char in enumerate(message):
        keyindex = keynum[index % len(keynum)]
        columns[keyindex] += char

        # columns[column] += char
        # column += 1
        # if column == len(keynum):
        #     column = 0
        #     row += 1
    print(columns)


def getAlphabetialOrder(
        keyString):  #TODO: include a scrambled alphabet for the keystring
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


print('the answer is of course: ',
      encodeColTransCy('tc mkrwna os frtuhem ee antea nnaoc', 'artfully'))
decodeColTransCy('tc mkrwna os frtuhem ee antea nnaoc', "artfully")
