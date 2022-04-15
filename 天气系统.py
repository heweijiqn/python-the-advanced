import pandas as pd

import matplotlib.pyplot as plt

filename = 'end od a term.txt'

import os


def main():
    while True:
        stumenu()

        choice = int(input("温度情况："))

        if choice in [0, 1, 2, 3, 4]:  # 选择数字输出

            if choice == 0:

                answer = input("确定要退出吗？y/n:")

                if answer == 'y' or answer == 'Y':  # 如果输入y或Y

                    print("谢谢你的使用！！！")
                    break
                else:
                    continue  # 继续

            elif choice == 1:
                cloudy()
            elif choice == 2:
                sunny()
            elif choice == 3:
                rain()
            elif choice == 4:
                haze()


def stumenu():
    print(
        "==========================================================低温天气查询============================================")

    print(
        "-----------------------------------------------------------主界面功能菜单---------------------------------------------------------------------------------")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1.多云时最低温度")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2.晴天时最低温度")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3.小雨时最低温度")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4.霾时最低温度")

    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t0.退出系统")
    print("------------------------------------------------")


def cloudy():
    df = pd.read_excel('myLife.xlsx', sheet_name='Scene')
    df = df.loc[df["天气"] == "多云"]

    df = df[['日期', '最低温度']]

    df.plot('日期', '最低温度')

    plt.show()


def sunny():
    df = pd.read_excel('myLife.xlsx', sheet_name='Scene')
    df = df.loc[df["天气"] == "晴"]

    df = df[['日期', '最低温度']]

    df.plot('日期', '最低温度')

    plt.show()


def rain():
    df = pd.read_excel('myLife.xlsx', sheet_name='Scene')
    df = df.loc[df["天气"] == "小雨"]

    df = df[['日期', '最低温度']]

    df.plot('日期', '最低温度')

    plt.show()


def haze():
    df = pd.read_excel('myLife.xlsx', sheet_name='Scene')
    df = df.loc[df["天气"] == "霾"]

    df = df[['日期', '最低温度']]

    df.plot('日期', '最低温度')

    plt.show()


if __name__ == '__main__':
    main()
