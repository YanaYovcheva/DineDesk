# Documentation

---

### Project Overview
DineDesk is a **Restaurant Management System**. This is a Django-based web application  
designed to support internal restaurant staff in managing daily operations efficiently.

The system provides structured management of:
- Menu categories and items
- Restaurant tables
- Customer orders and order items
- Order status workflow

The application follows Django best practices, including class-based views,   
custom validation, search functionality, clean application separation and  
CUD operations.

The goal of this project is to simulate a real-world internal restaurant management  
system where staff members can manage menu content, assign orders to tables,  
add and remove items from orders, search for items within categories.

---

### Application Structure
The project is organized into separate Django apps to ensure modularity, separation  
of concerns and future maintainability.

Core Models:
- _Category_ - Represents a logical grouping of menu items (e.g., Salads, Main Dishes, Desserts).
  - fields:
    - name - unique
    - slug - automatically generated URL-friendly identifier
  - relationships - One Category → Many MenuItems (One-to-Many)
- _MenuItem_ - Represents an individual dish offered by the restaurant
  - fields:
    - title - name of dish
    - description - short textual description
    - price – decimal field with validation 
    - image – optional image of the item 
    - category – foreignKey to Category 
    - slug – Auto-generated identifier
- _Table_ - Represents a physical table inside the restaurant.
  - fields:
    - number – table number
    - seats – number table seats 
    - is_available – boolean indicating table availability
  - relationships:
    - One Table → Many Orders
- _Order_ - Represents a customer order associated with a specific table.
  - fields:
    - table – foreignKey to Table
    - status – current order state (Pending, Preparing, Served, Paid)
    - created_at – timestamp of order creation
  - business logic:
    - contains a method total_price() which calculates the total cost dynamically  
    by summing all related OrderItems.
- _OrderItem_ - Represents a single menu item within an order.
  - fields:
    - order – foreignKey to Order
    - menu_item – foreignKey to MenuItem
    - quantity – number of items ordered.
  - business logic: contains total_price() method calculating quantity × item price.

---

### Key Functionalities

- Create, edit and delete menu categories and items.
- Manage restaurant tables and their availability.
- Create and process customer orders.
- Add and remove order items dynamically.
- Automatically calculate total order price.
- Prevent modification of paid orders.
- Search functionality within category detail page.

---

### Setup Instructions
To run this project, you will need:
- Python 3.10+
- PostgreSQL for the database.

#### Step 1: Clone the Repository
First, clone the repository to your local machine:
```
git clone <repository-url>  
cd <repository-directory>
```

#### Step 2: Configure Environment Variables
You need to set up the environment variables to run the project. A .env.template  
file is included in the repository to guide you.
1. Copy the .env.template file:  
```cp .env.template .env```
2. Edit the .env file and fill in the required values, such as:
- SECRET_KEY: A secret key for Django.
- Database connection settings (DB_NAME, DB_USER, DB_PASSWORD, etc.).
- DEBUG: Set to True for development, False for production.

#### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

#### Step 4: Set Up the Database
Ensure PostgreSQL is running and set up your database using the credentials provided  
in the .env file. Next, run the following commands to apply database migrations:
```
python manage.py migrate
```

#### Step 5: Run Development Server
```
python manage.py runserver
```
