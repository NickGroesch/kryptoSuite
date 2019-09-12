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
    for index, letter in enumerate(message):
        column = index % len(keynum)
        ciphertext[keynum[column]] += letter
    print(ciphertext)
    return "".join(ciphertext)


def decodeColTransCy(message, key):
    import math
    keynum = getAlphabetialOrder(key)
    length = max(keynum) + 1
    keyLen = len(keynum)
    mesLen = len(message)
    # print('a', length, keyLen, keynum, mesLen)
    rows = []
    rowLen = int(math.floor(mesLen / keyLen))
    fatRows = mesLen - (rowLen * keyLen)
    # print('b', rowLen, fatRows)
    goalLengths = []
    counts = []
    for i in range(length):  #TODO: refactor these into list comprehensions
        counts.append(keynum.count(i))
    for index, count in enumerate(counts):
        # print(index, count)
        goalLengths.append(count * rowLen)
    for i in range(fatRows):
        goalLengths[keynum[i]] += 1
    # print('c', goalLengths)
    divisonCounter = 0
    for i in range(len(counts)):
        rows.append(message[divisonCounter:divisonCounter + goalLengths[i]])
        divisonCounter += goalLengths[i]
    # print('d', rows, len(rows))
    # print('e', counts, len(counts))
    reconstructionCounter = [0 for row in rows]
    # print(reconstructionCounter)
    decoded = ''
    for i in range(rowLen + 1):  #ÄHHHH
        for j, k in enumerate(keynum):
            if len(decoded) == mesLen:
                break
            else:
                # print(rows[k][reconstructionCounter[k]])
                decoded += rows[k][reconstructionCounter[k]]
                reconstructionCounter[k] += 1
    return decoded


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


# print('encoded ', encodeColTransCy('abcdefghijklmnopqrstuvwxyz', 'abbc'))
# decodeColTransCy('aeimquybcfgjknorsvwzdhlptx', "abbc")

# print('encoded ',
#       encodeColTransCy('there once was a man from nantucket', 'artfully'))
print(decodeColTransCy('tc mkrwna os frtuhem ee antea nnaoc', "artfully"))