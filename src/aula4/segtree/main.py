N = 4

a = [1 for i in range(N)]

t = [0 for i in range(4*N)]

def build(i, l, r):
    if(l == r):
        t[i] = a[l]
    else:
        m = int((l+r)/2)
        build(2*i, l, m)
        build(2*i + 1, m+1, r)

        t[i] = t[2*i] + t[2*i + 1]

def update(i, l, r, ul, ur, val):
    #print(i, l, r, ul, ur, val)
    # if(ul < l or ur > r):
    #     print('caso 1')
    #     return

    if(l != r):
        #print('caso 3')
        m = int((l+r)/2)

        update(2*i, l, m, ul, ur, val)
        update(2*i+1, m+1, r, ul, ur, val)

        t[i] = t[2*i] + t[2*i + 1]
    elif(ul <= l and l <= ur):
        #print('caso 2')
        t[i] = val
    
def query_sum(i, l, r, ql, qr):
    #print(i, l, r, ql, qr)
    if(ql <= l and r <= qr):
        #print('caso 1')
        return t[i]
    
    if(l > qr or r < ql):
        #print('caso 2')
        return 0

    m = int((l+r)/2)

    #print('caso 3') 
    return query_sum(2*i, l, m, ql, qr) + query_sum(2*i+1, m+1, r, ql, qr)


build(1, 0, len(a)-1)
update(1, 0, len(a)-1, 1, 3, 3)

print(query_sum(1, 0, len(a)-1, 1, 3))
