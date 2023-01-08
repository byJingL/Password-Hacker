# Password Hacker

## Main Skill
socket module, itertools module, JSON, time module, generator and iterator
## Theory
1. Find out the correct username using [logins.txt](/logins.txt).
   - If login username is wrong, the response will be 'Wrong login!'.
   - If login username is correct, the response will be 'Wrong password!'.
2. Find out the correct password through brute force.
   - The passwords only contains numbers and alphabets(lowercase and uppercase).
   - The characters of the password will be found one by one.
   - If the character is correct, there will be a delay in the server response, which means the execution time will be much longer. Therefore, if a delay is detected, a correct character is found.

## How to use
- Download [hack.py](/hack.py) with [logins.txt](/logins.txt).
- Run [hack.py](/hack.py) with arguments of which server to connect (IP address and port). eg.
    ```
    python3 hack.py localhost 9090
    ```

## Two ways to find the password
### Brute Force
Define characters available
```
NUM = '0123456789'
L_CHAR = 'abcdefghijklmnopqrstuvwxyz'
U_CHAR = L_CHAR.upper()
```
Try all possibles cases
```
CHAR = NUM + L_CHAR + U_CHAR

def brute_force_find_password():
    for i in range(1, len(CHAR)+1):
        pool = itertools.product(CHAR, repeat=i)
        for item in pool:
            yield ''.join(item)
```
The outer loop tests all possible password lengths. For a specific password length, the inner loop iterates through each combination using `itertools.product()`. The combination is converted from tuple to string for testing.
### Dictionary-Based Brute Force
A dictionary with the most typical passwords provided in [password.txt](/passwords.txt) is used.
All possible combinations of upper and lower case for each letter for all words of the password dictionary will be checked one by one.
```
def dict_based_find_password():
    with open('passwords.txt', 'r') as file:
        data = file.read().splitlines()
        for password in data:
            possible_letters = [[letter.lower(), letter.upper()] for letter in password]
            # or
            # possible_letters = ([letter.lower(), letter.upper()] for letter in password)

            pw_pool = itertools.product(*possible_letters)
            for s in pw_pool:
                yield ''.join(s)
```
How to understand the iterator `pw_pool` can create all the different combinations of uppercase and lowercase of a word? 
- Take `12qwerty` as an example.
- `[[letter.lower(), letter.upper()] for letter in password]` will return a list `[['1', '1'], ['2', '2'], ['Q', 'q'], ['W', 'w'], ['E', 'e'], ['R', 'r'], ['T', 't'], ['Y', 'y']]`
- Also can use `([letter.lower(), letter.upper()] for letter in password)` to return a tuple.
- By placing a `*` before list/tuple to unpacking, the contents in the list/tuple will be returned without "[]" or "()". It means pass every single item in list/tuple as iterables to `itertools.product()`
- Thus, `itertools.product(['1', '1'], ['2', '2'], ['Q', 'q'], ['W', 'w'], ['E', 'e'], ['R', 'r'], ['T', 't'], ['Y', 'y']) ` will find all the possible combinations.

## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.
