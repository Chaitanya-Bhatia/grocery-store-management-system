# Grocery Store Management System

This project is a console-based Grocery Store Management System written in Python. It uses MySQL as the database to manage products, customers, and sales. The system supports various functionalities such as adding/modifying products and customers, generating invoices, and viewing sales reports.

## Prerequisites

- Python 3.x
- MySQL

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/gsms.git
    cd gsms
    ```

2. Install the required Python packages:
    ```bash
    pip install mysql-connector-python tabulate
    ```

3. Set up the MySQL database:
    - Open MySQL and create a user and a database if you haven't already.
    - Update the MySQL connection details in the script (username and password).

## Configuration

Edit the following lines in the script to add your own MySQL user and password:

```python
# mysql connectivity

db = mysql.connect(host="localhost", user="your-username", password="your-password")
mycursor = db.cursor(buffered=True)
db.autocommit = True
