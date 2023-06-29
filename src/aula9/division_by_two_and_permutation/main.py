#https://codeforces.com/blog/entry/101380
import math

ntests = int(input())

for _ in range(ntests):
    n = int(input())

    numbers = list(map(lambda x : int(x), input().split(" ")))

    numbers.sort(reverse=True)

    used = [False] * (n+1)

    ok = True

    for no in numbers:
        x = no

        while (x > n or used[x]):
            x = math.floor(x/2)
        
        if (x > 0):
            used[x] = True
        else:
            ok = False
            break
    
    result = 'YES' if ok else 'NO'

    print(result)