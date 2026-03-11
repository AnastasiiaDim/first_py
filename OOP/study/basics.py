class Robot:
    def __init__(self, name, color, weight): #givenName, givenColor...
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)
        print("I am " + self.color)
        print(f"I am {self.weight} lbs")
        print("_______________________")

# r1 = Robot()
# r1.name = "SlimShady"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Marshall"
# r2.color = "blue"
# r2.weight = 30

r1 = Robot("SlimShady", "red", 30)
r2 = Robot("Marshall", "blue", 30)

r1.introduce_self()
r2.introduce_self()
