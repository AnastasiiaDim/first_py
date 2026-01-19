capitals = {"USA": "Washington D.C",
            "Ukraine": "Kyiv",
            "Spain": "Madrid"
            }

capital = input("Enter your key (country): ")

if capital in capitals:
    print("Key found")
else:
    print("Key not found")