# db.py

import mysql.connector
from .item import Item

def fetch_items():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="minu_me0w",
        database="upmods_sofa"
    )

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")

    items = []
    for row in cursor.fetchall():
        items.append(
            Item(
                row["id"],
                row["name"],
                row["type"],
                row["price"],
                row["location"]
            )
        )

    cursor.close()
    conn.close()
    return items
