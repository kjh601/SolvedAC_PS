from collections import Counter
from sys import stdout
write = stdout.write

inputs = open(0).read().split()
eng_dict = Counter([word for word in inputs[2:]
                   if len(word) >= int(inputs[1])])

result = list(eng_dict.items())
result.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, num in result:
    write(word+'\n')
