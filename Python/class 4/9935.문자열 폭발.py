import sys

print = sys.stdout.write

string = input().rstrip()
bomb = input().rstrip()
bomb_char = bomb[-1]
stack = []
bomb_len = len(bomb)

for char in string:
    stack.append(char)
    if char == bomb_char and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)
