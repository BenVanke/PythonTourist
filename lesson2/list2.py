bicycles = ['stek', 'cannodale', "redline", 'special']
print(bicycles)
bicycles[0] = "stekds"
print(bicycles)

# 在结尾添加
bicycles.append('hongda')
print(bicycles)

# 在索引0插入，其余元素都自动后移了
bicycles.insert(0, "yamaha")
print(bicycles)

# 删除元素
del bicycles[0]
print(bicycles)

# 弹出末尾的元素
bicycles.pop()
print(bicycles)

bicycles.pop(0)
print(bicycles)

bicycles.remove('redline')
print(bicycles)


