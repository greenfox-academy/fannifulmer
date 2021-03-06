# Adds a and b, returns as result
def add(a, b):
    return a +b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    highest_number = 0
    for i in (a, b, c):
        while i > highest_number:
            highest_number = i
    return highest_number


# Returns the median value of a list given as param
def median(pool):
    pool.sort()
    if len(pool) % 2 != 0:
        return pool[len(pool)//2]
    elif len(pool) % 2 ==0:
        return (pool[(len(pool)//2)] + pool[(len(pool) // 2) -1]) //2

#Returns true if the param is a vovel
def is_vovel(char):
    return char.lower() in 'aeiouéáőűöüóí'

#Create a method that translates hungarian into the teve language
def translate(hungarian):
    word = 'hungarian'
    teve = []
    for char in word:
        if is_vovel(char):
            teve.append(char+'v'+char)
        else:
            teve.append(char)
    return ''.join(teve)
