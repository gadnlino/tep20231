ntests = int(input())

for __ in range(0, ntests):
    nnumbers = int(input())

    numbers = list(map(lambda x : int(x), input().split(" ")))

    #print(numbers)

    ans = 'YES'

    numbers.sort(reverse=True)
    
    if(nnumbers == 1 and numbers[0] == 1):
        ans = 'YES'
    elif(nnumbers == 1 and numbers[0] > 1):
        ans = 'NO'
    elif(numbers[0] - numbers[1] > 1):
        ans = 'NO'

    print(ans)