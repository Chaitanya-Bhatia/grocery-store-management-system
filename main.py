# modules

import mysql.connector as mysql
from tabulate import tabulate
import datetime
import json

# mysql connectivity

db = mysql.connect(host="localhost", user="", password="")
mycursor = db.cursor(buffered=True)
db.autocommit = True

mycursor.execute('CREATE DATABASE IF NOT EXISTS gsms')
mycursor.execute('USE gsms')


mycursor.execute('''CREATE TABLE IF NOT EXISTS product_table (
  product_id int NOT NULL AUTO_INCREMENT,
  product_name varchar(100) Default NULL,
  price float default NULL,
  quantity int default NULL,
  PRIMARY KEY (product_id)
)  AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 ''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS customer_table (
  customer_id int NOT NULL AUTO_INCREMENT,
  customer_name varchar(100) Default NULL,
  phone varchar(100) DEFAULT NULL,
  PRIMARY KEY (customer_id)
)  AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 ''')

# start of program

print('''\033[01m
 ╒────────────────────────────────────────────╕
 │ Welcome To Grocery Store Management System │
─────────────────────────────────────────────────
\033[0m''')

print('\033[01mImportant Points :- \033[0m')
print(
    '  1. Anywhere in the program,\033[01menter 0 to EXIT\033[0m the program')
print('  2. Change Username and Password directly in the code in login() function\n')
# Utility Functions


def exit_program(substitute):
    if substitute == '0':
        print('\n\nExiting Program.....\n')
        exit()
    elif substitute == 0:
        print('\n\nExiting Program.....\n')
        exit()


def clean_screen():
    print('\n'*100)

# login


def login():
    a = 0
    while 1:
        print('\033[01mLogin Screen\033[0m')
        print('─'*50)
        print("Enter your Login Credentials")
        username = str(input("Username : "))
        exit_program(username)
        password = str(input("Password : "))
        exit_program(password)
        if username == 'admin':  # change username in the aperenthesis('')
            if password == 'admin':  # change password in the aperenthesis('')
                print("\nLogin Successful")
                main_menu()
            else:
                a = a+1
                print("\nIncorrect password !\nTry Again\n")
        else:
            a = a+1
            print("\nLogin details not recognised\nTry Again\n")
        if a == 3:
            print("\n\nToo many wrong attempts.....\nExiting Program.....\n")
            exit()

# product management code


def check_product(product_name):

    sql = 'select * from product_table where product_name=%s'
    data = (product_name,)
    mycursor.execute(sql, data)
    r = mycursor.rowcount
    if r == 1:
        return True
    else:
        return False


def add_product():

    try:
        clean_screen()
        print('\033[01mADD PRODUCT SCREEN\033[0m')
        print('─'*50)
        print("Enter Product Details")
        product_name = input('Enter Product Name :')
        exit_program(product_name)

        if check_product(product_name) == True:
            print('\n\nProduct already Exist.....\nPress any key to continue....')

        else:
            product_price = int(input('Enter Product Price :'))
            exit_program(product_price)
            product_quantity = int(input('Enter Product Quantity :'))
            exit_program(product_quantity)
            data = (product_name, product_price, product_quantity)

            sql = 'insert into product_table(product_name,price,quantity) values(%s,%s,%s)'
            mycursor.execute(sql, data)

            print(
                '\n\nNew Product added successfully.....\nPress any key to continue....')
        wait = input()

    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        add_product()


def modify_product():

    try:
        clean_screen()
        print('\033[01mMODIFY PRODUCT DETAILS SCREEN\033[0m')
        print('─'*50)

        product_id = int(input('Enter Product Id :'))
        exit_program(product_id)
        if find_product(product_id) == None:
            print('\n\nProduct not found.....\nPress any key to try again....')
            wait = input()
            modify_product()
        while 1:
            product_name = find_product(product_id)[1]
            print("\n\033[01m"+"Change Product " +
                  product_name+" Details"+"\033[0m")
            print('1 => Change Product Name')
            print('2 => Change Product Price')
            print('3 => Add Product Quantity')
            print('4 => Main Menu')
            print('0 => Exit\n')
            choice = int(input('Enter your choice :'))
            if choice == 0:
                exit_program(choice)
            elif choice == 1:
                product_name = input('Enter New Product Name :')
                exit_program(product_name)
                data = (product_name, product_id)
                sql = 'update product_table set product_name=%s where product_id=%s'
                mycursor.execute(sql, data)
                print(
                    '\n\nProduct Name Changed Successfully.....\nPress any key to continue....')
                wait = input()

            elif choice == 2:
                new_product_price = int(input('Enter New Product Price :'))
                exit_program(new_product_price)
                data = (new_product_price, product_name)
                sql = 'update product_table set price=%s where product_id=%s'
                mycursor.execute(sql, data)
                print(
                    '\nProduct Price Updated Successfully.....\nPress any key to continue....')
                wait = input()

            elif choice == 3:

                add_quantity = int(input('Enter Quantity to Add :'))
                exit_program(add_quantity)
                data = (add_quantity, product_id)
                sql = 'update product_table set quantity=quantity+%s where product_id=%s'
                mycursor.execute(sql, data)

                print(
                    '\n\nProduct Quantity Added Successfully........\nPress any key to continue....')
                wait = input()

            elif choice == 4:
                main_menu()
            else:
                print('\n\nInvalid Choice.....\nTry Again....\n')

    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        modify_product()


