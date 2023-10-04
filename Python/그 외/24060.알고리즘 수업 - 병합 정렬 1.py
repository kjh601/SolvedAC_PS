def merge_sort(A, p, r, saved, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, saved, K)
        merge_sort(A, q + 1, r, saved, K)
        merge(A, p, q, r, saved, K)


def merge(A, p, q, r, saved, K):
    i = p
    j = q + 1
    t = 1
    tmp = [0] * (r - p + 2)

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

        if len(saved) < K:
            saved.append(tmp[t - 1])

    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1
        if len(saved) < K:
            saved.append(tmp[t - 1])

    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1
        if len(saved) < K:
            saved.append(tmp[t - 1])

    i = p
    t = 1
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
saved = []

merge_sort(A, 0, N-1, saved, K)

print(saved[K-1] if len(saved) >= K else -1)
