# import mysql.connector as mysql_conn
# from getpass import getpass


# while True:
#     host = input("Enter your MySQL host name(e.g., localhost): ").strip()
#     user = input("Enter your MySQL Username: ").strip()
#     # password = input("Enter your MySQL password: ")
#     password = getpass("Enter MySQL password: ").strip()

#     try:
#         conn = mysql_conn.connect(
#             host = host,
#             user = user,
#             password = password
#         )

#         if conn.is_connected():
#             print("Successfully connection established to MySQL")

#             cursor = conn.cursor()
#             cursor.execute("show databases;")

#             databases = cursor.fetchall()
#             print("Available Databases are: ")

#             for db in databases:
#                 print(db[0])

#             cursor.close()
#             conn.close()

#             break

#     except Exception as e:
#         print(f"Error:{e}\n Please try again with valid credentials")













# import mysql.connector as mysql_conn
# from getpass import getpass
# import pandas as pd

# while True:
#     host = input("Enter your MySQL host name (e.g., localhost): ").strip()
#     user = input("Enter your MySQL Username: ").strip()
#     password = getpass("Enter MySQL password: ").strip()

#     try:
#         conn = mysql_conn.connect(
#             host=host,
#             user=user,
#             password=password
#         )

#         if conn.is_connected():
#             print("Successfully connected to MySQL")

#             cursor = conn.cursor()
#             cursor.execute("SHOW DATABASES;")

#             databases = cursor.fetchall()
#             print("Available Databases are:")
#             for db in databases:
#                 print(db[0])

#             # Ask for the database and table names
#             db_name = input("Enter the name of the database you want to create: ").strip()
#             cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
#             cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
#             cursor.execute(f"USE {db_name}")

#             table_name = input("Enter the name of the table you want to create: ").strip()

#             # Ask the user for the file path and sheet name
#             file_path = input("Enter the file path of the Excel file (e.g., C:\\path\\to\\file.xlsx): ").strip()
#             sheet_name = input("Enter the sheet name you want to read: ").strip()

#             # Load the specified sheet into a DataFrame
#             try:
#                 df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', header=1)
#                 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#                 print("File successfully loaded into DataFrame.")
#             except Exception as e:
#                 print(f"An unexpected error occurred: {e}")
#                 break

#             # Create table with columns from the DataFrame
#             columns = ", ".join([f"'{col}' TEXT" for col in df.columns])  # Adjust data type as needed
#             cursor.execute(f"DROP TABLE IF EXISTS '{table_name}'")
#             cursor.execute(f"CREATE TABLE '{table_name}' ({columns})")
#             print(f"Table '{table_name}' created successfully.")

#             # Insert data into the table
#             placeholders = ", ".join(["%s"] * len(df.columns))
#             insert_query = f"INSERT INTO '{table_name}' ({', '.join(df.columns)}) VALUES ({placeholders})"
#             cursor.executemany(insert_query, df.values.tolist())
#             conn.commit()

#             print(f"{cursor.rowcount} rows were inserted into '{table_name}'.")

#             cursor.close()
#             conn.close()
#             break

#     except Exception as e:
#         print(f"Error: {e}\nPlease try again with valid credentials")













# import mysql.connector as mysql_conn
# from getpass import getpass
# import pandas as pd

# while True:
#     host = input("Enter your MySQL host name (e.g., localhost): ").strip()
#     user = input("Enter your MySQL Username: ").strip()
#     password = getpass("Enter MySQL password: ").strip()

#     try:
#         conn = mysql_conn.connect(
#             host=host,
#             user=user,
#             password=password
#         )

#         if conn.is_connected():
#             print("Successfully connected to MySQL")

#             cursor = conn.cursor()
#             cursor.execute("SHOW DATABASES;")

#             databases = cursor.fetchall()
#             print("Available Databases are:")
#             for db in databases:
#                 print(db[0])

