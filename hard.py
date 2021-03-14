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


# 24: keyence2020_b
def problem_24():
    n = int(input())
    xl = [list(map(int,input().split())) for _ in [0]*n]
    xl.sort()
    tmp = xl[0][0] + xl[0][1]
    ans = 1
    for x,l in xl[1:]:
        if (x-l)<tmp:
            tmp = min(tmp,x+l)
        else:
            tmp = x+l
            ans +=1
    print(ans)


# 26: codefestival_2016_qualC_b
def problem_26():
    k,_ = map(int,input().split())
    *a, = map(int,input().split())
    a = max(a)
    print(0 if a<=(k+1)//2 else (a-(k+1)//2)*2-1)


# 28: arc101_a
def problem_28():
    n,k = map(int,input().split())
    *x, = map(int,input().split())
    ans = 10**9
    if (x[0]>=0):
        ans = x[k-1]
    elif (x[-1]<=0):
        ans = -x[n-k]
    else:
        for i in range(n-k+1):
            if x[i]*x[i+k-1]<0:
                ans = min(ans,-x[i]*2+x[i+k-1])
                ans = min(ans,-x[i]+x[i+k-1]*2)
            else:
                ans = min(ans,max(abs(x[i]),abs(x[i+k-1])))
    print(ans)


# 29: agc011_b
def problem_29():
    n = int(input())
    *a, = map(int,input().split())
    a.sort()
    ans = n
    for i in range(n-1):
        if a[i]*2<a[i+1]:
            ans = n-i-1
        a[i+1] += a[i]
    print(ans)


# 31: abc134_d
def problem_31():
    n = int(input())
    *a, = map(int,input().split())
    b = [0]*n
    for i in range(n-1,-1,-1):
        if sum(b[i::i+1])%2!=a[i]:
            b[i] = 1
    m = 0
    ans = []
    for bi in range(n):
        if b[bi]==1:
            ans.append(bi+1)
            m += 1
    print(m)
    if m!=0:
        print(*ans)


# 32: arc067_a
def problem_32():
    import math
    n = int(input())
    INF = 10**9+7
    c = [2]
    for i in range(3,n+1,2):
        flag = True
        for ci in c:
            if math.gcd(i,ci)!=1:
                flag = False
                break
        if flag:
            c.append(i)
    cnt = [1]*len(c)
    for ci in range(len(c)):
        tmp = n
        while tmp//c[ci]>0:
            tmp //=c[ci]
            cnt[ci]+=tmp   
    ans=1
    for i in cnt:
        ans = (ans*i)%INF
    print(ans)


# 34: arc066_a
def problem_34():
    n = int(input())
    *a, = map(int,input().split())
    INF = 10**9+7
    c = [0]*((n+1)//2)
    for ai in a:
        c[ai//2]+=1
    if c==([1] + [2]*(len(c)-1)) or c==([2] + [2]*(len(c)-1)):
        ans = 1
        for ci in c:
            ans =(ans*ci)%INF
        print(ans)
    else:
        print(0)


# 35: abc085_d
def problem_35():
    n,h = map(int,input().split())
    a,b = [],[]
    for _ in [0]*n:
        aa,bb = map(int,input().split())
        a.append(aa)
        b.append(bb)
    tmp = max(a)
    b.sort(reverse=True)
    ans = 0
    for bi in b:
        if bi > tmp:
            h -= bi
            ans +=1
            if h <= 0:break
        else: break
    if h>0: ans += h//tmp+[1,0][h%tmp==0]
    print(ans)


# 37: ddcc2020_qual_c
def problem_37():
    h,w,_ = map(int,input().split())
    s = [input() for _ in [0]*h]
    c = [[0]*w for _ in [0]*h]
    i,cnt = 0,0
    for hi in range(h):
        i += 1
        flag = True
        for wi in range(w):
            if s[hi][wi]=='#':
                if flag:
                    flag = False
                else:
                    i += 1
            c[hi][wi] = i
        if flag:
            i +=-1
            if hi==cnt:
                cnt = hi+1
            else:
                c[hi] = c[hi-1]
    for i in range(cnt-1,-1,-1):
        c[i] = c[cnt]
    for ci in c:
        print(*ci)

# 38: abc151_d
def problem_38():
    from collections import deque
    h,w = map(int,input().split())
    s = ['#'*(w+2)]+['#'+input()+'#' for _ in range(h)]+['#'*(w+2)]
    ans = 0
    for hi in range(1,h+1):
        for wi in range(1,w+1):
            if s[hi][wi]=='.':
                c,q = [[-1]*(w+2) for _ in range(h+2)],deque()
                c[hi][wi] = 0
                q.append((hi,wi))
                while q:
                    hj,wj=q.popleft()
                    for hd,wd in [(0,-1),(0,1),(1,0),(-1,0)]:
                        if s[hj+hd][wj+wd]=='.' and c[hj+hd][wj+wd]<0:
                            q.append((hj+hd,wj+wd))
                            c[hj+hd][wj+wd] = c[hj][wj]+1
                ans = max(ans,max(max(c,key=max)))
    print(ans)


# 39: tenka1_2019_c
def problem_39():
    n = int(input())
    s = input()
    ans = [0,0]
    w,b = 0,0
    for si in range(n-1,-1,-1):
        if s[si]=='#':
            b +=1
            ans[1] = min(ans[1]+b,ans[0]+b)
            ans[0]+=w
            w,b = 0,0
        else:
            w +=1
    print(min(ans))


# 40: code_festival_2017_qualc_c
def problem_40():
    s = input()
    sx = s.replace('x','')
    if sx == sx[::-1]:
        ans = 0
        left,right = 0,len(s)-1
        for i in range((len(sx)+1)//2):
            tmp = 0
            while s[left]!=sx[i]:
                tmp +=1
                left +=1
            left += 1
            while s[right]!=sx[i]:
                tmp -=1
                right -=1
            right -=1
            ans += abs(tmp)
        print(ans)
    else:
        print(-1)


# 41: arc102_a
def problem_41():
    n,k = map(int,input().split())
    ans = (n//k)**3
    if k%2==0:
        ans += ((n+k//2)//k)**3
    print(ans)


# 42: abc064_d
def problem_42():
    _ = int(input())
    s = input()
    a,b = 0,0
    for si in s[::-1]:
        if si==')':
            a +=1
        else:
            a = max(0,a-1)
    for si in s:
        if si=='(':
            b +=1
        else:
            b = max(0,b-1)
    print('('*a+s+')'*b)


# 44: abc147_c
def problem_43():
    n = int(input())
    xy = []
    ans = 0
    for _ in [0]*n:
        a = int(input())
        xy.append([list(map(int,input().split())) for _ in [0]*a])
    for i in range(2**n):
        cnt = [0]*n
        for ci in range(n):
            cnt[ci] = i%2
            i //= 2
        flag = True
        for ci in range(n):
            if cnt[ci] == 1:
                for x,y in xy[ci]:
                    x -=1
                    if (y==1 and cnt[x]==0) or (y==0 and cnt[x]==1):
                        flag = False
                        break
                else:
                    continue
        if flag:
            ans = max(ans,sum(cnt))
    print(ans)


# 46: agc005_a
def problem_46():
    x = input()
    ans = len(x)
    cnt = 0
    for xi in x:
        if xi=='S':
            cnt +=1
        else:
            if cnt>0:
                ans -=2
                cnt -=1
    print(ans)
