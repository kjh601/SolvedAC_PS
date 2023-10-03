import sys
input = sys.stdin.readline
write = sys.stdout.write


def recursive(n):
    global string

    if n == 0:
        string += '-'
    else:
        recursive(n-1)
        spaces = ' '*len(string)
        string += spaces+string


while True:
    try:
        string = ""
        recursive(int(input()))
        write(string+'\n')
    except:
        break
