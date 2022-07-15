import mysql.connector
import matplotlib.pyplot as plt
cnx = mysql.connector.connect(user='root',
password='Famira44$',
host='127.0.0.1',
database = 'masterData',
auth_plugin = 'mysql_native_password')

cursor = cnx.cursor()
sql= ("""
SELECT DATE_FORMAT(tDate,'%d-%m-%Y') AS 'Month' , total_Retail_and_food_services_sales AS sales 
FROM data
ORDER BY 'Month'
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