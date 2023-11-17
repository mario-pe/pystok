# source https://www.youtube.com/watch?v=rp1QR3eGI1k
from urllib.error import HTTPError

import requests as requests
from pip._internal.utils.misc import enum, logger


#### 1  any
def use_any_instead_of_loop():
    numbers = [-1, -2, -4, 0, 3, 7]
    has_positives = False

    for n in numbers:
        if n > 0:
            has_positives = True
            break

    has_positives = any(n > 0 for n in numbers)

    return has_positives


#### 2 Replace if statement with if expression
condition = True

if condition:
    x = 1
else:
    x = 2

x = 1 if condition else 2


#### 3 Add guard clause
class Hat:
    pass


def should_i_wear_this_hat(self, hat):
    if isinstance(hat, Hat):
        jacket_color = self.get_jacket_color()
        current_weather = self.get_current_weather()
        is_stylish = self.is_stylish(hat, jacket_color)
        if current_weather.is_raining():
            print("Oh no, it's raining! I can't wear this hat!")
            return True
        else:
            print("Nice")
            return is_stylish
    else:
        print("This is not a hat!")
        return False


def should_i_wear_this_hat(self, hat):
    if not isinstance(hat, Hat):
        return False
    jacket_color = self.get_jacket_color()
    current_weather = self.get_current_weather()
    is_stylish = self.is_stylish(hat, jacket_color)
    if current_weather.is_raining():
        print("Oh no, it's raining! I can't wear this hat!")
        return True
    else:
        print("Nice")
        return is_stylish


#### 4 Move assignmernts closer to their usage
def should_i_wear_this_hat(self, hat):
    if not isinstance(hat, Hat):
        return False
    jacket_color = self.get_jacket_color()
    current_weather = self.get_current_weather()
    if current_weather.is_raining():
        print("Oh no, it's raining! I can't wear this hat!")
        return True
    else:
        print("Nice")
        return self.is_stylish(hat, jacket_color)


# https://www.youtube.com/watch?v=KTIl1MugsSY


#### 5 isnumeric
example = []
data = "1"


def loop_over_1():
    for i in range(0, 10):
        try:
            data = int(data)
        except:
            pass
    example.append(data)


def loop_over_2():
    for i in range(0, 10):
        data = int(data) if data.isnumeric() else data
        example.append(data)


#### 6 Structural Pattern Matching
def lets_if(input: str):
    splited_input = input.split()
    if splited_input[0] == "load" and len(splited_input) == 2 and splited_input[1]:
        print(f"Loading file: {splited_input[1]}")
    elif splited_input[0] == "save" and len(splited_input) == 2 and splited_input[1]:
        print(f"Saving file: {splited_input[1]}")
    elif splited_input[0] in ["quit", "exit", "bye"]:
        print("Quitting")
    else:
        print(f"Unknown input: {splited_input[0]}")


def lets_match(input: str):
    match input.split():
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["save", filename]:
            print(f"Saving file: {filename}")
        case ["quit" | "exit" | "bye"]:
            print("Quitting")
        case other:
            print(f"Unknown input: {other}")


#### 7 Python dict setdefault -> file

plumbers: dict = {"mario": "present", "luigi": "present"}
print(f"get        plumber mario  {plumbers.get('mario', 'not present')}")
print(f"setdefault plumber mario  {plumbers.setdefault('mario', 'not present')}")
print(f"all        plumbers  {plumbers}")
# get        plumber mario  present
# setdefault plumber mario  present
# all        plumbers  {'mario': 'present', 'luigi': 'present'}


print(f"get        plumber kazik  {plumbers.get('kazik', 'not present')}")
print(f"all        plumbers  {plumbers}")
print(f"setdefault plumber kazik  {plumbers.setdefault('kazik', 'not present')}")
print(f"setdefault plumbers  {plumbers}")
# get        plumber kazik  not present
# all        plumbers  {'mario': 'present', 'luigi': 'present'}
# setdefault plumber kazik  not present
# setdefault plumbers  {'mario': 'present', 'luigi': 'present', 'kazik': 'not present'}



