import sqlite3
from data_dict import random_users

def init():
    with sqlite3.connect("flask_ex.db") as con:

        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS members')

        cur.execute('''CREATE TABLE members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    first_name TEXT, 
                    last_name TEXT, 
                    birth_date TEXT, 
                    gender TEXT, 
                    email TEXT, 
                    phonenumber TEXT, 
                    address TEXT, 
                    nationality TEXT,
                    active INTEGER,
                    github_username TEXT)
                ''')


        cur.executemany('''INSERT INTO members (
                    "first_name" , 
                    "last_name" , 
                    "birth_date" , 
                    "gender" , 
                    "email" , 
                    "phonenumber" , 
                    "address" , 
                    "nationality" ,
                    "active",
                    "github_username")
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                    ''', 
                    random_users["first_name"],
                    random_users["last_name"],
                    random_users["birth_date"],
                    random_users["gender"],
                    random_users["email"],
                    random_users["phonenumber"],
                    random_users["address"],
                    random_users["nationality"],
                    random_users["active"],
                    random_users["github_username"])
        

        con.commit()
        con.close()