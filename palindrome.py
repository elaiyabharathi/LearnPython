print('enter word or  number')
str = input()
revstr = str[::-1]
print(revstr)
if str == revstr:
    print('palindrome')
else:
    print('not palindrome')
