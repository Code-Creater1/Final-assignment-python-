

# Question 1
import os
files = [
    "/path/to/document.pdf",
    "/home/user/images/photo.png",
    "data.jpg",
    "report.docx"
]

print("----------- file names ----------")

for file in files:
    file_name = os.path.basename(file)
    print(file_name)

#FOR SEPARATING OUTPUTS 
print("\n")

# Question 2
students = [
    {"roll_number": 1, "name": "Alice"},
    {"roll_number": 2, "name": "Bob"},
    {"roll_number": 3, "name": "John"},
    {"roll_number": 4, "name": "Dave"}
]

for student in students:
    print(f"Roll Number: {student['roll_number']}, Name: {student['name']}")

print("\n")

# Question 3
email_list = [
    "user-1@gmail.com",
    "user-2@gmail.com",
    "user-3@yahoo.com",
    "user-4@gmail.com",
    "user-5@mail.com",
    "user-6@gmail.com",
    "user-7@yahoo.com"
]

for email in email_list:
    if email.endswith("@gmail.com"):
        print(email)
print("\n")

# Question 4
product_prices = [500,650,700,780,850,1000]
for price in product_prices:
    print(f"{price} PKR")

print("\n")

# Question 5
contacts = [
    {"phone": "1234567890"},
    {"phone": "9876543210"},
    {"phone": "5551234567"}
]

for contact in contacts:
    phone = contact["phone"]
    contact["masked_phone"] = "*" * (len(phone) - 4) + phone[-4:]
    print(f"masked numbers except last four {contact['masked_phone']}")

print("\n")

# Question 6
transactions = [4000,50000,45000,60000,65000]
for value in transactions:
    if value >= 50000:
        print(f"value of transactions is {value}")

print("\n")

# Question 7
sentence = "this is a simple sentence"
words = sentence.split()
reverse_words = words[::-1]
for reverse_word in reverse_words:
    print(reverse_word)

print("\n")

# Question 8
Shopping_cart = [
    {"item": "Apple", "quantity": 5},
    {"item": "Banana", "quantity": 0},
    {"item": "Orange", "quantity": 3},
    {"item": "Mango", "quantity": 0}
]
for product in Shopping_cart:
    if product["quantity"] == 0:
        print(f"{product["item"]}: out of stock")

print("\n")

# Question 9
todo_list = [
    {"task": "Buy Groceries", "status": "pending"},
    {"task": "Assignment", "status": "done"},
    {"task": "Finish report", "status": "pending"},
    {"task": "Pay Bills", "status": "done"}
]

print("Pending Works")
for items in todo_list:
    if items["status"] == "pending":
        print(f" {items["task"]}")

print("\n")

# Question 10

notifications = [
    "Email from Alice",
    "New comment on your post",
    "System update available",
    "Meeting at 3 PM",
    "New follower: JohnDoe",
    "Backup completed",
    "Reminder: Dentist appointment"
]

print("First Five Notifications:")
for notification in notifications[:5]:
    print(f" - {notification}")

print("\n")

# Question 11

# Use for item in list: when you only care about the values.
# Use for i in range(len(list)): when you need to use the index, e.g. to update or track position.

names = ["Ali", "Sara", "Ahmed"]

# for item in list
for name in names:
    print(name)

# for i in range(len(list))
for i in range(len(names)):
    print(names[i])

print("\n")

# Question 12
'''
 iter() function:
     Python converts the iterable (like a list, tuple, string) into an iterator using iter().
     This object knows how to fetch the next item.

next() function:
      Python calls next() to get the next element from the iterator.
      If there are no more elements, it raises a StopIteration exception.

 StopIteration:
      When Python sees this exception, it automatically ends the for loop.
'''
some_list = [10,20,30]
iterator = iter(some_list)    
while True:
    try:
        item = next(iterator)  
        print(item)
    except StopIteration:
        break                 


print("\n")

# Question 13
password = ""

while password != "secure123":
    password = input("Enter password: ")

print("Access granted.")

print("\n")

# Question 14

correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter your ATM PIN: ")
    if entered_pin == correct_pin:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Card blocked due to 3 incorrect attempts.")

print("\n")

# Question 15
import time
import sys

