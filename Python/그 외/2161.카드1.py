from collections import deque

N = int(input())

cards = deque(range(1, N + 1))

discarded_cards = []

while len(cards) > 1:
    discarded_cards.append(cards.popleft())
    cards.append(cards.popleft())

print(' '.join(map(str, discarded_cards + list(cards))))
