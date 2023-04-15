ntests = int(input())

for __ in range(0, ntests):
    nnumbers = int(input())

    numbers = list(map(lambda x : int(x), input().split(" ")))

    #print(numbers)

    ans = 'YES'

    if(len(numbers) == 1 and numbers[0] == 1):
        ans = 'YES'
    else:
        maxi = max(numbers)
        idx_maxi = list(filter(lambda i : numbers[i] == maxi, range(0, nnumbers)))
        old_idx_maxi = idx_maxi.copy()

        while(maxi > 0):
            if(len(idx_maxi) > 1):
                others = list(filter(lambda i: i not in idx_maxi, range(0, nnumbers)))
                next_maxi = 0 if len(others) == 0 else max(list(map(lambda i: numbers[i], others)))

                for idx in idx_maxi:
                    numbers[idx] = numbers[idx] - (maxi - next_maxi)
            else:
                numbers[idx_maxi[0]] = numbers[idx_maxi[0]] - 1
            
            old_idx_maxi = idx_maxi.copy()

            maxi = max(numbers)
            idx_maxi = list(filter(lambda i : numbers[i] == maxi, range(0, nnumbers)))

            if(len(idx_maxi) == 1 and len(old_idx_maxi) == len(idx_maxi) and idx_maxi[0] == old_idx_maxi[0]):
                ans = 'NO'
                break
    
    print(ans)