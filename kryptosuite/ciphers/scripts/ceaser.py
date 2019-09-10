ROMANaLPAHBET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
ignorePunctuation = [
    ' ',
    ',',
    '.',
    '?',
    '!',
    "'",
    '"',
]


def split(word):
    return list(word)


def encodeCeaser(letterValue,
                 message,
                 alphabet=ROMANaLPAHBET,
                 ignore=ignorePunctuation):
    messageArray = split(message)
    offset = alphabet.index(letterValue)
    # print('offset is {0}'.format(offset))
    encoded = []
    for letter in messageArray:
        if letter in ignore:  #condition needs work
            encoded.append(letter)
            pass
        else:
            encoded.append(alphabet[(alphabet.index(letter) + offset) %
                                    len(alphabet)])
            pass
    return "".join(encoded)