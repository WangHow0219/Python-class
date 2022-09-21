inputCode = input("輸入密碼")

code = list(inputCode)
for u in range(0, 6):
    code[u] = int(code[u])

newCode = list()
for x in range(0,6):
    if code[x] <= 3:
        p = 7 * (code[x]) + (code[x])
        q = p // 4
        newCode.append(q)
    elif code[x] == 4:
        p = code[x]
        q = p // 4
        newCode.append(q)
    elif code[x] <= 8:
        p = 7 * (code[x]-4) + (code[x])
        q = p // 4
        newCode.append(q)

print(newCode)
newCode.clear()