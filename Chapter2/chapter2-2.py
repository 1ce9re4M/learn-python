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

#リストと演算子から