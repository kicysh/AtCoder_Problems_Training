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


# 11: abc142_d
def problem_11():
    import math
    a,b = map(int,input().split())
    c = math.gcd(a,b)
    ans = 1
    i = 2
    while i<=round(c**0.5)+1:
        if c%i==0:
            ans += 1
            c //=i
            while c%i==0:
                c //= i
        i += 1
    if c>1:
        ans += 1
    print(ans)


# 12: nikkei2019_2_qual_b
def problem_12():
    from collections import Counter
    _ = int(input())
    *d, = map(int,input().split())
    INF = 998244353
    c = Counter(d)

    if len(c.keys())==max(c.keys())+1 and d[0]==0 and c.setdefault(0,0)==1:
        ans = 1
        for k in range(max(c.keys())):
            ans = ans*c[k]**c[k+1]%INF
        print(ans)
    else:
        print(0)


# 13: sumitb2019_d
def problem_13():
    n = int(input())
    s = input()
    ans = 0
    si = set()
    for i in range(n-2):
        sj = set()
        if s[i] in si:
            continue
        else:
            si.add(s[i])
        for j in range(i+1,n-1):
            if s[j] in sj:
                continue
            else:
                sj.add(s[j])
                ans += len(set(s[j+1:]))
    print(ans)


# 15: abc125_d
def problem_15():
    _ = int(input())
    *a, = map(int,input().split())
    cnt = [ai for ai in a if ai<0]
    a = [abs(ai) for ai in a]
    print(sum(a)-[0,min(a)*2][len(cnt)%2])


# 17: diverta2019_c
def problem_17():
    n = int(input())
    ans = 0
    a,b,c = 0,0,0
    for _ in [0]*n:
        s = input()
        ans += s.count('AB')
        if s[-1]=='A':
            a += 1
        if s[0]=='B':
            b += 1
        if (s[-1]=='A') and (s[0]=='B'):
            c += 1
    if (a==c) & (b==c) & (c!=0):
        print(ans+c-1)
    else:
        print(ans+min(a,b))


# 18: abc051_c
def problem_18():
    sx,sy,tx,ty = map(int,input().split())
    x,y = tx-sx,ty-sy
    ans = 'L'
    ans = ans+'U'*(y+1)
    ans = ans+'R'*(x+1)
    ans = ans+'D'*(y+1)
    ans = ans+'L'*(x)
    ans = ans+'U'*(y)
    ans = ans+'R'*(x+1)
    ans = ans+'D'*(y+1)
    ans = ans+'L'*(x+1)
    ans = ans+'U'
    print(ans)


# 19: arc080_b
def problem_19():
    h,w = map(int,input().split())
    _ = int(input())
    *a, = map(int,input().split())
    i = 0
    for hi in range(h):
        ans = []
        for _ in [0]*w:
            if a[i]==0:
                i += 1
            ans.append(i+1)
            a[i] -=1
        if hi%2==1:
            ans.reverse()
        print(*ans)


# 20: abc113_c
def problem_20():
    n,m = map(int,input().split())
    yp = []
    for _ in [0]*m:
        p,y = map(int,input().split())
        yp.append([y,p])
    q = sorted(yp)
    c = [1]*n
    ans = dict()
    for y,p in q:
        ans[y] = str(p).zfill(6)+str(c[p-1]).zfill(6)
        c[p-1]+=1
    for y,p in yp:
        print(ans[y])


# 21: arc095_b
def problem_21():
    n = int(input())
    *a, = map(int,input().split())
    n = max(a)
    r = 0
    for ai in a:
        if min(ai,n-ai)>min(r,n-r):
            r = ai
    print('{} {}'.format(n,r))


# 23: arc065_a
def problem_23():
    s = input()
    add = ['dream','dreamer','erase','eraser']
    while len(s)>0:
        if s.endswith(add[0]):
            s = s[:-len(add[0])]
        elif s.endswith(add[1]):
            s = s[:-len(add[1])]
        elif s.endswith(add[2]):
            s = s[:-len(add[2])]
        elif s.endswith(add[3]):
            s = s[:-len(add[3])]
        else:
            break
    print('YES' if len(s)==0 else 'NO')
