import psycopg2  # CBDMS (CRYPTO BANK DATA MANAGEMENT SYSTEM)


# debit accounts
def delete_debit_account_Crypto(name=str, email=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    delete = '''DELETE from CryptoDebitAccounts WHERE name=?, email=?'''
    curr.execute(delete, [name, email])
    conn.commit()
    conn.close()
    return "account deleted"


# all info of Debit account holders
def all_debit_account_info_Crypto():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CryptoDebitAccounts''')
    result1 = curr.fetchall()
    result = 'Crypto Debit Accounts '
    print(result)
    for row in result1:
        print(row)
