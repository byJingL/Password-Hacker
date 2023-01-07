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

# ------------------ Socket module -------------- #
# import socket

# with socket.socket() as client_socket:
#     hostname = '127.0.0.1'
#     port = 5000
#     address = (hostname, port)

#     client_socket.connect(address)

#     data = 'Wake up, Jane'
#     data = data.encode()

#     client_socket.send(data)

#     response = client_socket.recv(1024)

#     response = response.decode()
#     print(response)

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

# ------------------ Generator -------------- #
# Generator expression
my_list = [1, 2, 3, 4]
my_generator = (n ** 2 for n in my_list)
for power in my_generator:
    print(power)

# Genetator function
def multipuls(a, n):
    for i in range(n):
        yield a * i

mul_generator = multipuls(20, 20)
print(mul_generator) # <generator object multipuls at 0x104631f50>

print(next(mul_generator)) # 0 Just print one for once call
print(next(mul_generator)) # 20
for mul in mul_generator:
    if mul < 100:
        print(mul, 'Less than 100')

# ------------------ Iterator -------------- #
first_names = ['John', 'Anna', 'Tom']
last_names = ['Smith', 'Williams', 'Davis']
names = zip(first_names, last_names)
for first, last in names:
    print(first, last)

day_list = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

for n, month in enumerate(day_list):
    print(n + 1, month)

# ------------------ Map and filter -------------- #
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = filter(lambda x: x % 2, numbers)

print(list(odd_numbers))

# ------------------ Itertools module -------------- #
import itertools

# Example 1
main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]
desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]
drinks = ['cola', 'wine']
price_drinks = [3, 10]

all_foods = itertools.product(main_courses, desserts, drinks)
all_price = itertools.product(price_main_courses, price_desserts, price_drinks)
combination = zip(all_foods, all_price)
for food, price in combination:
    print(*food, sum(price))

# Example 2
flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
for i in range(1, len(flower_names)+1):
    bouquets = itertools.combinations(flower_names, i)
    for bouquet in bouquets:
        print(bouquet)

# Example 3
char = 'abc'
passwords = itertools.product(char, repeat=2)
for password in passwords:
    print(*password)

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

# ------------------ JSON Module -------------- #
import json
movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
  ]
}

# Encoding to JSON
with open('pre-tpics/data.json', 'w') as data_file:
    json.dump(movie_dict, data_file, indent=4)
    
# Decoding JSON
with open('pre-tpics/data.json', 'r') as data_file:
    movie_data = json.load(data_file)
    print(type(movie_data))
    print(movie_data == movie_dict)

# Not with file
json_str = json.dumps(movie_dict, indent=4)
print(type(json_str))

another_data = json.loads(json_str)
print(type(another_data))

# ------------------ Time Module -------------- #
import time

# Get current time

# return struct time object
gm_time = time.gmtime()
print(gm_time)
# time.struct_time(tm_year=2023, tm_mon=1, tm_mday=6, tm_hour=18, tm_min=47, tm_sec=28, tm_wday=4, tm_yday=6, tm_isdst=0)

asc_time = time.asctime()
print(asc_time) # Fri Jan  6 18:49:55 2023

print(time.time()) # 1673124689.5367749
time3 = time.ctime(time.time()) # same format as asctime()
print(time3)

str_time =  time.strftime("%a, %d, %b %H:%M:%S %Y", time.localtime())
print(str_time)
str_time2 = time.strftime("%a, %d, %b %H:%M:%S %Y", time.gmtime())
print(str_time2)

# time measurement
time.sleep(5)
print('wait for 5s')

# time difference
current_time = time.time()
time.sleep(5)
new_current_time = time.time()
time_passed = new_current_time - current_time
print('Time passed', time_passed)

start = time.perf_counter()
time.sleep(6)
end = time.perf_counter()
total_time = end - start
print(f"Time passed {total_time} seconds.")


