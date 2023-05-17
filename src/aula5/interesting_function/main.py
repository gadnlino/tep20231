# https://www.youtube.com/watch?v=33SidTjF2tc

import math

ntests = int(input())

for _ in range(ntests):
    args = input().split(" ")
    
    l = int(args[0].strip())
    r = int(args[1].strip())

    max_len = max(len(args[0]), len(args[1]))

    lf = args[0].zfill(max_len)
    rf = args[1].zfill(max_len)

    diff = r - l

    tens = 10

    for _ in range(max_len):
        diff += (math.floor(r/tens) - math.floor(l/tens))
        tens *= 10
    
    print(diff)