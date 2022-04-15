import pandas as pd

import matplotlib.pyplot as plt

filename = 'end od a term.txt'

import os


def main():  # 使用main主函数（只能有一个，程序的入口）
    while True:
        stumenu()  # menu菜单组件

        choice = int(input("请选择您的服务类型："))

        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:  # 选择数字输出

            if choice == 0:

                answer = input("您确定要退出系统吗？y/n:")

                if answer == 'y' or answer == 'Y':  # 如果输入y或Y

                    print("谢谢您的使用！！！")
                    break
                else:
                    continue  # 继续

            elif choice == 1:

                water()
            elif choice == 2:

                walk()
            elif choice == 3:

                sleep()
            elif choice == 4:

                shopping()
            elif choice == 5:

                shoot()
            elif choice == 6:

                program()
            elif choice == 7:
                write()


def stumenu():
    print(
        "==========================================================学生日常管理系统============================================")

    print(
        "-----------------------------------------------------------主界面功能菜单---------------------------------------------------------------------------------")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1.查找学生喝水信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2.查找学生步行信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3.查找学生睡眠信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4.查找学生购物信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t5.查找学生拍摄信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t6.查找学生编程信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t7.查找学生写作信息")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t0.退出系统")

    print("------------------------------------------------")


df = pd.read_excel('myLife.xlsx', sheet_name='Activity')

df = df.loc[df["操作"] == "喝水"]


def water():
    student_informastion = []

    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')

    df = df.loc[df["操作"] == "喝水"]

    # df=df[['日期','时长']]#统计喝水时长

    df = df[['日期', '数量']]  # 统计喝水数量

    print(df)

    # plt.bar(range(len(df)))#列表呈现

    df.plot('日期', '数量')  # 统计喝水数量

    # df.plot('日期','时长')#统计喝水时长

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('喝水')

    plt.show()


def walk():
    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')

    df = df.loc[df["操作"] == "步行"]

    df = df[['日期', '数量']]  # 统计步行数量

    # df=df[['日期','时长']]统计步行时长

    print(df)

    # plt.bar(range(len(df)))#列表呈现

    df.plot('日期', '数量')

    # df.plot('日期','时长')#统计步行时长

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('步行')

    plt.show()


def sleep():
    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
    df = df.loc[df["操作"] == "睡眠"]

    df = df[['日期', '时长']]

    print(df)

    df.plot('日期', '时长')

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('睡眠')

    plt.show()


def shopping():
    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
    df = df.loc[df["操作"] == "购物"]

    df = df[['日期', '数量']]

    print(df)

    df.plot('日期', '数量')

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('购物')

    plt.show()


def shoot():
    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')

    df = df.loc[df["操作"] == "拍摄"]

    df = df[['日期', '数量']]

    df.plot('日期', '数量')

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('拍摄')

    plt.show()


def program():
    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
    df = df.loc[df["操作"] == "编程"]

    df = df[['日期', '时长']]

    df.plot('日期', '时长')

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('编程')

    plt.show()


def write():
    df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
    df = df.loc[df["操作"] == "写作"]

    df = df[['日期', '数量']]

    # df=df[['日期','时长']]

    df.plot('日期', '数量')

    # df.plot('日期','时长')

    plt.ylabel('日期')

    plt.xlabel('数量')

    plt.title('写作')

    plt.show()


if __name__ == '__main__':
    main()
