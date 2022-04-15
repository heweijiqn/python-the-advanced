# 字典
# dict = {} 变量 = {key: value} key为字符串或数字类型 value为任意值
my_dict = {}
# my_dict = dict()

my_dict1 = {'name': 'Hej', 'age': 18}
print(my_dict1)
# 无下标值
print(my_dict1['age'])
print(my_dict1.get('age'))  # 存在既是数据值 ，不存在是书写值
print(my_dict1.get('mm', 'ma'))
print(my_dict1.get('name', '1'))

# 添加 无该数据
my_dict1['my'] = 'hwj'
print(my_dict1)
# 修改 有
my_dict1['age'] = 19
print(my_dict1)
# 在字典中1与1.0相同

# 删除 根据key值
del my_dict1['my']
print(my_dict1)
# del my_dict删除变量
# .pop()
result = my_dict1.pop('age')  # 返回值是value
print(result)
print(my_dict1)
# .clear()清空字典
my_dict1.clear()
print(my_dict1)

# 字典的遍历
my_dict2 = {'name': 'hwj', 'age': 18, 'gender': '男'}
for key in my_dict2:
    print(key, my_dict2[key])

# 可以用list（）进行类型转换为列表
result = my_dict2.keys()
print(result, type(result))  # <class 'dict_keys'>
for key in result:
    print(key)

# 字典获取values
result = my_dict2.values()
for value in result:
    print(value)
# 元组
result = my_dict2.items()
for item in result:  # item可改成k,v
    print(item[0], item[1])  # print(k,v)
# 列表
# enumerate 可将元素的下标和具体数值结合，变成元组
for j in enumerate(my_dict2):
    print(j)


print(my_dict2['name'])
