# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Database configuration - UPDATE WITH YOUR CREDENTIALS
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'KIRTI@1980pw',  # Add your MySQL password here
    'database': 'art_inventory'
}

def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

@app.route('/')
def index():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor(dictionary=True)
    
    # Get counts for dashboard
    cursor.execute('SELECT COUNT(*) as warehouse_count FROM warehouses')
    warehouse_count = cursor.fetchone()['warehouse_count']
    
    cursor.execute('SELECT COUNT(*) as product_count FROM products')
    product_count = cursor.fetchone()['product_count']
    
    cursor.execute('SELECT COUNT(*) as order_count FROM orders WHERE status != "delivered"')
    order_count = cursor.fetchone()['order_count']
    
    cursor.close()
    conn.close()
    
    return render_template('index.html', 
                         warehouse_count=warehouse_count,
                         product_count=product_count,
                         order_count=order_count)

# Warehouse routes with full CRUD
@app.route('/warehouses')
def warehouses():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM warehouses ORDER BY id DESC')
    warehouses = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('warehouses.html', warehouses=warehouses)

@app.route('/add_warehouse', methods=['POST'])
def add_warehouse():
    name = request.form['name']
    location = request.form['location']
    capacity = request.form['capacity']
    
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    cursor.execute('INSERT INTO warehouses (name, location, capacity) VALUES (%s, %s, %s)',
                   (name, location, capacity))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/warehouses')

@app.route('/delete_warehouse/<int:warehouse_id>')
def delete_warehouse(warehouse_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM warehouses WHERE id = %s', (warehouse_id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Delete error: {err}")
    cursor.close()
    conn.close()
    return redirect('/warehouses')

# Product routes with full CRUD
@app.route('/products')
def products():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products ORDER BY id DESC')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    description = request.form['description']
    category = request.form['category']
    price = request.form['price']
    
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, description, category, price) VALUES (%s, %s, %s, %s)',
                   (name, description, category, price))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/products')

@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM products WHERE id = %s', (product_id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Delete error: {err}")
    cursor.close()
    conn.close()
    return redirect('/products')

# Inventory routes with full CRUD
@app.route('/inventory')
def inventory():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT i.*, p.name as product_name, p.price as product_price, 
               w.name as warehouse_name
        FROM inventory i
        JOIN products p ON i.product_id = p.id
        JOIN warehouses w ON i.warehouse_id = w.id
        ORDER BY i.id DESC
    ''')
    inventory = cursor.fetchall()
    
    # Calculate total value for each inventory item
    for item in inventory:
        item['total_value'] = item['quantity'] * item['product_price']
    
    # Get products and warehouses for dropdowns
    cursor.execute('SELECT id, name FROM products')
    products = cursor.fetchall()
    
    cursor.execute('SELECT id, name FROM warehouses')
    warehouses = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('inventory.html', 
                         inventory=inventory, 
                         products=products, 
                         warehouses=warehouses)

@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    product_id = request.form['product_id']
    warehouse_id = request.form['warehouse_id']
    quantity = request.form['quantity']
    min_stock_level = request.form['min_stock_level']
    
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    
    # Check if inventory entry already exists
    cursor.execute('SELECT id FROM inventory WHERE product_id = %s AND warehouse_id = %s',
                   (product_id, warehouse_id))
    existing = cursor.fetchone()
    
    if existing:
        cursor.execute('UPDATE inventory SET quantity = quantity + %s WHERE id = %s',
                       (quantity, existing[0]))
    else:
        cursor.execute('''
            INSERT INTO inventory (product_id, warehouse_id, quantity, min_stock_level) 
            VALUES (%s, %s, %s, %s)
        ''', (product_id, warehouse_id, quantity, min_stock_level))
    
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/inventory')

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    inventory_id = request.form['inventory_id']
    quantity = request.form['quantity']
    min_stock_level = request.form['min_stock_level']
    
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    cursor.execute('UPDATE inventory SET quantity = %s, min_stock_level = %s WHERE id = %s',
                   (quantity, min_stock_level, inventory_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/inventory')

@app.route('/delete_inventory/<int:inventory_id>')
def delete_inventory(inventory_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM inventory WHERE id = %s', (inventory_id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Delete error: {err}")
    cursor.close()
    conn.close()
    return redirect('/inventory')

# Order routes with full CRUD
@app.route('/orders')
def orders():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT o.*, p.name as product_name, p.price as unit_price
        FROM orders o
        JOIN products p ON o.product_id = p.id
        ORDER BY o.order_date DESC
    ''')
    orders = cursor.fetchall()
    
    # Calculate total price for each order manually
    for order in orders:
        order['total_price'] = order['quantity'] * order['unit_price']
    
    cursor.execute('SELECT id, name FROM products')
    products = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('orders.html', orders=orders, products=products)

