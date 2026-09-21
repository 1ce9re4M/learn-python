def greeting():
    print("Hello")

# greeting()

def greeting(greeting_local):
    print(greeting_local)

# greeting("Up The Villa")

def greeting(greeting_local):
    return greeting_local
# print(greeting("Sorachan!"))

def ave(nums):
    return sum(nums)/len(nums)
# print(ave([1,3,5,7,9]))

greet = greeting("Hello")
# print(greet)

def greeting(en, fr, de):
    print(en + "," + fr + "," + de)
# greeting("hello", "bonjour", "guten tag")

def greeting(en, number, name):
    print(en * number + "," + name)
# greeting("Hello ", 3, " I'm Mike")

def greeting():
    global greeting_global
    greeting_global = "Bonjour"
    print(greeting_global)
# greeting()
# print(greeting_global)

def greeting(en, number, name):
    print(en*number+ "," +name)
# greeting(en="hello ", name="japan", number=2)

def greeting(name, en="hello "):
    print(en + "," + name)
# greeting("world")

#   タプルとして引き出せる
def greeting(*args):
    print(args)
# greeting("hello", "bonjour", "guten tag")

#   リストをタプルとして渡す
gre_list = ["hello", "bonjour", "guten tag"]
# greeting(*gre_list)

#   **で辞書として引き出せる
def greeting(**kwargs):
    print(kwargs)
#   キー = 値   の形になる
# greeting(en="hello", fr="bonjour", de="gurten tag")

greeting_dict = {"en": "hello", "fr":"bonjour", "de":"guten tag"}
# greeting(**greeting_dict)


#   def 関数名(位置引数, 初期値を持つ引数, 可変長引数, 辞書型の可変長引数)
def greeting(greet, en="hello", *args, **kwargs):
    print(greet)
    print(en)
    print(args)
    print(kwargs)
greeting_list = ["bonjour"]
greeting_dict = {"de":"guten tag"}
greeting("Hi", "Hello", *greeting_list, **greeting_dict)