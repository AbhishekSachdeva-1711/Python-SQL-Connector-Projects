import mysql.connector

mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234"
            )
mycursor=mydb.cursor()
##mycursor.execute("drop database if exists collage")
mycursor.execute("CREATE DATABASE if not exists collage")
mycursor.execute("use collage")
mycursor.execute("CREATE TABLE if not exists record(rollno int AUTO_INCREMENT primary key, name varchar(20), course varchar(20), semester int, year int)")

def add():
##    rollno=1
##    year=23
##    rollnumber = f"{rollno:04n}"
##    rollnumber=str(year)+str(rollnumber)
##    rollnumber=int(rollnumber)
##    print(rollnumber)
    
    n=input("Enter your name: ")
    course="BCA (General)"
    semester="1"
    year=1
    
    mycursor=mydb.cursor()
    sql="INSERT INTO record(name,course,semester,year)value(%s,%s,%s,%s)"
    val=(n,course,semester,year)
    mycursor.execute(sql,val)
    mydb.commit()

def subject():
    s1=(1,"coa","ctps","os","oops","culture education","comm. skill")
    s2=(2,"dbms","python","evs","foc","culture education","pro. skill")
    s3=(3,"dsa","ctps","os","python","mathamatics","comm. skill")
    s4=(4,"AssertionError","dsa","os","java","mathamatics","comm. skill")
    s5=(5,"internet of things","Open elevtive-1",)
    s6=(6,"big data anyalytics","open elevtive-2")
    mycursor.execute("CREATE TABLE if not exists subject(semno int,s1 varchar(50),s2 varchar(50),s3 varchar(50),s4 varchar(50),s5 varchar(50),s6 varchar(50))")
    sql="insert into subject (semno,s1,s2)values(%s,%s,%s)"
    mycursor.execute(sql,s6)
    mydb.commit()
    
def marks():
    rollno=int(input("Enter your roll number: "))
    sem=int(input("Enter Semester:"))
    print("1.first in sem\n2.Second in sem\n3.End sem")
    typeofexam=int(input("Enter your choice: ")) 
    mycursor=mydb.cursor()
    sql="select * from subject where semno =%s"
    seme=(sem,)
    mycursor.execute(sql,seme)
    mr=mycursor.fetchall()
    print(mr)
    print(mr[0][1],end="")
    s1=int(input(" :"))
    print(mr[0][2],end="")
    s2=int(input(" :"))
    print(mr[0][3],end="")
    s3=int(input(" :"))
    print(mr[0][4],end="")
    s4=int(input(" :"))
    print(mr[0][5],end="")
    s5=int(input(" :"))
    print(mr[0][6],end="")
    s6=int(input(" :"))
    
    mycursor.execute("CREATE TABLE if not exists marks(rollno int,sem int ,typeofexam varchar(20),s1 int,s2 int,s3 int,s4 int,s5 int,s6 int)")
    sql="insert into marks (rollno,sem,typeofexam,s1,s2,s3,s4,s5,s6)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(rollno,sem,typeofexam,s1,s2,s3,s4,s5,s6)
    mycursor.execute(sql,val)
    mydb.commit()
def show():
    mycursor=mydb.cursor()
    mycursor.execute("select * from subject")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x[0],x[1],x[2],x[3],x[4],x[5],x[6])

def marksshow():    
    mycursor=mydb.cursor()
    mycursor.execute("select * from marks")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x[0],x[1],x[2],x[3],x[4],x[5],x[6])

def marksheet():
    z=int(input("Enter roll no. from the record: "))
    mycursor=mydb.cursor()
    sql="select * from record where rollno =%s"
    val=(z,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x[0],x[1],x[3])

def marksheet2():
    q=int(input("Enter roll no. for marks: "))
    mycursor=mydb.cursor()
    sql="select * from marks where rollno =%s"
    val=(q,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])




    
while True:
    print("***Collage Report***")
    print("1.Add student \n2.Enter the marks\n3.Show marks\n4.Show Subjects\n5.Show Marksheet1\n6.Show Marksheet2\n7.Exit")
    y=int(input("Enter your choice: "))
    if(y==1):
        add()
    elif(y==2):
        marks()
    elif(y==3):
        marksshow()
    elif(y==4):
        show()
    elif(y==5):
        marksheet()
    elif(y==6):
        marksheet2()
    elif(y==7):
        break
    

    
    





    
    
