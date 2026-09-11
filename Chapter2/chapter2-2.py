numbers = [0, 10, 20, 30, 40, 50]
# print(numbers)
# print(type(numbers))

#       練習問題
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
