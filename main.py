# 1
def problems_1():
    pass


# 2
def problems_2():
    s = input()
    ans = 0
    while 'W' in s:
        index = s.index('W')
        ans += index
        s = s[:index] + s[index+1:]
    print(ans)


# 3
def problems_3():
    pass


# 4
def problems_4():
    s = input()
    index = 0
    if len(s)%2==0:
        index = 2
    else:
        index = 1
    ans = 0
    for i in range(len(s)//2):
        ii = (len(s)-index-i*2)//2
        if s[:ii] == s[ii:ii*2]:
            ans = len(s[:ii])*2
            break
    print(ans)


# 5
def problems_5():
    n = int(input())
    print(n*(n-1)//2)


# 6
def problems_6():
    pass


# 7
def problems_7():
    n = int(input())
    s = input()
    ans = 0
    for i in range(1,n-1):
        c = set(list(s[:i])) & set(list(s[i:]))
        if ans < len(c):
            ans = len(c)
    print(ans)


# 8
def problems_8():
    input()
    a = [int(i)//400 for i in input().split()]
    cnt,ans = 0,[]
    for i in a:
        if i > 7:
            cnt += 1
        else:
            ans.append(i)
    ans = len(set(ans))
    print('{} {}'.format(max(1,ans),ans+cnt))

# 9
def problems_9():
    a,b,c = map(int,input().split())
    ab = a%b
    ans = 'NO'
    for i in range(b):
        aa = ab*i%b
        if aa==c:
            ans = 'YES'
            break
    print(ans)

# 10
def problems_10():
    # n 
    int(input())
    a = [int(i) for i in input().split()]
    aa = [0 for i in range(0,max(a)+1)]
    for i in a:
        aa[i] += 1
    ans = [sum(aa[max(i-1,0):min(i+2,len(aa)+1)]) for i in range(len(aa))]
    print(max(ans))

# 11
def problems_11():
    n,m = map(int,input().split())
    a,b = [],[]
    c,d = [],[]
    for _ in range(n):
        i,j = map(int,input().split())
        a.append(i)
        b.append(j)
    for _ in range(m):
        i,j = map(int,input().split())
        c.append(i)
        d.append(j)
    for i in range(n):
        cnt = 10**9
        ans = None
        for j in range(m):
            s = abs(a[i]-c[j])+abs(b[i]-d[j])
            if cnt > s:
                ans = j
                cnt = s
        print(ans+1)

# 12
def problems_12():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    cnt = []
    for i in range(h):
        if a[i]==('.'*w):
            cnt.append(i)
    a = [a[i] for i in range(len(a)) if i not in cnt]
    cnt = []
    for i in range(w):
        s = ''
        for ii in range(len(a)):
            s += a[ii][i]
        if s=='.'*len(a):
            cnt.append(i)
    for i in range(len(a)):
        for ii in range(len(a[i])):
            if ii not in cnt:
                print(a[i][ii],end='')
        print('')

# 13
def problems_13():
    n = int(input())
    txy = [list(map(int,input().split())) for _ in range(n)]
    ans = 'Yes'
    pre_t,pre_x,pre_y = 0,0,0
    for i in range(n):
        t,x,y = txy[i][0],txy[i][1],txy[i][2]
        d_t,d_x,d_y = t-pre_t,abs(x-pre_x),abs(y-pre_y)
        if (d_t>=(d_x+d_y)) and (d_t%2==(d_x+d_y)%2):
            pre_t,pre_x,pre_y = t,x,y
        else:
            ans = 'No'
            break
    print(ans)

# 14
def problem_14():
    h,w = map(int,input().split())
    s = ['.'*(w+2)]
    for i in range(h):
        s.append('.'+input()+'.')
    s.append('.'*(w+2))

    ans = 'Yes'
    for i in range(1,h+1):
        for ii in range(1,w+1):
            if s[i][ii] == '#':
                ss = []
                for n,m in zip([0,0,1,-1],[-1,1,0,0]):
                    ss.append(s[i+n][ii+m])
                if '#' not in ss:
                    ans = 'No'
                    break
        else:
            continue
    print(ans)

# 15
def problems_15():
    s = input()
    ss = 'keyence'
    ans = 'NO'
    for i in range(len(ss)):
        ii = i - len(ss)
        if s[:i]==ss[:i] and s[ii:]==ss[ii:]:
            ans = 'YES'
            break
    print(ans)


# 16
def problems_16():
    pass


# 17
def problems_17():
    n,T = map(int,input().split())
    t = list(map(int,input().split()))
    ans = []
    for i in range(1,n):
        if (t[i]-t[i-1])>T:
            ans.append(T)
        else:
            ans.append(t[i]-t[i-1])
    ans = sum(ans) + T
    print(ans)


# 18
def problems_18():
    c = [list(map(int,input().split())) for _ in range(3)]
    ans = 'Yes'
    for i in range(2):
        a = c[0][i+1] - c[0][i]
        b = c[i+1][0] - c[i][0]
        for ii in range(1,3):
            if a==c[ii][i+1]-c[ii][i] and b==c[i+1][ii]-c[i][ii]:
                pass
            else:
                ans='No'
        else:
            continue
    print(ans)

# 19
def problems_19():
    r,g,b,n = map(int,input().split())
    ans = 0
    for rr in range(n//r+1):
        for gg in range((n-rr*r)//g+1):
            if (n-rr*r-gg*g)%b==0:
                ans += 1
    print(ans)


# 20
def problems_20():
    n = int(input())
    ans = set()
    for _ in range(n):
        a = {int(input())}
        ans ^= a
    print(len(ans))


# 21
def problems_21():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0]*n
    for i in a:
        cnt[i-1] += 1
    ans = [0]*n
    for i in a:
        s = cnt[i-1]
        ans[i-1] = s*(s-1)/2
    ans_sum = sum(ans)
    for i in a:
        s = cnt[i-1]
        print(int(ans_sum-(s-1)))

# 22
def problems_22():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        cnt = 0
        while i<k:
            i *= 2
            cnt += 1
        ans += 0.5**cnt/n
    print(ans)

# 23
def problems_23():
    n,m = map(int,input().split())
    ans = 'a'*n
    for _ in range(m):
        s,c = map(int,input().split())
        if ans[s-1]=='a':
            ans = '{}{}{}'.format(ans[:s-1],c,ans[s:])
        elif ans[s-1]!=str(c):
            ans = -1
            break
    if (n!=1)&(ans!=-1):
        if ans[0]=='0':
            ans = -1    
    if ans!=-1:
        if (n!=1)&(ans[0]=='a'):
            ans = '{}{}'.format('1',ans[1:])
        ans = ans.replace('a','0')

        ans = int(ans)
    print(ans)


# 24
def problems_24():
    n,a,b = map(int,input().split())
    ans = 0
    if (n>1)&(a<=b):
        ans = (b-a)*(n-2)+1
        print(ans)
    elif (n==1)&(a==b):
        print(1)
    else:
        print(0)


# 25
def problems_25():
    pass


# 26
def problems_26():
    n = int(input())
    a = list(map(int,input().split()))
    shift = 0
    ans = 1
    for i in range(n-1):
        if (a[i]-a[i+1])*shift<0:
            ans += 1
            shift = 0
        elif (a[i]-a[i+1])!=0:
            shift = a[i]-a[i+1]
    print(ans)


# 27
def problems_27():
    n = int(input())
    s = input()
    t = input()
    ans = n
    if (len(s)+len(t)>n):
        ans = len(s)+len(t)
        for i in range(min(len(s),len(t))):
            if s[i:] == t[:len(t)-i]:
                ans = max(n,len(s)+len(t)-len(s[i:]))
                break
    print(ans)


# 28
def problems_28():
    pass


# 29
def problems_29():
    s = sorted(input())
    t = sorted(input(),reverse=True)
    if s<t:
        ans='Yes'
    else:
        ans='No'
    print(ans)


# 30
def problems_30():
    n,m = map(int,input().split())
    if (n>=2)&(m>=2):
        print((n-2)*(m-2))
    elif max(n,m)>1:
        print(max(n,m)-2)
    else:
        print(1)

# 31
def problems_31():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0,0,0]
    for i in range(len(a)):
        s = a[i]
        if s%4==0:
            cnt[2]+=1
        elif s%2!=0:
            cnt[0] += 1
    if cnt[2]>=(cnt[0]-n%2):
        print('Yes')
    else:
        print('No')


# 32
def problems_32():
    n,y = map(int,input().split())
    cnt = [-1,-1,-1]
    y = y/(10**3)
    for i in range(n+1):
        if (y-i*10)<0:
            break
        for ii in range(n-i+1):
            if (y-i*10-ii*5)<0:
                break
            iii = n-i-ii
            #print('{}:{}:{}'.format(i,ii,iii))
            if (y-i*10-ii*5-iii)==0:
                cnt = [i,ii,iii]
    print('{} {} {}'.format(*cnt))


# 33
def problems_33():
    ans = ''
    s = input()
    for i in s:
        if i != 'B':
            ans = ans+i
        else:
            ans = ans[:-1]
    print(ans)


# 34
def problems_34():
    import math
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    index = a.index(1)
    ans = math.floor(index/(k-1))+math.floor((n-index-1)/(k-1))
    d = ((index%(k-1))+((n-index-1)%(k-1))+1)
    if d>k:
        ans += 2
    elif d!=1:
        ans += 1
    print(ans)


# 35
def problems_35():
    import math
    a,b,c,d = map(int,input().split())
    e = math.gcd(c,d)
    e = int(c*d/e)
    a -=1
    ans = b-a-(b//c-a//c+b//d-a//d-(b//e-a//e))
    print(ans)

# 36
def problems_36():
    import math
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    x = [abs(i-X) for i in x]
    ans = x[0]
    for i in x[1:]:
        ans = math.gcd(ans,i)
    print(ans)