#### 8  defaultdict

from collections import defaultdict

def def_value():
    return "not present"

plumbers = defaultdict(def_value)
plumbers["mario"] = "present"
plumbers["luigi"] = "present"

print(f"defaultdict plumber mario  {plumbers['mario']}")
print(f"defaultdict plumber luigi  {plumbers['luigi']}")
print(f"defaultdict plumber kazik  {plumbers['kazik']}")
print(f"defaultdict plumbers        {plumbers}")

# defaultdict plumber mario  present
# defaultdict plumber luigi  present
# defaultdict plumber kazik  not present
# defaultdict plumbers       {'mario': 'present', 'luigi': 'present', 'kazik': 'not present'}   defaultdict(<function def_value at 0x0000024BF37104A0>


#### 9 one line if-else

score = 57
if score > 90:
    grade = "A*"
elif score > 50:
    grade = "pass"
else:
    grade = "fail"

score = 57
grade = "A*" if score > 90 else "pass" if score > 50 else "fail"

#### 10 dict play
cities_us = {"New York City": "US", "Los Angeles": "US"}
cities_uk = {"London": "UK", "Birmingham": "UK"}
cities_jp = {"Tokyo": "JP"}

cities = {}

for city_dict in [
    cities_us,
    cities_uk,
    cities_jp,
]:  # kawał dobrej, nikomu niepotrzebnej roboty
    for city, country in city_dict.items():
        cities[city] = country

print(cities)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK', 'Tokyo': 'JP'}

cities = cities_us | cities_uk | cities_jp

print(cities)
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK', 'Tokyo': 'JP'}

#### 11
cities = {**cities_us, **cities_uk, **cities_jp}
print({**cities_us, **cities_uk, **cities_jp})
# {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK', 'Tokyo': 'JP'}


#### 12  contex manager with requests

s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

import requests

with requests.Session() as session:
    session.request(method="get", url='https://httpbin.org/cookies')


#### 13   Itertools
# w itertools znajduje sie wiecej metod do iterowania po kolekcjach  np permutations, combinations
# tylko o nich wspominam bo mają zastosowania w konkretnych przypadkach i ten kto potrzebuje na pewno je znajdzie

from itertools import groupby

for key, group in groupby("YAaANNGGG"):
    lg = list(group)
    print(key, len(lg), lg)

# Y 1 ['Y']
# A 1 ['A']
# a 1 ['a']
# A 1 ['A']
# N 2 ['N', 'N']
# G 3 ['G', 'G', 'G']

#### 14   Itertools.chain
from itertools import chain

x = [0, 1, 2, 3, 4]
y = tuple(("a", "b", "c"))
z = set((9, 7))

w = x + y

# Traceback (most recent call last):
#   File "C:\Users\mariusz.perkowski\warsztat\PyStok\warsztat.py", line 7, in <module>
#     w = x + y
#         ~~^~~
# TypeError: can only concatenate list (not "tuple") to list


w = x + list(y) + list(z)
# [0, 1, 2, 3, 4, 'a', 'b', 'c', 9, 7]

# gdyby bog chciał inaczej to inaczej swiat by stwożył,
# no i chyba chciał inaczej bo natchnął kogoś aby stworzył metode chain z itertools


print(list(chain(x, y, z)))

# [0, 1, 2, 3, 4, 'a', 'b', 'c', 9, 7]


#### 15 flat the nested list
from itertools import chain

x = [0, 1, 2, 3, 4]
y = tuple(("a", "b", "c"))
z = [x, y]

print(list(chain(z)))

# [[0, 1, 2, 3, 4], ('a', 'b', 'c')]

print(list(chain.from_iterable(z)))
# [0, 1, 2, 3, 4, 'a', 'b', 'c']


#### 16   zip
x = [0, 1, 2, 3, 4]  # elementy 3,4 nie sa brane pod uwage
y = tuple(("a", "b", "c"))
print(list(zip(x, y)))

# [(0, 'a'), (1, 'b'), (2, 'c')]


