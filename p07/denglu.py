c = "baibing"
d = "zhu"
e = 1
while e<=4:
    a = input("请输入你的用户名:")
    b = input("请输入你的密码:")
    if a==c and b==d:
        print("欢迎进入傻袍子白冰世界。")
        break
    else:
        print("请重新输入用户和密码")
    e += 1

