#Darwyn Avila-Medina
#Assignment 7 User Input and While Loops

#7-1 Rental Car 
message = input("What kind of rental car would you like? ")
print (f"Let me see if I can find you a {message}!")

#7-2 Restaurant Seating 
party = (input("How many people are in your dinner group? "))
party = int(party)
if party > 8:
    print ("Sorry, you'll have to wait for a table.")
else:
    print ("Great, a table is ready for your party!")

#7-3 Multiples of Ten 
number = input("Please select a number: ")
number = int(number)

if number % 10 == 0:
    print ("Nice, that's a multiple of 10!")
else: 
    print ("It's not a multiple of 10 my friend.")

#7-4 Pizza Toppings 
while True:
    topping = input("Enter a pizza topping (or 'quit to finish): ")

    if topping.lower() == 'quit':
        print (f"Thanks! Your pizza will be ready soon.")
        break
    else: 
        print (f"Adding {topping} to your pizza.")

#7-5 Movie Tickets 
while True:
    ticket = input("How old are you? ")
    ticket = int(ticket)

    if ticket < 3:
        print ("Alrighty then, a free ticket.")
        break
    elif ticket > 3 and ticket < 12:
        print ("That'll be $10 per ticket please.")
        break
    else:
        print ("$15 for the ticket please.")
        break

#7-7 Infinity 
# while True:
#     print ("I love food!")

# 7-8
sandwich_orders = ['pb&j', 'ham & cheese', 'italian']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print (f"I made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)

print ("\nAll sandwiches have been made! All sandwiches made include:")
for sandwich in finished_sandwiches:
    print (f"{sandwich.title()} Sandwich.")

# 7-9
sandwich_orders = ['pb&j', 'pastrami', 'ham & cheese', 'italian']
finished_sandwiches = []

print ('Apologies in advance, the deli has run out of pastrami today!\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print (f"I made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)

print ("\nAll sandwiches have been made! All sandwiches made include:")
for sandwich in finished_sandwiches:
    print (f"{sandwich.title()} Sandwich.")

#7-10
responses = {}

polling_active = True

while polling_active:
    name = input('\nWhat is your name? ')
    response = input ("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat.lower() == 'no':
        polling_active = False

print ("\n ---  Polling Results --- ")
for name, response in responses.items():
    print (f"{name.title()} would like to visit {response.title()}.")