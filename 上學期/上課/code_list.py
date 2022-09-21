# 取得串列的'項目數'
# len(list)
list_abc = ['a', 'b', 'c', 'd' ,'e' ,'f', 'g']
print(len(list_abc))

# 找到項目的'位置'
# list.index()
color1 = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
X = (color1.index('green'))
print(X)

# 計算項目'出現的次數'
# list.count()
color2 = ['red', 'black', 'red', 'black', 'black', 'black']
print(color2.count('black'))

# 提取子串列 
# list[起點 : 終點 : 間隔]
numb1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(numb1[0:7:2])
print(numb1[:5:])
print(numb1[::3])
print(numb1[::-1])

# 給串列內的項目一個'變數名稱'
# name = list[位置]
color1 = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
A = color1[0]
B = color1[1]
C = color1[2]
print(A, B, C)
# 整批一起給 (變數的數量需與串列中的項目數量一致)
# name1, name2, name3 = list
A, B, C, D, E, F = color1
print(A, B, C, D, E, F)

'''
===排序 sort()===
預設是由小到大，會改變原串列
語法 : list.sort()

如果要由大到小
語法 : list.sort(reverse = True)
'''
numb2 = [5, 7, 9, 1, 3, 55]
numb2.sort()
print(numb2)

numb2.sort(reverse=True)
print(numb2)

# 將項目加到串列尾端
# list.append()
list_abc = ['a', 'b', 'c', 'd' ,'e' ,'f', 'g']
list_abc.append('h')

'''
== 取代'字串'中的'字元' ==
語法 : TEXT.replace('舊', '新', 次數)
'''
TEXT = 'glglglttaa'
Anser = TEXT.replace('gl','X',2)
print(Anser)
