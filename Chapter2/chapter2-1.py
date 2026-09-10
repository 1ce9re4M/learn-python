# word1 = "hello"
# print(type(word1))

f = ("123.4")
# print(type(f))
# f = int("123")
# print(type(f))
# f = float("123.4")
# print(type(f))    #int,float = 文字列を実数にできる

# print(len(f))

digits1 = "0123456789"
# print(digits1[1::2])
price = "2,489円"
a = price.replace(",", "")  #文字列の入れ替え、””で削除
# print(a[1])
# print(a)
# print(price.replace("2","3" ))


text = "Aston Villa Football Club is a professional football club based in Aston, Birmingham, England. Founded in 1874, it competes in the Premier League, the top tier of English football, and has played at its home ground, Villa Park, since 1897. Aston Villa is one of the oldest and most successful clubs in England, having won the Football League First Division seven times, the FA Cup seven times, the League Cup five times, as well as the European Cup, European Super Cup, and Europa League once. Aston Villa has been a leading English club since the 1880s, when it was a pioneer of the modern passing game. This short, slick combination passing style was introduced by Scotsman George Ramsay, who was appointed as the world's first professional football manager in 1886. The club was influential in the sport's move to professionalism in 1885, and it was a Villa director, William McGregor, who founded the world's first Football League in 1888."
# print(text)
# x = input("検索したい言葉：")
def word(x):
    if x in text:
        return "検出しました"
    else:
        return "検出できません"

# print(word(x))

#特殊文字   \" \", \n, \\や'''〇〇'''など
# print("You are my \"Girl\"")
# print("You are \"Mine♡\"")
# print('''I cant see anymore but \"You\"\nI\'ll steal your Love''')

#      練習問題
def remove_punctuations(str_engsentencees):
    str1 = str_engsentencees.replace(".", "")
    str1 = str1.replace(",", "")
    str1 = str1.replace(":", "")
    str1 = str1.replace(";", "")
    str1 = str1.replace("?", "")
    str1 = str1.replace("!", "")
    return str1

# print(remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?') == 'Quiet uh donations you want me to make a donation to the coast guard youth auxiliary')

#           練習問題２
def atgc_bppair(str_atgc):
    Atot = str_atgc.replace("A", "t")
    Ttoa = Atot.replace("T","a").replace("a","A")
    Gtoc = Ttoa.replace("G", "c").replace("t", "T")
    CtoG = Gtoc.replace("C","G").replace("c","C")
    return CtoG

# print(atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT')

word1 = "hello"
# print(word1.index('lo'))    #findも同様、エラーは-1となる
# print(word1.index('l'))

#           練習問題
def swap_colon(str1):
    n = str1.find(':')
    str2 = str1[n+1:] + ':' + str1[0:n]
    return str2

# print(swap_colon('hello:world'))

word1 = 'hello'
# print(word1.count('l'))

#           練習問題
def atgc_count(str_atgc, str_bpname):
    return str_atgc.count(str_bpname)

# print(atgc_count('AAGCCCCATGGTAA', 'A') == 5)

#       大文字小文字
upper_dna = "DNA"
a = upper_dna.lower()
# print(a)
b = a.upper()
# print(b)


lower_text = "hello world"
c = lower_text.capitalize()
# print(c)

#       空白文字の削除
# print('     abc\n'.strip())     #abc
# print('   a b c   '.strip())    #a b c
# print('     abc\n'.lstrip())    #abc\n
# print('     abc\n'.rstrip())    #     abc

#           練習問題１
def check_lower(str_engsentences):
    a = str_engsentences.lower()
    if a == str_engsentences:
        return True
    else:
        return False
# print(check_lower('down down down') == True)
# print(check_lower('There were doors all round the hall, but they were all locked') == False)

#           模範解答
# def check_lower(str_engsentences):
#     if str_engsentences == str_engsentences.lower():
#         return True
#     return False

#           練習問題２
def remove_clause(str_engsentences):
    n = str_engsentences.find(",")
    a = str_engsentences[n+1:]
    a = a.lstrip()
    b = a.capitalize()
    return b

# print(remove_clause("It's being seen, but you aren't observing.") == "But you aren't observing.")

#           模範解答
# def remove_clause(str_engsentences):
#     int_index = str_engsentences.find(',')
#     str1 = str_engsentences[int_index+2:]
#     return str1.capitalize()