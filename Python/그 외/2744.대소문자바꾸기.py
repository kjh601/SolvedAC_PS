string = ""

for ch in list(input().rstrip()):
    if ch.isupper():
        string += ch.lower()
    else :
        string += ch.upper()

print(string)