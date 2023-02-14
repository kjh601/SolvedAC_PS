N = int(input())
X = list(map(int, input().split()))
X_dict = {value : idx for idx, value in enumerate(sorted(set(X)))}
print(' '.join(map(str, [X_dict[value] for value in X])))