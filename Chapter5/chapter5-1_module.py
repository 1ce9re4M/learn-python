# import モジュール名
import math
def math_func():
    print(math.sqrt(2)) # sqrt 平方根
    print(math.pi)  # pi の値
    print(math.sin(math.pi/4))  # sin 
    print(math.cos(0))  # cos
    print(math.log(32,2))   # 2 を底とする 32 の対数

# from モジュール名 import 関数名
from math import sqrt   # math. がいらない
def sqsq():
    print(sqrt(3))
# sqsq()

# from math import * <- ワイルドカード：＿以外で始まるものをすべて読み込む
# 非推奨！！

# as
import numpy
# print(numpy.ones((3, 5)))   # 3×5の行列
import numpy as np
# print(np.ones((3, 5)))


#------- 練習問題　練習問題　練習問題　練習問題　練習問題　 -----------------------
#------- 練習問題　練習問題　練習問題　練習問題　練習問題　 -----------------------
from math import sqrt, sin, pi
# print(sqrt(2))
# print(sin(pi))