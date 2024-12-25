import sqlite3
import time


#Ask stock ticker
#Ask number of shares
#Ask Average Purchase Price
#Parse Stock Name
#Parse Stock Price

def create_stock(ticker, user_id, avg_price, n_shares):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    query = """INSERT INTO stocks 
                    (ticker, user_id, avg_purchase_price, shares) VALUES (?, ?, ?, ?);"""
    
    cur.execute(query, (ticker, user_id, avg_price, n_shares))

    con.commit()
    con.close()
    return True

def get_stock(ticker, user_id):

    con = sqlite3.connect("database.db")
    cur = con.cursor()
    query = "SELECT * FROM stocks WHERE user_id = ? AND ticker = ?"
    res = cur.execute(query, (user_id, ticker))
    row = res.fetchone()
    con.close()
    return row

   

def update_stock(user_id, ticker, n_shares, avg_price):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    if n_shares < 0 or avg_price < 0:
        raise ValueError("Input of Number of Shares or Price is impossible")

    if n_shares == 0:
        return remove_stock(ticker, user_id)
        
        
    query = "UPDATE stocks SET shares = ?, avg_purchase_price = ? WHERE ticker = ? AND user_id = ?"
    cur.execute(query, (n_shares, avg_price,ticker,user_id))
    
    con.commit()
    con.close()
    return True


def grab_all_stocks(user_id):

    

    pass


def remove_stock(ticker, user_id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    query = "DELETE FROM stocks WHERE ticker = ? AND user_id = ?"
    cur.execute(query, (ticker, user_id))
    con.commit()
    con.close()
    return True



    


