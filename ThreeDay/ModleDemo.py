from random import randint  # 导入模块中的函数
import platform as plf  # 导入模块并重命名

print(dir(plf))  # 查看模块中的所有函数

print(plf.machine())  # 查看机器类型

print(plf.architecture())  # 查看机器位数

print(plf.system())  # 查看操作系统

print(plf.python_version())  # 查看python版本

print(randint(1, 10))  # 生成1-10的随机数
