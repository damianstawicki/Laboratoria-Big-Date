def check_if_is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

print("Podaj słowo do sprawdzenia: ")
word = input()
is_palindrome = check_if_is_palindrome(word)

if is_palindrome:
    print(word, "to palindrom")
else:
    print(word, "to nie palindrom")




