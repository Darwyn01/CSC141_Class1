#Darwyn Avila-Medina 

#8-1 Message 
def display_message():
    print ("I learned what a Function is in Python.")
display_message()

#8-2 Favorite Book 
def favorite_book(title):
    print (f"One of my favorite books is {title}!")
favorite_book("The Giver")

#8-3 T-Shirt 
def make_shirt(size, text):
    print (f"\nMy shirt size is {size}.")
    print (f"I'd like my shirt to say {text}!")
make_shirt (size='medium', text='Soccer Dad') #Keyword Argument
make_shirt('medium', 'Soccer Dad') #Positional Argument 

#8-4 Large Shirts 
def make_shirt(size= 'large', text= 'I love Python'):
    print (f"\nThe shirt size is {size}.")
    print (f"I'd like my shirt to say {text}!")
make_shirt()
make_shirt('medium')
make_shirt('small', 'Cool Soccer Dad')

#8-5 Cities 
def describe_city(name, country= "Spain"):
    print (f"{name} is in {country}!")
describe_city('Barcelona') 
describe_city('New York') 
describe_city('Sevilla') 

#8-6 City Names 
def city_country(city, country):
    city_pair = (f"{city}, {country}")
    return city_pair.title()
city_final1 = city_country('\nparis', 'france')
city_final2 = city_country('barcelona', 'spain')
city_final3 = city_country('michoacan', 'mexico')

print (city_final1)
print (city_final2)
print (city_final3)

#8-7 Album 
def make_album (artist_name, album_title, songs=None):
    description = {'name': artist_name, 'title': album_title}
    if songs:
        description['songs'] = songs
    return description

artist = make_album ('J. Cole', 'KOD', songs=12)
print (artist)

#8-8 User Albums 
def make_album (artist_name, album_title, songs=None):
    description = {'name': artist_name, 'title': album_title}
    return description

while True:
    print ("\nInsert album's artist and title:")
    print ("(enter 'q' at any time to quit)")

    a_name = input('Artist name:')
    if a_name == 'q':
        break
    
    a_title = input ('Album title:')
    if a_title == 'q':
        break

    artist = make_album (a_name, a_title)
    print (artist)

#8-9 Messages 
messages = ['Hi there!', 'I miss you', "How's it going?"]

def show_messages(message_list):
    for message in message_list:
        print (message)
show_messages(messages)

#8-10 Sending Messages 
messages = ['Hi there!', 'I miss you', "How's it going?"]
sent_messages = []

def send_messages (message_list, sent_list): 
    while message_list:
        current_message = message_list.pop(0)
        print (f"Sending message: {current_message}")
        sent_list.append(current_message)

send_messages(messages, sent_messages)

#8-11 Archived Messages 
messages = ['Hi there!', 'I miss you', "How's it going?"]
sent_messages = []

def send_messages (message_list, sent_list): 
    while message_list:
        current_message = message_list.pop(0)
        print (f"Sending message: {current_message}")
        sent_list.append(current_message)

send_messages(messages[:], sent_messages)

print ("\nOriginal messages list:", messages)
print ("Sent messages:", sent_messages)

#8-12 Sandwiches 
def make_sandwich (*items):
    print ("\nMaking a sandwich with the following items:")
    for item in items:
        print (f"- {item}")
    print ("Your sandwich is ready!")

make_sandwich("ham", 'cheese')
make_sandwich('peanut butter', 'jelly')
make_sandwich('turkey', 'lettuce', 'tomato')

#8-13 User Profile 
def build_profile (first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'Darwyn', 'Avila',
    location = 'Reading',
    sport = 'soccer',
    hobby = 'spending time with girlfriend')

print (my_profile)

#8-14 Cars 
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car = make_car('buick', 'regal', color='white', tow_package=True)

print (car)
