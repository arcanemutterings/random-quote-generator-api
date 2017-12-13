import sqlite3

def getQuote():
    conn = sqlite3.connect('quotes.db')
    cur = conn.cursor()
    cur.execute("""
                SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1;
                """)           
    try: 
        return cur.fetchall()
    finally:
        conn.close()

