bicycles = ['stek', 'cannodale', "redline", 'special']
new_bicycles = bicycles[:]
print(new_bicycles)

bicycles.append("wenjie")
new_bicycles.append("byd")
print(bicycles)
print(new_bicycles)

ref_bicycles = bicycles
ref_bicycles.append("dongfeng")
print(ref_bicycles)
print(bicycles)
