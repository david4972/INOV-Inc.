from sqlalchemy import create_engine

# import sqlite3

# Personal Credit/Debit Account Database
db_connect = create_engine('sqlite:///data.db')
# Transactions Database
db = create_engine('sqlite:///transactions.db')
# Business Credit Account Database
cd_connect = create_engine('sqlite:///BusinessAccntdata.db')
# Personal Credit & Debit Account Database
pcd_connect = create_engine('sqlite:///JointAccountdata.db')


# delete account
def delete_accnt(name=str, email=str):
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    conn.execute("DELETE from InovClientsData WHERE name=?, email=?", name, email)
    conn.close()
    print("account deleted")
    # Business Credit Account
    cd = cd_connect.connect()
    cd.execute("DELETE from InovClientsBusiness WHERE name=?, email=?", name, email)
    cd.close()
    print("account deleted")
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    pcd.execute("DELETE from InovClientsJointAccountData WHERE name=?, WHERE email=?", name, email)
    pcd.close()
    print("account deleted")



def get_account_info_Country():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, Country from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Accounts Country of Residence:")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, Country from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Accounts Country of Residence:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, Country from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit & Debit Accounts Country of Residence")
    print(result)


# Digital Credit Code (shortened code that will be credit card number)
def get_account_DCC():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, SDC from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account DCC :")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, SDC from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Account DCC:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, SDC from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Pins of clients:")
    print(result)


# encrypted code for securing accounts
def get_account_DCL():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, DCL from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account DCL:")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, DCL from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Digital credit of clients:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, DCL from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Digital credit of clients:")
    print(result)


# currency of account holder
def get_account_Currency():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, Currency from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account Currencies:")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, Currency from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Account currencies:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, Currency from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit & Debit Account currencies:")
    print(result)


# address of account holder
def get_account_Address():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, Address from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account address:")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, Address from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Account address:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, Address from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit & Debit Account address:")
    print(result)


def get_account_checkings_balance():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, Current from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account checkings Balance :")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, Current from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Current Balance of clients:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, CreditChecking, DebitChecking from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Current Balance of clients:")
    print(result)


def get_account_savings_balance():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select name, Saving from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Savings Balance of clients:")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select name, Saving from InovClientsBusinessData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Account Savings Balance:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select name, CreditSaving, DebitSaving  from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Current Balance of clients:")
    print(result)


# Transactions Database
def get_all_Transactions():
    dub = db.connect()
    sort = dub.execute("select name, Value, Region, Currency from BankTransactions ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("All Transaction Information:")
    print(result)


def get_all_Bank_info():
    # Personal Credit/Debit Account
    conn = db_connect.connect()
    sort = conn.execute("select * from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account Data:")
    print(result)
    # Business Credit Account
    cd = cd_connect.connect()
    sort = cd.execute("select * from InovClientsBusiness ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Account Data:")
    print(result)
    # Personal Credit & Debit Account
    pcd = pcd_connect.connect()
    sort = pcd.execute("select * from InovClientsJointAccountData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit & Debit Account Data:")
    print(result)
