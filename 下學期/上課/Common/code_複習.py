print("hello world")

grade=45
grade=grade+10
print(grade)
if grade>=60:
    print("pass")
else:
    print("fail")

year=1997
month=3
day=28

years=year//1000+year%1000//100+year%100//10+year%10
days=day//10+day%10
months=month//10+month%10
sum=years+months+days
if sum>=10:
    sum=(sum//10+sum%10)
    if sum>=10:
        sum=(sum//10+sum%10)
        print(sum)
else:
    print(sum)

birthday='19971231'
for i in birthday:
    sum=sum+int(i)
if sum>=10:
    sum=sum//10+sum%10
    print(sum)
if sum>=10:
    sum=sum//10+sum%10
    print(sum)

sum=0
for i in list(range(1,11,1)):
    sum=sum+i
print(sum)
sum=0
for i in list(range(1,11,2)):
    sum=sum+i
sum2=0
for i in list(range(2,11,2)):
    sum2=sum2+i
print(sum-sum2)

sum=0
for i in list(range(1,11,1)):
    if i%2==1:
        sum=sum+i
    if i%2==0:
        sum=sum-i
print(sum)

sum=0
for i in list(range(1,11,1)):
    if i%4==0 or i%4==1:
        sum=sum+i
    if i%4==2 or i%4==3:
        sum=sum-i
print(sum)

sum=0
for i in range(1,11,1):
    if i%2==0:
        sum=sum-1/i
    else:
        sum=sum+1/i
print(sum)