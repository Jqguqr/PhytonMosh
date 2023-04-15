from pprint import pprint

sentence = "This is a commo ninterview question"

char_frecuency = {}

for char in sentence:
    if char in char_frecuency:
        char_frecuency[char] += 1
    else:
        char_frecuency[char] = 1

# pprint(char_frecuency)

# pprint(char_frecuency.items())

char_frecuency_sorted = sorted(
    char_frecuency.items(),
    key=lambda kv: kv[1],
    reverse=True)

pprint(char_frecuency_sorted[0])