for i in range(0, 101, 10):
    bar = '#' * (i // 10) + ' ' * (10 - (i // 10))
    sys.stdout.write(f"\r[{bar}] {i}%")
    sys.stdout.flush()
#    time.sleep(0.3)  # Simulates download delay
print("\nDownload complete.")


print("\n")

# Question 16
marks = []  

while True:
    entry = input("Enter student mark (or type 'done' to finish): ")
    
    if entry.lower() == "done":
        break  
    
    try:
        mark = float(entry)  
        marks.append(mark)   
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

print("\nMarks collected:", marks)
print("Total students:", len(marks))
if marks:
    print("Average mark:", sum(marks) / len(marks))


print("\n")

# Question 17

internet_connection = ""
while True:
    user = input("enter a internet connection").lower()
    internet_connection = user
    if internet_connection == "true":
        break
        print(internet_connection)


print("\n")

# Question 18
print("Chatbot: Hi there! Type something to chat. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! 👋")
        break  

    print("Chatbot: You said —", user_input)


print("\n")

# Question 19

import time

current_light = "Red"

while True:
    if current_light == "Red":
        print("🚦 RED - Stop")
        time.sleep(3)  # Wait for 3 seconds
        current_light = "Green"
        

    elif current_light == "Green":
        print("🟢 GREEN - Go")
        time.sleep(3)
        current_light = "Yellow"

    elif current_light == "Yellow":
        print("🟡 YELLOW - Slow down")
        time.sleep(2)
        current_light = "Red"
        break


print("\n")

# Question 20

import time

base_fare = 3.00         
per_km_rate = 2.50       
distance = 0.0           
speed = 0.5              

print("🚕 Taxi Meter Started...")
print(f"Base Fare: ${base_fare:.2f}")
print("-----------------------------")

while True:
    time.sleep(1) 

    distance += speed
    fare = base_fare + (distance * per_km_rate)

    print(f"Distance: {distance:.1f} km | Fare: ${fare:.2f}")

    # Optional: stop after a certain distance
    if distance >= 2:
        print("\n🛑 Ride complete.")
        break

print("\n")

# Question 21

'''
 Python does not have a built-in do-while loop like some other languages (e.g., C, C++, Java), but you can simulate it.

| Feature                    | `while` Loop                      | `do-while` Loop                      |
| -------------------------- | --------------------------------  | -----------------------------------  |
| **Condition check**        | At the **beginning** of the loop  | At the **end** of the loop           |
| **Executes at least once** | ❌ Not guaranteed                 | ✅ Always executes **at least once** |
| **Syntax in Python**       | Built-in                          | No native syntax (must simulate it)  |

'''
# while loop
num = 5
while num > 0:
    print("num =", num)
    num -= 1

# do-while loop
x = 0
while True:
    print("x =", x)
    x += 1
    if x >= 5:
        break

print("\n")

# Question 22
# If the while loop condition is always True, then the loop becomes an infinite loop — it never stops running unless you explicitly tell it to break out.


print("\n")

# Question 23

rows = ['A', 'B', 'C']

seats = range(1, 6)

for row in rows:
    for seat in seats:
        print(f"{row}{seat}")

print("\n")

# Question 24
shirts = ['Red', 'Blue', 'Green']
pants = ['Black', 'White']

for shirt in shirts:
    for pant in pants:
        print(f"{shirt} shirt with {pant} pants")

print("\n")

# Question 25
for minute in range(0, 11):
    print(f"12:{minute:02d}")

print("\n")

# Question 26

days = [1, 2, 3]
slots = ["Morning", "Evening"]

for day in days:
    for slot in slots:
        print(f"Day {day} - {slot} slot")


print("\n")

# Question 27
Rows = range(1,4)
Seats = ["a","b","c","d"]

for row in Rows:
    for seat in Seats:
        print(f"{row}{seat.upper()}", end=" ")
    print()  

print("\n")

# Question 28
#  opetional fo write a number on blank boxes
count = 1
for row in range(3):
    print(f"{count} | {count+1} | {count+2}")
    if row <= 2:
        print("--+---+--")
    count += 3

print("\n")

# Question 29
rows = 5

for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

print("\n")

# Question 30
players = ["Alice", "Bob", "Charlie", "Diana"]

for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print(f"{players[i]} - {players[j]}")

print("\n")

# Question 31
for num in range(2, 6):  
    print(f"\nMultiplication Table for {num}")
    print("-" * 25)
    for i in range(1, 11): 
        print(f"{num} x {i} = {num * i}")

print("\n")

# Question 32
shopping = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Vegetables": ["Carrot", "Spinach", "Broccoli"],
    "Dairy": ["Milk", "Cheese", "Yogurt"]
}

for category, products in shopping.items():
    print(f"{category}:")
    for product in products:
        print(f"  - {product}")
    print()  

