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
