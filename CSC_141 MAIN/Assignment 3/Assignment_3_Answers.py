#Darwyn Avila-Medina
#3-1 Names
Names = ['Angel', 'Jairo', 'Ramirez', 'Alex']
print(Names[0])
print(Names[1])
print(Names[2])
print(Names[3])
#3-2 Greetings 
message0 = f"How's it going {Names[0].title()}?"
message1 = f"How's it going {Names[1].title()}?"
message2 = f"How's it going {Names[2].title()}?"
message3 = f"How's it going {Names[3].title()}?"
print(message0)
print(message1)
print(message2)
print(message3)
#3-3 My Own List
vehicle = ['Buick', 'Toyota Camry', 'Chevy Suburban']
print(f"I drive my {vehicle[0]} to class.")
print (f"My father drives a {vehicle[1]}.")
print (f"We have a {vehicle[2]} that we use as a family car.")
#3-4 Guest List 
people = ["Cristiano Ronaldo", "Leonel Messi", "Hugo Sanchez"]
message_ronaldo = (f"Hello {people[0]}, how are you? It would be my honor if you woud attend this lovely dinner on Friday at 6PM.")
message_messi = (f"Good Afternoon {people[1]}. I invite you to come out and eat with a couple friends this Friday at 6PM.")
message_hugo = (f"{people[2]} como estas? Estas invitado a una cena de amigos este viernes a las 6PM por si gustas acompanarnos!")
print (message_ronaldo)
print (message_messi)
print (message_hugo)
#3-5 Guest Change
print(f"{people[2]} can't make it")
people[2] = "Pele"
print(people)
message_ronaldo = (f"Hello {people[0]}, how are you? It would be my honor if you woud attend this lovely dinner on Friday at 6PM.")
message_messi = (f"Good Afternoon {people[1]}. I invite you to come out and eat with a couple friends this Friday at 6PM.")
message_pele = (f"{people[2]} how are you? You are invited to have dinner with some friends this Friday at 6PM if you'd like to join us!")
print (message_ronaldo)
print (message_messi)
print (message_pele)
#3-6 Additional Guests
print("I have found a bigger table and have invited three more guests to join us!")
people.insert(0, "Neymar")
people.insert(2, "Zidane")
people.append("Xavi")
message_ronaldo = (f"Hello {people[1]}, you are cordially invited to attend a dinner party this Friday at 6PM!")
message_messi = (f"Hello {people[3]}, you are cordially invited to attend a dinner party this Friday at 6PM!")
message_pele = (f"Hello {people[4]}, you are cordially invited to attend a dinner party this Friday at 6PM!")
message_neymar = (f"Hello {people[0]}, you are cordially invited to attend a dinner party this Friday at 6PM!")
message_zidane = (f"Hello {people[2]}, you are cordially invited to attend a dinner party this Friday at 6PM!")
message_xavi = (f"Hello {people[5]}, you are cordially invited to attend a dinner party this Friday at 6PM!")
print (f"\n{message_neymar}\n{message_ronaldo}\n{message_zidane}\n{message_messi}\n{message_pele}\n{message_xavi}")
#3-7 Shrinking Guest List
print("I apologize for the inconvenience, however, I can only have two guests for this dinner.")
popped_people1 = people.pop(0)
popped_people2 = people.pop(2)
popped_people3 = people.pop(1)
popped_people4 = people.pop()
print(popped_people1)
print("I'm sorry my friend but you are officially uninvited to the dinner.")
print(popped_people2)
print("I'm sorry my friend but you are officially uninvited to the dinner.")
print(popped_people3)
print("I'm sorry my friend but you are officially uninvited to the dinner.")
print(popped_people4)
print("I'm sorry my friend but you are officially uninvited to the dinner.")
message_cristiano = people[0]
message_brazil = people [1]
print (message_cristiano,"you are still invited to the dinner my friend!")
print (message_brazil,"you are still invited to the dinner my friend!")
del people[0]
del people
#print(people)
#3-8
places = ['Spain', 'England', 'Italy', 'Japan', 'Hawaii']
print(places)
print(sorted(places))
print(places)
places.sort(reverse=True)
print(places)
places.reverse
print(places)
#3-9
people0 = 'Alex', 'Ramirez', 'Angel'
print (len(people0))
#3-10
team = 'United', 'City', 'Madrid', 'Barca'
print(team[0])
message_united = f"My favorite team is Manchester {team[0].title()}!"
print (message_united)
print(sorted(team))
print(team)
#3-11
#print(sorted(team)(places))
print (f"\n{sorted(team)}\n{sorted(places)}")