
def plural_fsm(noun):
    # Finite-state machine for plural formation

    if noun.endswith(("s", "sh", "ch", "x", "z")):
        plural = noun + "es"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        plural = noun[:-1] + "ies"
    else:
        plural = noun + "s"

    return plural


words = ["cat", "bus", "box", "baby", "book"]

print("Singular\tPlural")
for word in words:
    print(word, "\t\t", plural_fsm(word))
