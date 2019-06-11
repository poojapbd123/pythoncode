num = int( input())
if num%2 == 0:
    print("Positive num ")
else:
    print('-',num)
    print("Negative of ",num)

if num == 0:
    print("Zero")

print("Done")

print("___________")

if num < 0:
    print("neg", abs(num))
elif num > 0:
    print("Pos")
else:
    print("zero")
print("Done")