import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "echamber"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO pharmaceuticals_name_list (name) SELECT DISTINCT pharmaceuticals  FROM ep_medicine_list")
mydb.commit()


