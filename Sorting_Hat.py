gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q_1 = int(input("Q1) Do you like Dawn or Dusk?      1) Dawn      2) Dusk     "))

if q_1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q_1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong Input")

q_2 = int(input("Q2) When I’m dead, I want people to remember me as:    1) The Good      2) The Great     3) The Wise    4) The Bold  "))

if q_2 == 1:
    hufflepuff += 2
elif q_2 == 2:
    slytherin += 2
elif q_2 == 3:
    ravenclaw += 2
elif q_2 == 4:
    gryffindor += 2
else:
    print("Wrong Input")

q_3 = int(input("Q3) Which kind of instrument most pleases your ear?   1) The violin    2) The trumpet    3) The piano    4) The drum  "))
if q_3 == 1:
    slytherin += 4
elif q_3 == 2:
    hufflepuff += 4
elif q_3 == 3:
    ravenclaw += 4
elif q_3 == 4:
    gryffindor += 4
else:
    print("Wrong Input")

houses = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

print(houses)

