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

    return members
        
def read(id):
    with sqlite3.connect('flask_ex.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM members WHERE id = ?", id)
        row = cur.fetchone()

        if row:
            member = [{"id": row[0], 
                "first_name": row[1] , 
                "last_name": row[2] , 
                "birth_date": row[3] , 
                "gender": row[4] , 
                "email": row[5] , 
                "phonenumber": row[6] , 
                "address": row[7] , 
                "nationality": row[8] ,
                "active": row[9],
                "github_username": row[10]}]
        else:
            return None
        
    return member
        
def create(member):
    with sqlite3.connect('flask_ex.db') as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO members (
                "first_name", 
                "last_name", 
                "birth_date", 
                "gender", 
                "email", 
                "phonenumber", 
                "address", 
                "nationality", 
                "active", 
                "github_username") 
                VALUES (:first_name,:last_name,:birth_date,:gender,:email,:phonenumber, :address,:nationality,:active,:github_username)''', member)
        
        new_student_id = cur.lastrowid

        conn.commit()

    return new_student_id


def update(id, member):
    with sqlite3.connect('flask_ex.db') as conn:
        cur = conn.cursor()
        cur.execute('''
            UPDATE students SET
                "first_name" = :first_name,
                "last_name" = :last_name,
                "birth_date" = :birth_date,
                "gender" = :gender,
                "email" = :email,
                "phonenumber" = :phonenumber,
                "address" = :address,
                "nationality" = :nationality,
                "active" = :active,
                "github_username" = :github_username
            WHERE "id" = ?
        ''', (member, id))

        conn.commit()

def delete(id):
    with sqlite3.connect('flask_ex.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id= ?", id)
        conn.commit()


