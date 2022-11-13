wide = 5 
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
