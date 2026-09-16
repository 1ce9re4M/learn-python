a = {"apple": 0, "orange": 1, "banana": 2}
# print(type(a))
# print(a)
# print(a["apple"])
# print(a["orange"])

#--- 数値の変更と追加 ----------------------------------------------
a["apple"] = 10
a["pineapple"] = 3    
# print(a)

# print("banana" in a)      #キーが存在するか in で判別可能

#   削除
del a["orange"]
# print(a)
# --------------------------------------------------------------------------------



#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題
#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題
def reverse_lookup(list1):
    value_key = {}
    n = 0
    for x in list1:
        value_key[x] = n
        n += 1
    return value_key
#-----------模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　 ------------------------------------------
#-----------模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　 ------------------------------------------
def reverse_lookup(list1):
    dic1 = {}
    for value in list1:
        dic1[value] = list1.index(value)
    return dic1

# print(reverse_lookup(["apple", "orange"]))
# print(reverse_lookup(['apple', 'pen', 'orange']) == {'apple': 0, 'orange': 2, 'pen': 1})



#------------- 辞書のメソッド -------------------------------------------

#      .get()
a = {"apple": 2, "orange": 5, "pineapple": 10, "banana": 40}
# print("キーappleに対応する値 =", a.get("apple"))
# print("キーorengeに対応する値 =", a.get("orange"))
# print("そらちゃんと俺の関係性 =", str(a.get("sorachan")) + "😢")

#       .setdefault()
a.setdefault("apple", 100)  #既存のキーは対応する値を返す
a.setdefault("そらちゃん", 100) #新しくキーと値を追加できる

#ーーーーー以下と同様の手続きであるーーーーーーーーーーーーーーーーーーーーーー

a = {"apple":2, "orange":5, "pineapple":10, "banana":40}
if "apple" not in a:
    a["apple"] = 7
if "そらちゃん" not in a:
    a["そらちゃん"] = 100

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

# print(a)

#------------ .pop() による削除 ------------------------------------------------------
a.pop("pineapple")
# print(a)

#------------- .clear() で全消去 ----------------------------------------------------

# a.clear()
# print(a)

#------------- 辞書における list() ---------------------------------------------
b = list(a.keys())      #キーをリスト化
c = list(a.values())    #値をリスト化
d = list(a.items())     #キーと値をペアでリスト化
# print(b)
# print(c)
# print(d)

#           .copy   で複製可能

ks = a.keys()      #こっちはリアルタイムビュー

#print(ks, list(ks))
#それぞれの出力結果
# dict_keys(['apple', 'orange', 'banana', 'そらちゃん']) 
# ['apple', 'orange', 'banana', 'そらちゃん']

#----------辞書とリスト--------------------------------------------------
numbers = {"dozens": [10,20,40], "hundreds": [100, 101, 120, 140]}
a = numbers["dozens"]
b = numbers["hundreds"][1]
# print(a, b)

#----------- 辞書を連結させリストにすることも可能----------------------
fru = {"apple":1, "orange":2, "pine":3, "banana":4}
spo = {"football":10, "baseball":20, "basketball":30}
id = [fru, spo]
# print(id)
# print(id[1]["football"])




#-------- 練習問題　練習問題　練習問題 --------------------------------------------
#-------- 練習問題　練習問題　練習問題 --------------------------------------------
def handle_collision(dic1, str1):
    n = len(str1)
    #リスト化してキーにｎ値にそのリストをいれればいけるか？
    if n not in dic1:
        ls = list(str1)
        #teaが["t", "e", "a"]となるので不適
        # ls = [str] -> ["tea"]が正解

        dic1.setdefault(n, ls)
        return dic1
    #dic1のキーｎの値にstr1を追加したい
    else:
        dic1[n].append(str1)
        return dic1

#--------- 模範解答 -----------------------------------------------------------------------------------------
def hundle_collision(dic1, str1):
    #.get() 値が存在すれば値を返しなければNoneを返す
    if dic1.get(len(str1)) is None: 
        ls = [str1]
    else:
        ls = dic1[len(str1)]
        ls.append(str1)
    dic1[len(str1)] = ls



# dic1_orig = {3: ['ham', 'egg'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
# dic1_result = {3: ['ham', 'egg', 'tea'], 6: ['coffee', 'brandy'], 9: ['port wine'], 15: ['curried chicken']}
# handle_collision(dic1_orig, 'tea')
# print(dic1_orig == dic1_result)