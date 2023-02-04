nouns =  ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

import random

poem = []

noun1 = random.choice(nouns)
noun2 = random.choice(nouns)
noun3 = random.choice(nouns)

while noun1 == noun2:
    noun2 = random.choice(nouns)
while noun1 == noun3 or noun3 == noun2:
    noun3 = random.choice(nouns)


v1 = random.choice(verbs)
v2 = random.choice(verbs)
v3 = random.choice(verbs)

while v1 == v2:
    v2 = random.choice(verbs)
while v1 == v2 or v2 == v3:
    v3 = random.choice(verbs)


a1 = random.choice(verbs)
a2 = random.choice(verbs)
a3 = random.choice(verbs)

while a1 == a2:
    a2 = random.choice(verbs)
while a1 == a2 or a2 == a3:
    a3 = random.choice(verbs)

p1 = random.choice(prepositions)
p2 = random.choice(prepositions)

while p1 == p2:
    p2 = random.choice(prepositions)

adv1 = random.choice(adverbs)


poem = (
    f"{a1} {noun1}\n\n"
    f"{a1} {noun1} {v1} {p1} the {a2} {noun2}\n"
    f"{a1}, the {noun1} {v2}\n"
    f"the {noun2} {v3} {p2} a {a3} {noun3}"
)

print(poem)

# def noun_list(nouns):
#     random_list = []
#     i = 0
#     while i <= 2:
#         random_list.append(random.choice(nouns))
#         i += 1
#     return random_list
# poem.append(noun_list(nouns))

# def verb_list(verbs):
#     random_list = []
#     i = 0
#     while i <= 2:
#         random_list.append(random.choice(verbs))
#         i += 1
#     return random_list
# poem.append(verb_list(verbs))

# def adjective_list(adjectives):
#     random_list = []
#     i = 0
#     while i <= 2:
#         random_list.append(random.choice(adjectives))
#         i += 1
#     return random_list
# poem.append(adjective_list(adjectives))

# def preposition_list(prepositions):
#     random_list = []
#     i = 0
#     while i <= 2:
#         random_list.append(random.choice(prepositions))
#         i += 1
#     return random_list
# poem.append(preposition_list(prepositions))


# print(f"A/An {random.choice(rand_list(adjectives, 3))} {random.choice(rand_list(nouns, 3))}")
# print(f"A/An {random.choice(rand_list(adjectives, 3))} {random.choice(rand_list(nouns, 3))} {random.choice(rand_list(verbs, 3))} {random.choice(rand_list(prepositions, 3))} the {random.choice(rand_list(adjectives, 3))} {random.choice(rand_list(nouns, 3))}")
# print(f"{random.choice(rand_list(adverbs, 1))} {random.choice(rand_list(verbs, 3))}")