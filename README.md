# Bank Management System

This is a simple Bank Management System implemented in Python, utilizing MySQL as the database for managing bank accounts. The system allows you to create accounts, deposit and withdraw funds, check account balances, display account details, and view the last 5 transactions for a specific account.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create a new bank account
- Deposit funds into an account
- Withdraw funds from an account
- Check the account balance
- Display account details
- View the last 5 transactions for an account

## Prerequisites

Before using the Bank Management System, ensure you have the following:

1. Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. The `mysql-connector-python` library installed. You can install it using pip:
             pip install mysql-connector-python
   
A MySQL database set up with the following tables:

accounts table to store account information:

Fields: account_number, account_holder, balance
transactions table to store transaction history:

Fields: transaction_id, transaction_date, account_number, description, amount

##Getting Started
1.Clone or download this repository to your local machine.

2.Ensure that your MySQL server is running. You can use tools like XAMPP, MAMP, or a local MySQL server.
3.Create a new database named bank in your MySQL server.
4.Open the bank_management_system.py file and update the database connection parameters (host, user, password) to match your MySQL server settings:

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="bank"
)

5.Run the Python script:
python bank_management_system.py

##Usage
To create a new account, select option 1 and provide the account details.
To deposit funds into an account, select option 2 and enter the account number and deposit amount.
To withdraw funds from an account, select option 3 and enter the account number and withdrawal amount.
To check the account balance, select option 4 and provide the account number.
To display account details, select option 5 and enter the account number.
To view the last 5 transactions for an account, select option 6 and input the account number.
To exit the system, select option 7.

##Contributing
Contributions to the project are welcome. You can fork the repository, make your improvements, and create a pull request.

##License
This project is open-source and available under the MIT License.
