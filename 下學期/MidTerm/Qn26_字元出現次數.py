# Qn26_字元出現次數
while True:
    inp = input('檢測的字串(end 結束)')
    if inp == 'end':
        print('檢測結束')
        break

    else:
        text = input('搜尋目標字元')
        count = inp.count(text)

        print(f"字元'{text}'出現次數為:{count}")
