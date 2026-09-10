#          １－１　数値演算
# a = float(10**20)
# print(a)
# print(int(a))

import math
# print(math.sqrt(2))
# print(math.pi)

# 黄金比(５の平方根に１を加え２で割ったもの)を求めよ
# a = float((math.sqrt(5) + 1) / 2 )
# print(a)






#          １－２　変数と関数の基礎
def bmi(height, weight):    #bmiという関数
    return weight / (height/100.0) ** 2

# h = float(input("身長："))
# w = float(input("体重："))
# a = bmi(h, w)
# bmi = round(a, 1)

# print("あなたのBMIは" + str(bmi) )

# if bmi >= 35:
#     print("高度の肥満です")
# elif bmi >= 30:
#     print("中度の肥満です")
# elif bmi >= 25:
#     print("低度の肥満です")
# elif bmi >= 18.5:
#     print("適正体重です")
# else:
#     print("低体重です")


def felt_air_temperature(temperture, humidity): #気温と湿度から体感温度を出す
    a = temperture - 1 / 2.3 * (temperture - 10) * (0.8 - humidity / 100)
    a = round(a, 1)
    return a

# print(felt_air_temperature(28, 50))



#          練習問題１
#   インチをセンチに変えよう　1ft=12in=30.48cm
def ft_to_cm(f,i):
    i /= 12
    return (f + i) * 30.48

assert round(ft_to_cm(5, 2) - 157.48, 6) == 0
assert round(ft_to_cm(6, 5) - 195.58, 6) == 0

#          練習問題２
#   ２次関数を計算しよう
def quadratic(a, b, c, x):
    return a*x**2 + b*x + c

assert quadratic(1, 2, 1, 3) == 16
assert quadratic(1, -5, -2, 7) == 12

def heron(a, b, c):
    s = 0.5*(a+b+c)
    return math.sqrt(s * (s-a) * (s-b) * (s-c) )

# s = 100
# print(heron(3,4,5))
# print(s)

#          練習問題１
#１　b^2-4acを求める
def qe_disc(a, b, c):
    return b**2 - 4*a*c

assert qe_disc(1, -2, 1) == 0
assert qe_disc(1, -5, 6) == 1

#２　解のうち小さいほうを選ぶ
def qe_solution1(a, b, c):
    z = math.sqrt(b**2 - 4*a*c)
    if z >= 0:
        x1 = (-b + z) // 2*a
        x2 = (-b - z) // 2*a
        return min(x1, x2)

    else:
        return None

assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
assert round(qe_solution1(1, -5, 6) - 2, 6) == 0

#３　解のうち大きいほうを選ぶ
def qe_solution2(a, b, c):
    z = math.sqrt(b**2 - 4*a*c)
    if z >= 0:
        x1 = (-b + z) // 2*a
        x2 = (-b - z) // 2*a
        return max(x1, x2)

    else:
        return None

assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
assert round(qe_solution2(1, -5, 6) - 3, 6) == 0

#   グローバル変数 関数の外で定義された変数を使うもの
g = 9.8

def force(m):
    return m*g

# print(force(104))

a = 10
def foo():
    return a
# print(foo())

def bar():  #ローカル変数なのでa = 10,20は干渉しない
    a = 3
    return a

# print(bar())
a = 20
# print(bar())




#         １－３
def bmax(a, b):
    if a > b:       #!= 等しくない、== 等しい
        return a
    else:
        return b

# print(bmax(3, 5))

def absolute(X):
    if X < 0:
        return X * (-1)
    else:
        return X

assert absolute(5) == 5
assert absolute(-5) == 5
assert absolute(0) == 0

def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

assert sign(5) == 1
assert sign(-5) == -1
assert sign(0) == 0

def is_even(x):
    return x%2 == 0

# print(is_even(2))
# print(is_even(3))

#再帰
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# print(fib(10))