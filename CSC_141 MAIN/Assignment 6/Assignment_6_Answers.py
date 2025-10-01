#Darwyn Avila-Medina
#Assignment 5 --> Dictionaries 

#6-1 Person 
person_1 = {'first name': 'Javier', 
          'last name': 'Hernandez', 
          'age': '34', 
          'city': 'Guadalajara'}
print (person_1['first name'])
print (person_1['last name'])
print (person_1['age'])
print (person_1['city'])

#6-2 Favorite Number 
favorite_number = {'Angel': '1', 
                   'Ramirez':'17', 
                   'Darwyn': '27'}
print (f"Angel's favorite number is {favorite_number['Angel']}.")
print (f"Ramirez's favorite number is {favorite_number['Ramirez']}.")
print (f"Darwyn's favorite number is {favorite_number['Darwyn']}.")

#6-3 Glossary 
glossary = {'dictionary': 'allows you to connect pieces of related info.',
            'print': 'allows you to go forward in pasting info into the terminal.',
            'list': 'allows you to store info.'}
print (f"\nDictionary: {glossary['dictionary']}\nGlossary: {glossary['print']}\nList: {glossary['list']}")

#6-4 Glossary 2
for key, value in glossary.items():
    print (f"\nKey: {key}")
    print (f"Value: {value}")

#6-5 Rivers 
rivers = {'Nile River': 'Egypt',
          'Mississippi River': 'U.S.A',
          'Amazon River': 'Brazil'}

for name, river in rivers.items():
    print (f"\nThe {name} runs through part of {river}.")

for name in rivers.keys():
    print (f"\n{name}")

for name in rivers.values():
    print (f"\n{name}")

#6-6 Polling 
favorite_languages = ['jen', 'edward', 'ramirez', 'angel']
new_favorite_languages = ['ramirez', 'angel']

for name in (favorite_languages):
     if name in new_favorite_languages:
         print (f"\n{name.title()}, please consider taking the poll!")
     else:
         print (f"\n{name.title()}, your response is much appreciated!")

#6-7 People 
person_2 = {'first name': 'Angel', 
          'last name': 'Ramirez', 
          'age': '20', 
          'city': 'Toyko'}
person_3 = {'first name': 'Alex', 
          'last name': 'Lopez', 
          'age': '19', 
          'city': 'Toronto'}
peoples = [person_1, person_2, person_3]

for people in peoples:
    for key, value in people.items():
        print (f"\n{key}: {value}") 

#6-8 Pets 
pet_1 = {'kind': 'dog', 'owner': 'Ramirez'}
pet_2 = {'kind': 'cat', 'owner': 'Jenni'}
pet_3 = {'kind': 'fish', 'owner': 'Lily'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print (f"\nPet Information:")
    for key, value in pet.items():
        print (f"{key}: {value}")

#6-9 Favorite Places 
places1 = {'person': 'Alisson', 'place': 'Tokyo'}
places2 = {'person': "Darwyn", 'place': 'Hawaii'}
places3 = {'person': 'Jose', 'place': 'Mexico'}
favorite_places = places1, places2, places3

for person in favorite_places:
    print (f"\nFavorite places:")
    for key, value in person.items():
        print (f"{key}: {value}")

#6-10 Favorite Numbers 
favorite_number = {'Angel': ['1','0'],
                   'Ramirez':['17','9'],
                   'Darwyn': ['27','5']}
for name, numbers in favorite_number.items():
    print (f"\n {name}'s favorite numbers are:")
    for number in numbers:
        print (f"\t{number}")

#6-11 Cities 
city1 = {'city': 'Reading', 'fact': 'contains the Pagoda', 'country': 'USA'}
city2 = {'city':'Tokyo', 'fact': 'many Naruto fans', 'country': 'Japan'}
city3 = {'city': 'Manchester', 'fact': 'favorite club', 'country': 'UK'}

cities = city1, city2, city3

for city in cities:
    print (f"\nCity Information:")
    for key, value in city.items():
        print (f"{key.title()}: {value}")

#6-12 Extensions 
cities = {'Reading': {'fact': 'contains the Pagoda', 'country': 'USA'},
          'Tokyo': {'fact': 'many Naruto fans', 'country': 'Japan'},
          'Manchester': {'fact': 'favorite club', 'country': 'UK'}
          }

for city, info in cities.items():
    print (f"\nCity Information for {city}:")
    for key, value in info.items():
        print (f"{key.title()}: {value}")
