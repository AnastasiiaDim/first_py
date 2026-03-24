ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def caesar_decode(message, offset):
    result = []
    for char in message.lower():
        if char in ALPHABET:
            original_index = ALPHABET.index(char)
            new_index = (original_index - offset) % 26
            result.append(ALPHABET[new_index])
        else:
            result.append(char)
    return "".join(result)
def caesar_encode(message, offset):
    return caesar_decode(message, -offset)

print(caesar_decode("hello!", 3))
print(caesar_encode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))