def view_product():

    clean_screen()
    mycursor.execute('select * from product_table')
    records = mycursor.fetchall()
    print("\033[01mProduct Table\033[0m")
    print('─'*50)
    print(tabulate(records, headers=[
          '\033[93mId\033[0m', '\033[93mName\033[0m', '\033[93mPrice\033[0m', '\033[93mQuantity\033[0m'], tablefmt="fancy_grid"))
    print('\nPress any key to continue.....')
    wait = input()


def find_product(product_id):
    sql = 'select * from product_table where product_id=%s'
    data = (product_id,)
    mycursor.execute(sql, data)
    r = mycursor.fetchone()
    return r


def get_price(product_id):

    sql = 'select price from product_table where product_id=%s'
    data = (product_id,)
    mycursor.execute(sql, data)
    r = mycursor.fetchone()
    return r[0]


def reduce_quantity(product_id, quantity):
    mycursor.execute(
        'select quantity from product_table where product_id=%s', (product_id,))

    r = mycursor.fetchone()

    q = r[0]
    if q >= quantity:
        q = q - quantity
        sql = 'update product_table set quantity=%s where product_id=%s'
        data = (q, product_id)
        mycursor.execute(sql, data)

    else:
        print('\n\nProduct Quantity is not sufficient\nPress any key to try again....')
        wait = input()
        search_customer()


# customer management code


def check_customer(customer_name):

    sql = 'select * from customer_table where customer_name=%s'
    data = (customer_name,)
    mycursor.execute(sql, data)
    r = mycursor.rowcount
    if r == 1:
        return True
    else:
        return False


def add_customer():

    try:
        clean_screen()
        print('\033[01mAdd Customer Screen\033[0m')
        print('─'*50)
        customer_name = input('Enter Customer Name :')
        exit_program(customer_name)
        if check_customer(customer_name) == True:
            print('\n\nCustomer already Exist.....\nPress any key to continue....')

        else:
            phone = input('Enter Customer Phone :')
            exit_program(phone)
            data = (customer_name, phone)
            sql = 'insert into customer_table(customer_name,phone) values(%s,%s)'
            mycursor.execute(sql, data)
            mycursor.execute('Create table if not exists '+customer_name+''' (
                      invoice_id int NOT NULL AUTO_INCREMENT,
                      dte DATE ,
                      products varchar(255) Default NULL,
    
                      total_amount float ,
                      PRIMARY KEY (invoice_id)
                    )  AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 ''')

            print(
                '\n\nNew Customer added successfully.....\nPress any key to continue....')

        wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        add_customer()


def modify_customer():

    try:
        clean_screen()
        print('\033[01mMODIFY CUSTOMER DETAILS SCREEN\033[0m')
        print('─'*50)
        customer_name = input("Enter Customer Name : ")
        exit_program(customer_name)
        if(check_customer(customer_name) == False):
            print("\n\nCustomer does not  exists......\nPress any key to continue....")
        else:
            phone = input("Enter Updated Customer Phone No. : ")
            exit_program(phone)
            data = (phone,)

            sql = 'update customer_table set phone=%s where customer_name=%s'
            data = (phone, customer_name)
            mycursor.execute(sql, data)

        print('\n\nCustomer Details Updated Successfully.............\nPress any key to continue....')
        wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        modify_customer()


