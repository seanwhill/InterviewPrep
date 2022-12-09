def solution(A, K):
    n = len(A)
    best = 0
    count = 1
    for i in range(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            count = 1
        best = max(best, count)
    result = min(max(best + K, K + 1), n)
    return result


solution([1, 2], 1) #best would be 0 in this case. Need the K + 1