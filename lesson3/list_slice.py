bicycles = ['stek', 'cannodale', "redline", 'special']
print(bicycles[1:3])  # 索引范围为 1 到 3-1
print(bicycles[:3])
print(bicycles[1:])
print(bicycles[-3:])

for bicycle in bicycles[:3]:
    print(bicycle.title())