#用户简介
def build_profile(first, last, **user_info):
    """创建一个字典，包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('lijun', 'ma',
                             location='tongliao',
                             habbit='study Python',
                             age='25')
print(user_profile)
