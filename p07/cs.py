b=0
for a in range(1,101):
    print(a)
    if a%2 == 0:
        b+=a
print("1到100偶数和为 %d" % b)
