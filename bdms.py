import sqlite3  # BDMS (BANK DATA MANAGEMENT SYSTEM)


# debit accounts
def delete_debit_account(name=str, email=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    delete = '''DELETE from DebitAccounts WHERE name=?, email=?'''
    curr.execute(delete, [name, email])
    conn.commit()
    conn.close()
    return "account deleted"


# all info of Debit account holders
def all_debit_account_info():
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * FROM DebitAccounts''')
    result1 = curr.fetchall()
    result = 'Debit Accounts Country of Residence data'
    print(result)
    for row in result1:
        print(row)


# Credit Accounts
def delete_credit_account(name=str, email=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    delete = '''DELETE FROM CreditAccounts WHERE name=?, email=?'''
    curr.execute(delete, [name, email])
    conn.commit()
    conn.close()
    return "account deleted"


# all info of Credit account holders
def all_credit_account_info():
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    sort = curr.execute('''SELECT * FROM CreditAccounts ''')
    result = 'Credit Account data'
    print(result)
    for row in sort:
        print(row)


# Business Credit Account
def all_business_credit_account_info():
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    sort = curr.execute('''SELECT * FROM B-CreditAccounts ''')
    result = 'Business Credit Account data'
    print(result)
    for row in sort:
        print(row)

