# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).


line = 6
def wierdbunnyearcal(line):
    if line == 0:
        return line
    elif line % 2 == 0:
        return 3 + wierdbunnyearcal(line-1)
    else:
        return 2 + wierdbunnyearcal(line-1)

print((wierdbunnyearcal(line)))