#按顺序遍历字典中的所有键
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favourite_languages.keys()):#用sorted先排序
    print(name.title() + ',thank you for taking the poll.')
# Edward,thank you for taking the poll.
# Jen,thank you for taking the poll.
# Phil,thank you for taking the poll.
# Sarah,thank you for taking the poll.
