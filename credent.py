import os
import subprocess
import sys
import mysql.connector

cred_dir = 'mysql_cred_data'

if not os.path.exists(cred_dir):
    os.makedirs(cred_dir)
    print("Directory successfully created..")
else:
    print("Directory already exists.")

print("Please Enter the credentials for connecting the Database to your program..")

uname = input("Enter the MySQL Username: ")

uname_file_path = os.path.join(cred_dir, 'uname.txt')
with open(uname_file_path, 'w') as file:
    file.write(uname)


passwd = input("Enter the MySQL Password: ")

passwd_file_path = os.path.join(cred_dir, 'passwd.txt')
with open(passwd_file_path, 'w') as file:
    file.write(passwd)

host = input("Enter the host for the database: ")

host_file_path = os.path.join(cred_dir, 'host.txt')
with open(host_file_path, 'w') as file:
    file.write(host)

db_confrmation = input("Do you want to create a new database for your project? (Y/N): ")

if db_confrmation == 'y' or db_confrmation == 'Y':

    dbname = input("Enter the database name: ")

    dbname_path = os.path.join(cred_dir, 'dbname.txt')
    with open(dbname_path, 'w') as file:
        file.write(dbname)

    with open(uname_file_path, 'r') as file:
        uname_cont = file.read()
    with open(host_file_path, 'r') as file:
        host_cont = file.read()
    with open(passwd_file_path, 'r') as file:
        passwd_cont = file.read()
    db_config = {
        'host': host_cont,
        'user': uname_cont,
        'password': passwd_cont
    }

    connection = mysql.connector.connect(**db_config)
    db_cursor = connection.cursor()
    db_cursor.execute(f"CREATE DATABASE {dbname}")

else:
    dbname = input("Enter your existing database name: ")
    dbname_path = os.path.join(cred_dir, 'dbname.txt')
    with open(dbname_path, 'w') as file:
        file.write(dbname)

connec_script_content = """
import os
import mysql.connector

directory = 'mysql_cred_data'

uname_filePath = os.path.join(directory, 'uname.txt')
with open(uname_filePath, 'r') as file:
    uname_cont = file.read()

passwd_filePath = os.path.join(directory, 'passwd.txt')
with open(passwd_filePath, 'r') as file:
    passwd_cont = file.read()

host_filePath = os.path.join(directory, 'host.txt')
with open(host_filePath, 'r') as file:
    host_cont = file.read()

dbname_filePath = os.path.join(directory, 'dbname.txt')
with open(dbname_filePath, 'r') as file:
    dbname_cont = file.read()

def connect_to_database():
    db_config = {
        'host': host_cont,
        'user': uname_cont,
        'password': passwd_cont,
        'database': dbname_cont
    }

    # Create a connection to the database
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connected to the database")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

"""

cred_script_path = os.path.join(cred_dir, 'cred.py')

with open(cred_script_path, 'w') as file:
    file.write(connec_script_content)

print("Completed!!!")
print("Please refer to the GitHub repo for connecting the database to your program")
print("Script Executed Successfully!!!!")