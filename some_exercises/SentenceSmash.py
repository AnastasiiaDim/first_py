# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
def smash(words):
sentence = "['hello', 'world', 'this', 'is', 'great']"
for word in words:
    if sentence != "":
        sentence += " "
        sentence += word
    return sentence.strip()
    
