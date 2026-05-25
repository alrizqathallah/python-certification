# Mendeklarasikan Variabel
name = 'John Doe'
age = 25

# Format camel-case varibel
my_varible_name = 'freeCodeCamp'

# Descriptive
user_age = 30

# Penamaan yang perlu dihindari
x = 56  # Apa maksdunya x?

# This is a single-line comment

# This is
# multi-line
# comment

# Fungsi print
print("Hello world!")  # Hello world!

# Fungsi print dengan multiple argumen
print("My favorite colors are", "blue", "green", "red")
# Output: My favorite  colors are blue green red

# Tipe Data
name = "John Doe"  # Python mengethaui ini sebagai sebuah STRING
age = 25  # Python mengetahui ini sebagai sebuah INTEGER

# Integer
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10

# Float
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5

# String
my_string_var = "hello"
print("String:", my_string_var)  # String: hello

# Boolean
my_boolean_var = True
print("Boolean:", my_boolean_var)  # Boolean: True

# Sets
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}

# Dictionary
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

# Tuple
my_tuple_var = (7, "hello", 8.5)
print("Tuple:", my_tuple_var)  # Tuple: (7, 'hello', 8.5)

# Range
my_range_var = range(5)
print("Range:", my_range_var)  # Range: range(0, 5)

# List
my_list = [22, "Hello world", 3.14, True]
print(my_list)  # [22, 'Hello world', 3.14, True]

# None
my_none_var = None
print("None:", my_none_var)  # None: None

# Fungsi `type()`
my_var_1 = "Hello world"
my_var_2 = 21

print(type(my_var_1))  # <class 'str'>
print(type(my_var_2))  # <class 'int'>

# Konvensi `type()` untuk semua tipe data
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = "hello"
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, "hello", 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {"name": "Alice", "age": 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, "hello", 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, "Hello world", 3.14, True]
print(type(my_list))  # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

# Fungsi `isinstance()`
isinstance("Hello world", str)  # True
isinstance(True, bool)  # True
isinstance(42, int)  # True
isinstance("John Doe", int)  # False

# String
my_str_1 = "Hello"
my_str_2 = "World"

# Multiline string
my_str_3 = """Multiline
string"""
my_str_4 = """Another
multiline
string"""

# Kutip berlawanan
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Menggunakan karakter sequence
msg = "It's a sunny day"
quote = 'She said, "Hello!"'

# Operator `in`
my_str = "Hello world"

print("Hello" in my_str)  # True
print("hey" in my_str)  # False
print("hi" in my_str)  # False
print("e" in my_str)  # True
print("f" in my_str)  # False

# Fungsi `len()`
my_str = "Hello world"
print(len(my_str))  # 11

# String index
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

# Negative Indexing
my_str = "Hello world"
print(my_str[-1])  # d
print(my_str[-2])  # l

# String immutable
greeting = "hi"
greeting = "hello"
print(greeting)  # hello

# String Concatenation
my_str_1 = "Hello"
my_str_2 = "World"

str_plus_str = my_str_1 + " " + my_str_2
print(str_plus_str)  # Hello World

# Fungsi Casting str()
name = "John Doe"
age = 26

name_and_age = name + str(age)
print(name_and_age)  # John Doe26

# String Concatenation dengan Operator Augmented Assignment
name = "John Doe"
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

# F-String
name = "John Doe"
age = 26
name_and_age = f"My name is {name} and I am {age} years old"
print(name_and_age)  # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f"The sum of {num1} and {num2} is {num1 + num2}")  # The sum of 5 and 10 is 15

# String slicing
my_str = "Hello world"
print(my_str[1:4])  # ell

my_str = "Hello world"
print(my_str[:7])  # Hello w

my_str = "Hello world"
print(my_str[8:])  # rld

# Reverse string
my_str = "Hello world"
print(my_str[::-1])  # dlrow olleH

# Method upper()
my_str = "hello world"

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

# Method lower()
my_str = "Hello World"

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

# Method strip()
my_str = "  hello world  "

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

# Method replace(old, new)
my_str = "hello world"

replaced_my_str = my_str.replace("hello", "hi")
print(replaced_my_str)  # hi world

# Method split(separator)
my_str = "hello world"

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

# Method join(iterable)
my_list = ["hello", "world"]

joined_my_str = " ".join(my_list)
print(joined_my_str)  # hello world

# Method startswith(prefix)
my_str = "hello world"

starts_with_hello = my_str.startswith("hello")
print(starts_with_hello)  # True

# Method endswith()
my_str = "hello world"

ends_with_world = my_str.endswith("world")
print(ends_with_world)  # True

# Method find(substring)
my_str = "hello world"

world_index = my_str.find("world")
print(world_index)  # 6

# Method count(substring)
my_str = "hello world"

o_count = my_str.count("o")
print(o_count)  # 2

# Method Capitalize()
my_str = "hello world"

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

