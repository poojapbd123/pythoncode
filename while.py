print("nos in while loop")
num = 1
while num < 11:
    print(num)
    num = num + 1
   
print("Odd nos in while loop")

a = 1
while a < 11:
    print(a)
    a = a + 2
    
print("Print *** for 3 and ***** for 5 divisiblility")

b = 1
while b < 11:
    if b % 3 == 0:
        print("* * *")
        
    elif b % 5 == 0:
        print("* * * * *")
        
    else:
        print(b)
    b = b + 1
    

print("Print *** for all nos from 10 to 1") 

c = 11
while c > 0:
    print('*' *c)
    c = c - 1
    
       
print("Print *** for all nos from 1 to 11")

c = 1
while c < 11:
    print('*' *c)
    c = c + 1