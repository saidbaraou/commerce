# Commerce

This project is an implementation of a marketplace website using Django.

## 🔍 Overview

This web application allows users to:

* Browse listings of items for sale.
* View details of individual items.
* Bid on auction listings.
* Create their own auction listings.
* Add items to a watchlist.

## ➡️ Getting Started

⚙️ To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/saidbaraou/commerce.git](https://github.com/saidbaraou/commerce.git)
    cd commerce
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Make migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.**

## ✨ Features

* **Listings:** Display of active and closed auction listings.
* **Product Page:** Detailed information about each listed item.
* **Create Listing:** Option for logged-in users to create new auction listings.
* **Watchlist:** Ability for users to track items they are interested in.
* **Categories:** View listings from different categories by filtering them.
* **Bidding:** System for placing bids on auction items.
* **Admin Interface:** Django's built-in admin interface for managing the application.

## 🛠️ Technologies Used

![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![image](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## ➕ Further Development

This project could be further enhanced with features such as:

* Payment gateway integration.
* User profile management.
* More advanced search and filtering options.
* Real-time updates for bidding.
* Improved user interface and design.
