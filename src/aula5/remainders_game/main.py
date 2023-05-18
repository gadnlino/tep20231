while True:
    try:
        
        args = list(map(lambda x : int(x), input().split(" ")))
 
        k = args[1]
 
        numbers = list(map(lambda x : int(x), input().split(" ")))
 
        numbers.sort(reverse=True)

        result = 'No'
        
        for nn in numbers:
            if(nn < k):
                break
 
            if(nn % k == 0):
                result = 'Yes'
                break
 
        print(result)
    except EOFError:
        break