# 打开文件
# open(file（str）,mode='r'只读，'w'只写,'a'追加,encoding=none)
# f = open('bo2.txt', 'w', encoding='utf-8')
#
# buf = f.read()  # 读
# print(buf)
# f.write('jiu')
# f.close()  # 存
f = open('bo2.txt', 'a', encoding='utf-8')
f.write('111')
f.close()