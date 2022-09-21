from sqlite3 import Cursor
import pymysql
import json
#建立連線
conn = pymysql.connect(host='20.239.64.24',port=3306,user='test',passwd='test',db='test',charset='utf8')
# 建立游標
cursor = conn.cursor()

cursor.execute("INSERT INTO `student` (`id`, `name`) VALUES ('07', 'Thomas')")

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
for i in rows:
    print(i)
print("==================================================")

data=[]
for i in rows:
    data.append(i)
print(data)
print("==================================================")

# dic --> byte str
tmp=json.dumps(data, indent=4, ensure_ascii=False)
print(tmp)
 
conn.commit()
# 關閉游標
cursor.close()
# 關閉連線
conn.close()

'''
CREATE TABLE `ic`.`c110156246` ( `id` VARCHAR(10) NOT NULL , `name` VARCHAR(10) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;
INSERT INTO `c110156246` (`id`, `name`) VALUES ('001', 'How')
'''