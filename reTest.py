import re


# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')


result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')


def print_result(name, result):
    if result:
        print(name, result.group())
    else:
        print(name, '匹配失败')


print_result('result1', result1)
print_result('result2', result2)
print_result('result3', result3)
print_result('result4', result4)


print(result1.string)
print(result1.re)
print(result1.pos)
print(result2.endpos)
print(result2.lastindex)
print(result2.lastgroup)

