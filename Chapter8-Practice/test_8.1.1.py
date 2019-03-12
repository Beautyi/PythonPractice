#向函数传递信息
def greet_user(username):#username为形参
    """显示简单的问候语"""
    print("Hello! " +username.title() + "!" )


greet_user('jesse')#Jesse为实参
