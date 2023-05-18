#https://www.baeldung.com/java-least-common-multiple#:~:text=Using%20the%20Euclidean%20Algorithm,-There's%20an%20interesting&text=As%20stated%2C%20gcd(a%2C,gcd(a%2Cb).

def gcd(n1, n2):
    while(n1 % n2 > 0):
        r = n1 % n2
        n1 = n2
        n2 = r
    
    return n2


while True:
    try:
        args = list(map(lambda x : int(x), input().split(" ")))

        a = args[0]
        b = args[1]

        gc = gcd(max(a, b), min(a, b))

        if()
    except EOFError:
        break