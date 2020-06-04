print("Podaj słowo: ")
word = input()
word_as_list = list(word)

for i in range(len(word_as_list)):
    as_number = ord(word_as_list[i])+1
    as_char = chr(as_number)
    word_as_list[i] = as_char
    
word_rotated = "".join(word_as_list)
print(word_rotated)
