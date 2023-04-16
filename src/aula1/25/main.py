def d25(strr: str):
    result = True

    ending = strr[len(strr)-2:len(strr)]

    return ending in ['00', '25', '50', '75']

def get_d25_steps(strr: str, actual_steps: int):
    
    if(d25(strr)):
        return actual_steps
    
    minn = 100000000

    for i in range(0, len(strr)):
        new_str = (strr[0:i] + strr[i+1:len(strr)]).lstrip('0')

        minn = min(minn, get_d25_steps(new_str, actual_steps + 1))

        #print('new_str', new_str, 'minn', minn)
    
    return minn


ntests = int(input())

for __ in range(0, ntests):
    nstr = input()

    s = get_d25_steps(nstr, 0)

    print(s)