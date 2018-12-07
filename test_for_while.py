# -*- coding: utf_8 -*-

# 范围 for 基本用法

# 打印 [0, 9]
# 0 1 2 3 4 5 6 7 8 9

for n in range(10):
    print(n, end=' ')
print("end.")


# for ... else ...
# 关联的 for 中如果没有因 break 而结束循环的，则最后会执行一次 else

# 以下是两段毫无意义的循环
for n in range(10):
    print(n, end=' ')
else:
    print("end.")

for n in range(10):
    print(n, end=' ')
    if n == 5:
        print("end.")
        break
else:
    # never run here
    print("nothing todo.")


# continue, break 关键字用法同 C++ 理解


# while

n = 10
while n > 0:
    print(n, end=' ')
    n -= 1
print("end.")


# for 枚举遍历 (k, v)

for k, v in enumerate(range(10)):
    print(k, v)

wdict = {"a": 1, "b": 2, "c": 3}
for k, v in wdict.items():
    print(k, v)


# zip() 使用, 组合同 idx 项，同时遍历多个 list

lista = [1, 2, 3, 4]
listb = ['a', 'b', 'c', 'd']
listc = ['x', 'xx', 'xxx']

for x, y, z in zip(lista, listb, listc):
    print(x, y, z)