# db.py
import mysql.connector
from .item import Item

_ITEMS_CACHE = None


def fetch_items(force=False):
    global _ITEMS_CACHE

    if _ITEMS_CACHE is not None and not force:
        return _ITEMS_CACHE

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

    _ITEMS_CACHE = items
    return items
