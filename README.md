# 🎨 Art Inventory & Logistics Management System

This is a **web-based inventory and logistics management system** built with **Python (Flask)**.  
It helps manage an **art business** by keeping track of **warehouses, products, inventory, customer orders, and shipments** — all in one platform.

---

## 📘 Project Overview

The **Art Inventory & Logistics Management System** is designed to make managing an art business easier and more organized.

It acts like a **digital warehouse manager**.  
You can check where each product is stored, how much stock is available, what orders are pending, and how shipments are moving.

This project was created to automate and simplify daily tasks in managing art collections, inventory, and logistics operations.

---

## 🎯 Purpose of the Project

The main goal is to help art businesses:
- Keep their **inventory organized**
- Track **warehouse storage capacity**
- Manage **customer orders and shipments**
- Analyze **business performance and stock value**

So, it’s basically a **complete art inventory management system** — useful for small galleries, online art shops, or logistics companies that handle art items.

---

## ⚙️ Key Features

### 🏠 Dashboard (Home Page)
- Displays quick statistics such as:
  - Total number of warehouses
  - Products in stock
  - Pending customer orders
  - Total inventory value
- The dashboard gives a quick summary of your business at a glance.

---

### 🏢 Warehouse Management
- Add new warehouses with details like **name, location, and capacity**.
- View and delete existing warehouses.
- Helps manage multiple storage locations easily.

---

### 🖼️ Product Management
- Add, view, and delete art products.
- Each product includes:
  - Name  
  - Description  
  - Category  
  - Price  
- Works as a central database for all the products being sold or stored.

---

### 📦 Inventory Management
- Keeps track of **which products are stored in which warehouse**.
- Monitors the **quantity** of each product.
- Lets you set **minimum stock levels** so you know when to restock.
- Calculates the **total value of inventory** based on stock and price.

---

### 🧾 Orders Management
- Keeps record of all customer orders.
- Tracks the **status** of each order (Pending, Processing, Delivered, etc.).
- Shows order details like:
  - Order date
  - Customer name
  - Products ordered

---

### 🚚 Shipments & Analytics
- Records shipment details and delivery information.
- Uses **Plotly charts** to show:
  - Sales trends
  - Shipment statistics
  - Warehouse performance
- Helps visualize business performance in an easy-to-understand way.

---

## 🧰 Technology Stack

| Component | Technology Used |
|------------|-----------------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML, CSS, JavaScript |
| **Database** | MySQL |
| **Data Visualization** | Plotly |
| **Server** | Flask development server |

---

## 🖥️ How It Works (Step-by-Step)

1. The user opens the web app in a browser.  
2. Flask connects to the MySQL database and fetches data.  
3. The data is displayed in user-friendly HTML pages.  
4. Users can:
   - Add, edit, or delete products, warehouses, or orders.  
   - Track inventory and shipments.  
5. The changes are saved instantly to the database.  
6. The dashboard updates automatically to reflect new data.

---

## 🧮 Database Design (Basic Structure)

| Table | Purpose |
|--------|----------|
| **warehouses** | Stores warehouse info like name, location, and capacity. |
| **products** | Contains product details such as name, category, and price. |
| **inventory** | Connects products with warehouses and stores quantity info. |
| **orders** | Stores order data, customer info, and order status. |
| **shipments** | Manages shipment and logistics data for deliveries. |

---

## 🚀 How to Run the Project

### 🧩 Prerequisites
Before running this project, make sure you have:
- [Python 3.8+](https://www.python.org/downloads/)
- [MySQL](https://www.mysql.com/downloads/)
- [pip (Python package manager)](https://pip.pypa.io/en/stable/)

---

### ⚙️ Steps to Run

```bash
# 1️⃣ Clone this repository
git clone https://github.com/<your-username>/art-inventory-management.git
cd art-inventory-management

# 2️⃣ Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate      # For Windows
# source venv/bin/activate  # For macOS/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Configure your database
# Create a new MySQL database and update credentials in app.py or config.py

# 5️⃣ Run the Flask server
python app.py

# 6️⃣ Open your browser
http://127.0.0.1:5000

