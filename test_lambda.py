# -*- coding: utf_8 -*-
# lambda and closure func


# python 中的 lambda 没有 C++ 中的那么像一个函数
# 更多的受限于单个表达式


# 不需要 return
# error:
# Sum = lambda a, b: return a + b
Sum = lambda a, b: a + b
print(Sum(1, 2))



# 闭包
def ClosureFunc(a, b):
    # 函数内的闭包
    def inter_func(a, b):
        return a + b

    return inter_func(a, b)

print(ClosureFunc(1, 2))