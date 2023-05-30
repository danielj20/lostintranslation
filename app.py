import random


def makeWord():
    var = random.randint(1, 8)
    vowel = ["a", "e", "i", "o", "u"]
    conso_blend = ['bl', 'br', 'kr', 'kl', 'ch', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'skr', 'spl', 'spr', 'str', 'thr']
    consoblend2 = random.choice(conso_blend)
    vowel2 = random.choice(vowel)
    vowel1 = random.choice(vowel)
    conso = ['b', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v']
    conso4 = random.choice(conso)
    conso6 = random.choice(conso)
    consoblend8 = random.choice(conso_blend)
    if var == 1:
        word = consoblend2 + vowel1 + conso4 + vowel2
    elif var == 2:
        word = vowel1 + consoblend2 + vowel2
    elif var == 3:
        word = consoblend2 + vowel1 + conso4
    elif var == 4:
        word = consoblend2 + vowel1
    elif var == 5:
        word = consoblend2 + vowel1 + consoblend8 + vowel2 + conso4
    elif var == 6:
        word = conso4 + vowel1 + conso6
    elif var == 7:
        word = consoblend8 + vowel1
    elif var == 8:
        word = consoblend2 + vowel1 + consoblend8 + vowel2
    
    return word




def structure():
    return random.choice(["OVS", "SVO", "SOV", "OSV", "VSO", "VOS"])




print(
    f"""
The: {makeWord()}
A: {makeWord()}
I: {makeWord()}
You: {makeWord()}
My: {makeWord()}
Your: {makeWord()}
Cat: {makeWord()}
Dog: {makeWord()}
House: {makeWord()}
Tree: {makeWord()}
to be (is, am, are): {makeWord()}
to run (runs, run): {makeWord()}
to want (wants, want): {makeWord()}
to eat (eats, eat): {makeWord()}
to see (sees, see): {makeWord()}
on: {makeWord()}
in: {makeWord()}
in front of: {makeWord()}
behind: {makeWord()}


STRUCTURE: {structure()}
"""
)


def makePrompt():
    subjects = ["I","You","Your dog","Your cat","The dog","The cat","A dog","A cat","My dog","My cat"]
    objects = ["Me","You","Your dog","Your cat","The dog","The cat","A dog","A cat","My dog","My cat", "Your tree","Your house","The tree","The house","A tree","A house","My tree","My house"]
    verbs = ["to see","to eat","to want","to want to see","to want to eat", "to be", "to want to be"]
    tr_verbs = ["to see","to eat","to want to see","to want to eat", "to run", "to want to run"]
    tr_verbs_plus_be = ["to see","to eat","to want to see","to want to eat", "to run", "to want to run", "to be", "to want to be"]
    prepositions = ["in front of","behind","in","on"]


    sentence_type = random.randint(1, 3)


    if sentence_type == 1:
        # subject verb
        return random.choice(subjects) + f" ({random.choice(tr_verbs)})"
    elif sentence_type == 2:
        # subject verb object
        return random.choice(subjects) + f" ({random.choice(verbs)}) " + random.choice(objects)
    elif sentence_type == 3:
        # subject verb preposition
        return random.choice(subjects) + f" ({random.choice(tr_verbs_plus_be)}) " + random.choice(prepositions) + " " + random.choice(objects)








while True:
    input("Next prompt? ")
    print(makePrompt())
