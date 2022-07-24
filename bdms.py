import psycopg2  # BDMS (BANK DATA MANAGEMENT SYSTEM)


# debit accounts
def delete_debit_account(card_num=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''DELETE from DebitInov WHERE CardNo=%s''', [card_num])
    conn.commit()
    conn.close()
    return "account deleted"


# all info of Debit account holders
def all_debit_account_info():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov''')
    result1 = curr.fetchall()
    result = 'Debit Accounts data'
    print(result)
    for row in result1:
        print(row)


# Credit Accounts
def delete_credit_account(card_num=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''DELETE FROM CreditInov WHERE CardNo=%s''', [card_num])
    conn.commit()
    conn.close()
    return "account deleted"


# all info of Credit account holders
def all_credit_account_info():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    sort = curr.execute('''SELECT * FROM CreditInov ''')
    result = 'Credit Account data'
    print(result)
    for row in sort:
        print(row)


# International Debit Account
def delete_InternationalDebit_account(card_num=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''DELETE FROM InterDebitInov WHERE CardNo=%s''', [card_num])
    conn.commit()
    conn.close()
    return "account deleted"


def all_InternationalDebit_account_info():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    sort = curr.execute('''SELECT * FROM InterDebitInov ''')
    result = 'International Debit Account data'
    print(result)
    for row in sort:
        print(row)


if __name__ == '__main__':
    all_InternationalDebit_account_info()
    all_credit_account_info()
    all_debit_account_info()
