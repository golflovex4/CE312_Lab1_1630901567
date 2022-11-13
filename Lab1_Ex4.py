X = int(input("Please Enter Number:\n"))
def Cal(x):
  if x < 2: 
    return 1 
  else:
    return 1 / x + Cal(x-1) 
print("Harmonic step = ",x)
print("Ans = ",Cal(x))
