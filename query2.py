import mysql.connector
import matplotlib.pyplot as plt
cnx = mysql.connector.connect(user='root',
password='Famira44$',
host='127.0.0.1',
database = 'masterData',
auth_plugin = 'mysql_native_password')

cursor = cnx.cursor()
sql= ("""
SELECT FLOOR(Year(tDate)/10)*10 AS 'Decade' , sum(total_Retail_sales) 'Total Retail Sales per Decade' 
FROM data 
GROUP BY decade
""")

cursor.execute(sql)
month = []
sales = []

#print all the rows
for row in cursor.fetchall():
    print(row)
    month.append(row[0])
    sales.append(row[1])
cursor.close()
cnx.close()

plt.plot(month,sales)
plt.show()