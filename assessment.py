import mysql.connector as mc

db = mc.connect(host = "localhost",user= "root",password ="",database= "customers_db")
cursor = db.cursor()

my_file = open(r"C:\Users\ravi\Desktop\test.txt", "r", encoding="utf-8")
content = my_file.read()

content_list = content.split("\n")
my_file.close()


for i in range(len(content_list)):
    content_list[i]=content_list[i].split("|")
    while("" in content_list[i]):
        content_list[i].remove("")
for k in content_list:
    print(k)
    query = "INSERT INTO customer_details (Customer_Name, Customer_ID, Customer_Open_Date, Last_Consulted_Date, Vaccination_Type,Doctor_Consulted,State,Country,Date_of_Birth,Active_Customer)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    value = (k[1],int(k[2]),k[3],k[4],k[5],k[6],k[7],k[8],k[9],k[10])
    cursor.execute(query, value)
    db.commit()
     