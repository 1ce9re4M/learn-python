numbers = [0, 10, 20, 30, 40, 50]
# print(numbers)
# print(type(numbers))

#       練習問題　練習問題　練習問題　練習問題　練習問題
def remove_evenindex(ln):
    return ln[1::2]

# print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
# print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])

#多重リスト
lns = [[1, 2, 3], [10, 20, 30], ["a", "b", "c"]]
# print(lns[1][0])
# print([2])
lns2 = [lns, [10, 20, 30], ['a', 'b', 'c']]
# print(lns2)         #[[[1, 2, 3], [10, 20, 30], ['a', 'b', 'c']], [10, 20, 30], ['a', 'b', 'c']]
# print(lns2[0])      #[[1, 2, 3], [10, 20, 30], ['a', 'b', 'c']]

numbers = [0, 10, 20, 30, 40, 50]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
chara = ['か', 'お', 'え']
# print(min(chara))     #max,minは文字列にも適用可能

#リストと演算子
# print(numbers + ['a', 'b', 'c'])
# print(numbers * 3)
# print(['a'] * 10)
x = [[0,1], ['a,b']]
# print(x[0][0])
y = x*3
# print(y)
x[0][0] = 100
# print(y)

#       a1 ＝＝　in　である。orが多いときはinを使えば見やすい
a1 = 1
# print(a1 == 1 or a1 == 3 or a1 == 7, a1 in [1, 3, 7])
a1 = 5
# print(a1 == 1 or a1 == 3 or a1 == 7, a1 in [1, 3, 7])

#       indexはリストでも使える。findはリストで使うことはできない
# print(numbers.index(20))
# print(numbers.find(20)) #これはエラーになる

numbers = ['b', 'a', 'c', '10', 'あ', 'd']
# numbers.sort()
# print(numbers)      #これはnumbersをそのまま入れ替えた(10, a, b, c, d, 'あ')

x = sorted(numbers)
# print(x)  #これはnumbersとxがそれぞれ存在(sorted関数)

x.sort(reverse = True)
# print(x)        #これは降順

# print(sorted(numbers, reverse=True))   #これも降順

ins = [[1,5], [5,2], [3,4], [4,1], [2,3]]
ins.sort()
# print(ins)      #多重リストもできちゃう

x.append('20')  #リストに要素を入れる.append()
x.append('30')
x.append('40')

x.extend(['100', '200'])    #リストにリストを追加.extend
# print(x)

numbers = [10, 20, 30, 40, 20]
numbers.insert(1, 1000)
# print(numbers)              #リストに要素を挿入する

numbers.remove(30)
# print(numbers)                #要素を削除（値を直接入れる）
numbers.remove(20)
# print(numbers)                #該当箇所が複数の場合最初を消す

#       インデックス指定で削除
numbers = [1, 2, 3, 4, 5]
# print(numbers.pop(4))   #これは削除した値が出てくる
# print(numbers)

ln = [10, 20, 30, 20, 40, 70]
ln.pop()        #インデックス指定なしで最後尾を削除
# print(ln)

del ln[2]   # del も可能
# print(ln)
del ln[0:3] #スライスでも可能
# print(ln)

numbers = [10, 20, 30, 40, 50, 60, 70]
numbers2 = numbers.copy()   #コピー
# numbers2 = numbers とする(代入)と変化が両方に効いちゃう

del numbers[1:3]
numbers.reverse()           #反転
# print(numbers2)
# print(numbers)

#   文章をリスト化  list()  逆は''.join()
a = list('Aston Villaは昨シーズン主力の選手が6名いなくなり戦力の刷新を行った。今シーズンは新たに取った若手選手やアンダーから上がってきた選手がいかにフィットするが勝敗の鍵になりそうだ。')
# print(a)
# print(''.join(a))

#       指定の文字で区切る 指定の文字は消える
a = 'banana'.split('n')     #[ba, a, a]
# print(a)



#           練習問題　練習問題　練習問題　練習問題　練習問題
def change_domain(email, domain):
    n = email.index('@')
    email = email[: n+1] + domain
    return email
#           模範解答
def change_domain(email, domain):
    return "@".join([email.split("@")[0], domain])



# print(change_domain('majhdiog@gmail.com', 'hfoeh.com.jp'))
# print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')

#       タプル  要素の変更不可。探すだけ
x, y = 3, 5
point = (x, y)
# print(point)
x = 1, 2, 3, 4, 5
# print(x)

list = [1, 2, 3 ,4 ,5]
# print(tuple(list))  #リストをタプル化



#              練習問題　練習問題　練習問題　練習問題　練習問題
def reverse_totuple(ln):
    ln.reverse()
    # print(ln)
    ln2 = tuple(ln)
    return ln2



# print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))

#           多重代入
numbers = [0, 10, 20, 30, 40]
[a, b, c, d, e] = numbers   # a, b, c, d, e でも同様
# print(a, c)

a, b, c, d, e = "Villa"
# print(a, c, e)

    #   書き方いろいろ
x, y, z = (1, 2, 3)
# print(y)
(x, y, z) = (1, 2, 3)
# print(y)
(x, y, z) = 1, 2, 3
# print(y)
x, y, z = 1, 2, 3
# print(y)

#       for文
ls = [0,1,2]
# for value in ls:
#     print("For loop:" + str(value))

numbers = [0,1,5,3,4,5]
num = []
for x in numbers:
    num.append(x**2)
# print(num)



#           練習問題　練習問題　練習問題　練習問題　練習問題
def sum_list(ln):
    sum_num = 0
    for x in ln:
        sum_num += x
    return sum_num



# print(sum_list([10, 20, 30]) == 60)
# print(sum_list([-1, 2, -3, 4, -5]) == -3)

str1 = "apple and pen"
# for x in str1:
    # print(x)
    # print(x.upper())


#           練習問題　練習問題　練習問題　練習問題　練習問題
def atgc_countlist(str_atgc):
    a = [[0,"A"], [0,"T"],[0,"G"],[0,"C"]]
    for x in str_atgc:
        if x == "A":
            a[0][0] += 1 
        elif x == "T":
            a[1][0] += 1
        elif x == "G":
            a[2][0] += 1
        else:
            a[3][0] += 1
    return a   
#           模範解答　模範解答　模範解答　模範解答　模範解答
def atgc_countlist(str_atgc):
    list_count = []
    for x in 'ATGC':
        int_bpcnt = str_atgc.count(x)
        list_count.append([int_bpcnt, x])
#           Gemini　Gemini　Gemini　Gemini　Gemini　Gemini
def atgc_countlist(str_atgc):
    counts = {"A":0, "T":0, "G":0, "C":0}
    for x in str_atgc:
        if x in counts:
            counts[x] += 1
    return [[counts[x], x] for x in "ATGC"]

from collections import Counter
def atgc_countlist(str_atgc):
    c = Counter(str_atgc)
    return [[c[x], x] for x in "ATGC"]



# print(atgc_countlist("AAATTGCGC"))
# print(sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))


#       for文によるリストの初期化

numbers = [0,1,2,3,4,5]
squares1 = []

for x in numbers:
    squares1.append(x**2)
# print(squares1)
#   内包表記を用いると。。。
squares2 = [x**2 for x in numbers]
# print(squares2)
