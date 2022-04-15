# 字符串（引号）3个及以下 3个也是注释
# 下标从0开始,-1是最后的字符往前增大
my_str = 'hello'
print(my_str[0])
print(my_str[-2])
# len()计算长度
print(len(my_str))
# 运用长度，获取字符
print(my_str[len(my_str) - 1])

# 切片
# 变量=【start:end:step】
# 没end就是取到最后
# 没start就是重头到尾
# 变量 = {：}完整的字符
my_str = 'hwj good bad and'
# 找不到是-1
# my_str.find(查找内容，start，end)
# rfind
# 找不到会报错
# index
# r index
print(my_str.find('hwj'))
# count()统计次数
print(my_str.count('hwj'))
# my_str.replace(old,new,count替换次数)
my_str1 = my_str.replace('hwj', 'hej')
print(my_str1)
# my_str.split(,count)默认空格 切割
result = my_str.split()
print(result)
# 连接
# mt_str.join()
result = ' = '.join('hwj')
print(result)
# h = w = j

