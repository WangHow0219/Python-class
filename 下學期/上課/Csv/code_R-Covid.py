class Covid19:
    def __init__(self,NotifDay,NIDN,HomeQuarant,EMI,Total):
        self.NotifDay = NotifDay
        self.NIDN = NIDN
        self.HomeQuarant = HomeQuarant
        self.EMI = EMI
        self.Total = Total

f = open('C:/ALL/NKUST/VS_Code/程式設計/下學期/上課/CSV/data_Covid.csv','r',encoding='utf-8')
data = f.readlines()

header = data[0]
data.pop(0)
group = []
for i in data:
    tmp = i.split('\n')[0].split(',')
    NotifDay = tmp[0]
    NIDN = float(tmp[1])
    HomeQuarant = float(tmp[2])
    EMI = float(tmp[3])
    Total = float(tmp[4])

    tmp2 = Covid19(NotifDay,NIDN,HomeQuarant,EMI,Total)
    group.append(tmp2)
f.close()
