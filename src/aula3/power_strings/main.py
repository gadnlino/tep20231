def prefix_function(s) :
    n = len(s)
    pi = [0 for i in range(n)]
    for i in range(n):
        j = pi[i-1]
        while (j > 0 and s[i] != s[j]):
            j = pi[j-1]
        if (s[i] == s[j]):
            j += 1
        pi[i] = j
    
    return pi

def get_ans(s):
    n = len(s)

    pi = prefix_function(s)
    
    ans = [0 for i in range(n+1)]

    for i in range(n):
        ans[pi[i]]+=1
    for i in range(n-1, 0,-1):
        ans[pi[i-1]] += ans[i]
    for i in range(n+1):
        ans[i]+=1
    
    return ans


s = "ababab"

print(get_ans(s))