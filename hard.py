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


# 2: jsc2019_qual_b
def problem_2():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    INF = 10**9+7
    ans = 0
    for ai in range(n-1,-1,-1):
        cnt = 0
        for aj in range(n-1,-1,-1):
            if ai==aj:
                ans = (ans+cnt*k)%INF
            elif a[ai]>a[aj]:
                cnt +=1
        ans += cnt*k*(k-1)//2
        ans %=INF
    print(ans)
