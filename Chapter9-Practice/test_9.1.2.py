#根据类创建实例
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over.")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
my_dog.sit()
my_dog.roll_over()
print("My dog's name is " + str(my_dog.name.title()) + ".")
print("Your dog's name is " + str(your_dog.name.title()) + ".")
