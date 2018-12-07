# -*- coding: utf_8 -*-
# 三元运算符
# C/C++ 中 xx ? xxx : xx;

# res_true if true else res_false;


cond = 1
res = 10 if cond == 1 else 12
print(res)

res = 10 if cond == 2 else 12
print(res)


# 短路结果
res = cond or 10
print(res)
# res = 1

cond = 0
res = cond or 10
print(res)
# res = 10