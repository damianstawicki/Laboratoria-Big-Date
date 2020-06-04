base = {":)": "😃", ":(": "😞"}

def print_pretty_emoji(i):
    print(base[i])

print("Podaj emotkę: ")
x = input()
print_pretty_emoji(x)
