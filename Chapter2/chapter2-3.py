#              ２－３　条件分岐


#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
def exception3(x,y,z):
    if x != y and x != z:
        return(x)
    elif y != x:
        return(y)
    else:
        return(z)

# print(exception3(1,2,2))
# print(exception3(4,2,4))
# print(exception3(9,3,9))

#           練習問題　練習問題　練習問題　練習問題　練習問題　練習問題　
def exception9(a):
    for x in a:
        if a.count(x) < 2:
            return x

# print(exception9([1,2,2,2,2,2,2,2,2]))
# print(exception9([4,4,4,4,4,2,4,4,4]))
# print(exception9([9,9,9,9,9,9,9,9,3]))



#       複数行の条件式