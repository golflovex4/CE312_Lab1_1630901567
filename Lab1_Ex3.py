Number = int(input("Please Enter Number:\n")) 
if Number > 1:
  for i in range(2,Number):
    if(Number % i) == 0:
      print(Number,"Is not prime number") 
    else:
      print(Number,"Is prime number") 
else:
  print(Number,"Is not prime number")
