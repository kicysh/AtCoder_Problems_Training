# 1: abc136_d
def problem_1():
    s = input()
    r,l = 0,0
    p = 0
    ans = [0]*len(s)
    s = s+'R'
    for si in range(len(s)-1):
        if s[si:si+2]=='RR':
            r +=1
        elif s[si:si+2]=='LL':
            l +=1
        elif s[si:si+2]=='RL':
            p = si
            ans[p]+=(r+2)//2
            ans[p+1]+=(r+1)//2
        elif s[si:si+2]=='LR':
            ans[p]+=(l+1)//2
            ans[p+1]+=(l+2)//2
            r,l = 0,0 
    print(('{} '*len(ans[:-1])).format(*ans[:-1])+str(ans[-1]))
