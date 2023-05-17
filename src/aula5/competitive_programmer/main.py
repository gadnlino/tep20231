#https://github.com/SaruarChy/Codeforces-Solution/blob/master/1266%20A.%20Competitive%20Programmer.cpp

# endings = ['00', '20', '40', '80']

ntests = int(input())

for _ in range(ntests):
    nstr = input()

    s = 0
    c_even = 0
    c_zeros = 0

    for c in nstr:
        ic = int(c)

        s += ic

        if(ic % 2 == 0):
            c_even += 1
        
        if(ic == 0):
            c_zeros += 1

    multiple_3 = s % 3 == 0

    result = 'red' if multiple_3 and c_zeros > 0 and c_even>=2 else 'cyan'

    # has_endings = False

    # for e in endings:
    #     if(e == '00'):
    #         has_endings = nstr.count('0') >= 1
    #     elif(e[0] in nstr and e[1] in nstr):
    #         has_endings = True
    #         break
            
    # result = 'cyan'

    # if(s == 0):
    #     result = 'red'
    # elif(multiple_3 and has_endings):
    #     result = 'red'

    # print(multiple_3, has_endings, nstr)

    print(result)