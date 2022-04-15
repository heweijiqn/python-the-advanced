import os

stu_list = []


def show_menu():
    print('1.添加学生 ')
    print('2.删除学生 ')
    print('3.修改学生信息 ')
    print('4.查询单个学生信息 ')
    print('5.查询所有学生信息 ')
    print('6.退出系统  ')


def insert_student():
    name = input('请输入学生的名字: ')
    for stu in stu_list:
        if stu['name'] == name:
            print('该学生信息存在 ')

            return
    age = input('请输入学生年龄: ')
    stu_dict = {'name': name, 'age': int(age)}
    stu_list.append(stu_dict)
    print('========学生信息添加成功 =========')


def show_all_info():
    if len(stu_list) > 0:
        for stu in stu_list:
            print(f"姓名 :{stu['name']},年龄:{stu['age']} ")
    else:
        print('目前还没有信息 ')


def remove_stu():
    name = input('请输入要操作de学生的名字 ')
    for stu in stu_list:
        if stu['name'] == name:
            stu_list.remove(stu)
            return
    else:
        print('该学生信息不存在 无法删除 ')


def modify_stu():
    name = input('请输入要操作de学生的名字 ')
    for stu in stu_list:
        if stu['name'] == name:
            stu['age'] == int(input('请输入新的 年龄 :'))
            break
    else:
        print('该学生信息不存在 wu法修改 ')


def search_stu():
    name = input('请输入要操作de学生的名字 ')
    for stu in stu_list:
        if stu['name'] == name:
            print(f"姓名 :{stu['name']},年龄:{stu['age']} ")
            return
    else:
        print('该学生信息不存在')


def save():
    f = open('stu.txt', 'w', encoding='utf-8')
    f.write(str(stu_list))
    f.close()


def load_file():
    global stu_list
    if os.path.exists('stu.txt'):
        f = open('stu.txt', 'w', encoding='utf-8')
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()


def main():
    load_file()
    while True:
        show_menu()
        opt = input('请输入用来选择的操作编号: ')
        if opt == '1':
            insert_student()
            # print('1.添加学生 ')
        elif opt == '2':
            remove_stu()
            # print('2.删除学生 ')
        elif opt == '3':
            modify_stu()
            # print('3.修改学生信息 ')
        elif opt == '4':
            search_stu()
            # print('4.查询单个学生信息 ')
        elif opt == '5':
            show_all_info()
            # print('5.查询所有学生信息 ')
        elif opt == '6':
            print('6.欢迎下次使用本系统   ')
            save()
            break
        else:
            print('输入有误请再次输入 ')
            continue

        input('....回车键继续使用 ....')


main()
