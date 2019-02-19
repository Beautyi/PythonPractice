names = ['Jobs', 'Mia', 'Ava', 'Zoe']
print(names)
del names[0]#永久删除任意已知位置元素del加空格加变量名[索引]
print(names)#['Mia', 'Ava', 'Zoe']
names.pop()#删除最后一个元素，删除后仍可使用
print(names)#['Mia', 'Ava']


