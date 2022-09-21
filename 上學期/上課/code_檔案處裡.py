"""
檔案處裡
"""
text1 = "WangHow is good"

# w => 覆蓋寫入
f = open('book_A.txt','w',encoding='UTF-8')
f.write(text1)
f.close()

# r => 讀取
f = open('book_A.txt','r',encoding='UTF-8')
for line in f:
    print(line,end="")
f.close()

# a => 不覆蓋寫入
f = open('book_A.txt','a',encoding='UTF-8')
f.write(text1)
f.close()
