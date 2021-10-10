import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='tanmay',database='hostel_management')
conn.autocommit=True
if conn.is_connected():
    print('connected succesfully')
else:
    print('not connected')

c1=conn.cursor()
#c1.execute("create table fees(department int primary key,fees int)")
v_department=input("enter your department")
v_fees=input("enter your fee")
abc=("insert into fees values ('"+v_department+"',"+v_fees+")")
print(abc)
c1.execute(abc)
conn.commit()
#c1.execute("create table hostel_management(roll_no int primary key,name varchar(20),address varchar(100),room_no int,dept varchar(15),fees int,bal int)")

print("                                   WELCOME TO  HOSTEL MANAGEMENT                                   ")

print("     1.ADMISSION FORM")

print("     2.FEE CHECKING")

print("     3.MODIFY DATA")

print("     4.AUTHORITIES ONLY")

print("     5.QUIT")
choice=int(input('ENTER YOUR CHOICE'))
if choice==1:
    v_roll=input("ENTER YOUR ROLL NUMBER")
    v_name=input("ENTER YOUR NAME")                    
    v_add=input("ENTER YOUR ADDRESS")
    v_room_no=input("ENTER YOUR ROOM NUMBER")
    v_dept=input("ENTER YOUR DEPARTMENT")
    v_fees=input("ENTER YOUR FEES")
    v_bal=input("ENTER YOUR BALANCE")
    
    abc=("insert into hostel_management values ("+v_roll+",'"+v_name+"','"+v_add+"',"+v_room_no+",'"+v_dept+"',"+v_fees+","+v_bal+")")
    print(abc)
    c1.execute(abc)
    conn.commit()
elif choice==3:
    roll_no=int(input("enter your roll number"))
    mysql="select*from hostel_management where roll_no={}".format(roll_no)
    c1.execute(mysql)
    data=c1.fetchall()
    print("roll_no:",data[0][0])
    print("name:",data[0][1])
    print("address:",data[0][2])           
    print("room_no:",data[0][3])
    print("dept:",data[0][4])
    print("fees:",data[0][5])           
    print("bal:",data[0][6])
elif choice==2:
    print("AVAILABLE DEPARTMENTS AS FOLLOWS")
    print("1.COMPUTER")
    print("2.BIO")
    print("3.TECH")
    print("4.PHYSICS")
    print("5.ECO")
    print("6.ENG")
    department=input("ENTER YOUR DEPARTMENT")
    mysql="select*from fees where department='{}'".format(department)
    c1.execute(mysql)
    data=c1.fetchall()
    print("your fees is:",data[0][1])

elif choice==4:
    print( "SORRY,YOU ARE NOT AUTHORIZED TO USE THIS SITE  ")                       

else:
     print("QUITTING!!!!!!!!!")
