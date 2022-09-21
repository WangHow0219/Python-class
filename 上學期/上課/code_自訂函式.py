"""
===自訂函式===
語法 :
def 函式名稱()
    程式區塊

def 函式名稱(參數1, 參數2, ...)
    程式區塊
    return 回傳值1, 回傳值2,...
"""

#無回傳值
def hello():
    print("hi!")
hello()

#有回傳值
def min(a, b):
    if a > b:
        return b
    else:
        return a
print(min(2, 4))
print(min(3, 1))

#計算面積
def area(w, h):
    area = w * h
    return area
print(area(5, 4))

#計算面積(有預設值)
def area(w, h=6):
    area = w * h
    return area
print(area(5))


"""
===全域變數 & 區域變數===
"""
def scope():
    var1 = 1
    print(var1,var2)

var1 = 10
var2 = 20

scope()
print(var1,var2)

def scope():
    global var1
    var1 = 1
    print(var1,var2)

var1 = 10
var2 = 20

scope()
print(var1,var2)

g = 5
def f1():
    print(g)
f1()

g = 5
def f1():
    g = 10
    print(g)
    #g = 10 (UnboundLocalError)
f1()

"""
===import 模組===
語法 : 
# 1.
import random
random.randint(參數)

# 2.
from random import *
randint(參數)

# 3.給模組別名
import random as r
r.randint(參數)
"""
# random.randint 隨機產生 5 個 0-10 的數
import random as r
for i in range(0,5):
    print(r.randint(0,10),end=" ")

# .randrange=>有增減值 (隨機產生5個 0-10 的'偶'數)
import random as r
for i in range(0,5):
    print(r.randrange(0,10,2),end=" ")

#隨機抽 5 個自訂樣本的數
import random as r
for i in range(0,5):
    print(r.choice([0,3,2,4,7,8]),end=" ")

import random as r
print(r.sample("abcdefg",8),end=" ")

"""
猜拳遊戲(自訂外部檔案模組)
"""
import guess
game = guess.gameStart()
print(game)

import guess as G
game = G.gameStart()
print(game)
