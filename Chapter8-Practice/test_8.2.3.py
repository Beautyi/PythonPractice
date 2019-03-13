#默认值
def describe_pet( pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(animal_type='hamster', pet_name='harry')#提供实参，Python将忽略形参的默认值
