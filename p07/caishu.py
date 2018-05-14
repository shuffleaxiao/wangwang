for a in range(1,101):
    a = int(input("请输入数字1到100:"))
    if a>=1 and a<=50:
        print("小了")
    elif a==51:
        print("恭喜你猜对了")
        break
    else:
        print("大了")
