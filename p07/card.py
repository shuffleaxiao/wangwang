name_num = []
import card1
card1.systemMenue()
while True:
    user = input("请输入你想做的操作:")
    if user in ("1","2","3","4","5"):
        if user == "1":
            z = input("请输入你的名字:")
            x = input("请输入你的公司:")
            c = input("请输入你的邮件:")
            dic = {}
            dic = {"name":z,"com":x,"email":c}
            name_num.append(dic)
            print(name_num)
            card1.systemMenue()
        elif user == "2":
            r = input("请输入你要查询的人的xingming:")
            for dic in name_num:
                if r == dic["name"]:
                    print("*"*10)
                    print("姓名: %s" % dic["name"])
                    print("公司: %s" % dic["com"])
                    print("邮箱: %s" % dic["email"])
            card1.systemMenue()
        elif user == "3":
            print("原内容是: %s"  % (name_num))
            r = input("请输入你要修改的地方是(name or email or com):")
            if r == "name":
                new = input("请你输入新的名字:")
                dic["name"] = new
                print("修改信息如下")
                print("名字: %s" % dic["name"])
                print("公司: %s" % dic["com"])
                print("邮箱: %s" % dic["email"])
            elif r == "email":
                new = input("请你输入新的email:")
                dic["email"] = new
                print("修改信息如下")
                print("名字: %s" % dic["name"])
                print("公司: %s" % dic["com"])
                print("邮箱: %s" % dic["email"])
            elif r == "com":
                new = input("请你输入新的公司:")
                dic["com"] = new
                print("修改信息如下")
                print("名字: %s" % dic["name"])
                print("公司: %s" % dic["com"])
                print("邮箱: %s" % dic["email"])
            else:
                print("书写错误.")
            card1.systemMenue()
        elif user == "4":
            xiu = input("请输入你要删除的位子name,com,email:")
            if xiu == "name":
                dic.pop(xiu)
                print("名字: 无")
                print("公司: %s" % dic["email"])
                print("邮箱: %s" % dic["email"])
            elif xiu == "com":
                dic.pop(xiu)
                print("名字: %s" % dic["email"])
                print("公司: 无")
                print("邮箱: %s" % dic["email"])
            elif xiu == "email":
                dic.pop(xiu)
                print("名字: %s" % dic["email"])
                print("公司: %s" % dic["email"])
                print("邮箱: 无")
            else:
                print("书写错误,请确认之后在输入.")
            card1.systemMenue()
        elif user == "5":
            card1.exit()
            break
else:
    print("输入有误，请重新输入")
