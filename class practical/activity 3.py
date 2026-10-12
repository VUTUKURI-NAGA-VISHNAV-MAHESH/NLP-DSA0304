
words = ["playing", "played", "studies", "running", "helping"]

print("Word\t\tRoot Word")

for word in words:
    if word.endswith("ing"):
        root = word[:-3]
    elif word.endswith("ied"):
        root = word[:-3] + "y"
    elif word.endswith("ed"):
        root = word[:-2]
    elif word.endswith("s"):
        root = word[:-1]
    else:
        root = word

    print(word, "\t\t", root)
