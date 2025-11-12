# 📦 Inventory & Logistics Management System

This is a **web-based Inventory and Logistics Management System** built using **Flask (Python)**, **MySQL**, and **HTML/CSS/JavaScript**.  
It helps users **manage warehouses, products, stock levels, customer orders, and shipments** — all in one place with a clean and modern interface.

---

## 📘 Project Overview

This system acts as a **digital warehouse and inventory manager**.  
It allows users to:
- Store and organize warehouse information  
- Add and track products  
- Manage stock levels and quantities  
- Create and monitor customer orders  
- View analytics and low-stock alerts on a dashboard  

The system is designed for small or medium businesses that need an easy and efficient way to manage their inventory and logistics operations.

---

## 📸 Project Walkthrough (Screenshots & Steps)

Below is a step-by-step explanation of how the system works, along with what each page in the application does.

---

### 🏠 1. Home Page – Main Navigation and Overview

![Home Page](screenshots/home.png)

This is the **main home page** of the system.  
It serves as the starting point for users to navigate to different modules of the application.

#### ✨ Features:
- The navigation bar at the top gives quick access to all sections:  
  **Home, Dashboard, Warehouses, Products, Inventory, and Orders.**
- The page contains large, clickable cards for each section.  
- Each card briefly describes what that section does (e.g., manage warehouses, view dashboard, manage products).

💡 **Purpose:**  
Provides an easy and user-friendly way for users to access different parts of the inventory system.

---

### 📊 2. Dashboard – Analytics and Key Insights

![Dashboard Page](screenshots/dashboard.png)

The **Dashboard** is the analytical hub of the system.  
It gives a quick visual overview of business and stock information.

#### ✨ Features:
- **Low Stock Alerts:**  
  Highlights products or warehouses that have fallen below the minimum stock level.  
  Example: “Current: 7 | Minimum: 70 – Low Stock Alert!”
- **Order Status Distribution:**  
  Displays how many orders are pending or shipped.
- **Recent Orders Table:**  
  Lists the most recent customer orders with details like customer name, product, quantity, price, status, and date.

💡 **Purpose:**  
Gives a summary of the overall inventory health, order progress, and business activity.

---

### 🏢 3. Warehouse Management – Manage Storage Locations

![Warehouse Management](screenshots/warehouse.png)

This page handles **warehouse data management**.

#### ✨ Features:
- **Add New Warehouse Form:**  
  Allows users to add new warehouses with details like:
  - Warehouse Name  
  - Location  
  - Storage Capacity  
- **Warehouse List Table:**  
  Displays all existing warehouses with their names, addresses, and capacities.
- **Delete Button:**  
  Allows users to remove outdated or duplicate warehouse records.

💡 **Purpose:**  
Helps the user maintain an updated list of storage facilities or branches.

---

### 🏷️ 4. Product Management – Manage Product Details

![Product Management](screenshots/products.png)

This page helps users manage all the products in the system.

#### ✨ Features:
- **Add New Product Form:**  
  Users can enter product details including:
  - Product Name  
  - Description  
  - Category  
  - Price  
- **Product List Table:**  
  Displays all products currently in the system with their categories and prices.
- **Delete Button:**  
  Removes unwanted or outdated products.

💡 **Purpose:**  
Acts as a central place to maintain product information — what items exist in stock, along with their categories and prices.

---

### 📦 5. Inventory Management – Track Stock and Warehouse Quantities

![Inventory Management](screenshots/inventory.png)

This page connects products to specific warehouses and tracks the number of items in each location.

#### ✨ Features:
- **Add/Update Inventory Form:**  
  Allows users to select a product, choose a warehouse, enter stock quantity, and set a minimum stock alert.
- **Current Inventory Table:**  
  Displays all existing stock entries with:
  - Product name  
  - Warehouse location  
  - Current quantity  
  - Minimum stock value  
  - Total inventory value  
- Includes “Update” and “Delete” buttons for easy management.

💡 **Purpose:**  
Makes it easy to see how much stock is available at each location and identifies low-stock items that need restocking.

---

### 🧾 6. Order Management – Create and Track Customer Orders

![Order Management](screenshots/orders.png)

This page manages customer order data and helps track their processing status.

#### ✨ Features:
- **Create New Order Form:**  
  Lets users input:
  - Customer Name  
  - Customer Email  
  - Product Name  
  - Quantity Ordered  
- **Order List Table:**  
  Shows all current and past orders with:
  - Order ID  
  - Customer Name  
  - Product Name  
  - Quantity  
  - Total Amount  
  - Status (Pending, Shipped, etc.)  
  - Order Date  
- Each order can be **deleted or updated** as needed.

💡 **Purpose:**  
Helps businesses handle orders efficiently and monitor their delivery status.

---

## 🔁 How the System Works Together

Here’s the simple flow of how the whole system operates:

1. **Warehouses** are added to store items.  
2. **Products** are created and listed.  
3. **Inventory** links products to specific warehouses and keeps count of each item.  
4. **Orders** are created when customers make purchases.  
5. The **Dashboard** updates automatically to show:
   - Total products and warehouses  
   - Pending or shipped orders  
   - Low-stock warnings  
   - Recent orders and financial summaries  

💡 This flow ensures smooth tracking of inventory and orders from start to finish.

---

## 🧰 Technology Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask (Python Framework) |
| **Database** | MySQL |
| **Data Visualization** | Plotly |
| **IDE/Tools** | VS Code, Flask Server, Git/GitHub |

---

## 🎨 UI Design Highlights

- Simple and modern **dark-theme interface**  
- Easy navigation with **top menu bar**  
- Clear buttons and forms for user-friendly experience  
- Data displayed in structured, readable tables  
- Consistent color coding (purple for actions, red for delete)

---

## 🧠 Key Learning Outcomes

While building this project, I learned how to:
- Build full-stack web applications using Flask and MySQL  
- Create CRUD operations (Add, View, Update, Delete)  
- Design responsive web interfaces with HTML/CSS  
- Handle data dynamically between frontend and backend  
- Manage databases effectively using SQLAlchemy or MySQL  

---

## 🚀 Future Enhancements

In future versions, I plan to add:
- User authentication (Admin and Staff roles)  
- Export reports to PDF/Excel  
- Integration with barcode scanners  
- Email or SMS alerts for low stock  
- Cloud database connectivity for multi-branch access  

---

## 👩‍💻 Author

**[Your Name]**  
📧 your.email@example.com  
🌐 [LinkedIn Profile](https://www.linkedin.com/in/yourname)

If you found this project helpful, please ⭐ star the repository to support!

---

## 📝 License

This project is released under the **MIT License**.  
You can use, modify, and share it for personal or educational purposes.

---

