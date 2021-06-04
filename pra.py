x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = []
l2 = []
for i in x:
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)
print('EVEN NUMBER:',l1)
print('ODD NUMBER:',l2)
