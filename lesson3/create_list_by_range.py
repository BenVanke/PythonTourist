for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

numbers = list(range(1, 10, 2))
print(numbers)

squares = []   # 这一句非常重要, 创建一个空列表
# squares = "123"
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))
