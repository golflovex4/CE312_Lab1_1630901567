while(1):   
  try:
    wide = int(input("Please Enter a Odd:\n")) 
  break
  except:
    wide = input("Error Please Enter a Odd:\n") 
    
while(1):
  try:
    star = int(input("Please Enter Number Of Star:\n")) 
    break
  except:
    star = input("Error Please Enter Number Of Star:\n")
    
for x in range(star+1): 
  space = wide // 2
  x = 1   
while space > 0: 
  print((space*" ")+(x*"*")) 
  space -= 1
  x +=2   
while space <= wide//2: 
  print((space*" ")+(x*"*"))        
  space += 1    
  x -=2
