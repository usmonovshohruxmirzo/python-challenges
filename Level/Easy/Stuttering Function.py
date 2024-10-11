def stutter(word):
    first_two = word[:2]
    return "{}... {}... {}?".format(first_two, first_two, word)

print(stutter("so"))