while True:
    try:
        
        args = list(map(lambda x : int(x), input().split(" ")))

        numbers = list(map(lambda x : int(x), input().split(" ")))

        prod = 1

        print('pre loop')

        for i in numbers:
            prod = prod * i
        
        print('post loop')
        
        mod = prod % args[1]

        result = 'Yes' if mod == 0 else 'No'

        print(result)
    except EOFError:
        break