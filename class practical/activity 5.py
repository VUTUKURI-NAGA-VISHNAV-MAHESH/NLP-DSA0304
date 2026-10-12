
def porter_stem(word):
    if word.endswith("ing") and len(word) > 4:
        word = word[:-3]
    elif word.endswith("ied"):
        word = word[:-3] + "i"
    elif word.endswith("ed") and len(word) > 3:
        word = word[:-2]
    elif word.endswith("es") and len(word) > 3:
        word = word[:-2]
    elif word.endswith("s") and len(word) > 2:
        word = word[:-1]

    return word


words = ["playing", "played", "plays", "running", "studies"]

print("Original Word\tStemmed Word")

for word in words:
    print(word, "\t\t", porter_stem(word))
