def inp():
  try:
      a= complex (input("enter input 1"))
  except:
      print("enter valid input")
      return 'x'
  return a
while(1): 
  print("1.add 2.sub 3.mul 4.div 5.mod 6.exit")
  try:
    ch= round((float(input())))
  except:
     print("invalid choice")
     continue
  if(ch==6):
     break
  elif(ch>6 or ch<=0):
    print("invalid choice")
    continue
  flag='x'
  while(flag=='x'):
    flag=inp()
  a=flag
  flag='x'
  while(flag=='x'):
    flag=inp()
  b=flag  
  if(ch==1):
    c=a+b
  elif(ch==2):
    c=a-b
  elif(ch==3):
    c=a*b
  elif(ch==4):
    if(b==0):
      print("divide by zero")
      continue
    c=a/b
  elif(ch==5):
    c=a%b
  if(c.imag==0): 
   print(c.real)
  else:
   print(c)