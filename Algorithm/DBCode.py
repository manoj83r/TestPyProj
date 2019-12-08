import mysql.connector
mydb = mysql.connector.connect(host="gator4148.hostgator.com", user ="sparkdat_user", passwd ="sparkdatabox", database="sparkdat_labs")
mycursor = mydb.cursor()
mycursor.execute("select * from CustomerBase WHERE Cust_ID like 'CC199%'")
for i in mycursor:
    print(i)



