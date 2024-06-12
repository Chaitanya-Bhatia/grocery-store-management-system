
```markdown
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
```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to use the system.

## Features

- **Product Management**: Add, modify, and view products.
- **Customer Management**: Add, modify, and view customers.
- **Invoice Generation**: Create invoices for customers.
- **Sales Reports**: View daily and monthly sales reports.

## Important Points

- Enter `0` anywhere in the program to exit.
- Update the admin username and password directly in the `login()` function:
    ```python
    def login():
        ...
        if username == 'admin':  # change username here
            if password == 'admin':  # change password here
                ...
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



