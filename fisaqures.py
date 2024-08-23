x = int(input())
y = int(input())
z = int(input())

sortnum = sorted([x, y, z])

a, b, c = sortnum

if a**2 + b**2 == c**2:
    print("YES")
else:
    print("NO")
