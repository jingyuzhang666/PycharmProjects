# 学习变量相关知识

a = 3
b = 30.0
B = 27
c = 40.0
C = 33

print('模块总数为', a, '个')
print('b模块的用例总数为', b, '个', '通过的用例数为', B, '个', '通过率为', (B / b) * 100, '%')

print('c模块的失败率为', ((c - C) / c) * 100, '%')

# String

test_type = "回归测试"
test_result = "失败"

print(test_type + test_result)