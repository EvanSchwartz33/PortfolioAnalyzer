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


def remove_user(username, user_id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    query = "DELETE FROM stocks WHERE user_id = ?"
    cur.execute(query, (user_id,))

    query = "DELETE FROM users WHERE username = ?"
    cur.execute(query, (username,))
    con.commit()
    con.close()
    return True
    