from itertools import zip_longest  # przejdzie po wszystkich elementach i doda None

print(list(zip_longest(x, y)))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, None), (4, None)]

print(
    list(zip_longest(x, y, fillvalue="*"))
)  # przejdzie po wszystkich elementach i doda default value
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, '*'), (4, '*')]


#### 17
def func_to_get_author():
    return "Adam Mickiewicz"


author = func_to_get_author()
if author:
    print(f"The author is {author}.")


if author := func_to_get_author():
    print(f"The author is {author}.")

#### 18
nums = [1, 2, 3, 4, 5]

def func(x):
    return x * 2


results = [(x, y) for x in nums if (y := func(x)) > 4]
print(results)
# [(3, 6), (4, 8), (5, 10)]

############# colledctions

#### 19

from collections import Counter

sentence = "This is a simple sentence for demonstration purposes. With a few repetitions in this sentence"


count_letters = Counter(sentence)
count_words = Counter(sentence.split())
most_common_words = Counter(sentence.split()).most_common(3)

print(count_letters)
print(count_words)
print(most_common_words)

# Counter({' ': 14, 'e': 12, 's': 10, 'i': 9, 'n': 8, 't': 8, 'o': 5, 'p': 4, 'r': 4, 'h': 3, 'a': 3, 'm': 2, 'c': 2, 'f': 2, 'T': 1, 'l': 1, 'd': 1, 'u': 1, '.': 1, 'W': 1, 'w': 1})
# Counter({'a': 2, 'sentence': 2, 'This': 1, 'is': 1, 'simple': 1, 'for': 1, 'demonstration': 1, 'purposes.': 1, 'With': 1, 'few': 1, 'repetitions': 1, 'in': 1, 'this': 1})
# [('a', 2), ('sentence', 2), ('This', 1)]


#### 20 namedtuple

point = (2, 4)
point
# (2, 4)

point[0]
# 2

point[1]
# 1

point[0] = 3
# Traceback (most recent call last):
#     point[0] = 3
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

from collections import namedtuple

Point = namedtuple("Point", "x y")  # x, y  nazwy atrybutów

issubclass(Point, tuple)
# True
point = Point(2, 4)
point
# Point(x=2, y=4)
point.x
# 2
point.y
# 4
point[0]
# 2
point[1]
# 4
point.x = 100
# Traceback (most recent call last):
#     john.name = "Frank"
#     ^^^^^^^^^
# AttributeError: can't set attribute

from collections import namedtuple

Person = namedtuple("Person", "name children")  # name children nazwy atrybutów
john = Person("John Doe", ["Timmy", "Jimmy"])
john
# Person(name='John Doe', children=['Timmy', 'Jimmy'])
id(john.children)
# 139695902374144

john.children.append("Tina")
john
# Person(name='John Doe', children=['Timmy', 'Jimmy', 'Tina'])
id(
    john.children
)  # zmieniamy obiekt który jest mutowalny ale to nie znaczy że zmienilismy tuple referencja do tuple jest ta sama
# 139695902374144

john.name = "Frank"
# Traceback (most recent call last):
#     john.name = "Frank"
#     ^^^^^^^^^
# AttributeError: can't set attribute


#### 21 lru cache memoization  lru ->  Least Recently Used
# functools.lru_cache(maxsize=128, typed=False)


def get_a_lot_of_data(query_params: dict) -> dict:
    return query_params


def complecated_alghorytm_replace_a_b(
    x: str,
):  # przykład z netstation bloczek z newsami województwa
    return x.replace("a", "b")


from functools import lru_cache


def endpoint_slow(query_params):
    very_complicated_query = get_a_lot_of_data(query_params)
    return [complecated_alghorytm_replace_a_b(x) for x in very_complicated_query]


@lru_cache()  # funkcja nie zsotanie wywołana jesli argumenty funkcji zostały użyte
def endpoint_fast(query_params):
    very_complicated_query = get_a_lot_of_data(query_params)
    return [complecated_alghorytm_replace_a_b(x) for x in very_complicated_query]


