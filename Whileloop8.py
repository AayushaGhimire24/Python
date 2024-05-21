'''A number is a good number if it contains equal no.of digits 0&1.
WAP to input a number and check whether it is a good number or not.
EG;123->Not a good number
1023->Good number
1102->Not a good number'''
n=int(input("Enter a number"))
c0=0
c1=0
while n>0:
    r=n%10
    if r==0:
      c0+=1
    elif r==1:
       c1+=1
    n=n//10
if c0==c1:
   print("good number")
else:
   print("bad number")


