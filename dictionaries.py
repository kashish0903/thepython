print('======= 6-1 to 3 from dictoinaries ======')


person = {
    'first_name': 'Kashish',
    'last_name': 'Sunar',
    'age': 20,
    'city': 'Kathmandu'
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print('======= the favorite number =====')
print('======= Favorite Numbers =====')
name = {
    "kashish": 18,  # Numbers don't need quotes
    "deepson": 11,
    'hari': 3,
    "kalam": 8,
    'rohan': 9  
}
for person_name, number in name.items():
    print(f"{person_name.title()}'s favorite number is {number}")
print('======= Programming Glossary =====\n')

glossary = {
    'variable': 'A container that stores data values in memory',
    'list': 'An ordered collection of items that can be modified',
    'dictionary': 'A collection of key-value pairs for storing related data',
    'loop': 'A programming structure that repeats a block of code',
    'function': 'A reusable block of code that performs a specific task'
}

# Method 1: Simple printing
for word_2, meaning in glossary.items():
    print(f"{word_2.title()}: {meaning}")

# OR Method 2: More formatted (as the exercise suggests)
for word_2, meaning in glossary.items():
    print(word_2.title())
    print(f"    {meaning}")