import sqlite3

# Establish connection with the SQLite database
def create_connection():
    return sqlite3.connect('inventory.db')

# Create the products table if it doesn't exist
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a new product to the database
def add_product(name, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()
    conn.close()

# Retrieve all products from the database
def get_all_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update product information
def update_product(product_id, name, quantity, price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?", (name, quantity, price, product_id))
    conn.commit()
    conn.close()

# Delete a product from the database
def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
