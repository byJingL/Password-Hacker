# ------------------ bytes in String -------------- #
print(ord('a'))  # 97
print(chr(97))  # a
print(ord('7'))  # 55

characters = bytes([55, 255])
print(characters)

array = bytes([31, 32, 126, 127])
print(array)
print(bytes([126]))

# ------------------ Creating bytes -------------- #
transed_number = (2024).to_bytes(2, byteorder='little')
print(transed_number[0]) 



# ------------------ Lambda Function -------------- #
# Simple call
print((lambda x: x > 10)(3))
print((lambda x: 'odd' if x % 2 == 1 else 'even')(3))
# Return in another func
def multi_func(n):
    return lambda x: x * n

doubler = multi_func(2)
trippler = multi_func(3)

print('double func', doubler(6))
print('tripple func', trippler(6))


# ------------------ String changes -------------- #
message = "bonjour and welcome to Paris!"
swap_m = message.swapcase()
print('Oringin-', message)
print('Changed-', swap_m)

sentence = "London is the capital of Great Britain."
sentence = sentence.lower() # london is the capital of great britain.
sentence.upper() # 
sentence = sentence.replace("a", "x", 2)
sentence.capitalize() # sentence not be changed 

# ------------------ escape sequences -------------- #
print('deleted\b sign')
print('name\tJohn')
print('age\r23') # 23e, `ag` be overwrited


face = '\^_^/'
print(face)  # \^_^/
print(repr(face))
print('\\^_^/')
path = 'C:\\Users\\Public\\Desktop\\Temporary\\Newsletters'.lower()
print(path)
mine = 'That is \n mine'
print(repr(mine))
print(len(repr(mine)))

# ------------------ String split -------------- #
text = 'WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!'
words = text.split(' ')
for word in words:
    # Using startswith method
    if word.lower().startswith('www.') or word.startswith('http'):
        print(word)


# ------------------ **kwargs -------------- #
def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, 'is the capital of', key)

capital(Canada='Ottawa', China='China', UK='London')

def say_bye(**kwargs): # **names
    for name in kwargs:
        print("Au revoir,", name)
        print("See you on", kwargs[name]["next appointment"])
        print()
humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}
say_bye(**humans)

