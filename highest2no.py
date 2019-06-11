x = int(input("Enter value x : "))
y = int(input("Enter value y : "))

if x > y:
    print("first")
    high=x
elif y > x:
    print("Second")
    high=y
elif x == y:
    print("Same")
    
print(high*high)