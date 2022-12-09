#net power consumption = max booting power among k processors + (Sum of processing power of processors) * k
# max(boot) + (sum(proccessing) * len(boot))
#power Max


from collections import deque



def maxPower(maxBootingPower, sumProcessing, lenBoot):
    power = maxBootingPower + (sumProcessing * lenBoot)
    # print("POWER: ", power)
    return power


# sumProcess: 9
# queue: 10


def maxCluster(bootingPower, processingPower, powerMax):


    maxCluster = l =  sumProcessing = 0

    # add sliding windows to the Deque and keep track of the highest value in the window. When l moves make sure to pop the queue
    decQ = deque([])

    for r in range(len(bootingPower)):

        sumProcessing += processingPower[r]

        while decQ and bootingPower[decQ[-1]] < bootingPower[r]:
            decQ.pop()
        decQ.append(r)
        
        # print("SUM: ", sumProcessing)
        # print("l", l)
        # print("r", r)
        # print(decQ)
        while ( l <= r and maxPower(bootingPower[decQ[0]], sumProcessing,  r - l + 1)) > powerMax:
            # print("ITERATING THORUGH LOOP")
            sumProcessing -= processingPower[l]
            l += 1
            if decQ[0] < l:
                decQ.popleft()



        maxCluster = max(maxCluster, r - l + 1)
        # print("MAX", maxCluster)

    return maxCluster


bootingPowers = [3, 6, 1, 3, 4]
processingPowers = [2, 1, 3, 4, 5]
powerMax = 25
print(maxCluster(bootingPowers, processingPowers, powerMax))


bootingPowers = [8, 8, 10, 9, 12]
processingPowers = [4, 1, 4, 5, 3]
powerMax = 33

print(maxCluster(bootingPowers, processingPowers, powerMax))