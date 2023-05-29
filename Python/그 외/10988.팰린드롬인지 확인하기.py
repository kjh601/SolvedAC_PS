string = input().rstrip()
length = len(string)-1

is_palindrome = 1
for i in range((length+1)//2):
    if string[i] != string[length-i]:
        is_palindrome = 0
        break

print(is_palindrome)
