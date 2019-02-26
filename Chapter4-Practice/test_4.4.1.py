names = ['Jack', 'Jobs', 'Tom', 'Martin', 'Ava', 'Zoe', 'Rose']
print(names[0:3])#打印前三名队员的切片，['Jack', 'Jobs', 'Tom']
print(names[1:4])#打印2-4名队员的切片，['Jobs', 'Tom', 'Martin']
print(names[:4])#未指定索引，从0开始，['Jack', 'Jobs', 'Tom', 'Martin']
print(names[-3:])#后三名，['Ava', 'Zoe', 'Rose']
print(names[-3:-1])#倒数第二和第三，上限不在内，['Ava', 'Zoe']，要想取到最后一个值，只能用上面的方法，[-3：]

