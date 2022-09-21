#取最大最小
grade=[28,98,65,74,32,56]
sum=0
for i in range(len(grade)):
    sum=sum+grade[i]
print(sum/len(grade))

grade.sort()
print(grade[5])

max=0
min=100
for i in range(grade[i]):
    if grade[i]>max:
        max=grade[i]
    if min<grade[i]:
        min=grade[i]
print(max)
print(min)
