import matplotlib.pyplot as plt
import numpy as np

ROMANaLPAHBET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
ignorePunctuation = [
    # ' ',
    ',',
    # '.',
    # '?',
    # '!',
    "'",
    '"',
]
# print(ROMANaLPAHBET)

text = input("enter a text:")
print(text)


def split(word):
    return list(word)


textList = (split(text))

print(textList.count("n"))


def freqCount(charlist):
    freqDict = {}
    # for letter in ROMANaLPAHBET:
    for letter in SYMBOLS:
        freqDict[letter] = charlist.count(letter) / len(charlist)
        # print(freqDict)
    return freqDict


frequency = (freqCount(textList))
print(frequency)
#https://stackoverflow.com/questions/21925007/using-dictionary-to-make-a-matplotlib-graph
fig, ax = plt.subplots()
ax.set_ylabel('frequency')
ax.set_xlabel('letter')
ax.set_title('frequency analysis analysis')
plt.bar(range(len(frequency)), list(frequency.values()), align='center')
plt.xticks(range(len(frequency)), list(frequency.keys()))
plt.show()


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


def decodeCeaser(letterValue,
                 message,
                 alphabet=ROMANaLPAHBET,
                 ignore=ignorePunctuation):
    messageArray = split(message)
    offset = alphabet.index(letterValue)
    # print('offset is -{0}'.format(offset))
    decoded = []
    for letter in messageArray:
        # print(letter)
        if letter in ignore:  #condition needs work
            decoded.append(letter)
            pass
        else:
            decoded.append(alphabet[(alphabet.index(letter) - offset) %
                                    len(alphabet)])
            pass
    return "".join(decoded)


# ceaserInput = input('enter a letter for ceasar shift:')
# secretcoded = encodeCeaser(ceaserInput, text)
# print(secretcoded)

# for i in range(len(ROMANaLPAHBET)):
#     print("key " + ROMANaLPAHBET[i] + " : " +
#           decodeCeaser(ROMANaLPAHBET[i], secretcoded))
for i in range(len(SYMBOLS)):
    print("key " + SYMBOLS[i] + " : " +
          decodeCeaser(SYMBOLS[i], text, SYMBOLS))
input("Press Enter to end the program.")