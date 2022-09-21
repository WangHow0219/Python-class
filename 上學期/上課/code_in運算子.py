# in 運算子
   #tuple
a = (1,2,3,4)
b = int(input("輸入一正數"))
if b in a:
    print(f"{b} 在 tuple a 中")
else:
    print(f"{b} 不在 tuple a 中")

    #lang
lang1 = {"謝謝":"Thank you"}
c = input("輸入謝謝")
if c in lang1:
    print("謝謝的英文是", lang1["謝謝"])
else:
    print("查無結果")

    #set
d = set("tiger")
e = input("輸入一字母")
if e in d:
    print(f"字母 {e} 在此集合中")
else:
    print(f"字母 {e} 不在此集合中")
