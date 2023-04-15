sentence = "This is a commo ninterview question"

# Cast to list
sentence_list = list(sentence)
# print(sentence_list)
for letter in sentence_list:
    if letter == " ":
        sentence_list.remove(" ")
# print(sentence_list)

counter_list = [[]]
char_list = []
counter = 0
aux_conter = 0
i = 0
j = 0
for character in sentence_list:
    counter = aux_conter
    counter = 0
    for charact in sentence_list:
        if charact == character and i != j:
            counter = counter + 1
            char_list.append(character)

        j = j + 1
    # print(character, counter)
    i = i + 1

counter_list.remove([])
print(counter_list)