print("\n")

# Question 33
'''
for i in range(n):
   for j in range(n):
         constant time operations

Outer loop runs n times.

Inner loop runs n times for each iteration of the outer loop.

Total operations = n * n = n².

So, time complexity = O(n²) (quadratic time).


print("\n")

# Question 34

When to replace nested loops with list comprehensions:

For readability and conciseness:

If the nested loop logic is simple (e.g., creating a list of pairs or filtered elements), list comprehensions make the code shorter and often easier to read.

When creating new lists from existing iterables:

List comprehensions are designed for building lists in a clear and expressive way.

When the operation inside loops is straightforward:

Simple expressions, no complicated logic or side-effects.

For performance:

List comprehensions can be faster than equivalent for-loops because they are optimized internally.
'''

print("\n")

# Question 35
def count_pdf_files(file_list):
    count = 0
    for filename in file_list:
        if filename.lower().endswith('.pdf'):
            count += 1
    return count

files = ["report.pdf", "image.jpg", "document.PDF", "notes.txt"]
print(count_pdf_files(files))  

print("\n")

# Question 36
def is_username_available(username, existing_usernames):
    username_lower = username.lower()
    existing_lower = [user.lower() for user in existing_usernames]
    return username_lower not in existing_lower

# Example usage:
existing_users = ["Alice", "Bob", "Charlie"]
print(is_username_available("bob", existing_users))
print(is_username_available("David", existing_users))


print("\n")

# Question 37
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

sentence = "The quick brown fox jumps over the lazy dog"
print(longest_word(sentence))  

print("\n")

# Question 38
def is_palindrome(s):
    s = s.lower()  
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("Racecar"))  
print(is_palindrome("Hello"))   

print("\n")

# Question 39
def print_multiplication_table(n):
    print(f"Multiplication Table for {n}")
    print("-" * 20)
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_multiplication_table(5)

print("\n")

# Question 40
import random

def roll_until_six():
    count = 0
    while True:
        roll = random.randint(1, 6)
        count += 1
        print(f"Roll {count}: {roll}")
        if roll == 6:
            print("Got a 6! Stopping.")
            break

roll_until_six()

print("\n")

# Question 41
products = [
    {"name": "Laptop", "price": 800},
    {"name": "Smartphone", "price": 300},
    {"name": "Headphones", "price": 50},
    {"name": "Keyboard", "price": 30},
    {"name": "Monitor", "price": 200}
]

def filter_products_by_price(price_limit):
    filtered_products = [product for product in products if product["price"] < price_limit]
    return filtered_products


price_limit = float(input("Enter the price limit: "))
filtered_products = filter_products_by_price(price_limit)


if filtered_products:
    print("\nProducts under the given price:")
    for product in filtered_products:
        print(f"{product['name']} - ${product['price']}")
else:
    print("No products found under the given price.")

print("\n")

# Question 42

def mask_passwords(password_list):
    return ["*" * len(password) for password in password_list]

passwords = ["myPassword123", "securePass456", "adminPassword", "12345"]
masked_passwords = mask_passwords(passwords)
print(masked_passwords)

print("\n")

# Question 43
from collections import Counter

def count_word_frequency(sentence):
    words = sentence.lower().split()
    word_count = Counter(words)
    return word_count

sentence = input("Enter a sentence: ")
word_frequency = count_word_frequency(sentence)
print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")


print("\n")

# Question 44
import re

def extract_hashtags(post):
    hashtags = re.findall(r'#\w+', post)
    return hashtags

post = input("Enter a social media post: ")
hashtags = extract_hashtags(post)
print("\nExtracted Hashtags:", hashtags)


print("\n")

# Question 45

#print in Functions
#Purpose: print is used to display output to the console (standard output).

#return in Functions:
#Purpose: return is used to send back a value from the function to the caller.


print("\n")

# Question 46

#Yes, functions in Python can return multiple values. This is achieved by returning a tuple. In Python, when you separate multiple values with commas in a return statement, they are automatically packed into a tuple.

print("\n")

# Question 47

salaries = [50000, 60000, 55000, 70000, 65000]
average_salary = sum(salaries) / len(salaries)
print("Salaries above average:")
for salary in salaries:
    if salary > average_salary:
        print(salary)
print("\n")

# Question 48
grades = [45, 67, 89, 32, 50, 76, 48]
pass_mark = 50
for grade in grades:
    if grade >= pass_mark:
        print(f"Grade: {grade} - Pass")
    else:
        print(f"Grade: {grade} - Fail")

