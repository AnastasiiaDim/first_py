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

# NO OFFSET GIVEN
coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(1, 26):
    candidate_message = caesar_decode(coded_message, i)
    if "the" in candidate_message or "and" in candidate_message:
        print(f"Offset {i}: {candidate_message}")

# Vigenere Cipher

def vigenere_cipher(message, key, mode):
    result = []
    key_index = 0
    for char in message.lower():
        if char in ALPHABET:
            key_char = key[key_index % len(key)]
            shift = ALPHABET.index(key_char)
            message_index = ALPHABET.index(char)
            if mode == "decode".lower():
                new_index = (message_index - shift) % 26
            else:
                if mode == "encode".lower():
                    new_index = (message_index + shift) % 26
            new_letter =ALPHABET[new_index]
            result.append(new_letter)
            key_index += 1
        else:
            if char not in ALPHABET:
                result.append(char)

    return "".join(result)

print(vigenere_cipher("txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!", "friends", "encode"))
print(vigenere_cipher("As a bonus, try calling your decoder function on the result of your encryption function. You should get the original message back!", "dog", "decode"))
print(vigenere_cipher("xe u yahre, nok wxxffza vaoo pyzaxbd zrzwquik ah qty oqmrxn lr slgl bzwokjquik rokonfah. vao ptirxx dqn qty ldcduhxx gbemxsy ymwh!", "dog", "encode"))

