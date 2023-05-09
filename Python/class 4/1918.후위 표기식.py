from sys import stdout
o = stdout.write

s = []
for ch in input():
    if ch.isalpha():
        o(ch)
    elif ch == ')':
        while True:
            t = s.pop()
            if t == '(':
                break
            o(t)
    else:
        if ch in "+-" and s and s[-1] != '(':
            while s and s[-1] != '(':
                o(s.pop())
        elif ch in "*/" and s and s[-1] in "*/":
            o(s.pop())
        s.append(ch)
while s:
    o(s.pop())
