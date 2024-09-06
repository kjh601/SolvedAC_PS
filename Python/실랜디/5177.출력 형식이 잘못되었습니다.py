from sys import stdin
input = stdin.readline

def normalize(string: str) -> str:
    string = string.strip()
    arr = []
    for i in range(len(string)):
        if len(arr) and string[i] in {'(', ')', '[', ']', '{', '}', '.', ',', ';', ':'} and arr[-1] == ' ':
            arr.pop()
            
        if string[i] in {'{', '['}:
            arr.append('(')
        elif string[i] in {'}', ']'}:
            arr.append(')')
        elif string[i].isupper():
            arr.append(string[i].lower())
        elif string[i] == ';':
            arr.append(',')
        elif len(arr) and arr[-1] == ' ' and string[i] == ' ':
            continue
        elif len(arr) and arr[-1] in {'(', ')', '[', ']', '{', '}', '.', ',', ';', ':'} and string[i] == ' ':
            continue
        else:
            arr.append(string[i])
    return ''.join(map(str, arr))

K = int(input())
results = []
for i in range(K):
    
    str1 = normalize(input())
    str2 = normalize(input())
    tmp = ''
    if str1 == str2:
        results.append(f'Data Set {i+1}: equal')
    else:
        results.append(f'Data Set {i+1}: not equal')
print('\n\n'.join(results))