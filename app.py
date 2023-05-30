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

def adjective_order():
    return random.choice(["ADJ + NOUN", "NOUN + ADJ"])




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
Very: {makeWord()}
Long: {makeWord()}
Tall: {makeWord()}
Wide: {makeWord()}
To be (is, am, are): {makeWord()}
To run (runs, run): {makeWord()}
To want (wants, want): {makeWord()}
To eat (eats, eat): {makeWord()}
To see (sees, see): {makeWord()}
On: {makeWord()}
In: {makeWord()}
In front of: {makeWord()}
Behind: {makeWord()}


STRUCTURE: {structure()}
ADJECTIVE ORDER: {adjective_order()}
"""
)


def makePrompt():
    subjects = ["I","You","I","You","I","You","I","You","I","You","I","You","I","You","I","You","Your dog","Your cat","The dog","The cat","A dog","A cat","My dog","My cat",'The long cat', 'The long dog', 'The tall cat', 'The tall dog', 'The wide cat', 'The wide dog', 'The very long cat', 'The very long dog', 'The very wide cat', 'The very wide dog', 'The very tall cat', 'The very tall dog', 'A long cat', 'A long dog', 'A tall cat', 'A tall dog', 'A wide cat', 'A wide dog', 'A very long cat', 'A very long dog', 'A very wide cat', 'A very wide dog', 'A very tall cat', 'A very tall dog', 'My long cat', 'My long dog', 'My tall cat', 'My tall dog', 'My wide cat', 'My wide dog', 'My very long cat', 'My very long dog', 'My very wide cat', 'My very wide dog', 'My very tall cat', 'My very tall dog', 'Your long cat', 'Your long dog', 'Your tall cat', 'Your tall dog', 'Your wide cat', 'Your wide dog', 'Your very long cat', 'Your very long dog', 'Your very wide cat', 'Your very wide dog', 'Your very tall cat', 'Your very tall dog']
    objects = ["Me","You","Me","You","Me","You","Me","You","Me","You","Me","You","Me","You","Me","You","Your dog","Your cat","The dog","The cat","A dog","A cat","My dog","My cat", "Your tree","Your house","The tree","The house","A tree","A house","My tree","My house",'The long tree', 'The long house', 'The long cat', 'The long dog', 'The tall tree', 'The tall house', 'The tall cat', 'The tall dog', 'The wide tree', 'The wide house', 'The wide cat', 'The wide dog', 'The very long tree', 'The very long house', 'The very long cat', 'The very long dog', 'The very wide tree', 'The very wide house', 'The very wide cat', 'The very wide dog', 'The very tall tree', 'The very tall house', 'The very tall cat', 'The very tall dog', 'A long tree', 'A long house', 'A long cat', 'A long dog', 'A tall tree', 'A tall house', 'A tall cat', 'A tall dog', 'A wide tree', 'A wide house', 'A wide cat', 'A wide dog', 'A very long tree', 'A very long house', 'A very long cat', 'A very long dog', 'A very wide tree', 'A very wide house', 'A very wide cat', 'A very wide dog', 'A very tall tree', 'A very tall house', 'A very tall cat', 'A very tall dog', 'My long tree', 'My long house', 'My long cat', 'My long dog', 'My tall tree', 'My tall house', 'My tall cat', 'My tall dog', 'My wide tree', 'My wide house', 'My wide cat', 'My wide dog', 'My very long tree', 'My very long house', 'My very long cat', 'My very long dog', 'My very wide tree', 'My very wide house', 'My very wide cat', 'My very wide dog', 'My very tall tree', 'My very tall house', 'My very tall cat', 'My very tall dog', 'Your long tree', 'Your long house', 'Your long cat', 'Your long dog', 'Your tall tree', 'Your tall house', 'Your tall cat', 'Your tall dog', 'Your wide tree', 'Your wide house', 'Your wide cat', 'Your wide dog', 'Your very long tree', 'Your very long house', 'Your very long cat', 'Your very long dog', 'Your very wide tree', 'Your very wide house', 'Your very wide cat', 'Your very wide dog', 'Your very tall tree', 'Your very tall house', 'Your very tall cat', 'Your very tall dog']
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


