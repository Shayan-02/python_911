import sqlite3

connection = sqlite3.connect("./asghar.db")

cursor = connection.cursor()

sql = """ 
    CREATE TABLE IF NOT EXISTS user ( 
        userId INTEGER , 
        name VARCHAR (60), 
        family VARCHAR (60), 
        email VARCHAR (60) 
    ); 
"""

cursor.execute(sql)

connection.commit()


sql = """ 
    CREATE TABLE IF NOT EXISTS Product ( 
        productId INTEGER , 
        productName VARCHAR (60), 
        price INTEGER , 
        description VARCHAR (60) 
    ); 
"""

cursor.execute(sql)

connection.commit()

sql = """ 
    INSERT INTO Product VALUES (4,'Django course',5000,'this is django course using python language'); 
 
""" 
# sql = """ 
#     INSERT INTO Product VALUES (2,'kotlin course',3000,'this is kotlin course'); 
#     INSERT INTO Product VALUES (3,'vue course',4000,'this is vue course'); 

# """ 
 
cursor.execute(sql) 
 
cursor.executescript(sql) 
 
connection.commit() 
 
import sqlite3 
 
connection = sqlite3.connect("./asghar.db") 
 
cursor = connection.cursor() 
 
sql = """ 
    DELETE FROM Product WHERE productId = 3; 
""" 
 
cursor.execute(sql) 
 
connection.commit() 


connection.close()