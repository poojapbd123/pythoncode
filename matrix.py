num = int(input())
for i in range(num):
    for j in range(num):
        print(i, j)
    i = i + 1
    print("---")
j = j + 1

print("---------")

num = int(input())
for i in range(num):
    for j in range(num):
        print(i+j, end=' ')
print()