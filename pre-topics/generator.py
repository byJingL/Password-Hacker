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

# ------------------ yield from -------------- #
def generator1():
    for x in range(100):
        yield x

def generator2():
    for y in range(100, 200):
        yield y

def generator():
    yield from generator1()
    yield from generator2()

nums = generator()
print(next(nums))

def one_more_generator(word):
    yield from word
    print(word)

word_generator = one_more_generator('Amy')
for item in word_generator:
    print(item)
