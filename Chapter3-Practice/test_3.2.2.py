names = ['Jobs', 'Mia', 'Ava', 'Zoe']
print(names)
names.append('Obama')
print(names)#['Jobs', 'Mia', 'Ava', 'Zoe', 'Obama']
names = []
names.append('Jobs')
names.append('Mia')
names.append('Ava')
print(names)#创建空列表，并逐一添加元素#['Jobs', 'Mia', 'Ava']
names = ['Jobs', 'Mia', 'Ava', 'Zoe']
print(names)
names.insert(0,'Obama')#插入元素，两个参数，第一个是索引，第二个是插入的元素
print(names)#['Obama', 'Jobs', 'Mia', 'Ava', 'Zoe']
names.insert(1,'Obama')
print(names)


