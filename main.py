import mysql.connector

# Connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="bank"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create a new bank account
def create_account(connection, account_number, account_holder, balance):
    cursor = connection.cursor()
    insert_query = "INSERT INTO accounts (account_number, account_holder, balance) VALUES (%s, %s, %s)"
    data = (account_number, account_holder, balance)
    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()

# Deposit funds into an account
def deposit(connection, account_number, amount):
    cursor = connection.cursor()
    update_query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
    data = (amount, account_number)
    cursor.execute(update_query, data)
    connection.commit()
    cursor.close()
    # Insert the transaction into the 'transactions' table
    insert_transaction(connection, account_number, "Deposit", amount)

# Withdraw funds from an account
def withdraw(connection, account_number, amount):
    cursor = connection.cursor()
    update_query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
    data = (amount, account_number)
    cursor.execute(update_query, data)
    connection.commit()
    cursor.close()
    # Insert the transaction into the 'transactions' table
    insert_transaction(connection, account_number, "Withdraw", amount)

# Check account balance
def check_balance(connection, account_number):
    cursor = connection.cursor()
    select_query = "SELECT balance FROM accounts WHERE account_number = %s"
    data = (account_number,)
    cursor.execute(select_query, data)
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return None

# Display account details
def display_account_details(connection, account_number):
    cursor = connection.cursor()
    select_query = "SELECT * FROM accounts WHERE account_number = %s"
    data = (account_number,)
    cursor.execute(select_query, data)
    result = cursor.fetchone()
    cursor.close()
    if result:
        account_number, account_holder, balance = result
        print(f"Account Number: {account_number}")
        print(f"Account Holder: {account_holder}")
        print(f"Balance: {balance}")
    else:
        print("Account not found.")

# Get the last 5 transactions for an account
def get_last_5_transactions(connection, account_number):
    cursor = connection.cursor()
    select_query = "SELECT * FROM transactions WHERE account_number = %s ORDER BY transaction_date DESC LIMIT 5"
    data = (account_number,)
    cursor.execute(select_query, data)
    transactions = cursor.fetchall()
    cursor.close()
    return transactions

# Display the last 5 transactions for an account
def display_last_5_transactions(connection, account_number):
    transactions = get_last_5_transactions(connection, account_number)
    if transactions:
        print(f"Last 5 transactions for Account {account_number}:")
        for transaction in transactions:
            transaction_id, transaction_date, account_number, description, amount = transaction
            print(f"Transaction ID: {transaction_id}")
            print(f"Date: {transaction_date}")
            print(f"Description: {description}")
            print(f"Amount: {amount}")
            print("-------------------")
    else:
        print("No transactions found for this account.")

# Insert a transaction into the 'transactions' table
def insert_transaction(connection, account_number, description, amount):
    cursor = connection.cursor()
    insert_query = "INSERT INTO transactions (account_number, description, amount) VALUES (%s, %s, %s)"
    data = (account_number, description, amount)
    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()

# Main function
def main():
    connection = connect_to_db()
    if not connection:
        print("Unable to connect to the database. Exiting.")
        return

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Display Last 5 Transactions")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            create_account(connection, account_number, account_holder, balance)
            print("Account created successfully!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            deposit(connection, account_number, amount)
            print("Amount deposited successfully!")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            balance = check_balance(connection, account_number)
            if balance is not None and balance >= amount:
                withdraw(connection, account_number, amount)
                print("Amount withdrawn successfully!")
            else:
                print("Insufficient balance.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            balance = check_balance(connection, account_number)
            if balance is not None:
                print(f"Account Balance: {balance}")
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = input("Enter account number: ")
            display_account_details(connection, account_number)

        elif choice == "6":
            account_number = input("Enter account number: ")
            display_last_5_transactions(connection, account_number)

        elif choice == "7":
            print("Exiting the Bank Management System.")
            connection.close()
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
