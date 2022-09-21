# Qn30_猜數字
print("猜數字遊戲開始 ! ")
ans="1234"
while True:
    inp = input("請猜4位數字(輸入'0000'離開):")
    if inp == '0000':
        print('已離開遊戲')
        break

    else:
        a=0
        b=0
        if ans==inp:
            print("恭喜全對")
            break
        for i in range(4):
            if inp[i] == ans[i]:
                a=a+1
            elif inp[i] in ans:
                b=b+1

        print(f"結果為:{a}A{b}B")
