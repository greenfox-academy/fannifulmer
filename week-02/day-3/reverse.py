# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]
def reverser(aj):
    new_list = []
    for i in range(len(aj)-1, -1, -1):
        new_list.append(aj[i])
    return new_list
    
print(reverser(aj))
# aj.reverse()
# print(aj)
