# Create a method that decrypts the texts/duplicated_chars.txt

my_file = open("duplicated-chars.txt", "r")
my_file = my_file.read()

def decrypt(my_file):
    text = ""
    for i in range(0, len(my_file), 2):
        text += my_file[i]
    return text
print(decrypt(my_file))
