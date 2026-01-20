capitals = {"USA": "Washington D.C",
            "Ukraine": "Kyiv",
            "Spain": "Madrid"
            }

capital = input("Enter your key (country): ")

if capital in capitals:
    print(capitals[capital])
else:
    print("Key not found")