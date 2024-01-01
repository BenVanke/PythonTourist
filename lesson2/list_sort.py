bicycles = ['stek', 'cannodale', "redline", 'special']
print(bicycles)

print(bicycles.sort())  #输出是 None

bicycles.sort() #排序并保存
print(bicycles)

bicycles.sort(reverse=True)
print(bicycles)