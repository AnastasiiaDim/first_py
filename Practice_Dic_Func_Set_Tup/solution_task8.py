main = (("Title", "App"), ("Version", 3.14), ("Debug", True))

def print_config(data):
    for key, value in data:
        print(f"Setting: {key} is set to {value}.")

print_config(main)