print("\n")

# Question 49
original_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("List without duplicates:", unique_list)

print("\n")

# Question 50
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = []
for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

print("\n")

# Question 51
emails = ['user@example.com', 'invalidemail.com', 'admin@mail.org', 'noatsymbol']

for email in emails:
    if '@' in email:
        print(f"Valid: {email}")
    else:
        print(f"Invalid: {email}")

print("\n")

# Question 52
chat_logs = [
    "Hey, are you coming?",
    "This is urgent, please respond!",
    "Reminder for the meeting tomorrow.",
    "URGENT: Server is down!",
    "Let me know when you're free."
]

urgent_count = 0

for message in chat_logs:
    if "urgent" in message.lower():
        urgent_count += 1

print(f"Number of urgent messages: {urgent_count}")

print("\n")

# Question 53
contacts = [
    "+92 3024536287",
    "+86 3024536287", 
    "+92 3024536287", 
    "+61 3024536287", 
    "+92 3024536287"
]
for contact in contacts:
    if contact.startswith("+92"):
        print(contact)
   
print("\n")

# Question 54
inventory = {
    "apple": 10,
    "banana": 15,
    "orange": 8
}

order = {
    "apple": 3,
    "orange": 2
}

for item, quantity in order.items():
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            print(f"{quantity} {item}(s) ordered. Remaining: {inventory[item]}")
        else:
            print(f"Not enough {item}s in stock!")
    else:
        print(f"{item} is not available in inventory.")

print("\nUpdated Inventory:")
print(inventory)
  
print("\n")

# Question 55
doctors = [
    {"name": "Dr. Ahmed", "specialist": True},
    {"name": "Dr. Sara", "specialist": False},
    {"name": "Dr. Khan", "specialist": True},
    {"name": "Dr. Ali", "specialist": False}
]

print("Specialist Doctors:")
for doctor in doctors:
    if doctor["specialist"]:
        print(doctor["name"])

print("\n")

# Question 56
student_courses = {
    "Alice": ["Math", "Science", "History"],
    "Bob": ["English", "Math"],
    "Charlie": ["Biology", "Chemistry", "Physics"]
}

for student, courses in student_courses.items():
    print(f"{student}'s courses:")
    for course in courses:
        print(f" - {course}")
    print() 



# Question 57

#To iterate over both keys and values in a Python dictionary, the most common and recommended method is to use the items() method.

# Question 58

#Breaking out of multiple nested loops in Python can be achieved using several methods, as the break statement only exits the innermost loop directly.
#1. Using a Flag Variable:
#2. Encapsulating in a Function and Using return:
#3. Using else Clause with for Loops:
#4. Raising an Exception:


# Question 59
input_str = "programming"
result = ""

for char in input_str:
    if char not in result:
        result += char

print(result)

print("\n")

# Question 60

def first_non_repeated_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None  # If all characters are repeated

input_str = "swiss"
result = first_non_repeated_char(input_str)

if result:
    print(f"First non-repeated character: {result}")
else:
    print("No non-repeated character found.")

print("\n")

# Question 61
def rotate_left(s):
    if len(s) == 0:
        return s
    return s[1:] + s[0]

input_str = "abc"
rotated_str = rotate_left(input_str)
print(rotated_str)


print("\n")

# Question 62
def compress_string(s):
    if not s:
        return ""
    
    compressed = ""
    count = 1
    prev_char = s[0]
    
    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed += prev_char + str(count)
            prev_char = char
            count = 1
    
    compressed += prev_char + str(count)  # for last group
    return compressed

input_str = "aaabb"
print(compress_string(input_str))

print("\n")

# Question 63
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for i in range(len(words)-1, -1, -1):
        reversed_words.append(words[i])
    return " ".join(reversed_words)

input_sentence = "Hello world this is Python"
print(reverse_words(input_sentence))

print("\n")