@app.route('/add_order', methods=['POST'])
def add_order():
    customer_name = request.form['customer_name']
    customer_email = request.form['customer_email']
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (customer_name, customer_email, product_id, quantity)
        VALUES (%s, %s, %s, %s)
    ''', (customer_name, customer_email, product_id, quantity))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/orders')

@app.route('/update_order_status', methods=['POST'])
def update_order_status():
    order_id = request.form['order_id']
    status = request.form['status']
    
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    
    # If shipping, update shipment date
    if status == 'shipped':
        cursor.execute('UPDATE orders SET status = %s, shipment_date = NOW() WHERE id = %s', 
                       (status, order_id))
    else:
        cursor.execute('UPDATE orders SET status = %s WHERE id = %s', (status, order_id))
    
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/orders')

@app.route('/delete_order/<int:order_id>')
def delete_order(order_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM orders WHERE id = %s', (order_id,))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Delete error: {err}")
    cursor.close()
    conn.close()
    return redirect('/orders')

# Dashboard routes
@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed", 500
        
    cursor = conn.cursor(dictionary=True)
    
    # Get counts
    cursor.execute('SELECT COUNT(*) as warehouse_count FROM warehouses')
    warehouse_count = cursor.fetchone()['warehouse_count']
    
    cursor.execute('SELECT COUNT(*) as product_count FROM products')
    product_count = cursor.fetchone()['product_count']
    
    cursor.execute('SELECT COUNT(*) as order_count FROM orders WHERE status != "delivered"')
    active_order_count = cursor.fetchone()['order_count']
    
    # Get low stock items
    cursor.execute('''
        SELECT p.name, i.quantity, i.min_stock_level, w.name as warehouse_name
        FROM inventory i
        JOIN products p ON i.product_id = p.id
        JOIN warehouses w ON i.warehouse_id = w.id
        WHERE i.quantity <= i.min_stock_level
    ''')
    low_stock = cursor.fetchall()
    
    # Get order statistics
    cursor.execute('SELECT status, COUNT(*) as count FROM orders GROUP BY status')
    order_stats = cursor.fetchall()
    
    # Get total inventory value
    cursor.execute('''
        SELECT SUM(p.price * i.quantity) as total_value
        FROM inventory i
        JOIN products p ON i.product_id = p.id
    ''')
    total_value_result = cursor.fetchone()
    total_value = total_value_result['total_value'] if total_value_result['total_value'] else 0
    
    # Get recent orders
    cursor.execute('''
        SELECT o.*, p.name as product_name, p.price as unit_price
        FROM orders o 
        JOIN products p ON o.product_id = p.id 
        ORDER BY o.order_date DESC 
        LIMIT 5
    ''')
    recent_orders = cursor.fetchall()
    
    # Calculate total price for recent orders
    for order in recent_orders:
        order['total_price'] = order['quantity'] * order['unit_price']
    
    cursor.close()
    conn.close()
    
    return render_template('dashboard.html', 
                         warehouse_count=warehouse_count,
                         product_count=product_count,
                         active_order_count=active_order_count,
                         low_stock=low_stock, 
                         order_stats=order_stats,
                         total_value=total_value,
                         recent_orders=recent_orders)

if __name__ == '__main__':
    app.run(debug=True)