# https://www.youtube.com/watch?v=tZC_530jbWg

ntests = int(input())

for _ in range(ntests):
    mapp = {}

    nno = int(input())

    numbers = list(map(lambda x : int(x), input().split(" ")))

    for n in numbers:
        if(n not in mapp):
            mapp[n] = 1
        else:
            mapp[n] = mapp[n] + 1

    result = 'YES'

    if((0 in mapp and 1 in mapp) or (1 in mapp and 2 in mapp)):
        result = 'NO'
    elif((1 in mapp and mapp[1] == nno) or (1 not in mapp)):
        result = 'YES'
    else:
        for k, v in mapp.items():
            if(k-1 in mapp):
                result = 'NO'
                break
    
    print(result)