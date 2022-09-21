# Qn27_最常迴文數字子數列
while True:
    inp = input('輸入整數數列(end 結束):')
    if inp == 'end':
        print('結束')
        break

    else:
        All_num = []
        for p in range(len(inp),0,-1):
            for u in range(p):
                All_num.append((inp[u:p]))

        trunOK = ""
        tmpLen = 0
        for i in range(len(All_num)):
            if All_num[i] == All_num[i][::-1]:
                if len(All_num[i]) > tmpLen:
                    tmpLen = len(All_num[i])
                    trunOK = All_num[i]
        
        print(f"最常迴文數字子數列為:{trunOK}")
