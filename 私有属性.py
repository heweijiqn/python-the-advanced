# 私有
#  保证数据的安全
# 通过公有访问私有
class People(object):
    def __init__(self):
        self.__money = 0  # 私有本质是修改属性的名字，在创建对象的时候会自动修改属性名，在属性名的前边加上类名前缀

    #     定义公有方法
    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money += money


xw = People()
# print(xw.__money)
#  __dict__可以查看属性信息 key属性名 value属性值
print(xw.__dict__)
xw.__money = 1000  # 添加公有属性
print(xw.__dict__)
print(xw.__money)
print('='*30)
print(xw.get_money())
xw.set_money(100)
print(xw.get_money())