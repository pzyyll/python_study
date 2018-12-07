# 包管理，整合各种模块使得可以使用 import packname.moudle
# __init__.py 中声明的函数可以直接 packname.func()


# __all__ 用于控制用户 from packname import * 导入的模块
# 例如以下包含了 ['test_func', 'test_pack_init']，
# 则 from test_pack import * 之后只有 test_func 模块和 test_pack_init 可以直接使用
__all__ = ['test_func', 'test_pack_init']


def test_pack_init():
    print("test_pack_init")