import csv 
#open file 
with open ('master_data.csv') as csv_file: 
    #read csv file 
    csv_reader = csv.reader(csv_file, delimiter=',')
    # loop through data 
    for row in csv_reader: 
        print(row)
