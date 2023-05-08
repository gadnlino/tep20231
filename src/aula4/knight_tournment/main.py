import math

def build_segment_tree(t, a, v, tl, tr):
    if(tl == tr):
       t[v] = a[tl]
    else:
        tm = math.floor((tl + tr)/2)
        build_segment_tree(t, a, 2*v, tl, tm)
        build_segment_tree(t, a, 2*v + 1, tm+1, tr)
        t[v] = t[2*v] + t[2*v+1]
def update_segment_tree(t, v, tl, tr, new_val):
    if(tl == tr):
        t[v] = new_val
    else:
        tm = math.floor((tl + tr)/2)

        update_segment_tree(t, 2*v, tl, tm, new_val)
        update_segment_tree(t, 2*v+1, tm+1, tr, new_val)

def query_segment_tree(t, v, tl, tr, i):
    print(t, v, tl, tr, i)

    value = None
    if(tl == tr):
        value = t[v]
    else:
        tm = math.floor((tl + tr)/2)

        if(i <= tm):
            value = query_segment_tree(t, v, tl, tm, i)
        else:
            value = query_segment_tree(t, v, tm+1, tr, i)

    return value

while True:
    try:
        args = list(map(lambda x : int(x), str(input()).split(" ")))
        n = args[0]
        m = args[1]

        a = [0 for i in range(n)]
        t = [0 for i in range(4*n)]

        build_segment_tree(t, a, 1, 0, n-1)

        for __ in range(m):
            fight = list(map(lambda x : int(x), str(input()).split(" ")))
            l = fight[0]
            r = fight[1]
            winner = fight[2]

            update_segment_tree(t, 1, l-1, r-1, winner)
        for i in range(n):
            r = query_segment_tree(t, 1, 0, n-1, i)
            print(r)

    except EOFError:
        break

