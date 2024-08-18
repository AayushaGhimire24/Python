'''
1
10
101
1010
10101'''
a=1
for i in range(1,6):
    print(a)
    if i%2==1:
        a=a*10
    else:
        a=a*10+1