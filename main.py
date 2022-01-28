import mysql.connector

i = 1

def insert(brand_name, generic_name, form, strength, pharmaceutical):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="medicinedb"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO medicines (brand_name, generic_name, form, strength, pharmaceutical) VALUES (%s, %s, %s, %s, %s )"
    val = (brand_name, generic_name, form, strength, pharmaceutical)

    mycursor.execute(sql, val)

    mydb.commit()

    global i
    print(f"[{i}] {brand_name} = record inserted.")
    i += 1


def app():
    with open('medx.txt') as f:
        for line in f:
            l = line.split('|')
            insert(l[0].strip(),l[1].strip(),l[2].strip(),l[3].strip(),l[4].strip())

if __name__ == '__main__':
    app()