#### 22 use enums
from enum import Enum


class Employee:
    def __init__(self, name: str, surname: str, role: str):
        self.name = name
        self.surname = surname
        self.role = role


john = Employee("John", "Doe", "manager")
kris = Employee("Kris", "Foo", "developer")
tom = Employee("Tom", "Barr", "tester")

print(john.role)
print(kris.role)
print(tom.role)

# manager
# developer
# tester


class Role(Enum):
    MANAGER = "manager"
    DEVELOPER = "developer"
    TESTER = "tester"


def __init__(self, name: str, surname: str, role: str):
    self.name = name
    self.surname = surname
    self.role = role


john = Employee("John", "Doe", Role.MANAGER.value)
kris = Employee("Kris", "Foo", Role.DEVELOPER.value)
tom = Employee("Tom", "Barr", Role.TESTER.value)

print(john.role)
print(kris.role)
print(tom.role)

# manager
# developer
# tester


#### 23 decorator timer
# w trakcie inwestygacji  rozwiązania warto sprawdzić jak czasowo wydajne jest rozwiązanie,
# ja zawsze lubie mieć dekorator który szybko mogę użyć i sprawdzić które rozwiązanie jest bardziej wydajne

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)


# Usage
slow_function()

#### 24 Slice

# slice(start, stop, step)
nums = [1, 2, 3, 4]

# reversed list
print(nums[::-1])

from itertools import islice


@timer
def slice():
    ite = range(1000)[1:]
    for item in ite:
        print(item)


@timer
def islice():
    ite = islice(range(1000), 1, None, 1)
    for item in ite:
        print(item)


# slice took 0.010000228881835938 seconds to execute.
# islice took 0.0050008296966552734 seconds to execute.


#### 25
def data_fetch_from_my_api(params):
    if "date" not in params.keys():
        raise KeyError("Params are required")
    return requests.get("https://my-api.com").raise_for_status()


# BAD
try:
    data_fetch_from_my_api()
except Exception as e:
    logger(e)


# BETTER
try:
    data_fetch_from_my_api()
except (HTTPError, KeyError) as e:
    logger(e)

# BEST
try:
    data_fetch_from_my_api()
except HTTPError as e:
    print("HTTPError api leży i kwiczy")
    logger(e)
except KeyError as e:
    print("KeyError no weś się ogarnij")
    logger(e)


#### 26 Raise custom exceptions
class ParamValidationException(Exception):
    pass


def data_fetch_from_my_api(params):
    if "date" not in params.keys():
        raise ParamValidationException("Params are required")
    return requests.get("https://my-api.com").raise_for_status()


try:
    data_fetch_from_my_api()
except HTTPError as e:
    print("HTTPError api leży i kwiczy")
    logger(e)
except ParamValidationException as e:
    print("ParamValidationException  no weś się ogarnij")
    logger(e)


#### 27 nie przesadzajcie z list comprehension
result = [value for value in nums if value % 2 == 0]

result = (
    (x, y, z)
    for x in range(5)
    for y in range(5)
    if x != y
    for z in range(5)
    if y != z
)


#### 28

import contextlib
import os

try:
    os.mkdir("frivolous_directory")
except FileExistsError:
    pass

with contextlib.suppress(FileExistsError):    # za pierwszym razem przejdzie bo tworzy folder a za drugim nie bo już istnieje i bedzie error
    os.mkdir("frivolous_directory")  # cicho i spokojnie przechodzimy dalej




# 29 regex

import re


text = "--- a0 ---"


def check_patern_1(text: str) -> bool:
    REGEX = re.compile("[0-9a-fA-f]")
    return re.match(REGEX, text)


# <_sre.SRE_Match object; span=(4, 5), match='a'>


import re

text = "--- a0 ---"
REGEX = re.compile("[0-9a-fA-f]")


def check_patern_2(text: str) -> bool:
    return re.match(REGEX, text)


# 30  Protocols  -> protocol.py



def print_hi(name):
    print(f"Hi, {name}")


if __name__ == "__main__":
    print_hi("PyCharm")
