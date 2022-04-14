import pymysql

#Connecting to mysql server from wampserver
conn = pymysql.connect(user='<username>',passwd='<password>',host='localhost',database='<database>')
cur = conn.cursor()

Choices = int(input("Enter 1 to Insert Data , 2 to update Data and 3 to delete Data: "))

#To Insert Data into Table
if Choices == 1:
    # Variables to store input from user
    user_id = int(input("Enter Student ID: "))
    user_name = input("Enter Student Name: ")
    user_sex = input("Enter Student Sex: ")
    user_roll_no = int(input("Enter Student Roll No: "))
    
    # SQL Table creation command
    STable = 'create table if not exists student (ID varchar(15) Not null, Name char(30), Sex char(15), Roll_No int);'
    cur.execute(STable)
    print("Table named Student created successfully.")

    # Python SQL execution command using cursor with keystring excecute()
    ValS = "insert into student (id,name,sex,roll_no) values ({},'{}','{}',{})".format(user_id,user_name,user_sex,user_roll_no)
    cur.execute(ValS)
    print("Student Info Saved to Database.")

#To Update Data from Table
if Choices == 2:
    select = input("Enter what do you want to update: ")
    if select == 'sex'or select =='gender':
        nameid = input("Enter the name of student you want to change: ")
        sex = input("Enter new data for Sex: ")
        UpdateSex = "update student set sex = %s where name = %s"
        data = (sex, nameid)
        cur.execute(UpdateSex,data)
        print("Gender Updated Successfully.")
    
    if select == 'roll_no' or select=='rollno' or select=='rollnumber':
        nameid = input("Enter the name of student you want to change: ")
        roll_no = input("Enter new data for Roll_no: ")
        UpdateRoll = "update student set roll_no = %s where name = %s"
        data = (roll_no,nameid)
        cur.execute(UpdateRoll, data)
        print("Roll No Updated Successfully.")

#To Delete Data from Table
if Choices == 3:
    nameid = input("Enter name of student you want to delete: ")
    Deletedata = 'delete from student where name = %s'
    cur.execute(Deletedata, nameid)
    print("Student Deleted Successfully.")

