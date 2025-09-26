#Darwyn Avila-Medina
#Conditional Tests & If Statements from Chapter 5

#5-1 Conditional Tests 
car = "buick"
print ("Is car == 'buick'? I predict True.")
print (car == 'buick')

print ("\nIs car == 'toyota'? I predict False.")
print (car == 'toyota')

food = "burger"
print ("\nIs food == 'burger'? I predict True.")
print (food == 'burger')

print ("\nIs food == 'pizza'? I predict False.")
print (food == 'pizza')

#5-2 More Conditional Tests 
car = 'Buick'
print (f"\n{car == "Buick"}")
print (car == 'buick')

print (f"\n{car}")
print (car.lower() == 'buick')

topping = "pepperoni"
if topping != "mushrooms":
    print ('No mushrooms please.')

age = 21
print (age == 21)
if age != 25:
    print ("That's not the right age.")

new_age = 24
print (new_age == 24)
print (new_age < 21)
print (new_age <= 21)
print (new_age > 21)
print (new_age >= 21)

print (age >= 22 and new_age >= 19)
print (age >= 22 or new_age >= 19)

toppings = "pepperoni", "mushrooms", "jalapenos"
print (f"\n{'mushrooms' in toppings}")
print ('olives' in toppings)

top = 'bacon'
if top not in toppings:
    print (f"\n{top.title()} is not a topping choice.")

#5-3 Alien Colors #1 
alien_color = 'green'
if alien_color == 'green':
    print ("You earned 5 points!")
print (alien_color == 'red')

#5-4 Alien Colors #2
alien_color = 'red'
if alien_color == 'green':
    print ("You earned 5 points for shooting the alien!")
else:
    print ("You earned 10 points!")

#5-5 Alien Colors #3
alien_color = 'red'
if alien_color == 'green':
    print ("You earned 5 points!")
elif alien_color == 'yellow':
    print ("You earned 10 points!")
else:
    print ("You earned 15 points!")

#5-6 Stages of Life 
age = 32
if age < 2:
    print ('This person is a baby.')
elif age >= 2 and age < 4:
    print ('This person is a toddler.')
elif age >= 4 and age < 13:
        print ('This person is a kid.')
elif age >= 13 and age < 20:
        print ('This person is a teenager.')
elif age >= 20 and age < 65:
        print ('This person is an adult.')
else:
    print ('This person is an elder.')

#5-7 Favorite Fruit
favorite_fruits = ['apple', 'pear', 'pineapple']
if 'apple' in favorite_fruits:
     print ("I enjoy eating apples!")
if 'pear' in favorite_fruits:
     print ("I enjoy eating pears!")
if 'pineapple' in favorite_fruits:
     print ("I enjoy eating pineapple!")
if 'orange' in favorite_fruits:
     print ("I enjoy eating oranges!")
if 'kiwi' in favorite_fruits:
     print ("I enjoy eating kiwi!")

#5-8 Hello Admin
usernames = ['admin', 'Jaden1', 'Alisson25', 'Jesus26', 'Michelle27']
for username in usernames:
    if username == 'admin':
        print ("Hello admin, would you like to see a status report?")
    else: 
        print (f"\n Hello {username}, thank you for logging in again.")

#5-9 No Users
hello_admin_users = []
if hello_admin_users:
    for user in hello_admin_users:
        print (user)
else: 
    print ("We need to find some users!")

#5-10 Checking Username
current_users = ['Alisson25', 'Jesus26', 'Michelle18']
new_users = ['Avila27', "Futbol04", 'Alisson25', 'Michelle18']
for users in new_users:
    if users in current_users:
        print(f"\n{users} has already been taken, use a different username.")
    else:
        print (f"{users} is available!")

#5-11 Ordinal Numbers 
numbers = list(range (1,10))
for number in numbers:
    if number == 1:
        print ('1st')
    elif number == 2:
        print ('2nd')
    elif number == 3: 
        print ('3rd')
    else:
        print (f"{number}th")
