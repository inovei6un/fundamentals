from string import punctuation

s = input().lower()


def is_palindrome(some_string):
    list_of_s = []
    for el in s:
        if el not in punctuation and el != ' ':
            list_of_s.append(el)

    some_string = ''.join(list_of_s)

    return some_string == some_string[::-1]


result = is_palindrome(s)

if result:
    print("Yes")
else:
    print('No')

'''
Zanimavam se s gluposti :)

A man, a plan, a canal: Panama
Bql hlqb
Neven
'''