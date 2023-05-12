import math

a = []
t = []

def build(i, l, r):
    if(l == r):
        t[i] = a[l]
    else:
        m = math.floor((l+r)/2)
        build(2*i, l, m)
        build(2*i + 1, m+1, r)

        t[i] = t[2*i] + t[2*i + 1]

def update(i, l, r, ul, ur, val):
    if(l != r):
        m = math.floor((l+r)/2)

        update(2*i, l, m, ul, ur, val)
        update(2*i+1, m+1, r, ul, ur, val)

        t[i] = t[2*i] + t[2*i + 1]
    elif(ul <= l and l <= ur):
        t[i] = val

def query(i, l, r, ql, qr):
    if(ql <= l and r <= qr):
        return t[i]
    
    if(l > qr or r < ql):
        return 0

    m = math.floor((l+r)/2)

    return query(2*i, l, m, ql, qr) + query(2*i+1, m+1, r, ql, qr)

while True:
    try:
        args = list(map(lambda x : int(x), str(input()).split(" ")))
        n = args[0]
        m = args[1]

        a = [0 for i in range(n)]
        t = [0 for i in range(4*n)]

        #build(1, 0, len(a)-1)

        for __ in range(m):
            fight = list(map(lambda x : int(x), str(input()).split(" ")))
            ul = fight[0]
            ur = fight[1]
            winner = fight[2]

            update(1, 0, len(a)-1, ul, ur, winner)

        for i in range(n):
            r = query(1, 0, len(a)-1, i, i)
            print(r)

    except EOFError:
        break

