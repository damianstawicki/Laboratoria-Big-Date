import random
import string

def count(s):
    char_sum = 0
    for char in s:
        char_sum += ord(char)
    return char_sum

def make_file():
    file = open("mutant.txt", "a+")
    for _ in range(300):
        random_string_list = [random.choice(string.ascii_uppercase) for _ in range(50)]
        s = "".join(random_string_list)
        file.write(s)
        file.write("\n")
    file.close()
    
def count_in_file():
    file = open("mutant.txt", "r")
    file_lines = file.readlines()
    for line in file_lines:
        print(line, count(line))
        
make_file()
count_in_file()



