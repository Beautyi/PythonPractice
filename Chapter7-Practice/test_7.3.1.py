#在列表之间移动元素
#首先创建一个待验证的列表和一个用于储存已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#验证每个用户，直到没有未验证的用户为止，将每个经过验证的列表移入已验证的列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)
#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

