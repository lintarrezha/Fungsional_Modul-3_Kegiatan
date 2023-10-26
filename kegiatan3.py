import math

# Fungsi memisahkan angka menjadi ratusan, puluhan, dan satuan
def split_numbers(number):
    return {
        'ratusan': math.floor(number / 100),  # Bagian ratusan
        'puluhan': math.floor((number % 100) / 10),  # Bagian puluhan
        'satuan': number % 10  # Bagian satuan
    }

# Fungsi mengelompokkan angka dalam tiga kategori: floats, ints, dan strings
def classify_numbers(numbers):
    floats = []
    ints = []
    strings = []

    for number in numbers:
        if isinstance(number, float):
            floats.append(number)  # Angka float
        elif isinstance(number, int):
            ints.append(number)  # Angka integer
        elif isinstance(number, str):
            strings.append(number)  # String

    return floats, ints, strings

# Fungsi ini mengelompokkan dan memisahkan angka-angka integer
def classify_and_split_numbers(numbers):
    floats, ints, strings = classify_numbers(numbers)
    ints_splitted = list(map(split_numbers, ints))  # Memisahkan angka integer menjadi ratusan, puluhan, dan satuan
    return floats, ints_splitted, strings

random_list = [3.1, 2.7, 5.5, 105, 737, 412, "Hello", "Python", "world", "AI"]

# Memisahkan dan mengelompokkan angka dalam daftar
floats, ints, strings = classify_and_split_numbers(random_list)

# Mencetak angka-angka float
print("Data Float:")
for f in floats:
    print(f)

# Mencetak angka-angka integer
print("\nData Int:")
for i in ints:
    print(i)

# Mencetak string
print("\nData String:")
for s in strings:
    print(s)
