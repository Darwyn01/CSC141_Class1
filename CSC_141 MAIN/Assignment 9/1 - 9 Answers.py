#Darwyn Avila-Medina

#9-1 Restaurants 
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print (f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print (f"{self.name} is open for business!")
    
restaurant = Restaurant("Texas Roadhouse", "American")

print (restaurant.name)
print (restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2 Three Restaurants 
restaurant1 = Restaurant("\nTexas Roadhouse", "America")
restaurant2 = Restaurant("Alebrije", "Mexican")
restaurant3 = Restaurant("P.F. Chang's", "Asian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9-3 Users 
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        print (f"\n{self.first_name} {self.last_name} info:\n{self.email}, {self.age}")

    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!")

user1 = User("Darwyn", "Avila", "daravi@gmail.com", 21)
user2 = User("Alisson", "Flores", "aliflo@icloud.com", 20)
user3 = User("Angel", "Ramirez", "angram1@yahoo.com", 20)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

#9-4 Number Served 
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print (f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print (f"{self.name} is open for business!")
    
    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else: 
            print ("Number served cannot be negative.")
    
    def increment_number_served (self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers
        else: 
            print ("Cannot decrease number served.")

restaurant = Restaurant("Texas Roadhouse", "American")

print (f"\nCustomers served: {restaurant.number_served}.")

restaurant.number_served = 25
print (f"Customers served (after manual updated): {restaurant.number_served}.")

restaurant.set_number_served(50) 
print (f"Customers served (after set_number_served): {restaurant.number_served}.")

restaurant.increment_number_served(20)
print (f"Customers served (after increment): {restaurant.number_served}.")

#9-5 Login Attempts 
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print (f"\n{self.first_name} {self.last_name} info:\n{self.email}, {self.age}")

    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Darwyn", "Avila", "daravi@gmail.com", 21)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print (f"\nLogin Attempts: {user1.login_attempts}.")


user1.reset_login_attempts()
print (f"Login Attempts Reset: {user1.login_attempts}")

#9-6 Ice Cream Stand 
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        print (f"\n{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        print (f"{self.name} is open for business!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else: 
            print ("Number served can't be negative.")
    
    def increment_number_served(self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers
        else: 
            print ("Cannot decrease number served.")
    
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="Ice Cream"):
        super().__init__(name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Cookies and Creme"]

    def display_flavors(self):
        print (f"\n{self.name} sells the following flavors:")

        for flavor in self.flavors:
            print (f"{flavor}")

ice_cream_stand = IceCreamStand("Sunset Sundaes")

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

#9-7 Admin 
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print (f"\n{self.first_name} {self.last_name} info:\n{self.email}, {self.age}")

    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user", 
            "can reset passwords",
        ]

    def show_privileges(self):
        print (f"\nAdmin privileges for {self.first_name} {self.last_name}:")
        for privileges in self.privileges:
            print (f"{privileges}")

admin_user = Admin("Jose", "Avila", "josavi1@g.com", 48)

admin_user.describe_user()
admin_user.show_privileges()

#9-8 Privileges 
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print (f"\n{self.first_name} {self.last_name} info:\n{self.email}, {self.age}")

    def greet_user(self):
        print(f"\nGreetings {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
            "can add post",
            "can delete post",
            "can ban user", 
            "can reset passwords",
            ]
        self.privileges = privileges

    def show_privileges(self):
        print ("\nPrivileges:")
        for privilege in self.privileges:
            print (f"{privilege}")

class Admin(User):

    def __init__(self, first_name, last_name, email, age):
        super().__init__(first_name, last_name, email, age)
        self.privileges = Privileges()


admin_user = Admin("Jose", "Avila", "josavi1@g.com", 48)

admin_user.describe_user()
admin_user.privileges.show_privileges()

#9-9 Battery Usage 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
    
    def get_descriptive_name(self):
        long_name = (f"{self.year} {self.make} {self.model}")
        return long_name.title()
    
    def read_odometer(self):
        print (f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else: 
            print ("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else: 
            print ("You can't add negative miles.")

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print (f"This car has a {self.battery_size} battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65!")
        else:
            print("Battery is already at the highest capacity.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

tesla = ElectricCar("tesla", "model 3", 2025)

print(tesla.get_descriptive_name)
tesla.battery.describe_battery()

tesla.battery.get_range()

tesla.battery.upgrade_battery()

tesla.battery.get_range()
