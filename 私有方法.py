# 保证不在外部直接调用,保证业务逻辑不被破坏
class Dog(object):
    def born(self):
        print('生了一只小狗')
        self.__sleep()  # 私有方法

    def __sleep(self):
        print('休息30天')


dog = Dog()
dog.born()
