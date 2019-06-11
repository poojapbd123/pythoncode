a, b = 0, 1
while b < 30:
    print(b, end=' ')
    a, b = b, a + b
    
    
print("----------------")

num = int(input("Enter num : "))
c, d = 0, 1
print(c)
for i in range(num-1):
    print(d)
    c, d = d, c + d
    


print("----------------")

n = int(input("Enter n value to calculate for dictionary  n list"))
a, b = 0, 1
result = [0]
for i in range(n-1):
    result.append(b)
    a, b = b, a+b
print(result)

print("----------------")

