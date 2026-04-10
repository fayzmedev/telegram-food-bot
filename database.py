import sqlite3
from datetime import datetime

DB_NAME = "orders.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        quantity INTEGER,
        drink TEXT,
        address TEXT,
        total INTEGER,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_order(user_id, product, quantity, drink, address, total):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO orders (user_id, product, quantity, drink, address, total, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        product,
        quantity,
        drink,
        address,
        total,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_monthly_stats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT strftime('%Y-%m', created_at) as month,
           COUNT(*) as total_orders,
           SUM(total) as total_income
    FROM orders
    GROUP BY month
    ORDER BY month DESC
    """)

    result = cursor.fetchall()
    conn.close()
    return result