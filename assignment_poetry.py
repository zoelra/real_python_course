import random

nouns = ("fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert",
         "gorilla")
verbs = ("kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles")
adjectives = ("furry", "balding", "incredulous", "fragrant", "exuberant", "glistening")
prepositions = ("against", "after", "into", "beneath", "upon", "for", "in", "like", "over",
                "within")
adverbs = ("curiously", "extravagantly", "tantalizingly", "furiously", "sensuously")


def make_poem():
    adj1 = random.choice(adjectives)
    noun1 = random.choice(nouns)
    adj2 = random.choice(adjectives)
    verb1 = random.choice(verbs)
    prep1 = random.choice(prepositions)
    noun2 = random.choice(nouns)
    adverb1 = random.choice(adverbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    prep2 = random.choice(prepositions)
    adj3 = random.choice(adjectives)
    noun3 = random.choice(nouns)
    my_first_line = "A/An {} {}".format(adj1, noun1)
    my_second_line = "A/An {} {} {} {} the {} {}".format(adj1, noun1, verb1, prep1, adj2, noun2)
    my_third_line = "{}, the {} {}".format(adverb1, noun1, verb2)
    my_fourth_line = "the {} {} {} a {} {}".format(noun2, verb3, prep2, adj3, noun3)
    print(my_first_line)
    print(my_second_line)
    print(my_third_line)
    print(my_fourth_line)


make_poem()
