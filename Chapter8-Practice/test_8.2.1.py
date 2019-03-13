#位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')#确保实参与形参位置一致
describe_pet('dog', 'willie')#调用函数多次
