#汽车
def make_car(manufacturer, model, **car_info):
    """描述车辆信息"""
    car_1 = {}
    car_1['manufacturer_name'] = manufacturer
    car_1['model_name'] = model
    for key,value in car_info.items():
        car_1[key] = value
    return car_1


car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)
