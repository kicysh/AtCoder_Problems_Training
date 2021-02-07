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