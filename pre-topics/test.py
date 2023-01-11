import itertools

test = '123qwerty'
# [['1', '1'], ['2', '2'], ['3', '3'], ['Q', 'q'], ['W', 'w'], ['E', 'e'], ['R', 'r'], ['T', 't'], ['Y', 'y']]
possible_letters = [[letter.upper(), letter.lower()] for letter in test]
print(possible_letters)
# <generator object <genexpr> at 0x1008b9ee0>
possible_letters = ([letter.upper(), letter.lower()] for letter in test)

pool = itertools.product(*possible_letters)
for item in pool:
    print(item)


def find_password():
    with open('./passwords.txt', 'r') as file:
        data = file.read().splitlines()
        for item in data:
            item_pool = map(lambda x: ''.join(x),
                            itertools.product(*([letter.lower(), letter.upper()] if letter.isalpha() else letter for letter in item)))
            for s in item_pool:
                yield s

password_generator = find_password()
print('====== Begin ======')
for password in password_generator:
    if password == 'passWord':
        print('Yeah')
        break
    else:
        print(password)

print('6u666'.isnumeric())