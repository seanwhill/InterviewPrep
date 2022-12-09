def maxWeight(packages):
    
    size = len(packages)
    res = [0 for i in range(size)]

    res[-1] = packages[-1]

    for i in range(size - 2, -1, -1):
        if packages[i] < res[i + 1]: #merge
            res[i] = packages[i] + res[i + 1]
        else: #leave
            res[i] = packages[i]

    return max(res)


print(f"Input: {[2, 9, 10, 3, 7]}")
print(f"Expected: 21\nResult: {maxWeight([2, 9, 10, 3, 7])}")


print(f"Input: {[4, 0]}")
print(f"Expected: 4\nResult: {maxWeight([4, 0])}")

print(f"Input: {[4]}")
print(f"Expected: 4\nResult: {maxWeight([4])}")

print(f"Input: {[4]}")
print(f"Expected: 4\nResult: {maxWeight([4])}")

print(f"Input: {[20, 13, 8, 9]}")
print(f"Expected: 50\nResult: {maxWeight([20, 13, 8, 9])}")