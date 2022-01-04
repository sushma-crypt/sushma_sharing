import mysql.connector
from mysql.connector import connection
cnx = mysql.connector.connect(user = "root",
                               password = "Sushmaravi@682@#0",
                               host = "localhost",
                               database = 'sushmadb1')
cursor = cnx.cursor()
query = ("SELECT * FROM sushmadb1.student =") 
studentmail = 'kj@gmail.com'
cursor.execute(query, (studentmail))
result = cursor . fetchone()
print(result)




                             
                               

