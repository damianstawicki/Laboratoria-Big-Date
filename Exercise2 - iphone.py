iphone = 3000
print('Ile masz pieniędzy?')

money = int(input())
print('Aktualna cena iPhoneX = ', 3000)
if iphone > money:
    print('Brakuje Ci ', 3000 - money, 'aby nabyć iPhoneX')
else:
    print('Stać Cię na ', money / 3000, 'iPhoneX')
