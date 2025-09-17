#Darwyn Avila-Medina
#Chapter 4 answers

#4-1
#Pizzas = ['Pepperoni', 'Cheese', 'Mushrooms', 'Deluxe']
#for pizza in Pizzas:
#    print(f"{pizza.title()} is my favorite topping!")
#    print(f"My brother also likes {pizza} pizza!\n")
#print("We really love pizza!")

#4-2
#Animals = ['dog', 'cat']
#for animal in Animals:
#    print(f"I adore {animal}s!")
#print(f"{Animals[0].title()} and {Animals[1]} both walk on four legs.")

#4-3
#for value in range(1,21):
#    print (value)

#4-4
#Numbers = range(1,1000001)
#for number in Numbers:
#    print(number)

#4-5
#print (min(Numbers))
#print (max(Numbers))
#print (sum(Numbers))

#4-6
#numbers = list(range(1,21))
#print(numbers)
#odd_numbers = list(range(1,21,2))
#print(odd_numbers)
#for number in odd_numbers:
#    print (number)

#4-7
#numbers = list(range(1,31))
#multiples_3 = list(range(3,31,3))
#print (multiples_3)
#for number in multiples_3:
#    print (number)

#4-8
#cubes = []
#for value in range (1,11):
#    cube = value ** 3
#    cubes.append(cube)
#print (cubes)
#for cube in cubes:
#    print (cube)

#4-9
#cubes = [value ** 3 for value in range (1,11)]
#print (cubes)

#4-10
#Animals = ['dog', 'cat', 'bird', 'fish', 'snake', 'bear']
#print("The first three animals on the list are:")
#for animal in Animals[:3]:
#    print(animal.title())
#print("\nThree animals in the middle are:")
#for animal in Animals[2:5]:
#    print (animal.title())
#print("\nThe last three items in the list are:")
#for animal in Animals[-3:]:
#    print (animal.title())

#4-11
#Pizzas = ['Pepperoni', 'Cheese', 'Mushrooms', 'Deluxe', 'Sausage']
#friend_pizzas = ['Pepperoni', 'Cheese', 'Mushrooms', 'Deluxe', 'Bacon']
#print ("My favorite pizzas are:")
#for pizza in Pizzas:
#    print(pizza)
#print ("\nMy friends favorite pizzas are:")
#for pizza in friend_pizzas:
#    print(pizza)

#4-12
#my_foods = ['pizza', 'falafel', 'carrot cake']
#for food in my_foods:
#    print (food)
#friend_foods = my_foods[:]
#friend_foods.append('burger')
#for food in friend_foods:
#    print (food)

#4-13
#rest_food = ('steak', 'salmon', 'burger', 'suchi', 'chicken')
#for food in rest_food:
#    print (food)
##rest_food[0]= 'rice'
#print("\nOriginal Menu:")
#for food in rest_food:
#    print (food)
#rest_food = ('steak', 'tilapia', 'burger', 'rice', 'chicken')
#print("\nModified Menu:")
#for food in rest_food:
#    print (food)
