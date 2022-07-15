import pandas as pd
userdata = pd.read_csv('/Users/raneemal-mindeel/Desktop/Module8/Project2/master_data.csv', index_col=False, delimiter = ',')

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
        cursor.execute("CREATE TABLE data(tDate date,total_Retail_and_food_services_sales INT,Retail_sales_and_food_services_excl_motor_vehicle_and_parts INT,Retail_sales_and_food_services_excl_gasoline_stations INT,Retail_sales_and_food_services_gasoline_stations INT,total_Retail_sales INT,total_Retail_sales_excl_motor_vehicle_and_parts_dealers INT,GAFO INT,Motor_vehicle_and_parts_dealers INT,Automobile_and_other_motor_vehicle_dealers INT,Automobile_dealers INT,New_car_dealers INT,Used_car_dealers INT,Automotive_parts_acc_and_tire_stores INT,Furniture_home_furn_electronics_and_appliance_stores INT,Furniture_and_home_furnishings_stores INT,Floor_covering_stores INT,All_other_home_furnishings_stores INT,Electronics_and_appliance_stores INT,Household_appliance_stores INT,Electronics_stores INT,Building_mat_and_garden_equip_and_supplies_dealers INT,Building_mat_and_supplies_dealers INT,Paint_and_wallpaper_stores INT,Hardware_stores INT,Food_and_beverage_stores INT,Grocery_stores INT,Supermarkets_and_other_grocery_except_convenience_stores INT,Beer_wine_and_liquor_stores INT,Health_and_personal_care_stores INT,Pharmacies_and_drug_stores INT,Gasoline_stations INT,Clothing_and_clothing_access_stores INT,Clothing_stores INT,Mens_clothing_stores INT,Womens_clothing_stores INT,Family_clothing_stores INT,Other_clothing_stores INT,Shoe_stores INT,Jewelry_stores INT,Sporting_goods_hobby_musical_instrument_and_book_stores INT,Sporting_goods_stores INT,Hobby_toy_and_game_stores INT,Book_stores INT,General_merchandise_stores INT,Department_stores INT,Department_stores_excl_discount_department_stores INT,Discount_dept_stores INT,Other_general_merchandise_stores INT,Warehouse_clubs_and_superstores INT,All_other_gen_merchandise_stores INT,Miscellaneous_store_retailers INT,Office_supplies_stationery_and_gift_stores INT,Office_supplies_and_stationery_stores INT,Gift_novelty_and_souvenir_stores INT,Used_merchandise_stores INT,Nonstore_retailers INT,Electronic_shopping_and_mail_order_houses INT,Fuel_dealers INT,Food_services_and_drinking_places INT,Drinking_places INT,Restaurants_and_other_eating_places INT,Full_service_restaurants INT,Limited_service_eating_places INT, primary key(tDate))")
        print("Table is created...")
        #loop through the data frame
        for i,row in userdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO masterData.data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print(row)
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)