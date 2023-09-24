import sys
write = sys.stdout.write

for i in range(int(input()), 0, -1):
    write('*'*i+'\n')
