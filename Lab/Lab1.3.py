'''create the following menu driven program:
1.Area of circle
2.vowel/consonant
3.Odd/even'''
print("1.Area of circle\n 2.Vowel/Consonant\n 3.Odd\Even")
d=int(input("choose between 1-3:"))
match d:
 case 1:
       r=int(input("enter radius:"))
       area=3.14**r
       print (area)

 case 2:
        vow=input("enter a letter: ")
        vow=vow.lower()
        match vow:
             case 'a'|'e'|'i'|'o'|'u':
                  print("vowel")
             case other:
                  print("consonant")
 case 3:
          num=int(input("enter a number"))
          if(num%2==0):
               print("even")
          else:
               print("Odd")
 case other:
          print("Invalid choice")
                   
