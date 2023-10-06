from collections import Counter
import sys

n = int(sys.stdin.readline())
counter = Counter(map(int, [sys.stdin.readline()
                  for _ in range(n)])).most_common()
most_common_value = counter[0][1]

result = float('inf')
for num, count in counter:
    if count != most_common_value:
        break
    result = min(result, num)

print(result)
