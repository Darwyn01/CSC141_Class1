#Darwyn Avila-Medina 

#10-1 Learning Python 
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
python_string = ''
for line in lines:
    python_string += line.lstrip()

print(python_string)
print(len(python_string))

#10-2 Learning C
print(python_string.replace('Python', 'C'))

#10-3 Simpler Code 
for line in contents.splitlines():
    python_string = line.lstrip()
print(python_string)

#10-4 Guest 
filename = 'guest.txt'

name = input ("What's your name? ")

with open(filename, 'w') as file_object:
    file_object.write(name)

#10-5 Guest Book 
# guest_book.py

filename = 'guest_book.txt'

print("Enter 'quit' to stop.")

while True:
    name = input("Please enter your name: ")
    if name.lower() == 'quit':
        break
    print(f"Welcome, {name}!")
    with open(filename, 'a') as file_object:  # 'a' = append mode
        file_object.write(name + "\n")

#10-6 Addition 
print("Enter two numbers, and I'll add them together.")
try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
except ValueError:
    print("Sorry, you must enter numbers only!")
else:
    total = num1 + num2
    print(f"The sum is {total}.")

#10-7 Additional Calculator 
print("Enter two numbers, and I'll add them together.")
print("Enter 'q' at any time to quit.")

while True:
    num1 = input("\nFirst number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        total = int(num1) + int(num2)
    except ValueError:
        print("Sorry, you must enter numbers only!")
    else:
        print(f"The sum is {total}.")

#10-8 Cats and Dogs 
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, I can't find {filename}.")
    else:
        print(f"\nContents of {filename}:")
        print(contents)

#10-9 Silent Cats and Dogs 
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass  
    else:
        print(f"\nContents of {filename}:")
        print(contents)

#10-10 Common Words 
def count_common_word(filename, word):
    """Count how many times a word appears in a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} not found.")
    else:
        count = contents.lower().count(word)
        print(f"'{word}' appears about {count} times in {filename}.")

filenames = ['dracula.txt', 'pride_and_prejudice.txt']
for file in filenames:
    count_common_word(file, 'the ')

#10-11 Favorite Number 
import json

filename = 'favorite_number.json'

favorite_number = input("What's your favorite number? ")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print("Thanks! I'll remember that.")

import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("I don't know your favorite number yet.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")

#10-12 Favorite Number Remembered 
# favorite_number_remembered.py

import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print("Got it! I'll remember that.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")

#10-13 User Dictionary 
import json

filename = 'user_info.json'

user = {}
user['name'] = input("What's your name? ")
user['age'] = input("How old are you? ")
user['favorite_color'] = input("What's your favorite color? ")

with open(filename, 'w') as f:
    json.dump(user, f)

print("\nI'll remember that about you!")

with open(filename) as f:
    stored_user = json.load(f)

print("\nHere's what I remember about you:")
print(f"Name: {stored_user['name']}")
print(f"Age: {stored_user['age']}")
print(f"Favorite color: {stored_user['favorite_color']}")

#10-14 Verify User 
import json

filename = 'username.json'

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        confirm = input(f"Are you {username}? (y/n) ")
        if confirm.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you next time, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you next time, {username}!")

greet_user()
