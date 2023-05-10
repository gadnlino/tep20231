import math

t = []

string = ''

def build(i, l, r):
    if(l == r):
        t[i] = 0 if string[l] == '0' else 1
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

def update_inverse(i, l, r, ul, ur):
    if(l != r):
        m = math.floor((l+r)/2)

        update_inverse(2*i, l, m, ul, ur)
        update_inverse(2*i+1, m+1, r, ul, ur)

        t[i] = t[2*i] + t[2*i + 1]
    elif(ul <= l and l <= ur):
        t[i] = not(t[i])

def query_sum(i, l, r, ql, qr):
    if(ql <= l and r <= qr):
        return t[i]
    
    if(l > qr or r < ql):
        return 0

    m = math.floor((l+r)/2)

    return query_sum(2*i, l, m, ql, qr) + query_sum(2*i+1, m+1, r, ql, qr)



ntests = int(input())

for test in range(ntests):
    print(f'Case {test  + 1}:')
    
    nparts = int(input())

    string = ''

    print('prebuildstring')

    for __ in range(nparts):
        times = int(input())
        part = str(input())

        for __ in range(times):
            string += part
    
    print('postbuildstring')
    
    t = [0 for i in range(4*len(string))]

    #print('prebuild')

    build(1, 0, len(string)-1)

    #print('postbuild')

    nqueries = int(input())
    qcount = 0

    for __ in range(nqueries):
        args = str(input()).split(" ")
        q = args[0]
        ul = int(args[1])
        ur = int(args[2])

        if(q == 'F'):
            update(1, 0, len(string)-1, ul, ur, 1)
        elif(q == 'E'):
            update(1, 0, len(string)-1, ul, ur, 0)
        elif(q == 'I'):
            update_inverse(1, 0, len(string)-1, ul, ur)
        elif(q == 'S'):
            qcount += 1
            result = query_sum(1, 0, len(string)-1, ul, ur)
            print(f'Q{qcount}: {result}')
            pass