# Question 64
text = "Hello World! Python is FUN."
def count_case(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")

count_case(text)

print("\n")

# Question 65
def validate_password(password):
    has_digit = False
    
    if len(password) < 8:
        return False

    for char in password:
        if char.isdigit():
            has_digit = True
            break

    return has_digit

# Test examples
print(validate_password("password"))    
print(validate_password("pass1234"))    
print(validate_password("short1")) 

print("\n")

# Question 66

def find_duplicate_words(paragraph):
    words = paragraph.lower().split()
    duplicates = []
    seen = []

    for word in words:
        word = ''.join(char for char in word if char.isalnum())  # remove punctuation
        if word in seen and word not in duplicates:
            duplicates.append(word)
        else:
            seen.append(word)

    return duplicates

text = "This is a test. This test is only a test."
print("Duplicate words:", find_duplicate_words(text))

print("\n")

# Question 67
def count_vowels(text):
    vowels = "aeiou"
    freq = {}

    for char in text.lower():
        if char in vowels:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    return freq

sentence = "This is an example sentence to count vowels."
result = count_vowels(sentence)
print("Vowel frequencies:", result)

print("\n")

# Question 68
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))     # True
print(are_anagrams("Hello", "Olelh"))       # True
print(are_anagrams("apple", "pale"))        # False

# Question 69
# Immutable Types (Strings, Tuples):
# Definition:
#   Once an immutable object is created, its internal state (its value or content)
#   cannot be altered. Any operation that seems to "modify" an immutable object actually 
#   results in the creation of a new object with the desired changes.

# Mutable Types (Lists, Dictionaries):
# Definition:
#   Mutable objects can be modified in-place after they are created. You can add, remove, 
# or change elements without creating a new object.

# Question 70

#✅ Reasons why strings are immutable in Python:

# Security & Integrity
# Strings are widely used as keys in dictionaries and identifiers in code. If they were mutable, their values could change — making them unreliable for consistent hashing and lookups.

# Performance (Hashing)
# Immutable objects can be hashed, which allows for fast access in data structures like sets and dictionaries.

print("\n")

# Question 71
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_or_odd(10)) 
print(even_or_odd(3))  

print("\n")

# Question 72
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)

print("\n")

# Question 73
emails = [
    "alice@example.com",
    "bob@university.edu",
    "carol@school.edu",
    "dave@gmail.com"
]

edu_emails = list(filter(lambda email: email.endswith(".edu"), emails))

print(edu_emails)

print("\n")

# Question 74
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print(product)

print("\n")

# Question 75
sentence = "Hello world this is ChatGPT"

first_chars = list(map(lambda word: word[0], sentence.split()))
print(first_chars)

print("\n")

# Question 76
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 60000},
]

sorted_employees = sorted(employees, key=lambda emp: emp['salary'])
print(sorted_employees)

print("\n")

# Question 77
users = [
    {"name": "Alice", "premium": True},
    {"name": "Bob", "premium": False},
    {"name": "Charlie", "premium": True}
]

premium_users = list(filter(lambda user: user["premium"], users))
print(premium_users)


print("\n")

# Question 78
names = ["John Smith", "Alice Johnson", "Bob Adams"]

sorted_names = sorted(names, key=lambda name: name.split()[-1])
print(sorted_names)

print("\n")

# Question 79
phone_numbers = ["1234567890", "9876543210"]

formatted = list(map(lambda p: f"({p[:3]}) {p[3:6]}-{p[6:]}", phone_numbers))
print(formatted)

print("\n")

# Question 80
files = ["image.jpg", "doc.txt", "photo.JPG", "report.pdf", "selfie.jpg"]

jpg_files = list(filter(lambda f: f.lower().endswith(".jpg"), files))
print(jpg_files)



# Question 81

# lambda Function

#Anonymous function (does not need a name)

#Single-expression function

#Used for simple operations

#Syntax: lambda arguments: expression

#def Function

#Used to define a named function

#Can contain multiple expressions and statements

#Supports loops, conditionals, docstrings, etc.

#More flexible and powerful



# Question 82
#1. Single Expression Only

#Lambdas can only contain one expression—no statements allowed.
#2. No Statements

#Can't use statements like if, for, while, try, print, etc., inside a lambda.
#3. Reduced Readability

#Complex lambdas are hard to read and understand.

print("\n")

# Question 83
roll_numbers = [f'BSE-{i}' for i in range(1, 51)]
print(roll_numbers)

print("\n")

# Question 84
def extract_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char in vowels]

text = "Hello World"
vowel_list = extract_vowels(text)
print(vowel_list)

print("\n")

# Question 85
words = ['Sun', 'Moon', 'Star', 'sky', 'Space', 'planet']
s_words = [word for word in words if word.startswith('S')]

print(s_words)

print("\n")

# Question 86
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]

print(flat_list)

print("\n")

# Question 87
words = ['apple', 'banana', 'kiwi', 'grape']
word_lengths = {word: len(word) for word in words}

print(word_lengths)

print("\n")

