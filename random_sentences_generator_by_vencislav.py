names = ['John', 'Andrew', 'Michael', 'Christina', 'Ben', 'Tim', 'Nicole', 'Maria']
places = ['Sofia', 'Plovdiv', 'Burgas', 'Varna', 'Pleven', 'Veliko Turnovo']
verbs = ['eats', 'plays with', 'sees', 'enjoys', 'brings', 'holds']
nouns = ["stones", "a cake", "an apple", "a laptop", "a bike"]
adverbs = ['slowly', 'diligently', 'warmly', 'sadly', 'rapidly']
details = ['near the river', 'at home', 'in the park', 'by the sea', 'outside', 'in the forest']


import random


def get_random_word(words):
    return random.choice(words)


print('Hello , this is your first random sentence')
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}')
    input('Click [Enter] to generate a new one.')