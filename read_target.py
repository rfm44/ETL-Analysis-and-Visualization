import pandas as pd
userdata = pd.read_csv('/Users/raneemal-mindeel/Desktop/Module8/Project2/target_data.csv',encoding='Windows-1252',index_col=False, delimiter = ',')
userdata.head()
import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='Famira44$')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE masterData")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host='localhost', database='masterData', user='root', password='Famira44$')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS data;')
        print('Creating table....')
# the following is the table creation statment 
        cursor.execute("CREATE TABLE data(tDate date,total_Retail_and_food_services_sales INT,total_Retail_sales INT,Pharmacies_and_drug_stores INT,Gasoline_stations INT,Clothing_stores INT,Men_clothing_stores varchar(255),Women_clothing_stores INT,Family_clothing_stores INT,Shoe_stores INT,Jewelry_stores INT,Sporting_goods_hobby_musical_instrument_and_book_stores INT,Sporting_goods_stores INT,Hobby_toy_and_game_stores INT, Book_stores INT,primary key(tDate))")
        print("Table is created...")
        #loop through the data frame
        for i,row in userdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO masterData.data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print(row)
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
