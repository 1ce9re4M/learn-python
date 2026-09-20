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
        while j < len(str2) and str1[i+j] == str2[j]:
            j += 1
        if j == len(str2):
            return j
    return -1


# ~~~~~~~~~~~模範解答　模範解答　模範解答　模範解答　～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～
# ~~~~~~~~~~~模範解答　模範解答　模範解答　模範解答　～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～
def simple_match(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        j = 0
        while j < len(str2) and str1[i+j] == str2[j]:
            j += 1
        if j == len(str2):
            return i
    return -1

# iの1周目
# i = 0
# | j = 0
# | str1[0]:l != str2[0]:c
# iの2周目
# i = 1
# | j = 0
# | str1[1+0]:o != str2[0]:c
# iの3周目
# i = 2
# | j = 0
# | str1[2+0]:c == str2[0]:c
# | j += 1
# | j = 1
# | str1[2+1]:a == str2[1]:a
# | j+= 1
# | j = 2
# | str1[2+2]:t == str2[2]:t
# | j += 1
# | j=3 == len(str):"cat"=3
# | return i 終わり


# print(simple_match('location', 'cat') == 2)
# print(simple_match('soccer', 'cat') == -1)
# print(simple_match('category', 'cat') == 0)
# print(simple_match('carpet', 'cat') == -1)

#------ continue文 ---------------------------------------
# continue:該当のループをスキップ　brek:ループ自体を終了
colors = ["red", "green", "blue", "black", "white"]
for c in colors:
    if c == "black":
        continue
    # print(c)

for c in colors:
    if c == "black":
        break
    # print(c)
#出力結果
# continue文       break文
# red              red
# green            green
# blue             blue
# white 

#---------- pass文 -------------------------------------------------
#空の実行文を作る
x = -1
def search_value(x):
    if x < 0:
        print("x is negative")
    elif x == 0:
        # no error
        pass
    elif 0 < x < 5:
        print("x is positive and smaller than 5")
    else:
        print("x is positive and larger than or equal to 5")

#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------

from time import sleep
x = 1
def yeah(x):
    while True:
        print("Yeah!", x)
        if x == 10:
            break
        x += 1 
        sleep(1)    # 1秒待つってこと


#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def collect_engwords(str_engsentence):
    str_engsentence = str_engsentence.replace("," , "").replace(".", "")
    a = str_engsentence.split(" ")
    result = []
    for x in a:
        # print(x)
        if len(x) >= 3:
            result.append(x)
    return result

# print(collect_engwords('Unfortunately no, it requires something with a little more kick, plutonium.') == ['Unfortunately', 'requires', 'something', 'with', 'little', 'more', 'kick', 'plutonium'])



#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def swap_lists(ln1, ln2):
    ln1_change_odd = []
    ln2_change_odd = []
    for i in range(len(ln1)):   #["12345"]ならi = 0~4
        # print(i)
        if i%2 != 0:    #インデックス(i)が奇数
            ln1_change_odd.append(ln2[i])
            ln2_change_odd.append(ln1[i])
        else:
            ln1_change_odd.append(ln1[i])
            ln2_change_odd.append(ln2[i])
        # print(ln1_change_odd, ln2_change_odd)
    return(ln1_change_odd, ln2_change_odd)

# print(swap_lists([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']) == ([1, 'b', 3, 'd', 5], ['a', 2, 'c', 4, 'e']))




#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def count_capitalletters(str1):
    upper_count = 0
    for x in str1:
        # print(x)
        if x.isalpha() == True: # .isaplhpa 英字かどうかの判定
            if x == x.upper():
                upper_count += 1
                # print(upper_count)
    return upper_count

# print(count_capitalletters('Que Será, Será') == 3)



#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def identify_codons(str_augc):
    str_threetimes = []
    for i in range(len(str_augc)//3):
        str_threetimes.append(str_augc[3*i:3*i+3])
    return str_threetimes

# print(identify_codons('CCCCCGGCACCT') == ['CCC', 'CCG', 'GCA', 'CCT'])



#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def add_commas(int1):
    int2 = int1.copy()
    count = 0
    for x in range(len(int1)):
        if x%3 == 0 and x != 0:
            int2 = int2[:x+count+1] + "," + int2[x+count+2:]
            count += 1

# 2回目
def add_commas(int1):
    count = 1
    list1 = list(str(int1))
    str1 = ""
    for i in range(len(list1)-1, -1, -1):
        str1 = list1[i] + str1
        if i%3 == 0 and i != 0:
            str1 = "," + str1
            # print(str1)
        count += 1
    return str1
# print(add_commas(1123456789))
# ^^^^^^^^^^^^^^^^^^^^^模範解答　模範解答　模範解答　模範解答　^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^^^^^^^^^^^^^^^^^模範解答　模範解答　模範解答　模範解答　^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def add_commas(int1):
    list1 = list(str(int1))
    str1 = ""
    ccnt = 1
    for i in range(len(list1)-1, -1, -1):   #(start, stop, step)
        print(i)
        str1 = list1[i] + str1
        if ccnt % 3 == 0 and ccnt != 0:
            str1 = "," + str1
        ccnt += 1
    return str1    


#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def sum_strings(list1):
    str1 = ""
    str_list1 = [str(i) for i in list1]

    for k in range(len(str_list1)-1, -1, -1):
        if k == len(str_list1)-1 and len(str_list1) > 0:
            str1 = " and " + str_list1[k]
        elif k == 0:
            str1 = str_list1[k] + str1
        else:
            str1 = ", " + str_list1[k] + str1
    return str1

# print(sum_strings(['a', 'b', 'c', 'd']))
# print(sum_strings(['a']))
# print(sum_strings(["a", "b"]))
# print(sum_strings([1, 2, 3]) == '1, 2 and 3')



#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def handle_collision2(dic1, str1):
    #str1の長さのキーがなければ長さをキー、str1自体を値とする
    if len(str1) not in dic1:
        dic1[len(str1)] = str1
        return dic1

    #lstr1の長さがすでにdic1のキーとして存在している場合
    for x in dic1:
        if x == len(str1):
            #len(str1)+1 ~ 10,1 ~ len(str1)-1 までで
            # 空いている数字をキー,str1を値として追加する
            for j in range(10):
                i = (len(str1)+1+j)%10
                if i not in dic1 and i != 0:
                    dic1[i] = str1
                    return dic1
    return dic1

                
# dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd'}
# print(handle_collision2(dic1_orig, 'Big Four'))
# print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four'})
# dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House'}
# print(handle_collision2(dic1_orig, 'Edgware'))
# print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware'})
# dic1_orig = {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'}
# print(handle_collision2(dic1_orig, 'ABC'))
# print(dic1_orig == {6: 'Styles', 4: 'Link', 7: 'Ackroyd', 8: 'Big Four', 10: 'Blue Train', 9: 'End House', 1: 'Edgware', 2: 'Orient', 3: 'Three Act', 5: 'Clouds'})



#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
#------練習問題 練習問題　練習問題　練習問題　練習問題-------------------------------------------------------------
def handle_collision3(list1):
    result_dic = {}
    for i in list1:
        if i[0] not in result_dic:
            result_dic[i[0]] = i[1]
        # else:
        #     pass     #elseはなくても成立するじゃん！
    return result_dic

print(handle_collision3([[3, 'Richard III'], [1, 'Othello'], [2, 'Tempest'], [3, 'King John'], [4, 'Midsummer'], [1, 'Lear']]) == {1: 'Othello', 2: 'Tempest', 3: 'Richard III', 4: 'Midsummer'})