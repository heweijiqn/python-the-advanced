"""
当一行代码发生异常之后会向外层将这个异常进行传递直到被捕获为止 或者程序进行报错

"""
"""
num = input('请输入一个数字：')
try:
    try:
        a = int(num)    若发生异常，其没有被捕获，会先外层转递
    except ZeroDivisionError:
        print('发生异常了')
    finally:
        print('*'*30)
# except (ZeroDivisionError, ValueError) as e:
except Exception as e:
    print(e)
"""


def func1():
    print('1')
    num = input('请输入数字：')
    num = 10 / int(num)
    print(num)
    print('2')


def func2():
    print('3')
    func1()
    print('4')


try:
    print('5')
    func2()
    print('6')
except Exception as e:
    print('7')
    print(e)
