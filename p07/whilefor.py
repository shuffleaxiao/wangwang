#for 抓娃娃 if
for i in range(1,5001,1):
    if i%5==0 and i%7==0:
        print("满足 %d" % i)
        continue
    print("不满足 %d" % i)

