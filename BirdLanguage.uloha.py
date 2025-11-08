import random
vowels = 'aeiou'
consonants = 'qwrtpsdfghjklzxcvbnm'
def translation(vstup):
    vystup = " "
    counter = 0
    while counter < len(vstup):
        if vstup[counter] in vowels:
            vystup += vstup[counter]*3
            counter += 1
        elif vstup[counter] in consonants:
            vystup += vstup[counter] + random.choice(vowels)
            counter += 1
        else:
            vystup += vstup[counter]
            counter += 1
    return vystup
print (translation("hello"))