import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="gurunath#2002", database="aems")

def Add_Employ():
    Id = input("Enter Employee Id : ")

    if check_employee(Id):
        print("Employee already exists\nTry Again\n")
        menu()

    else:
        Name = input("Enter Employee Name: ")
        address = input("Enter the Address: ")
        Post = input("Enter Employee Post: ")
        Salary = int(input("Enter Employee Salary: "))
        phone_no = input("Enter phone number: ")
        lifein = "N"
        heains = "N"
        SaDe = int(input("Enter Intial Salary Deduction: ")) 
        workstatus = input("Enter Workstatus: ")
        Attendance = "Not Given Yet"
        Reason_Life_Insurance = "Not Given Yet"
        Reason_Health_Insurance = "Not Given Yet"
        data = (Id, Name, address, Post, Salary, phone_no, lifein, heains, SaDe,
                workstatus, Attendance, Reason_Life_Insurance, Reason_Health_Insurance)

        sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Employee Added Successfully ")
        menu()


def Promote_Employ():
    Id = int(input("Enter Employee Id:"))

    if not check_employee(Id):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter Increase in Salary:"))

        sql = 'select salary from empdata where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        r = c.fetchone()
        t = r[0] + Amount

        sql = 'update empdata set salary=%s where id=%s'
        d = (t, Id)

        c.execute(sql, d)

        con.commit()
        print("Employee Promoted Successfully!!!")
        menu()


def Update_Employ():
    print("-->> Update Employee Record <<--\n")
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee Record Not exists\nTry Again")
        menu()
    else:   
        phone_no = int(input("Enter Employee Phone No.: "))
        if len(str(phone_no)) > 9 and len(str(phone_no)) < 9:
            print("Invalid Phone Number")
        else:
            print("Valid Phone Number")
            Address = input("Enter Employee Address: ")
            workstatus = input("Enter Workstatus: ")
            Attendance = input("Enter Attendance: ")
            phone_no = int(input("Enter New Phone Number: "))
            sql = 'UPDATE empdata set phone_no = %s, Address = %s, workstatus = %s, Attendance = %s where Id = %s'
            data = (phone_no, Address, workstatus, Attedance, Id)
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            print("Updated Employee Record SuccessFully!!!")
            menu()


def SaDe_Employ():
    Id = int(input("Enter Employee Id:"))

    if not check_employee(Id):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter Decrease in Salary:"))

        sql = 'select salary from empdata where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        r = c.fetchone()
        t = r[0] - Amount

        sql = 'update empdata set SaDe=%s where id=%s'
        d = (t, Id)

        c.execute(sql, d)

        con.commit()
        print("Salary Deducted Successfully")
        menu()


def Remove_Employ():
    Id = input("Enter Employee Id : ")

    if not check_employee(Id):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:

        sql = 'delete from empdata where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        con.commit()
        print("Employee Removed Successfully!!!")
        menu()


