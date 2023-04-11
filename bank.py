import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="bank"
            )
##mycursor = mydb.cursor()
##mycursor.execute("drop database if exists bank")
##mycursor.execute("CREATE DATABASE if not exists bank")
##mycursor.execute("use bank")
##mycursor.execute("CREATE TABLE if not exists customers(accno int primary key,name varchar(210),balance int,acctype varchar(20))")
def add():
            a=input("Enter accno:")
            b=input("Enter name:")
            c=input("Enter balance:")
            d=input("Enter acctype:")

            mycursor=mydb.cursor()
            mycursor.execute("use bank")
            sql="INSERT INTO customers (accno,name,balance,acctype) VALUES(%s,%s,%s,%s)"
            val=(a,b,c,d)
            mycursor.execute(sql,val)
            mydb.commit()

def show():
            mycursor=mydb.cursor()
            mycursor.execute("select * from customers")
            myresult=mycursor.fetchall()
            for x in myresult:
                print(x[0],x[1],x[2],x[3])
def deposit():
            b=int(input("Enter your accno: "))
            k=-1
            mycursor=mydb.cursor()
            sql="select * from customers where accno =%s"
            val=(b,)
            mycursor.execute(sql,val)
            myresult=mycursor.fetchall()
            if myresult:
                a=int(input("Enter your balance you deposit: "))
                for x in myresult:
                    k=x[2]
                k=k+a
                print("total balance is :",k)
                sql="update customers set balance =%s where accno =%s"
                
                val=(k,b)
                mycursor.execute(sql,val)
                mydb.commit()
            else:
                print("***account not found***")
                
def gayab():
            d=int(input("Enter accno to delete: "))
            mycursor=mydb.cursor()
            sql=("delete from customers where accno=%s")
            val=(d,)
            mycursor.execute(sql,val)
            mydb.commit()
            print("***a/c Deleted***")
def withdraw():
            w=int(input("Enter your accno: "))
            k=-1
            mycursor=mydb.cursor()
            sql="select * from customers where accno =%s"
            val=(w,)
            mycursor.execute(sql,val)
            myresult=mycursor.fetchall()
            a=int(input("Enter your balance to withdraw: "))  
                
            for x in myresult:
                k=x[2]
            if k<a:
                print("***Not Enough Balance***")
            else:        
                k=k-a
                print("total balance is :",k)
                sql="update customers set balance =%s where accno =%s"    
                val=(k,w)
                mycursor.execute(sql,val)
                mydb.commit()
            



while True:
    
    print("1.Add\n2.Show\n3.Deposit\n4.Delete a/c\n5.Withdraw\n6.Exit")
    y=int(input("Enter your choice: "))
    if (y==1):
        add()
    elif(y==2):
        show()
    elif(y==3):
        deposit()
    elif(y==4):
        gayab()
    elif(y==5):
        withdraw()
    elif(y==6):
        break


    