def view_customer():

    clean_screen()
    print("\033[01mCUSTOMERS LIST\033[0m")
    print('─'*50)
    mycursor.execute('select * from customer_table')
    records = mycursor.fetchall()
    print(tabulate(records, headers=[
          '\033[93mS.No.\033[0m', '\033[93mName\033[0m', '\033[93mPhone\033[0m'], tablefmt="fancy_grid"))
    print('\nPress any key to continue.....')
    wait = input()


def view_customer_invoice(customer_name):

    clean_screen()
    print("\033[01m" + "CUSTOMER "+customer_name+"'s RECORDS"+"\033[0m")
    print('─'*50)

    mycursor.execute('select * from '+customer_name+'')
    records = mycursor.fetchall()
    print(tabulate(records, headers=[
          '\033[93mId\033[0m', '\033[93mDate\033[0m', '\033[93mProducts\033[0m', '\033[93mTotal Amount\033[0m'], tablefmt="fancy_grid"))
    print('\nPress any key to continue.....')
    wait = input()


def create_invoice():

    try:
        clean_screen()
        print('\033[01mCREATE INVOICE SCREEN\033[0m')
        print('─'*50)
        x = datetime.datetime.now()

        dte = x.strftime("%Y-%m-%d")
        customer_name = input('Enter Customer Name :')
        exit_program(customer_name)

        if check_customer(customer_name) == True:
            product_dict = {}
            total_amount = 0
            while 1:
                try:
                    product_id = int(input('Enter Product ID :'))
                    exit_program(product_id)
                    quantity = int(input('Enter Product Quantity :'))
                    exit_program(quantity)

                    mycursor.execute(
                        'select quantity from product_table where product_id=%s', (product_id,))
                    r = mycursor.fetchone()
                    q = r[0]
                    if q < quantity:
                        print(
                            '\n\nProduct Quantity is not sufficient\nPress any key to try again....')
                        wait = input()
                        continue

                    print('\n\nEnter 1 to continue or 2 to add invoice .....')
                    choice = int(input())
                    if choice == 0:
                        exit_program(choice)
                    elif choice == 1:
                        pass
                    elif choice == 2:
                        price = get_price(product_id)
                        reduce_quantity(product_id, quantity)
                        amount = price*quantity
                        total_amount = total_amount+amount
                        product_name = find_product(product_id)[1]
                        product_dict[product_name] = {}
                        product_dict[product_name]['Price'] = price
                        product_dict[product_name]['Quantity'] = quantity
                        break
                    else:
                        clean_screen()
                        print(
                            '\n\nInvalid Choice.....\nPress any key to try Again.....')
                        wait = input()
                        continue
                except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
                    print("\n\nInvalid Input .....\nPress any key to try again....")
                    wait = input()
                    continue

                price = get_price(product_id)
                reduce_quantity(product_id, quantity)
                amount = price*quantity
                total_amount = total_amount+amount
                product_name = find_product(product_id)[1]
                product_dict[product_name] = {}
                product_dict[product_name]['Price'] = price
                product_dict[product_name]['Quantity'] = quantity

            mycursor.execute('insert into '+customer_name+' (dte,products,total_amount) values(%s,%s,%s)',
                             (dte, json.dumps(product_dict, indent=1), total_amount))
            print(
                '\n\nInvoice Created Successfully.............\nPress any key to continue....')
            wait = input()
        else:
            print('\n\nCustomer does not  exists......\nPress any key to continue....')
            wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print('\n\nInvoice Creation Failed.....\nPress any key to continue....')
        wait = input()
        create_invoice()


def search_customer():

    try:
        clean_screen()
        print('\033[01mSEARCH CUSTOMER SCREEN\033[0m')
        print('─'*50)

        customer_name = input("Enter Customer Name To Search : ")
        if(check_customer(customer_name) == False):
            clean_screen()
            print("\n\nCustomer does not  exists......\nPress any key to continue....")
        else:
            print("\nCustomer "+customer_name+" Found")
            while 1:
                print("ENTER")
                print("1 => View Customer Purchase History")
                print("2 => Create New Invoice")
                print("3 => Menu")
                print("0 => Exit")
                ch = int(input("Enter your Choice : "))
                if ch == 1:
                    view_customer_invoice(customer_name)
                elif ch == 2:
                    create_invoice()
                    customer_menu()
                elif ch == 3:
                    customer_menu()
                elif ch == 0:
                    exit_program(ch)
                else:

                    print("\n\nInvalid Choice.....\n")
                    wait = input()
        wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        search_customer()

# sales managment code


