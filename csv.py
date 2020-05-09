import scipy.io
import csv
import pymysql

# 21800370 seo jun pyo DB team project

conn = pymysql.connect(host='127.0.0.1', user='root', password='******',

                       db='test', charset='utf8')

curs = conn.cursor()

conn.commit()



f = open('insert.csv','r')

csvReader = csv.reader(f)



for row in csvReader:

    user_no = (row[0])

    user_pred = (row[1])



    print (user_pred)

    print (user_no)

    

    sql = """insert into mat (id, pred) values (%s, %s)"""

    curs.execute(sql, (user_no, user_pred))



#db의 변화 저장

conn.commit()

    

f.close()

conn.close()