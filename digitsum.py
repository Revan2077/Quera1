number = input()

digitSum = 0

for i in number:
        digitSum += int(i)


digitSum2 = 0

for a in str(digitSum) :
    digitSum2 += int(a)

print(digitSum2)
