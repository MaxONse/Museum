import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='26071986MaX',    #########################    Enter You're Password
        database='Museum',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("You in")
    try:
        with connection.cursor() as cursor:
            create_table = f"CREATE TABLE `users` (id int AUTO_INCREMENT, login varchar(30) UNIQUE , password varchar(12), PRIMARY KEY (id));"
            cursor.execute(create_table)
            connection.commit()
            create_table2 = f"CREATE TABLE `People` (id int AUTO_INCREMENT, fullName varchar(50) UNIQUE, birth date, death date, PRIMARY KEY (id));"
            cursor.execute(create_table2)
            connection.commit()
            create_table3 = f"CREATE TABLE `Exhibit` (id int AUTO_INCREMENT, name varchar(30) unique , typeEx varchar(30), year varchar(10), author varchar(50),  PRIMARY KEY (id), FOREIGN KEY (author) REFERENCES people (fullName));"
            cursor.execute(create_table3)
            connection.commit()
            insert1 = f"insert into `People`(fullname, birth, death) values ('Oscar-Claude Monet', '1840-11-14', '1926-12-05'), ('Pablo Picasso', '1881-10-25', '1973-04-08'), ('Leonardo da Vinci', '1452-04-15', '1519-05-02');"
            cursor.execute(insert1)
            connection.commit()
            insert3 = f"insert into `users`(login, password) values ('Max', '1111'), ('Some', '2222'), ('Else', '3333')"
            cursor.execute(insert3)
            connection.commit()
            insert = f"insert into `Exhibit` (name, typeEx, year, author) values ('Femmes au jardin', 'painting', '1866', 'Oscar-Claude Monet')," \
                     f" ('La Gare Saint-Lazare', 'painting', '1877', 'Oscar-Claude Monet'), ('Nymphéas', 'painting', '1915', 'Oscar-Claude Monet')," \
                     f"('Lady with a Fan', 'painting', '1909', 'Pablo Picasso'), ('Guernica', 'painting', '1937', 'Pablo Picasso')," \
                     f" ('Violin', 'painting', '1912', 'Pablo Picasso'), ('Madonna del Garofano', 'painting', '1478', 'Leonardo da Vinci')," \
                     f"('Parachute', 'inventions', '1480', 'Leonardo da Vinci'), ('Crossbow', 'inventions', '1500', 'Leonardo da Vinci');"
            cursor.execute(insert)
            connection.commit()
        print("Created")
    except Exception as ex:
        print(ex)
except Exception as ex:
    print(ex)