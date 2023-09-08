import random


def get_random_name():
    global names
    return random.choice(names)


def get_random_place():
    global places
    return random.choice(places)


def get_random_verb():
    global verbs
    return random.choice(verbs)


def get_random_noun():
    global nouns
    return random.choice(nouns)


def get_random_adverb():
    global adverbs
    return random.choice(adverbs)


def get_random_detail():
    global details
    return random.choice(details)


names = ['Anton', 'Petar', 'Dian', 'Teodor', 'Junian', 'Kiril']
places = ['Sofia', 'Stara Zagora', 'Plovdiv', 'Galabovo', 'Varna']
verbs = ['coding on', 'eats', 'holds', 'plays with', 'brings']
nouns = ['laptop', 'stones', 'bikes', 'cake']
adverbs = ['slowly', 'sadly', 'rapidly', 'warmly']
details = ['near the sea', 'at home', 'at work', 'in the park']

input('Hello! This will be your first random sentence:')

while True:
    random_name = get_random_name()
    random_place = get_random_place()
    random_verb = get_random_verb()
    random_noun = get_random_noun()
    random_adverb = get_random_adverb()
    random_detail = get_random_detail()
    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}')
    input('Hit [Enter] to generate a new one!')
