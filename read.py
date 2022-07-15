import pandas as pd
userdata = pd.read_csv('/Users/raneemal-mindeel/Desktop/Module8/Project2/users.csv', index_col=False, delimiter = ',')

import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='Famira44$')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE users")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host='localhost', database='users', user='root', password='Famira44$')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS users_data;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE users_data(name varchar(255),email varchar(255),dob date, country varchar(255),primary key(name))")
        print("Table is created....")
        #loop through the data frame
        for i,row in userdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO users.users_data VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)