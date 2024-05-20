sp=1
for i in range(9,0,-2):
  for k in range(1,sp+1):
    print(end=' ')
  for j in range(1,i+1):
    print('*',end='')
  print()
  sp=sp+1