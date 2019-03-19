#禁止函数修改列表
def print_models(unprinted_designs, completed_models):#包含两个形参
    """模拟打印每个设计，直到没有未打印的设计为止。打印后转移到completed_models中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #模拟根据设计制作的3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print_models(unprinted_designs[:], completed_models)#切片表示法