# Method isupper()
my_str = "hello world"

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

# Method islower()
my_str = "hello world"

is_all_lower = my_str.islower()
print(is_all_lower)  # True

# Method title()
my_str = "hello world"

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World

# Integer
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))  # <class 'int'>
print(type(my_int_2))  # <class 'int'>

# Penjumlahan dengan integer
my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print("Integer Addition:", sum_ints)  # Integer Addition: 68

# Pengurangan dengan integer
my_int_1 = 56
my_int_2 = 12

diff_ints = my_int_1 - my_int_2
print("Integer Subtraction:", diff_ints)  # Integer Subtraction: 44

# Perkalian dengan integer
my_int_1 = 12
my_int_2 = 4

product_ints = my_int_1 * my_int_2
print("Integer Multiplication:", product_ints)  # Integer Multiplication: 48

# Pembagian dengan integer
my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1 / my_int_2
print("Division:", div_ints)  # Division: 4.666666666666667

# Floats
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1))  # <class 'float'>
print(type(my_float_2))  # <class 'float'>

# Penjumlahan dengan Floats
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print("Float Addition:", float_addition)  # Float Addition: 17.4

# Pengurangan dengan Floats
my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print("Float Subtraction:", float_subtraction)  # Float Subtraction: 6.6

# Perkalian dengan Floats
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print(
    "Float Multiplication:", float_multiplication
)  # Float Multiplication: 64.80000000000001

# Pembagian dengan Floats
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print("Float Division:", float_division)  # Float Division: 2.222222222222222

# Integers adn Floats
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float)  # 61.4
print(type(sum_int_and_float))  # <class 'float'>

# Operator Modulu
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print("Integer Modulo:", mod_ints)  # Integer Modulo: 8
print("Float Modulo:", mod_floats)  # Float Modulo: 1.1999999999999993

# Operator Floor Division
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print("Integer Floor Division:", floor_div_ints)  # Integer Floor Division: 4
print("Float Floor Division:", floor_div_floats)  # Float Floor Division: 2.0

# Operator Exponents
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1**my_int_2
exp_floats = my_float_1**my_float_2

print(
    "Integer Exponentiation:", exp_ints
)  # Integer Exponentiation: 951166013805414055936
print("Float Exponentiation:", exp_floats)  # Float Exponentiation: 614787626.1765089

# Augmented Assigment
my_var = 10
my_var += 5

print(my_var)  # 15

# Operasi Komparasi
print(3 > 4)  # False
print(3 < 4)  # True
print(3 == 4)  # False
print(4 == 4)  # True
print(3 != 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True

# Pernyataan if
age = 18

if age >= 18:
    print("You are an adult")  # You are an adult

# Pernyataan if...else
age = 12

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")

# Pernyataan elif
age = 12

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are an teenager")
else:
    print("You are an child")

# Nested conditionals
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Truthy dan Falsy
print(bool(False))  # False
print(bool(0))  # False
print(bool(""))  # False

print(bool(True))  # True
print(bool(1))  # True
print(bool("Hello"))  # True

# Operator `and`
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print("You are eligible to vote")  # You are eligible to vote
else:
    print("You are not eligible to vote")

# Operator 'or'
age = 19
is_student = True

if age < 18 or is_student:
    print(
        "You are eligible for a student discount"
    )  # You are eligible for a student discount
else:
    print("You are not eligible for a student discount")

# Operator 'not'
print(not "")  # True, because empty string is falsy
print(not "Hello")  # False, because non-empty string is truthy
print(not 0)  # True, because 0 is falsy
print(not 1)  # False, because 1 is truthy
print(not False)  # True, because False is falsy
print(not True)  # False, because True is truthy

is_admin = False

if not is_admin:
    print(
        "Access denied for non-administrators."
    )  # Access denied for non-administrators.
else:
    print("Welcome, Administrator!")

# Input()
name = input("What is your name?")
print("Hello", name)


# Functions `def`
def calculate_sum(a, b):
    print(a + b)


calculate_sum(3, 1)


# Function return
def calculate_sum(a, b):
    return a + b


my_sum = calculate_sum(3, 1)
print(my_sum)

# Local Scope
def my_func():
  my_var = 10
  print(my_var)

# Enclosing scope
def outer_func():
    msg = 'Hello there!'
    
    def inner_func():
        print(msg)
    
    inner_func()

outer_func()


# Kata kunci `nonlocal`
def outer_func():
    msg = "Hello there!"
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = "How are you?"
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified


outer_func()

# Output:
# Hello there!
# How are you?

# Global Scope
my_var = 100


def show_var():
    print(my_var)


show_var()
print(my_var)

# Kata kunci `global`
my_var_1 = 7


def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)


show_vars()  # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2)  # 10

# Built-in function
print(str(45))  # '45'
print(type(3.14))  # <class 'float'>
print(isinstance(3, str))  # False
