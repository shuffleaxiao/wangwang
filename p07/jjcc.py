def yunsuan(x,y):#加法
    return a+b
def yunsuan(x,y):#减法
    return a-b
def yunsuan(x,y):#乘法
    return a*b
def yunsuan(x,y):#除法
    return a/b
print("欢迎使用小提莫计算器")
x = float(input("第一个数字:"))
while True:
    fuhao = input("请你输入运算符号(+ - * /,退出输入q)")
    if fuhao == "q":
        print("你当前的运算结果是 " , x)
        break
    y = float(input("第二个数字是:"))
    if fuhao == "+":
        s = x+y
        print(s)
    elif fuhao == "-":
        s = x-y
        print(s)
    elif fuhao == "*":
        s = x*y
        print(s)
    elif fuhao == "/":
        s = x/y
        print(s)
    else:
        print("你输入信息有误,请按照提示重新输入")
    x = s
