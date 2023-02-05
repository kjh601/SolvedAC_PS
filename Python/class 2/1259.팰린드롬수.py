"""Module providingFunction printing python version."""

while True:
    arr = input()
    if arr == '0':
        break
    if arr=="".join(ch for ch in arr[::-1]):
        print("yes")
    else :
        print("no")
