import sqlite3
import time



def create_user(username, password, salt):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    



    query = """INSERT INTO users
                    (username, hashed_password, salt) VALUES (?,?,?);"""
    cur.execute(query, (username, password, salt))
    con.commit()
    con.close()
    

def get_user(username):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    query = "SELECT * FROM users WHERE username = ?"

    res = cur.execute(query, (username,))
    row = res.fetchone()

    con.close()

    return row

    

def edit_user():
    
    pass

def remove_user():

    pass

