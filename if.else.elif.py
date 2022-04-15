# if else 语句
age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print("可以进入该网站")
else:
    print('请回')
    print('好好学习吧')
print("/" * 30)
# if elif else结构可判断多个条件
score = int(input("请输入你的分数："))
if score >= 95:
    print("A+")
    print("继续保持")
elif score >= 85:
    print("A")
    print('有很大的进步空间哦 ')
else:
    print("少年努力吧")
    print("加油")
print('|' * 30)
# 嵌套
money = int(input('请输入你拥有的钱：'))
if money >= 2:
    print('我上车啦')
    seat = eval(input("车上的座位："))
    if seat >= 1:
        print("我坐下来了")
    else:
        print('只能站着了')
else:
    print('呜~')
print('-'*30)