def check_employee(employee_id):
    sql = 'select * from empdata where id=%s'

    c = con.cursor(buffered=True)
    data = (employee_id,)

    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def lifein_Employ():
    print("-->> Life Insurance Employee Record <<--\n")
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee Record Not exists\nTry Again")
        menu()

    lifein = input("Enter Y or N to enter the value of Life Insurance: ")
    if lifein == "Y":
        print("Okay,Give Reason For Life insurance")
        Reason_Life_Insurance = input("Enter the Reason: ")
        sql = 'UPDATE empdata set lifein = %s, Reason_Life_Insurance = %s where Id = %s'
        data = (lifein, Reason_Life_Insurance, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Life Insurance Employee Record SuccessFully!!!")
        menu()
    elif lifein == "N":
        print("Okay,Give Reason For Not Giving Life insurance")
        Reason_Life_Insurance = input("Enter the Reason: ")
        sql = 'UPDATE empdata set lifein = %s, Reason_Life_Insurance = %s where Id = %s'
        data = (lifein, Reason_Life_Insurance, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Life Insurance Not Given!!!")
        menu()
    else:
        exit(0)


def heains_Employ():
    print("-->> Health Insurance Employee Record <<--\n")
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee Record Not exists\nTry Again")
        menu()

    heains = input("Enter Y or N to enter the value of Health Insurance: ")
    if heains == "Y":
        print("Okay,Give Reason For Health insurance")
        Reason_Health_Insurance = input("Enter the Reason: ")
        sql = 'UPDATE empdata set heains = %s,Reason_Health_Insurance = %s where Id = %s'
        data = (heains, Reason_Health_Insurance, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Updated Health Insurance Employee Record SuccessFully!!!")
        menu()
    elif heains == "N":
        print("Okay,Give Reason For Not Giving Health insurance")
        Reason_Health_Insurance = input("Enter the Reason: ")
        sql = 'UPDATE empdata set heains = %s, Reason_Health_Insurance = %s where Id = %s'
        data = (heains, Reason_Health_Insurance, Id)
        c = con.cursor()
        c.execute(sql, data)
        con.commit()
        print("Health Insurance Not Given!!!")
        menu()
    else:
        exit(0)

def Display_Employ():
    sql = 'select * from empdata'
    c = con.cursor()

    c.execute(sql)

    r = c.fetchall()
    ans = int(input("What is the Password:"))
    if ans == 4567:
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Address: ", i[2])
            print("Employee Post: ", i[3])
            print("Employee Salary: ", i[4])
            print("Employee phone_no: ", i[5])
            print("Employee Life Insurance: ", i[6])
            print("Employee Health Insurance: ", i[7])
            print("Employee Salary Deduction: ", i[8])
            print("Employee Workstatus: ", i[9])
            print("Employee Attendance: ", i[10])
            print("Employee REASON FOR LIFE INSURANCE: ", i[11])
            print("Employee REASON FOR HEALTH INSURANCE: ", i[12])
            print("*****************************")
    else:
        print("Not Displayed Successully!!!")
        menu()

def Search_Employ():
    print("-->> Search Employee Record <<--\n")

    Id = input("Enter Employee Id: ")

    if not check_employee(Id):
        print("Employee Record Not exists\nTry Again")
    else:

        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Address: ", i[2])
            print("Employee Post: ", i[3])
            print("Employee Salary: ", i[4])
            print("Employee phone_no: ", i[5])
            print("Employee Life Insurance: ", i[6])
            print("Employee Health Insurance: ", i[7])
            print("Employee Salary Deduction: ", i[8])
            print("Employee Workstatus: ", i[9])
            print("Employee Attendance: ", i[10])
            print("Employee REASON_LIFE_INSURANCE: ", i[11])
            print("Employee REASON_HEALTH_INSURANCE: ", i[12])
            print("*****************************")
        menu()

def menu():
    login_name = input("Enter the Login Name: ")
    password = int(input("Enter the Password: "))

    if login_name == "IDLD" and password == 48850:
        print("--->>Employee Management Record<<---")
        print("1.-For Add Employee")
        print("2.-For Promote Employee ")
        print("3.-For Update Employee")
        print("4.-For Salary Deduction")
        print("5.-For Remove Employee")
        print("6.-For Life Insurance")
        print("7.-For Health Insurance")
        print("8.-For Display Employee")
        print("9.-For Search Employee")
        print("10.to Exit")
        ch = int(input("Enter your Choice:"))
        if ch == 1:
            Add_Employ()
        elif ch == 2:
            Promote_Employ()
        elif ch == 3:
            Update_Employ()
        elif ch == 4:
            SaDe_Employ()
        elif ch == 5:
            Remove_Employ()
        elif ch == 6:
            lifein_Employ()
        elif ch == 7:
            heains_Employ()
        elif ch == 8:
            Display_Employ()    
        elif ch == 9:
            Search_Employ()
        elif ch == 10:
            exit(0)
    else:
        print("Invalid Login_name/Password!!! Access Denied")
        menu()    

menu()