#             # Ask for the database and table names
#             db_name = input("Enter the name of the database you want to create: ").strip()
#             cursor.execute(f"DROP DATABASE IF EXISTS `{db_name}`")
#             cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}`")
#             cursor.execute(f"USE `{db_name}`")

#             table_name = input("Enter the name of the table you want to create: ").strip()

#             # Ask the user for the file path and sheet name
#             file_path = input("Enter the file path of the Excel file (e.g., C:\\path\\to\\file.xlsx): ").strip()
#             sheet_name = input("Enter the sheet name you want to read: ").strip()

#             # Load the specified sheet into a DataFrame
#             try:
#                 df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', header=1)
#                 df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#                 print("File successfully loaded into DataFrame.")
#             except Exception as e:
#                 print(f"An unexpected error occurred: {e}")
#                 break

#             # Create table with columns from the DataFrame
#             columns = ", ".join([f"`{col}` TEXT" for col in df.columns])  # Wrap column names with backticks
#             cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`")
#             cursor.execute(f"CREATE TABLE `{table_name}` ({columns})")
#             print(f"Table '{table_name}' created successfully.")

#             # Insert data into the table
#             placeholders = ", ".join(["%s"] * len(df.columns))
#             insert_query = f"INSERT INTO `{table_name}` ({', '.join([f'`{col}`' for col in df.columns])}) VALUES ({placeholders})"
#             cursor.executemany(insert_query, df.values.tolist())
#             conn.commit()

#             print(f"{cursor.rowcount} rows were inserted into '{table_name}'.")

#             cursor.close()
#             conn.close()
#             break

#     except Exception as e:
#         print(f"Error: {e}\nPlease try again with valid credentials")





import mysql.connector as mysql_conn
from getpass import getpass
import pandas as pd

while True:
    host = input("Enter your MySQL host name (e.g., localhost): ").strip()
    user = input("Enter your MySQL Username: ").strip()
    password = getpass("Enter MySQL password: ").strip()

    try:
        conn = mysql_conn.connect(
            host=host,
            user=user,
            password=password
        )

        if conn.is_connected():
            print("Successfully connected to MySQL")

            cursor = conn.cursor()
            cursor.execute("show databases;")

            databases = cursor.fetchall()
            print("Available Databases are:")
            db_lst = list()
            for db in databases:
                db_lst.append(db[0])
            print(f"{db_lst}")

            db_name = input("Enter the name of the database you want to create: ").strip()
            cursor.execute(f"drop database if exists `{db_name}`")
            cursor.execute(f"create database if not exists `{db_name}`")
            cursor.execute(f"use `{db_name}`")

            table_name = input("Enter the name of the table you want to create: ").strip()

            file_path = input("Enter the file path of the Excel file (e.g., C:\\path\\to\\file.xlsx): ").strip()
            sheet_name = input("Enter the sheet name you want to read: ").strip()

            try:
                df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', header=1)
                
                df.columns = [col if col == col else f"Column_{i}" for i, col in enumerate(df.columns)]
                df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  

                df = df.fillna('')  
                
                print("File successfully loaded into DataFrame.")

            except Exception as e:
                print(f"Error: \n{e}")

                break

            columns = ", ".join([f"`{col}` text" for col in df.columns]) 
            cursor.execute(f"drop table if exists `{table_name}`")
            cursor.execute(f"create table `{table_name}` ({columns})")
            print(f"Table '{table_name}' created successfully.")

            placeholders = ", ".join(["%s"] * len(df.columns))
            insert_query = f"insert into `{table_name}` ({', '.join([f'`{col}`' for col in df.columns])}) values ({placeholders})"
            cursor.executemany(insert_query, df.values.tolist())
            conn.commit()

            print(f"{cursor.rowcount} rows were inserted into '{table_name}'.")

            cursor.close()
            conn.close()
            break

    except Exception as e:
        print(f"Error: \n{e}\nPlease try again with valid credentials")
