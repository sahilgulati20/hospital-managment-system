from sys import exit
import mysql.connector as sql

conn=sql.connect (host='localhost', user='root', passwd='Sahil@2085', database='project')
if conn.is_connected():
    #print('successfully connected')
    cl=conn.cursor()
print("-------------------------------------------------------------")
print("           !......WELCOME TO OUR HOSPITAL......!          ")
print("-------------------------------------------------------------")
print("1.  LOGIN")
print("2. EXIT")
choice=int(input("Enter Your Choice:"))
if choice==1:
    u1=input("Enter user name:")
    pwd1=input("Enter The Password:")
    while u1=='sahil'and pwd1=='sahil2085':
        #print('connected....!')

        print('-----------------------------------------')
        print("!........WELCOME TO HOSPITAL.......!")
        print('-----------------------------------------')
        #print("successfully connected")
        print(' ')
        print("1.  Registering Patient details")
        print("2.  Registering Doctor details")
        print("3.  Registering worker details")
        print("4.  Total patient details")
        print("5.  Total doctor details")
        print("6.  Total worker details")
        print("7.   Patient detail")
        print("8.   Doctor detail")
        print("9.   Worker detail")
        print("10.  Delete any patient detail")
        print("11.  Delete any doctor detail")
        print("12.  Delete any worker detail")
        print("13.  Exit")
        print(' ')
        choice=int(input('Enter your choice:'))
        if choice==1:
            p_name=input("Enter Patient Name:")
            p_age=int(input("Enter Age:"))
            p_problems=input("Enter the Problem/Disease:")
            p_phono=int(input("Enter Phone number:"))
            sql_insert="insert into patient_details values (""'"+p_name+"', "+str(p_age)+", '"+p_problems+"',"+str(p_phono)+")"
            cl.execute(sql_insert)
            print('-----------------------------------------')
            print('        Successfully Registered...!       ')
            print('-----------------------------------------')
            conn.commit()

        elif choice==2:
            d_name=input("Enter Doctor Name:")
            d_age=int(input("Enter Age:"))
            d_department=input("Enter the Department:")
            d_phono=int(input("Enter Phone number:"))
            sql_insert="insert into doctor_details values (""'"+d_name+"', "+str(d_age)+", '"+d_department+"', "+str(d_phono)+")"
            cl.execute(sql_insert)
            print('-----------------------------------------')
            print('        Successfully Registered...!       ')
            print('-----------------------------------------')
            conn.commit()

        elif choice==3:
            w_name=input("Enter Worker Name:")
            w_age=int(input("Enter Age:"))
            w_workname=input('Enter type of work:')
            w_phono=int (input('Enter Phone number:'))
            sql_insert="insert into worker_details values(""'"+w_name+"',"+str(w_age)+",'"+w_workname+"',"+str(w_phono)+")"
            cl.execute(sql_insert)
            print('-----------------------------------------')
            print('        Successfully Registered...!       ')
            print('-----------------------------------------')
            conn.commit()

        elif choice==4:
            sql_w="select * from patient_details"
            cl.execute(sql_w)
            r = cl.fetchall()
            for i in r:
                print (i)

        elif choice==5:
            sql_x="select * from doctor_details"
            cl.execute(sql_x)
            s=cl.fetchall()
            for i in s:
                print(i)

        elif choice==6:
            sql_y="select * from worker_details"
            cl.execute(sql_y)
            t=cl.fetchall()
            for i in t:
                print(i)

        elif choice==7:
            h=input("Enter the name:")
            sql_w='select * from patient_details where name="{}"'.format(h)
            cl.execute(sql_w)
            u = cl.fetchall()
            for i in u:
                print(i)

        elif choice==8:
            d=input("Enter the name:")
            sql_d='select * from doctor_details where d_name="{}"'.format(d)
            cl.execute(sql_d)
            v=cl.fetchall()
            for i in v:
                print (i)


        elif choice==9:
            f=input("Enter the name:")
            sql_f='select * from worker_details where w_name="{}"'.format(f)
            cl.execute(sql_f)
            w=cl.fetchall()
            for i in w:
                print(i)

        elif choice==10:
            k=input("Enter the name:")
            sql_w='delete from patient_details where name="{}"'.format(k)
            cl.execute(sql_w)
            r = cl.fetchall()
            print('--------------------------------------')
            print('          deleted sucessfully...!        ')
            print('--------------------------------------')
            conn.commit()

        elif choice==11:
            c=input("Enter the name:")
            sql_w='delete from doctor_details where d_name="{}"'.format(c)
            cl.execute(sql_w)
            r = cl.fetchall()
            print('---------------------------------------')
            print('          Sucessfully deleted....!        ')
            print('---------------------------------------')
            conn.commit()

        elif choice==12:
            m=input("Enter the name:")
            sql_w='delete from worker_details where w_name="{}"'.format(m)
            cl.execute(sql_w)
            r = cl.fetchall()
            print('---------------------------------------')
            print('          Sucessfully deleted....!        ')
            print('---------------------------------------')
            conn.commit()

        elif choice==13:
            print('----------------------------------------------')
            print('      !.....THANKS FOR VISITING.....!      ')
            print('----------------------------------------------')
            exit()
            break
        else:
            print('wrong username and password')

if choice==2:
    print('----------------------------------------------')
    print('      !.....THANKS FOR VISITING.....!      ')
    print('----------------------------------------------')
    exit()
