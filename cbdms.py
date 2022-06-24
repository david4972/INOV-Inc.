import sqlite3  # CBDMS (CRYPTO BANK DATA MANAGEMENT SYSTEM)


# debit accounts
def delete_debit_account_Crypto(name=str, email=str):
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    delete = '''DELETE from CryptoDebitAccounts WHERE name=?, email=?'''
    curr.execute(delete, [name, email])
    conn.commit()
    conn.close()
    return "account deleted"


# all info of Debit account holders
def all_debit_account_info_Crypto():
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CryptoDebitAccounts''')
    result1 = curr.fetchall()
    result = 'Crypto Debit Accounts '
    print(result)
    for row in result1:
        print(row)
