#-------------  -------------------------------------
words = ['dog', 'cat', 'mouse']
# for w in words:
#     print(w, len(w))
# print('finish')

word = 'supercalifragilisticexpialidocious'
# for c in word:
    # print(c)

#--------- ord関数, chr関数  ---------------------------------------------------------------
#   与えられた文字の番号(コード)を整数として返す
# print(ord('a'))     #97
# print(ord('b'))     #98
# print(chr(97))      # a

#   ordを用いた文字の出現回数判別
height = [0] * 26
for c in word:
    height[ord(c) - ord('a')] += 1
# print(height)

# -------------- for文と辞書 --------------------------------------------------------------
dic1 = {'cat':3, 'dog':3, 'elephant':8}
# for key in dic1:
#     print('key:', key, ',value:', dic1[key])

#   values関数を使うとそのまま取り出せるよ
# for value in dic1.values():
#     print('value', value)

#   itemsメソッドでキーと値を同時に取り出せる
# for key, value in dic1.items():
#     print('key:', key, 'value:', value)



#=============練習問題　練習問題 ===================================================================
#=============練習問題　練習問題 ===================================================================
# def reverse_lookup2(dic1):
#     for key,value in dic1.items():
#         if key not in dic1.values():
            
#         else:
            
#============= 模範解答　模範解答 =====================================================================
#============= 模範解答　模範解答 =====================================================================
def reverse_lookup2(dic1):
    dic2 = {} 
    for key, value in dic1.items():
        dic2[value] = key   #{value: key}の形を追加するよってこと
    return dic2


# print(reverse_lookup2({'apple': 3, 'pen': 5, 'orange': 7}))

# ------------- renge関数 -------------------------------------------------------------------------
# for value in range(5):
#     print('hi')

s = 0
for i in range(10):
    s = s+i
# print(s)

s = 0
for i in range(1,10,2):
    s = s+i
# print(s)



#=============練習問題　練習問題 ===================================================================
#=============練習問題　練習問題 ===================================================================
def sum_n(x, y):
    n = 0
    for i in range(x,y+1):
        n += i
    return n
# print(sum_n(2, 4))




#=============練習問題　練習問題 ===================================================================
#=============練習問題　練習問題 ===================================================================
def construct_list(int_size):
    ln = []
    for i in range(int_size):
        ln.append(i)
    return ln

# print(construct_list(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#------------ rangeとリスト ----------------------------------------------------------------------------

seq_list = list(range(5))
# print(seq_list)

#--------------- for文のリスト -------------------------------------------------------------------------

list1 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]

# for i in range(4):
#     for j in range(3):
#         print('list1の', i + 1, '番目の要素の', j + 1, '番目の要素 =', list1[i][j])

C = [[1]]
for i in range(100):
    C.append([1]+[0]*i+[1])
    for j in range(i):
        C[i+1][j+1] = C[i][j] + C[i][j+1]

# C[:10]

import matplotlib as plt
# plt.plot(C[100])



# ---------------- 練習 -----------------------------------------------------------------------------------
# ---------------- 練習 -----------------------------------------------------------------------------------
def sum_lists(list1):
    c = 0
    for x in list1:
        for n in x:
            c += n
    return c

# print(sum_lists([[20, 5], [6, 16, 14, 5], [16, 8, 16, 17, 14], [1], [5, 3, 5, 7]]) == 158)




# ---------------- 練習 -----------------------------------------------------------------------------------
# ---------------- 練習 -----------------------------------------------------------------------------------

def sum_matrix(list1, list2):
    list3 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            list3[i][j] += list2[i][j] + list1[i][j]
            
    return list3

# ---------------- 模範解答 -----------------------------------------------------------------------------------
# ---------------- 模範解答 -----------------------------------------------------------------------------------
def matrix(list1, list2):
    list3 = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(3):
        for j in range(3):
            list3[i][j] += list1[i][j] + list2[i][j]
    return list3

# print(sum_matrix([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]) == [[2, 6, 10], [6, 10, 14], [10, 14, 18]])


#--------------- 計算量　オーダー　O(n) --------------------------------------------------------------------------------------

#リストとして与えられたデータの平均と分散
def average(d):
    s = 0
    for x in d:
        s = s+x
    return s/len(d) #平均

def variance(d):
    s = 0
    for x in d:
        s = s + (x - average(d)) ** 2
    return s/len(d) #分散

import random
d100 = []
for i in range(100):
    d100.append(random.gauss(0,10)) # .gauss 正規分布に従う分布
d10000 = []
for i in range(10000):
    d10000.append(random.gauss(0,10))

# print(variance(d100))   # variance 分散を計算するためのもの
# print(variance(d10000)) #出力までめっちゃおそい

def variance(d):
    av = average(d)
    s = 0
    for x in d:
        s = s + (x-av)**2
    return s/len(d)

# ----------- enumerate()関数 ---------------------------------------------------------
#ループ時に値とインデックス(数値)を同時に取り出せる
words = ['dog', 'cat', 'mouse']
mapping = {}
for i, w in enumerate(words):
    mapping[w] = i

# print(mapping) # {'dog': 0, 'cat': 1, 'mouse': 2} が得られる。


#------------ while文 -------------------------------------------------------------
# Falseになるまで行うループ処理のこと
x = 1
total = 0
while x <= 10:
    total += x
    x += 1
# print(x, total)

#----------制御構造とreturn文-------------------------------------------------------------------
def simple_lsearch(lst, myitem):
    for item in lst:
        if item == myitem:
            return True
    return False

#--------break文-------------------------------------------------------------------------------
x = 256
total = 0
while x > 0:
    if total > 500:
        break
    total += x
    x = x//2
# print(x, total) #出力結果 4 504


#-----------練習問題　練習問題　練習問題　練習問題　----------------------------------------------------------
#-----------練習問題　練習問題　練習問題　練習問題　----------------------------------------------------------
def simple_match(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        j = 0
        while j 

# location, cat