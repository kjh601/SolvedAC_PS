string = input().rstrip()

stack = []

result = ""


def reverse_stack():
    global result, stack
    result += ''.join(reversed(stack))
    stack = []


is_tag = False
for ch in string:
    if ch == '<':
        reverse_stack()
        is_tag = True
        stack.append('<')

    elif ch == '>':
        stack.append('>')
        result += ''.join(stack)
        stack = []
        is_tag = False

    elif ch == ' ' and not is_tag:
        reverse_stack()
        result += ' '

    else:
        stack.append(ch)

print(result+''.join(reversed(stack)))
