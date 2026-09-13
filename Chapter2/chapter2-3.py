#              ２－３　条件分岐


#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
def exception3(x,y,z):
    if x != y and x != z:
        return(x)
    elif y != x:
        return(y)
    else:
        return(z)

#           模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　
#           模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　
def exception3(x,y,z):
    if x == y:
        return z
    elif y == z:
        return x
    else:
        return y



# print(exception3(1,2,2))
# print(exception3(4,2,4))
# print(exception3(9,3,9))




#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
def exception9(a):
    for x in a:
        if a.count(x) < 2:
            return x

#           模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　
#           模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　
def exception9(a):
    x = a[0] + a[1] + a[2]
    y = a[3] + a[4] + a[5]
    z = a[6] + a[7] + a[8]
    if x == y:
        return exception3(a[6],a[7],a[8])
    if x == z:
        return exception3(a[3],a[4],a[5])
    else:
        return exception3(a[0],a[1],a[2])


# print(exception9([1,2,2,2,2,2,2,2,2]))
# print(exception9([4,4,4,4,4,2,4,4,4]))
# print(exception9([9,9,9,9,9,9,9,9,3]))



#       複数行の条件式
x,y,z = (-1, -2, -3)
# if (x<0 and y<0 and z<0 and 
#     x != y and y != z and z != x):
#     print('x, y and z are different and negatives.')

#   行末にバックスラッシュを入れる
#   行を変えることができ視認性が上がる　\のあと空白はNG
x, y, z = (-1, -2, -3)
# if x < 0 and y < 0 and z < 0 and \
#     x != y and y != z and x != z:
#     # print('x, y and z are different and negatives.')



#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
x = -1
# if x < 3 and x >= 2:
#     print('x is larger than or equal to 2, and less than 3')
# elif x < 2 and x >= 1:
#     print('x is larger than or equal to 1, and less than 2')
# elif x < 1:
#     print('x is less than 1')
# else:
#     print('x is larger than or equal to 3')

#           模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　
#           模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　模範解答　
# x = -1
# if x < 1:
#     print('x is less than 1')
# elif x < 2:
#     print('x is larger than or equal to 1, and less than 2')
# elif x < 3:
#     print('x is larger than or equal to 2, and less than 3')
# else:
#     print('x is larger than or equal to 3')




#   3項演算子
x = 0
sign = 'positive or zero' if x >= 0 else 'negative'
print(sign)