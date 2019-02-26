a = 1
b = 1
print(a)
print(b)
for value in range(1, 100):
    c = a + b
    a = b
    b = c
    print(c)


