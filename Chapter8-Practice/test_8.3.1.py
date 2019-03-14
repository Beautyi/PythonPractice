#返回简单值
def get_formatted_name(first_name, last_name):
    """返回简洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
