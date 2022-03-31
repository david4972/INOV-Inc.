from data import get_database  # BDMS (BANK DATA MANAGEMENT SYSTEM)


# debit accounts
def delete_debit_account(name=str, email=str):
    db = get_database()
    curr = db.cursor()
    delete = "DELETE from DebitAccounts WHERE name=?, email=?"
    curr.execute(delete, [name, email])
    curr.commit()
    return "account deleted"


# country of residence for Debit account holders
def debit_account_info_Country():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Country from DebitAccounts ")
    result = {'Debit Accounts Country of Residence data': [dict(zip(tuple(sort.keys()), i)) for i in
                                                           sort.cursor]}
    return result


# Debit card Code (shortened code used to encrypt debit card number)
def debit_account_CardCode():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, SDC from DebitAccounts ")
    result = {'Debit Account DCC data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# encrypted code for securing Debit accounts
def debit_account_SecurityCode():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, DCL from DebitAccounts ")
    result = {
        'Debit Account Digital credit data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# currency of Debit account holders
def debit_account_Currency():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Country, Currency from DebitAccounts ")
    result = {'Debit Account Currencies data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# address of Debit account holders
def debit_account_Address():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Address from DebitAccounts ")
    result = {'Debit Account address data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# checkings balance of Debit account holders
def debit_account_checkings_balance():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Current from DebitAccounts ")
    result = {
        'Debit Account checkings Balance data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# savings balance of Debit account holders
def debit_account_savings_balance():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Saving from DebitAccounts ")
    result = {
        'Personal Credit/Debit Account Savings Balance data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# all info of Debit account holders
def all_debit_account_info():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select * from DebitAccounts ")
    result = {'Debit Account data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# Credit Accounts
def delete_credit_account(name=str, email=str):
    db = get_database()
    curr = db.cursor()
    delete = "DELETE from CreditAccounts WHERE name=?, email=?"
    curr.execute(delete, [name, email])
    curr.commit()
    return "account deleted"


# country of residence for Credit account holders
def credit_account_info_Country():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Country from CreditAccounts ")
    result = {'Credit Accounts Country of Residence data': [dict(zip(tuple(sort.keys()), i)) for i in
                                                            sort.cursor]}
    return result


# Credit card Code (shortened code used to encrypt credit card number)
def credit_account_CardCode():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, SDC from CreditAccounts ")
    result = {'Credit Account DCC data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# encrypted code for securing Credit accounts
def credit_account_SecurityCode():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, DCL from CreditAccounts ")
    result = {
        'Credit Account Digital credit data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# currency of Credit account holders
def credit_account_Currency():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Country, Currency from CreditAccounts ")
    result = {'Credit Account Currencies data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# address of Credit account holders
def credit_account_Address():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Address from CreditAccounts ")
    result = {'Credit Account address data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# checkings balance of Credit account holders
def credit_account_checkings_balance():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Current from CreditAccounts ")
    result = {
        'Credit Account checkings Balance data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# savings balance of Credit account holders
def credit_account_savings_balance():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Saving from CreditAccounts ")
    result = {
        'Credit Account Savings Balance data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# all info of Credit account holders
def all_credit_account_info():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select * from CreditAccounts ")
    result = {'Credit Account data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# Business Credit Account
def delete_business_credit_accnt(name=str, email=str):
    db = get_database()
    curr = db.cursor()
    delete = "DELETE from B-CreditAccounts WHERE name=?, email=?"
    curr.execute(delete, [name, email])
    curr.commit()
    return "account deleted"


# country of residence of Business Credit account holders
def business_credit_account_info_Country():
    db = get_database()
    curr = db.cursor()
    # Business Credit Account
    sort = curr.execute("select name, Country from B-CreditAccounts ")
    result = {
        'Business Credit Accounts Country of Residence data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# Business Credit card Code (shortened code used to encrypt business credit card number)
def business_credit_account_CardCode():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, SDC from B-CreditAccounts ")
    result = {'Business Credit Account DCC data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# encrypted code for securing Business Credit accounts
def business_credit_account_SecurityCode():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, DCL from B-CreditAccounts ")
    result = {
        'Business Credit Account Digital credit data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# currency of Business Credit account holders
def business_credit_account_Currency():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Country, Currency from B-CreditAccounts ")
    result = {'Business Credit Account Currencies data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# address of Business Credit account holders
def business_credit_account_Address():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Address from B-CreditAccounts ")
    result = {'Business Credit Account address data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# checkings balance of Business Credit account holders
def business_credit_account_checkings_balance():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Current from B-CreditAccounts ")
    result = {
        'Business Credit Account checkings Balance data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# savings balance of Business Credit account holders
def business_credit_account_savings_balance():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select name, Saving from B-CreditAccounts ")
    result = {
        'Business Credit Account Savings Balance data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result


# all info of Business Credit account holders
def all_business_credit_account_info():
    db = get_database()
    curr = db.cursor()
    sort = curr.execute("select * from B-CreditAccounts ")
    result = {'Business Credit Account data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    return result