# Question 88
emails = ['alice@gmail.com', 'bob@yahoo.com', 'carol@outlook.com']
domains = [email.split('@')[1] for email in emails]

print(domains)


print("\n")

# Question 89
even_numbers = [i for i in range(1, 101) if i % 2 == 0]
print(even_numbers)

print("\n")

# Question 90
transactions = [50000, 150000, 25000, 120000, 99000, 200000]
high_value = [amount for amount in transactions if amount > 100000]

print(high_value)

print("\n")

# Question 91
import re

tweets = [
    "Loving the weather today! #sunny #happy",
    "Python is awesome! #coding #python",
    "No hashtags here"
]

hashtags = [hashtag for tweet in tweets for hashtag in re.findall(r'#\w+', tweet)]

print(hashtags)

print("\n")

# Question 92
seat_numbers = [f"{row}{col}" for row in ['A', 'B', 'C'] for col in range(1, 6)]
print(seat_numbers)

# Question 93
# When to Prefer List Comprehension:
#   Conciseness & Readability
#          When you want to write cleaner and shorter code.
#          For simple transformations or filtering, list comprehension is more readable.

#   Creating New Lists
#           If your goal is to generate a new list from an existing iterable by applying some expression or filter.
#    Performance
#           List comprehensions are often faster than equivalent for loops due to internal optimizations.

# Question 94
# Yes, list comprehensions can often replace map() and filter() functions in Python, and 
# sometimes they are preferred for readability and flexibility.

print("\n")

# Question 95
def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("step must not be zero")

for num in my_range(1, 10, 2):
    print(num)

print("\n")

# Question 96
def my_enumerate(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

for i, value in my_enumerate(['a', 'b', 'c'], start=1):
    print(i, value)

print("\n")

# Question 97
original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in original_dict.items()}

print(reversed_dict)

print("\n")

# Question 98
def find_pairs(nums, target):
    seen = set()
    pairs = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    
    return list(pairs)

nums = [1, 5, 7, -1, 5]
target = 6
print(find_pairs(nums, target))

print("\n")

# Question 99
def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced_parentheses("(())")) 
print(is_balanced_parentheses("(()"))  

print("\n")

# Question 100
def menu_system():
    items = []

    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Delete")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            item = input("Enter item to add: ")
            items.append(item)
            print(f"Added: {item}")
        elif choice == '2':
            item = input("Enter item to delete: ")
            if item in items:
                items.remove(item)
                print(f"Deleted: {item}")
            else:
                print("Item not found.")
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        print(f"Current items: {items}")

menu_system()

print("\n")

# Question 101
def print_dict(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + str(key) + ':', end=' ')
        if isinstance(value, dict):
            print()
            print_dict(value, indent + 1)
        else:
            print(value)

# Example dictionary
data = {
    'name': 'Alice',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Wonderland',
        'zip': '12345'
    },
    'hobbies': ['reading', 'chess']
}

print_dict(data)

print("\n")

# Question 102
def login_system(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

users = {
    'user1': 'pass123',
    'admin': 'adminpass',
    'guest': 'guest123'
}

login_system(users)

print("\n")

# Question 103
def word_frequency(text):
    freq = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

text = "This is a test. This test is simple."
print(word_frequency(text))

print("\n")

# Question 104
def paginate(records, page_size=5):
    total = len(records)
    for i in range(0, total, page_size):
        yield records[i:i + page_size]

records = list(range(1, 21)) 

pages = paginate(records)
page_number = 1
for page in pages:
    print(f"Page {page_number}: {page}")
    page_number += 1

print("\n")

# Question 105
def restaurant_order_system():
    menu = {
        'burger': 150,
        'pizza': 250,
        'fries': 100,
        'cola': 50
    }
    order = {}
    
    while True:
        print("\nMenu:")
        for item, price in menu.items():
            print(f"{item}: {price} PKR")
        
        choice = input("Enter item to order (or 'done' to finish): ").lower()
        
        if choice == 'done':
            break
        
        if choice in menu:
            quantity = input(f"How many {choice}s? ")
            if quantity.isdigit():
                quantity = int(quantity)
                if choice in order:
                    order[choice] += quantity
                else:
                    order[choice] = quantity
            else:
                print("Please enter a valid number.")
        else:
            print("Item not found in menu.")
    
    print("\nYour order:")
    total = 0
    for item, qty in order.items():
        cost = menu[item] * qty
        print(f"{item} x {qty} = {cost} PKR")
        total += cost
    print(f"Total amount: {total} PKR")

restaurant_order_system()
