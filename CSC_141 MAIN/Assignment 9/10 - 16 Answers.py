# #9-10 Imported Restaurant 
# class Restaurant:
#     def __init__(self, name, cuisine):
#         self.name = name
#         self.cuisine = cuisine
#         self.number_served = 0
    
#     def describe_restaurant(self):
#         print (f"\n{self.name} serves {self.cuisine} cuisine.")

#     def open_restaurant(self):
#         print (f"{self.name} is open for business!")

# from restaurant import Restaurant
    
# place = Restaurant("Texas Roadhouse")
# place.describe_restaurant()

# #9-11 Imported Admin 
# class User:
#     def __init__(self, first_name, last_name, email, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age

#     def describe_user(self):
#         print (f"\n{self.first_name} {self.last_name} info:\n{self.email}, {self.age}")

#     # def greet_user(self):
#     #     print(f"\nGreetings {self.first_name} {self.last_name}!")

# class Privileges:
#     def __init__(self, privileges=None):
#         if privileges is None:
#             privileges = [
#             "can add post",
#             "can delete post",
#             "can ban user", 
#             "can reset passwords",
#             ]
#         self.privileges = privileges

#     def show_privileges(self):
#         print ("\nPrivileges:")
#         for privilege in self.privileges:
#             print (f"{privilege}")

# class Admin(User):

#     def __init__(self, first_name, last_name, email, age):
#         super().__init__(first_name, last_name, email, age)
#         self.privileges = Privileges()

# from user_admin import Admin

# admin_user = Admin("Jose", "Avila", "josavi1@g.com", 48)

# admin_user.describe_user()
# admin_user.privileges.show_privileges()

# #9-12 Multiple Modules 
# class User:
#     def __init__(self, first_name, last_name, email, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age

#     def describe_user(self):
#         print (f"\n{self.first_name} {self.last_name} info:\n{self.email}, {self.age}")

# from user import User

# class Privileges:
#     def __init__(self, privileges=None):
#         if privileges is None:
#             privileges = [
#             "can add post",
#             "can delete post",
#             "can ban user", 
#             "can reset passwords",
#             ]
#         self.privileges = privileges

#     def show_privileges(self):
#         print ("\nPrivileges:")
#         for privilege in self.privileges:
#             print (f"{privilege}")

# class Admin(User):

#     def __init__(self, first_name, last_name, email, age):
#         super().__init__(first_name, last_name, email, age)
#         self.privileges = Privileges()

# from admin_privileges import Admin

# admin_user = Admin("Jose", "Avila", "josavi1@g.com", 48)

# admin_user.describe_user()
# admin_user.privileges.show_privileges()

#9-13 Dice 
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)
    
die_6 = Die()
print ("Rolling a die 10 times:")

for _ in range(10):
    print(die_6.roll_die())

die_10 = Die(10)
print ("Rolling a 10-sided die 10 times:")

for _ in range(10):
    print(die_10.roll_die())

die_20 = Die(20)
print ("Rolling a 20-sided die 10 times:")

for _ in range(10):
    print(die_20.roll_die())

#9-14 Lottery 
import random 

lottery_items = [1, 5, 7, 9, 11, 23, 45, 56, 67, 89, 'A', 'B', 'C', 'D', 'E']

winning_combo = random.sample(lottery_items, 4)

print ("Any ticket matching these 4 numbers or letters wins a prize!")
print ("Winning Combos:", winning_combo)

#9-15 Lottery Analysis 
import random

lottery_items = [1, 5, 7, 9, 11, 23, 45, 56, 67, 89, 'A', 'B', 'C', 'D', 'E']

my_ticket = [9, 'B', 56, 11]

attempts = 0
winning_combo = []

while winning_combo != my_ticket:
    winning_combo = random.sample(lottery_items, 4)
    attempts += 1

print (f"It took {attempts} tries to win the lottery!")
