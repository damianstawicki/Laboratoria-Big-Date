def decimal_to_binary(num):
    if num is 0:
        return "0"
    res = []
    while(num>=1):
        res.append(str(num%2))
        num = int(num / 2)
    return "".join(res)

print("Podaj liczbę:")
a_decimal = int(input())
a_binary = decimal_to_binary(a_decimal)
print(a_decimal, "w systemie dwójkowym to", a_binary)
