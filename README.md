# DineDesk 🍽️

DineDesk is a Django-based web application designed to support internal restaurant staff in managing daily operations efficiently.

The system provides structured management of:
- Menu categories and items
- Restaurant tables
- Customer orders and order items
- Order status workflow

---

## 🚀 Tech Stack
- **Framework:** Python / Django 
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, Bootstrap / Custom CSS
- **Version Control:** Git & GitHub

---

## 🏛️ Application Structure & Core Models
The project is organized into separate Django apps to ensure modularity, separation of concerns, and maintainability.

- **Category:** Represents a logical grouping of menu items (e.g., Salads, Main Dishes, Desserts).
  - *Fields:* `name` (unique), `slug` (URL-friendly identifier).
  - *Relationship:* One-to-Many with `MenuItem`.
- **MenuItem:** Represents an individual dish offered by the restaurant.
  - *Fields:* `title`, `description`, `price` (with decimal validation), `image` (optional), `category` (ForeignKey), `slug`.
- **Table:** Represents a physical table inside the restaurant.
  - *Fields:* `number`, `seats`, `is_available` (boolean).
  - *Relationship:* One-to-Many with `Orders`.
- **Order:** Represents a customer order associated with a specific table.
  - *Fields:* `table` (ForeignKey), `status` (Pending, Preparing, Served, Paid), `created_at`.
  - *Business Logic:* Includes a `total_price()` method that dynamically calculates the total cost by summing all related `OrderItems`.
- **OrderItem:** Represents a single menu item within an order.
  - *Fields:* `order` (ForeignKey), `menu_item` (ForeignKey), `quantity`.
  - *Business Logic:* Includes a `total_price()` method (`quantity × item price`).

---

## ✨ Key Functionalities
- Create, edit, and delete menu categories and items.
- Manage restaurant tables and their availability.
- Create and process customer orders.
- Add and remove order items dynamically.
- Automatically calculate total order prices.
- Prevent modification of paid orders.
- Search functionality within category detail pages.

---

## ⚙️ Setup & Installation Instructions

To run this project locally, ensure you have **Python 3.10+** installed.

### Step 1: Clone the Repository
```bash
git clone [https://github.com/YanaYovcheva/DineDesk.git](https://github.com/YanaYovcheva/DineDesk.git)
cd DineDesk
```

### Step 2: Configure Environment Variables
You need to set up the environment variables to run the project. A **.env.template**
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
python manage.py makemigrations
python manage.py migrate
```


#### Step 5: Run Development Server
```
python manage.py runserver
```
By default, the server runs on http://127.0.0.1:8000/

#### Step 6: Create a Superuser(optional)
To access the admin panel, create a superuser account:
```
python manage.py createsuperuser
```