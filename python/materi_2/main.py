# List
cities = ["Los Angeles", "London", "Tokyo"]

# Cara mengakses list `[]`
cities = ["Los Angeles", "London", "Tokyo"]
cities[0]  # 'Los Angeles'

# Negative indexing, mengakses elemen dari yang paling akhir
cities = ["Los Angeles", "London", "Tokyo"]
cities[-1]  # Tokyo

# List konstruktor
developer = "Jessica"
list(developer)  # ['J', 'e', 's', 's', 'i', 'c', 'a']

# Mengetahui panjang list dengan fungsi `len()`
numbers = [1, 2, 3, 4, 5]
len(numbers)  # 5

# Melakukan update pada elemen pertama
programming_languages = ["Python", "Java", "C++", "Rust"]
programming_languages[0] = "JavaScript"
print(programming_languages)  # ['JavaScript', 'Java', 'C++', 'Rust']

# IndexError
programming_languages = ["Python", "Java", "C++", "Rust"]
programming_languages[10] = "JavaScript"

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""

# Menghapus elemen di dalam list
developer = ["Jane Doe", 23, "Python Developer"]
del developer[1]
print(developer)  # ['Jane Doe', 'Python Developer']

# Memastikan sebuah elemen ada di dalam sebuah list
programming_languages = ["Python", "Java", "C++", "Rust"]

"Rust" in programming_languages  # True
"JavaScript" in programming_languages  # False

# Nested List
developer = ["Alice", 25, ["Python", "Rust", "C++"]]
developer[2]  # ['Python', 'Rust', 'C++']

developer = ["Alice", 25, ["Python", "Rust", "C++"]]
developer[2][1]  # 'Rust'

# Unpacking list
developer = ["Alice", 34, "Rust Developer"]
name, age, job = developer

print(name)  # 'Alice'
print(age)  # 34
print(job)  # 'Rust Developer'

# Mengumpulkan elemen sisa dari sebuah list
developer = ["Alice", 34, "Rust Developer"]
name, *rest = developer

print(name)  # 'Alice'
print(rest)  # [34, 'Rust Developer']

# ValueError
developer = ['Alice', 34, 'Rust Developer']
name, age, job, city = developer

'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
'''

# List slicing
desserts = ["Cake", "Cookies", "Ice Cream", "Pie", "Brownies"]
desserts[1:4]  # ['Cookies', 'Ice Cream', 'Pie']

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2]  # [2, 4, 6]

