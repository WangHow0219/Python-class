#作業_1 - 分組
N = int(input("輸入座號:"))
print("你的座號是:" + str(N))
N = N - 1
K = N // 5 + 1
if K == 0:K + 1
    
print("你是第 " + str(K) + " 組")

print("--------------------------")

#作業_2 - 買飲料
Buy = int(input("你要買幾瓶飲料:"))
print("你要買 " + str(Buy) + " 瓶飲料")
Da = Buy // 12  #商 = 打數
MD = Da * 200   # $ * 打數
P = Buy % 12    #餘 = 個別瓶數
Mp = P * 20     # $ * 瓶數
Mall = MD + Mp
print("好，這樣總共是:" + str(Mall))
print("==========================")
