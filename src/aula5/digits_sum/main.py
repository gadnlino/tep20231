import math

ntests = int(input())
for __ in range(ntests):
    n = int(input())

    result = math.floor((n+1)/10)
    print(result)