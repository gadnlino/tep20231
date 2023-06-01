#https://www.baeldung.com/java-least-common-multiple#:~:text=Using%20the%20Euclidean%20Algorithm,-There's%20an%20interesting&text=As%20stated%2C%20gcd(a%2C,gcd(a%2Cb).
#https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2012/1155_English.htm

import math

def gcde(a, b, d, x, y):
    if (b == 0):
        d = a
        x = 1
        y = 0

        return a, b, d, x, y

    _, _, d, x, y = gcde(b, a % b, d, x, y)

    s = y
    y = x - math.floor((a / b)) * y
    x = s

    return a, b, d, x, y

while True:
    try:
        args = list(map(lambda x : int(x), input().split(" ")))

        a = args[0]
        b = args[1]

        a, b, d, x, y = gcde(a, b, a, 0, 0)

        print(x, y, d)
    except EOFError:
        break