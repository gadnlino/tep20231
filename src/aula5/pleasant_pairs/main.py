ntests = int(input())

for _ in range(ntests):
    n = int(input())

    numbers = list(map(lambda x : int(x), input().split(" ")))

    numbers.sort(reverse=True)

    maxx = numbers[0]

    count = 0

    for i in range(n):
        l = n-i-1

        if(i+1 + l + 1 == numbers[i]*numbers[l]):
            count += 1

    print(count)