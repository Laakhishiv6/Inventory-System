# 📦 Inventory & Logistics Management System

This is a **web-based Inventory and Logistics Management System** built with **Flask (Python)**, **MySQL**, and **HTML/CSS/JavaScript**.  
It helps users **manage warehouses, products, inventory stock levels, customer orders, and shipments** in one place, with an easy-to-use and modern interface.

---

## 📘 Project Overview

This system acts as a **digital warehouse and inventory tracker** for small or medium businesses.  
It helps automate the process of managing stock, tracking orders, and monitoring warehouse performance — saving time and reducing human error.

---

## 🎯 Purpose of the Project

The main goal of this project is to:
- Provide an efficient and user-friendly system for managing inventory operations.  
- Maintain accurate product and order records.  
- Support real-time tracking of stock levels.  
- Present a dashboard for analytics, alerts, and quick decision-making.

It ensures that **products, warehouses, and orders** are all linked and synchronized properly in a single database.

---

## ⚙️ Key Features

### 🏠 1. Home Page – Main Navigation
<img width="1891" height="923" alt="Screenshot 2025-11-12 173245" src="https://github.com/user-attachments/assets/4b4ae205-eba7-4740-b998-048ac2a2bfa4" />


- The **Home Page** gives users a clean starting point to navigate the system.  
- Includes navigation buttons for **Dashboard, Warehouses, Products, Inventory, and Orders**.  
- Each card briefly explains what that module does.

💡 **Purpose:** Easy navigation and quick access to different management modules.

---

### 📊 2. Dashboard – Insights and Analytics
<img width="1878" height="922" alt="Screenshot 2025-11-12 173307" src="https://github.com/user-attachments/assets/72e5f262-0641-4634-92db-e0479134107b" />


- Displays key business stats like:
  - Total warehouses  
  - Products in stock  
  - Pending and shipped orders  
  - Low stock alerts
- Shows **recent orders** with product, quantity, price, and order date.
- Displays stock health alerts for quick restocking decisions.

💡 **Purpose:** Gives an instant overview of inventory and order performance.

---

### 🏢 3. Warehouse Management
![Uploading Screenshot 2025-11-12 173317 - Copy.png…]()



- Users can **add, view, and delete warehouses**.  
- Each warehouse record includes **name, location, and capacity**.  
- Helps in organizing storage facilities efficiently.

💡 **Purpose:** Keeps track of multiple storage locations in a structured way.

---

### 🏷️ 4. Product Management
<img width="1879" height="911" alt="Screenshot 2025-11-12 173317" src="https://github.com/user-attachments/assets/9b768a63-42f7-417a-b500-be3a5159dadf" />


- Users can **add, view, and delete products**.  
- Each product has a **name, description, category, and price**.  
- The system displays a table of all existing products.

💡 **Purpose:** Maintains an updated list of products with complete details for better organization.

---

### 📦 5. Inventory Management
<img width="1890" height="914" alt="Screenshot 2025-11-12 173340" src="https://github.com/user-attachments/assets/5f3c534a-b545-4ad9-8711-a3903f60948e" />


- Links **products** with **warehouses** and tracks quantities.  
- Allows users to set **minimum stock levels** for alerts.  
- Displays total stock quantity and value in a detailed table.  
- Includes **update** and **delete** options for each record.

💡 **Purpose:** Real-time tracking of stock availability across different warehouses.

---

### 🧾 6. Order Management
<img width="1864" height="911" alt="Screenshot 2025-11-12 173443" src="https://github.com/user-attachments/assets/556da2c8-9c86-4578-b57c-730f688f2bef" />


- Allows users to **create, view, and manage customer orders**.  
- Order form captures:
  - Customer Name  
  - Customer Email  
  - Product Ordered  
  - Quantity  
- Displays all orders in a table with details like order ID, total amount, date, and status (Pending/Shipped).

💡 **Purpose:** Simplifies order processing and tracking from creation to delivery.

---

## 🔁 System Workflow

1. **Warehouses** are added first.  
2. **Products** are created and stored.  
3. **Inventory** links each product to a warehouse with stock quantity.  
4. **Orders** are created by customers and tracked through the dashboard.  
5. **Dashboard** displays live updates on stock, alerts, and order activity.

💡 *This makes it a complete end-to-end management system for logistics operations.*

---

## 🧮 Database Management & Optimization

The database is designed with **efficiency, reliability, and data integrity** in mind.  
Key principles applied include:

### ✅ **1. Database Normalization**
- The database is **normalized up to 3rd Normal Form (3NF)**.  
- This means:
  - Each table has a **single purpose** (warehouses, products, inventory, orders).  
  - Redundant data is eliminated.  
  - Relationships are maintained using **foreign keys**.  
- This structure improves data consistency and query performance.

### 🔐 **2. Transaction Control (ACID Properties)**
- All database operations follow **ACID (Atomicity, Consistency, Isolation, Durability)** principles.  
- This ensures:
  - **Atomicity:** Each transaction (like adding or deleting a product) is completed fully or not at all.  
  - **Consistency:** Database remains valid before and after each operation.  
  - **Isolation:** Multiple users can perform tasks without interfering with each other’s data.  
  - **Durability:** Once data is committed, it remains safe even after a crash or restart.  

💡 *Example:*  
If a user creates a new order and updates inventory, both actions happen in a single transaction.  
If one fails, the system rolls back — keeping data accurate.

---

## 🧰 Technology Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python Framework) |
| **Database** | MySQL |
| **Data Visualization** | Plotly |
| **Version Control** | Git / GitHub |
| **Tools** | VS Code, Flask Development Server |

---

## 🧠 Learning Outcomes

Through this project, I learned how to:
- Develop a full-stack web application with Flask and MySQL.  
- Create CRUD (Create, Read, Update, Delete) functionalities.  
- Design normalized database schemas and maintain relationships.  
- Use ACID-compliant transaction handling for reliability.  
- Build an interactive and responsive front-end using HTML/CSS/JS.  
- Implement dashboards for real-time analytics and monitoring.

---

## 🚀 Future Enhancements

In the future, the system can be improved by adding:
- User authentication and roles (Admin, Staff).  
- Export reports to PDF or Excel.  
- Email/SMS alerts for low stock or order status.  
- Integration with barcode scanners.  
- Cloud database and Docker deployment for scalability.

---



