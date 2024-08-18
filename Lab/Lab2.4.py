#WAP to print the following 
'''
1
12
113
1114
11115'''
# Construct and print the sequence using a for loop
for i in range(1, 6):
    for j in range(1,i+1):
        if j==i:
            print(j)
        else:
            print('1',end='')
