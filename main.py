from easygui import *
import pymysql


def showByExName(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    with connection.cursor() as cursor:
        showEx = f"select * from museum.exhibit where name = '{ins}';"
        msgbox(showEx)


def showAll(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
        aaa = "\n".join([f"{element.get('id')}, {element.get('name')}, {element.get('typeex')}, {element.get('year')},"
                         f" {element.get('author')}" for element in all_prod])
        msgbox(aaa)


def showAuthByExhibit(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    with connection.cursor() as cursor:
        cursor.execute (f"select * from museum.people where fullname = (select author from museum.exhibit where name = '{ins}');")
        all_people = cursor.fetchall()
        aaa = "\n".join([f"{element.get('id')}, {element.get('fullName')}, {element.get('birth')},"
                         f" {element.get('death')}" for element in all_people])
        msgbox(aaa)


def showExByAuthor(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.people;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('fullName')}" for element in all_prod])
    fff = [f"{element.get('fullName')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    with connection.cursor() as cursor:
        cursor.execute (f"select * from museum.exhibit where author = '{ins}';")
        all_ex = cursor.fetchall()
        aaa = "\n".join([f"{element.get('id')}, {element.get('name')}, {element.get('typeex')}, {element.get('year')},"
                         f" {element.get('author')}" for element in all_ex])
        msgbox(aaa)


def showExByCategory(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select distinct typeEx from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('typeEx')}" for element in all_prod])
    fff = [f"{element.get('typeEx')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    with connection.cursor() as cursor:
        cursor.execute (f"select * from museum.exhibit where typeEx = '{ins}';")
        all_ex = cursor.fetchall()
        aaa = "\n".join([f"{element.get('id')}, {element.get('name')}, {element.get('typeex')}, {element.get('year')},"
                         f" {element.get('author')}" for element in all_ex])
        msgbox(aaa)


def addEx(connection):
    with connection.cursor() as cursor:
        request = multenterbox("Add new:", "Exhibit", ["Name", "Category", "Year", "Author"])
        insert = f"insert into museum.exhibit (name, typeEx, year, author), values ('{request[0]}', '{request[1]}'," \
                 f" '{request[2]}', '{request[3]}'))"
        cursor.execute(insert)
        connection.commit()
        msgbox("Success")


def deleteEx(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    with connection.cursor() as cursor:
        delete_data = f"DELETE FROM museum.exhibit WHERE name = '{ins}';"
        cursor.execute(delete_data)
        connection.commit()
        msgbox("Deleted")


def changeExName(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    new_name = enterbox("Enter new name")
    with connection.cursor() as cursor:
        change_data = f"update museum.exhibit set name = '{new_name}' where name = '{ins}';"
        cursor.execute(change_data)
        connection.commit()
        msgbox("Changed")

def changeExCategory(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    new_name = enterbox("Enter new category")
    with connection.cursor() as cursor:
        change_data = f"update museum.exhibit set typeex = '{new_name}' where name = '{ins}';"
        cursor.execute(change_data)
        connection.commit()
        msgbox("Changed")

def changeExYear(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    new_name = enterbox("Enter new year")
    with connection.cursor() as cursor:
        change_data = f"update museum.exhibit set year = '{new_name}' where name = '{ins}';"
        cursor.execute(change_data)
        connection.commit()
        msgbox("Changed")

def changeExAuthor(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"select * from museum.exhibit;")
        all_prod = cursor.fetchall()
    asd = "\n".join([f"{element.get('name')}" for element in all_prod])
    fff = [f"{element.get('name')}" for element in all_prod]
    ins = buttonbox(asd, "Choose", fff)
    new_name = enterbox("Enter new author")
    with connection.cursor() as cursor:
        change_data = f"update museum.exhibit set author = '{new_name}' where name = '{ins}';"
        cursor.execute(change_data)
        connection.commit()
        msgbox("Changed")


def authorization(login, password, connection):
    with connection.cursor() as cursor:
        if cursor.execute(f"select password from sales.users where login = '{login}';"):
            if cursor.execute(f"select login from sales.users where login = '{login}' and password = '{password}'"):
                msgbox("Success")
            else:
                msgbox("Wrong password")
        else:
            msgbox("Wrong user data")


def registration(login, password, connection):
    st = f"insert into sales.users (login, password) values ('{login}', '{password}')"
    with connection.cursor() as cursor:
        cursor.execute(st)
        connection.commit()
        msgbox("Success")


try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='###########',         #########################    Enter You're Password
        database='Museum',
        cursorclass=pymysql.cursors.DictCursor
    )
    msgbox("You in")

    try:
        request = buttonbox("Choice", "Choice", ["Authorization", "Registration"])
        if request == "Authorization":
            # log_pass = multpasswordbox("Login and Password", "Enter", ["Login:", "Password:"])
            # authorization(log_pass[0], log_pass[1], connection)
            authorization(login="Some", password="2222", connection=connection)
            invite = buttonbox("Select", "Enter", ["Add exhibit", "Remove exhibit", "Edit exhibit", "Show BY", "Close"])
            if invite == "Add exhibit":
                addEx(connection)
            elif invite == "Remove exhibit":
                deleteEx(connection)
            elif invite == "Edit exhibit":
                chioce = buttonbox("What to change", "Choice", ["Name", "Category", "Year", "Author"])
                if chioce == "Name":
                    changeExName(connection)
                elif chioce == "Category":
                    changeExCategory(connection)
                elif chioce == "Year":
                    changeExYear(connection)
                elif chioce == "Author":
                    changeExAuthor(connection)
            elif invite == "Show BY":
                choice = buttonbox("Choice what", "Choice", ["Name Exhibit", "All Exhibits", "Authors by Exhibits",
                                                             "Exhibits by Author", "Exhibits by Category"])
                if choice == "Name Exhibit":
                    showByExName(connection)
                elif choice == "All Exhibits":
                    showAll(connection)
                elif choice == "Authors by Exhibits":
                    showAuthByExhibit(connection)
                elif choice == "Exhibits by Author":
                    showExByAuthor(connection)
                elif choice == "Exhibits by Category":
                    showExByCategory(connection)
            elif invite == "Close":
                pass
        elif request == "Registration":
            log_pass = multpasswordbox("Login and Password", "Enter", ["Login:", "Password:"])
            registration(log_pass[0], log_pass[1], connection)


    finally:
        connection.close()

except Exception as ex:
    print(ex)
