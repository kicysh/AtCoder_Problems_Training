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


# 4: abc048_b
def problem_4():
    a,b,x = map(int,input().split())
    print(b//x-(a-1)//x)


# 5: abc141_d
def problem_5():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    while m>0:
        a[0] //= 2
        m -=1
        i = 1
        while m>0 and i<n and a[i]>a[0]:
            a[i] //=2
            m -= 1
            i += 1
        a.sort(reverse=True)
    print(sum(a))


# 6: abc076_c
def problem_6():
    s = input()
    t = input()
    ans = 'UNRESTORABLE'
    if len(s)<len(t):
        print(ans)
    elif t in s:
        print(s.replace('?','a'))
    else:
        for si in range(len(s)-len(t),-1,-1):
            flag = True
            for ti in range(len(t)):
                if not (t[ti]==s[si+ti] or s[si+ti]=='?'):
                    flag = False
                    break
            if flag:
                s = s.replace('?','a')
                ans = s[:si]+t+s[si+len(t):]
                break
        print(ans)


# 7: abc127_d
def problem_7():
    n,m = map(int,input().split())
    *a, = map(int,input().split())
    cb = list()
    for _ in [0]*m:
        b,c = map(int,input().split())
        cb.append([c,b])
    a.sort()
    cb.sort(reverse=True)
    cnt = 0
    for c,b in cb:
        i = 0
        while (c>a[cnt+i])&(i<b):
            a[cnt+i] = c
            i +=1
            if (cnt+i)==n:
                break
        cnt += i
        if cnt==n:
            break
    print(sum(a))


# 8: abc148_e
def problem_8():
    n = int(input())
    if n%2==1:
        print(0)
    else:
        ans = 0
        d = 10
        while d<=n:
            ans += n//d
            d *=5
        print(ans)


# 9: abc054_b
def problem_9():
    n,m = map(int,input().split())
    a = [input() for _ in [0]*n]
    b = [input() for _ in [0]*m]
    ans = 'No'
    flag = False
    for ai in range(n-m+1):
        for aj in range(n-m+1):
            for bi in range(m):
                if a[ai+bi][aj:aj+m] != b[bi]:
                    break
                if bi==m-1:
                    flag = True
                    ans='Yes'
            if flag:
                break
        if flag:
            break
    print(ans)


# 10: abc130_d
def problem_10():
    n,k = map(int,input().split())
    *a, = map(int,input().split())
    s = 0
    tmp = 0
    ans = 0
    for i in range(n):
        if s<k:
            for j in range(max(i,tmp),n):
                s += a[j]
                tmp = j+1
                if s>=k:
                    ans += n-j
                    break
        else:
            ans += n-j
        s -=a[i]
    print(ans)
