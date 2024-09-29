import sqlite3
from data_dict import random_users

def init():
    with sqlite3.connect("flask_ex.db") as con:

        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS members (
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

        cur.execute('SELECT COUNT(*) FROM members')
        row_count = cur.fetchone()[0]
        
        if row_count == 0:
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
                        VALUES (:first_name,:last_name,:birth_date,:gender,:email,:phonenumber,:address,:nationality,:active,:github_username)
                        ''', random_users)
            con.commit()
            
def read_all():
    with sqlite3.connect('flask_ex.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM members")
        rows = cur.fetchall()

        members = [{"id": row[0], 
                "first_name": row[1] , 
                "last_name": row[2] , 
                "birth_date": row[3] , 
                "gender": row[4] , 
                "email": row[5] , 
                "phonenumber": row[6] , 
                "address": row[7] , 
                "nationality": row[8] ,
                "active": row[9],
                "github_username": row[10] } for row in rows]
        con.commit()

    return members
        