def monthly_report():

    try:
        clean_screen()

        print('\033[01mMONTHLY SALES REPORT SCREEN\033[0m')
        print('─'*50)

        ch = input("Enter Month(e.g=> 2022-01): ")
        exit_program(ch)
        mycursor.execute('select customer_name from customer_table')
        records = mycursor.fetchall()
        total = 0
        for i in records:
            mycursor.execute('select total_amount from ' +
                             i[0]+' where dte like %s', ('%'+ch+'%',))
            records = mycursor.fetchall()
            for j in records:
                total = total+j[0]

        print("\n\nTotal Amount Generated For this Month : ₹"+str(total))
        print('\nPress any key to continue.....')
        wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        monthly_report()


def daily_report():

    try:
        clean_screen()

        print('\033[01mDAILY SALES REPORT SCREEN\033[0m')
        print('─'*50)

        ch = input("Enter Date(e.g=> 2022-01-01): ")
        exit_program(ch)
        mycursor.execute('select customer_name from customer_table')
        records = mycursor.fetchall()
        total = 0
        for i in records:
            mycursor.execute('select total_amount from ' +
                             i[0]+' where dte like %s', ('%'+ch+'%',))
            records = mycursor.fetchall()
            for j in records:
                total = total+j[0]

        print("\n\nTotal Amount Generated For this Day : ₹"+str(total))
        print('\nPress any key to continue.....')
        wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        daily_report()
# menu codes


def customer_menu():

    try:
        while 1:
            clean_screen()
            print("\033[01mCUSTOMER MANAGAMENT SCREEN\033[0m")
            print('─'*50)
            print("ENTER")
            print("1 => Search Customer")
            print("2 => Add Customer")
            print("3 => Display Customers")
            print("4 => Modify Customer Details")
            print("5 => Menu")
            print("0 => Exit\n")
            ch = int(input("Enter your Choice : "))
            if ch == 1:
                search_customer()
            elif ch == 2:
                add_customer()
            elif ch == 3:
                view_customer()
            elif ch == 4:
                modify_customer()
            elif ch == 5:
                main_menu()
            elif ch == 0:
                exit_program(ch)
            else:
                clean_screen()
                print("\n\nInvalid Choice.....\nPress any key to try again")
                wait = input()
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        customer_menu()


def product_menu():

    try:
        clean_screen()
        while 1:

            print("\033[01mPRODUCT MANAGAMENT MENU\033[0m")
            print('─'*50)
            print("ENTER")
            print("1 => Add Product")
            print("2 => Display Products")
            print("3 => Modify Product Details")
            print("4 => Menu")
            print("0 => Exit\n")
            ch = int(input("Enter your Choice : "))
            if ch == 1:
                add_product()
            elif ch == 2:
                view_product()
            elif ch == 3:
                modify_product()
            elif ch == 4:
                main_menu()
            elif ch == 0:
                exit_program(ch)
            else:
                clean_screen()
                print("\n\nInvalid Choice.....\nTry Again\n")
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        product_menu()


def sales_menu():

    try:
        clean_screen()
        while 1:
            print("\033[01mSALES MANAGEMENT MENU\033[0m")
            print('─'*50)
            print("ENTER")
            print("1 => Monthly Sales Report")
            print("2 => Daily Sales Report")
            print("3 => Menu")
            print("0 => Exit\n")
            ch = int(input("Enter your Choice : "))
            if ch == 1:
                monthly_report()
            elif ch == 2:
                daily_report()
            elif ch == 3:
                main_menu()
            elif ch == 0:
                exit_program(ch)
            else:
                clean_screen()
                print("\n\nInvalid Choice.....\nTry Again\n")
    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        sales_menu()


def main_menu():

    try:
        clean_screen()
        while 1:

            print("\033[01mMAIN MENU\033[0m")
            print('─'*50)
            print("ENTER")
            print("1 => Create New Invoice")
            print("2 => Sales Management")
            print("3 => Customer Management")
            print("4 => Product Management")
            print("0 => Exit\n")

            ch = int(input("Enter your Choice : "))
            if ch == 1:
                create_invoice()

            elif ch == 2:
                sales_menu()
            elif ch == 3:
                pass
                customer_menu()
            elif ch == 4:

                product_menu()
            elif ch == 0:
                exit_program(ch)
            else:
                clean_screen()
                print("\n\nInvalid Choice.....\nTry Again\n")

    except (SyntaxError, ValueError, TypeError, NameError, AttributeError, IndexError):
        print("\n\nInvalid Input .....\nPress any key to try again....")
        wait = input()
        main_menu()


login()
