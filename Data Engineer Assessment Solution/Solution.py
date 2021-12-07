##########################################
# Author : Goutam Awadiya                #
# Date   : 2021-12-06                    #
# Email  : goutam.awadhiya@gmail.com     #
##########################################

#Libraries
import sqlite3

#function to read the users.txt.
def userData(file_name):
    with open(file_name) as file:
        user_data = file.read()
        user_data = user_data.splitlines()
        return user_data

#taking out useful attributes and data row from data.
def dataModification(user_data):
    user_data = [tuple(x.split("|")[2:]) for x in user_data]
    return user_data[1:]

#get all existing tables names
def getAllTablesNames(cursor):
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = tables.fetchall()
    return tables

#creating master table to store all the users.
def createMasterTable(cursor):
    #check if table already exists
    table_found = False
    tables = getAllTablesNames(cursor)
    for table in tables:
        if table[0]=='AllUsers':
            table_found = True
        
    #create if table does not exists
    if table_found == False:
        all_user_query = cursor.execute('''create table AllUsers (
                                        Customer_Name VARCHAR(255) NOT NULL PRIMARY KEY,
                                        Customer_Id VARCHAR(18) NOT NULL,
                                        Open_Date DATE NOT NULL,
                                        Last_Consulted_Date DATE,
                                        Vaccination_Id CHAR(5),
                                        Dr_Name VARCHAR(255),
                                        State CHAR(5),
                                        Country CHAR(5),
                                        DOB DATE,
                                        Is_Active CHAR(1))''')

#inserting data from file to master table  
def insertDataIntoAllUsers(database,cursor,user_data):
    cursor.executemany("insert into AllUsers values (?,?,?,?,?,?,?,?,?,?)",user_data)
    database.commit()
    cursor.execute("select * from AllUsers")
    #print(cursor.fetchall())

#checking and creating country table if does not exist
def createCountryTableIfNot(user_country):
    table_name = 'Table_'+user_country
    #check if table exists 
    table_found = False
    tables = getAllTablesNames(cursor)
    for table in tables:
        if table[0]==table_name:
            table_found = True
        
    #create if table does not exists
    if table_found == False:
        all_user_query = cursor.execute('''create table '%s'(
                                        Customer_Name VARCHAR(255) NOT NULL PRIMARY KEY,
                                        Customer_Id VARCHAR(18) NOT NULL,
                                        Open_Date DATE NOT NULL,
                                        Last_Consulted_Date DATE,
                                        Vaccination_Id CHAR(5),
                                        Dr_Name VARCHAR(255),
                                        State CHAR(5),
                                        Country CHAR(5),
                                        DOB DATE,
                                        Is_Active CHAR(1))'''%table_name)

#insert user to their country table
def insertUserToCountryTable(database,cursor,user):
    user_country = user[7]
    createCountryTableIfNot(user_country)
    #insert data into country Table
    country_name = 'table_'+user_country
    cursor.execute("insert into '%s' values(?,?,?,?,?,?,?,?,?,?)"%country_name,user)
    database.commit()
    

#create country table
def createCountryTables(database,cursor):
    cursor.execute("select * from AllUsers")
    all_users = cursor.fetchall()
    for user in all_users:
        insertUserToCountryTable(database,cursor,user)
        
#drop all the tables if needed
def dropAllTables(tables):
    for table in tables:
        cursor.execute("drop table '%s'"%table)
    
#display all the tables and it's data
def showAllTables(tables):
     for table in tables:
        cursor.execute("select * from '%s'"%table)
        table_data = cursor.fetchall()
        print("-------------------------------------------------------- Table : {0} -------------------------------------------------------".format(table[0]))
        header = ['Customer_Name','Customer_Id','Open_Date','Last_Consulted_Date','Vaccination_Id','Dr_Name','State','Country','DOB','Is_Active']
        print("{:^16}{:^14}{:^13}{:^22}{:^18}{:^10}{:^8}{:^8}{:^10}{:^12}".format('Customer_Name','Customer_Id','Open_Date','Last_Consulted_Date','Vaccination_Id','Dr_Name','State','Country','DOB','Is_Active'))
        for data in table_data:
            Customer_Name,Customer_Id,Open_Date,Last_Consulted_Date,Vaccination_Id,Dr_Name,State,Country, DOB,Is_Active = data
            print("{:^16}{:^14}{:^13}{:^22}{:^18}{:^10}{:^8}{:^8}{:^10}{:^12}".format(Customer_Name,Customer_Id,Open_Date,Last_Consulted_Date,Vaccination_Id,Dr_Name,State,Country,DOB,Is_Active))
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
    
#start here
if __name__ == '__main__':
    
    file_name = 'users.txt'
    user_data = userData(file_name)
    user_data = dataModification(user_data)
    
    #connect database
    database = sqlite3.connect('UserDatabase.db')
    cursor = database.cursor()

    #delete all existing data
    tables = getAllTablesNames(cursor)
    dropAllTables(tables)

    #create master table 'AllUsers' for all the users if doesn't exists already
    createMasterTable(cursor)

    #insert data into master table - AllUsers
    insertDataIntoAllUsers(database,cursor,user_data)

    #Divide data into different tables according to country
    createCountryTables(database,cursor)
    
    #show data across all tables
    tables = getAllTablesNames(cursor)
    showAllTables(tables)

    input("\npress enter to exit...")
