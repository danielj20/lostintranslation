import random
import logging
import time
import datetime

all_vowels = ["a", "e", "i", "o", "u", "aa", "ae", "ai", "ao", "au", "ea", "ee", "ei", "eo", "eu", "ia", "ie", "io", "iu", "oa", "oe", "oi", "oo", "ou", "ua", "ue", "ui", "uo", "uu"]
vowels_num = random.randint(6, 12)
vowels_list = random.sample(all_vowels, vowels_num)
all_conso_blend = ['bl', 'br', 'kr', 'kl', 'ch', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'skr', 'spl', 'spr', 'str', 'thr']
conso_blend_num = random.randint(10, 15)
conso_blend_list = random.sample(all_conso_blend, conso_blend_num)
all_conso = ['b', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v']
conso_num = random.randint(5, 10)
conso_list = random.sample(all_conso, conso_num)


def makeWord():
    var = random.randint(1, 8)
    vowel = vowels_list
    conso_blend = conso_blend_list
    consoblend2 = random.choice(conso_blend)
    vowel2 = random.choice(vowel)
    vowel1 = random.choice(vowel)
    conso = conso_list
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


word_for_i = makeWord()

dictionary = {
    "the": makeWord(),
    "a": makeWord(),
    "I": word_for_i,
    "me": word_for_i,
    "you": makeWord(),
    "my": makeWord(),
    "your": makeWord(),
    "cat": makeWord(),
    "dog": makeWord(),
    "house": makeWord(),
    "tree": makeWord(),
    "very": makeWord(),
    "long": makeWord(),
    "tall": makeWord(),
    "wide": makeWord(),
    "be": makeWord(),
    "run": makeWord(),
    "want": makeWord(),
    "eat": makeWord(),
    "see": makeWord(),
    "on": makeWord(),
    "in": makeWord(),
    "front": makeWord(),
    "behind": makeWord()
}

sentence_structure = structure()
adj_order = adjective_order()


print(
    f"""
The: {dictionary["the"]}
A: {dictionary["a"]}
I: {dictionary["I"]}
You: {dictionary["you"]}
My: {dictionary["my"]}
Your: {dictionary["your"]}
Cat: {dictionary["cat"]}
Dog: {dictionary["dog"]}
House: {dictionary["house"]}
Tree: {dictionary["tree"]}
Very: {dictionary["very"]}
Long: {dictionary["long"]}
Tall: {dictionary["tall"]}
Wide: {dictionary["wide"]}
To be (is, am, are): {dictionary["be"]}
To run (runs, run): {dictionary["run"]}
To want (wants, want): {dictionary["want"]}
To eat (eats, eat): {dictionary["eat"]}
To see (sees, see): {dictionary["see"]}
On: {dictionary["on"]}
In: {dictionary["in"]}
In front of: {dictionary["front"]}
Behind: {dictionary["behind"]}


STRUCTURE: {sentence_structure}
ADJECTIVE ORDER: {adj_order}
"""
)


def makeSubject():
    articles = ["the", "a", "my", "your"]
    adjectives = ["long", "tall", "wide", "very long", "very tall", "very wide"]
    nouns = ["cat", "dog"]
    standalones = ["I", "you"]
    subject = ""
    raw_subject = ""
    var = random.randint(1, 3)
    if var == 1:
        subject = random.choice(standalones)
        raw_subject = subject
    elif var == 2:
        subject = random.choice(articles) + " " + random.choice(nouns)
        raw_subject = subject
    elif var == 3:
        if adj_order == "ADJ + NOUN":
            subject = random.choice(articles) + " " + random.choice(adjectives) + " " + random.choice(nouns)
            raw_subject = subject
        else:
            article = random.choice(articles)
            noun = random.choice(nouns)
            adj = random.choice(adjectives)
            subject = article + " " + noun + " " + adj
            raw_subject = article + " " + adj + " " + noun
    return {
        "subject": subject,
        "raw_subject": raw_subject
    }

def makeObject():
    articles = ["the", "a", "my", "your"]
    adjectives = ["long", "tall", "wide", "very long", "very tall", "very wide"]
    nouns = ["cat", "dog", "house", "tree"]
    standalones = ["me", "you"]
    subject = ""
    raw_subject = ""
    var = random.randint(1, 3)
    if var == 1:
        subject = random.choice(standalones)
        raw_subject = subject
    elif var == 2:
        subject = random.choice(articles) + " " + random.choice(nouns)
        raw_subject = subject
    elif var == 3:
        if adj_order == "ADJ + NOUN":
            subject = random.choice(articles) + " " + random.choice(adjectives) + " " + random.choice(nouns)
            raw_subject = subject
        else:
            article = random.choice(articles)
            noun = random.choice(nouns)
            adj = random.choice(adjectives)
            subject = article + " " + noun + " " + adj
            raw_subject = article + " " + adj + " " + noun
    return {
        "object": subject,
        "raw_object": raw_subject
    }



def makePrompt():
    verbs = ["see","eat","want","want see","want eat", "be", "want be"]
    raw_verbs = ["(to see)","(to eat)","(to want)","(to want to see)","(to want to eat)", "(to be)", "(to want to be)"]
    tr_verbs = ["see","eat","want see","want eat", "run", "want run"]
    raw_tr_verbs = ["(to see)","(to eat)","(to want to see)","(to want to eat)","(to run)", "(to want to run)"]
    tr_verbs_plus_be = ["see","eat","want see","want eat", "run", "want run","be","want be"]
    raw_tr_verbs_plus_be = ["(to see)","(to eat)","(to want to see)","(to want to eat)","(to run)", "(to want to run)","(to be)", "(to want to be)"]
    prepositions = ["front","behind","in","on"]
    raw_prepositions = ["in front of", "behind", "in", "on"]


    sentence_type = random.randint(1, 3)
    sentence = ""
    sentence_words = []
    pure_sentence = ""
    translation = ""
    translation_words = []


    if sentence_type == 1:
        # subject verb
        sub = makeSubject()
        verb_index = random.randint(0, len(tr_verbs) - 1)
        verb = tr_verbs[verb_index]
        pure_verb = raw_tr_verbs[verb_index]
        if sentence_structure == "VSO" or sentence_structure == "VOS":

            sentence = verb + " " + sub["subject"]
        else:
            sentence = sub["subject"] + " " + verb
        pure_sentence = sub["raw_subject"] + " " + pure_verb
    elif sentence_type == 2:  
        # subject verb object
        sub = makeSubject()
        obj = makeObject()
        verb_index = random.randint(0, len(verbs) - 1)
        verb = verbs[verb_index]
        pure_verb = raw_verbs[verb_index]
        if sentence_structure == "SVO":
            sentence = sub["subject"] + " " + verb + " " + obj["object"]
        elif sentence_structure == "SOV":
            sentence = sub["subject"] + " " + obj["object"] + " " + verb
        elif sentence_structure == "OSV":
            sentence = obj["object"] + " " + sub["subject"] + " " + verb
        elif sentence_structure == "OVS":
            sentence = obj["object"] + " " + verb + " " + sub["subject"]
        elif sentence_structure == "VSO":
            sentence = verb + " " + sub["subject"] + " " + obj["object"]
        elif sentence_structure == "VOS":
            sentence = verb + " " + obj["object"] + " " + sub["subject"]
        pure_sentence = sub["raw_subject"] + " " + pure_verb + " " + obj["raw_object"]
    elif sentence_type == 3:
        # subject verb preposition
        sub = makeSubject()
        obj = makeObject()
        verb_index = random.randint(0, len(tr_verbs_plus_be) - 1)
        verb = tr_verbs_plus_be[verb_index]
        pure_verb = raw_tr_verbs_plus_be[verb_index]
        prep_index = random.randint(0, len(prepositions) - 1)
        prep = prepositions[prep_index]
        pure_prep = raw_prepositions[prep_index]
        if sentence_structure == "SVO":
            sentence = sub["subject"] + " " + verb + " " + prep + " " + obj["object"]
        elif sentence_structure == "SOV":
            sentence = sub["subject"] + " " + prep + " " + obj["object"] + " " + verb
        elif sentence_structure == "OSV":
            sentence = prep + " " + obj["object"] + " " + sub["subject"] + " " + verb
        elif sentence_structure == "OVS":
            sentence = prep + " " + obj["object"] + " " + verb + " " + sub["subject"]
        elif sentence_structure == "VSO":
            sentence = verb + " " + sub["subject"] + " " + prep + " " + obj["object"]
        elif sentence_structure == "VOS":
            sentence = verb + " " + prep + " " + obj["object"] + " " + sub["subject"]
        pure_sentence = sub["raw_subject"] + " " + pure_verb + " " + pure_prep + " " + obj["raw_object"]

    sentence_words = sentence.split(" ")
    for i in range(len(sentence_words)):
        translation_words.append(dictionary[sentence_words[i]])
    translation = " ".join(translation_words)

    pure_sentence = pure_sentence.capitalize() + "."
    translation = translation.capitalize() + "."
    
    return {
        "sentence": pure_sentence,
        "translation": translation
    }


while True:
    gen_sentence = makePrompt()
    print(f"{datetime.datetime.fromtimestamp(time.time())}\nSentence: {gen_sentence['sentence']}\nTranslation: {gen_sentence['translation']}")
    input("")
