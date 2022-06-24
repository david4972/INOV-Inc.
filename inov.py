import sqlite3
from forex_python.converter import CurrencyRates
from cryptography.fernet import Fernet
import smtplib
import invp
import random


def intro():
    text = "WELCOME TO INOV!!!!!! We are a Saas startup that build creative, innovative and simpler " \
           "apis for more transparent financial services. " \
           "We only operate in the US as of right now but we look to expand."
    return text


# CODE STATUS: Complete
# Create Accounts STATUS: Complete
# create Business Credit Account
def create_business_account(account_name=str, email=str, address=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    Curr = "USD"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    business_type = input("what Industry does your business operate in:")
    Credit_Checking_amt = float(input('How much do you want to deposit into your Business Credit Checkings account '
                                      'p.s. '
                                      'min deposit is. 50,000 '
                                      'required max '
                                      'deposit is '
                                      '100,000: '))
    if Credit_Checking_amt > 100000 or Credit_Checking_amt < 50000:
        print("deposit does not meet requirement, try again")
    Credit_Savings_amt = float(
        input('How much do you want to deposit into your Business Credit Savings account p.s. min deposit is 150,000'
              'required max '
              'deposit is '
              '500,000: '))
    if Credit_Savings_amt > 500000 or Credit_Savings_amt < 150000:
        print("deposit does not meet requirement, try again")

    read_data = "INSERT INTO BusinessCreditAccounts (name, email, industry, CardNo, CardCode, SecurityCode, Checking, " \
                "Saving, " \
                "Address, " \
                "Country, " \
                "Currency) " \
                "VALUES ( " \
                "?, " \
                "?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
    val = (account_name, email, business_type, CardNo, CardCode, Sec_code, Credit_Checking_amt, Credit_Savings_amt,
           address,
           country, Curr)
    curr.execute(read_data, val)
    conn.commit()
    dclNo = 'Congrats on your new Business Credit account!!! This -> {}  is your secured Business credit card ' \
            'number, and this number ' \
            'will ' \
            'be your main account charged with ' \
            'most ' \
            'transactions you make.' \
            'This -> {} is your security card code, it can also serve as your card number. Be sure to keep it ' \
            'secure. This is to ensure safer payment ' \
            'and build a more secure wall ' \
            'around your credit. Please memorize ' \
            'these first five digits. '
    msg = dclNo.format(CardNo, CardCode)
    conn.close()
    print("Account created")
    send_mail_for_new_account(email, msg)


# create Credit Account
def create_Credit_account(account_name=str, email=str, address=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    Curr = "USD"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    Credit_Checking_amt = float(input('How much do you want to deposit into your Credit Checkings account p.s. no '
                                      'min deposit '
                                      'required max '
                                      'deposit is '
                                      '5,000: '))
    if Credit_Checking_amt > 5000 or Credit_Checking_amt < 0:
        print("deposit does not meet requirement, try again")
        intro()
    Credit_Savings_amt = float(
        input('How much do you want to deposit into your Credit Savings account p.s. no min deposit '
              'required max '
              'deposit is '
              '15,000: '))
    if Credit_Savings_amt > 15000 or Credit_Savings_amt < 0:
        print("deposit does not meet requirement, try again")
        intro()
    read_data = "INSERT INTO CreditAccounts (name, email, CardNo, CardCode, SecurityCode, Checking, " \
                "Saving, " \
                " Address, Country, " \
                "Currency) " \
                "VALUES ( " \
                "?, " \
                "?, ?, ?, ?, ?, ?, ?, ?, ?) "
    val = (account_name, email, CardNo, CardCode, Sec_code, Credit_Checking_amt, Credit_Savings_amt,
           address,
           country, Curr)
    curr.execute(read_data, val)
    conn.commit()
    dclNo = "Congrats on your new Credit Bank account!!! This -> {} is your card number. This -> {} is your secured " \
            "card " \
            "code that will be used to secure your account. "
    msg = dclNo.format(CardNo, CardCode)
    send_mail_for_new_account(email, msg)
    conn.close()
    return "Account created"


# create Debit Account
def create_Debit_account(account_name=str, email=str, address=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    Curr = "USD"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    Debit_Checking = float(input('How much do you want to deposit into this account p.s. no min deposit required max '
                                 'deposit is '
                                 '5,000: '))
    if Debit_Checking > 5000 or Debit_Checking < 0:
        print("deposit does not meet requirement, try again")
    Debit_Saving = float(input('How much do you want to deposit into this account p.s. no min deposit required max '
                               'deposit is '
                               '15,000: '))
    if Debit_Saving > 15000 or Debit_Saving < 0:
        print("deposit does not meet requirement, try again")
    read_data = "INSERT INTO DebitAccounts (name, email, CardNo, CardCode, SecurityCode, Checking, Saving, " \
                "Address, Country, " \
                "Currency) " \
                "VALUES ( " \
                "?, " \
                "?, ?, ?, ?, ?, ?, ?, ?, ?) "
    val = (account_name, email, CardNo, CardCode, Sec_code, Debit_Checking, Debit_Saving,
           address,
           country, Curr)
    curr.execute(read_data, val)
    conn.commit()
    dclNo = "Congrats on your new Debit Bank account!!! This -> {} is your card number. This -> {} is your secured " \
            "card " \
            "code that will be used to secure your account. "
    msg = dclNo.format(CardNo, CardCode)
    print("Account created")
    conn.close()
    send_mail_for_new_account(email, msg)


# Deposits STATUS: Complete
def deposit_option(name=str, deposit=float, ans=str, CardNo=int):
    if ans == "1":
        deposit_Checking(name, deposit, CardNo)
        return "processing deposit"

    if ans == "2":
        deposit_Savings(name, deposit)
        return "processing deposit"


def deposit_Checking(name=str, deposit=float, CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = '''SELECT * from DebitAccounts where CardNo=? where name=?'''
    read_data2 = '''SELECT * from CreditAccounts where CardNo=? where name=?'''
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    curr.execute(read_data1, [CardNo, name])
    for row in curr.fetchall():
        email = row[1]
        if name == row[0]:
            if CardNo == row[2]:
                # processing transaction
                transaction = "UPDATE DebitAccounts SET Checking=Checking+? WHERE CardNoe=?"
                curr.execute(transaction, [deposit, CardNo])
                conn.commit()
                print("deposit complete")
                conn.close()  # completing transaction
                send_mail_for_deposits_checking(deposit, email)
    else:
        curr.execute(read_data2, CardNo)
        for row in curr.fetchall():
            email2 = row[1]
            if name == row[0]:
                if CardNo == row[2]:
                    # processing transaction
                    transaction = "UPDATE DebitAccounts SET Checking=Checking+? WHERE CardNo=?"
                    curr.execute(transaction, [deposit, CardNo])
                    conn.commit()
                    print("deposit complete")
                    conn.close()  # completing transaction
                    send_mail_for_deposits_checking(deposit, email2)



def deposit_Savings(name=str, deposit=float, CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = '''SELECT * from DebitAccounts WHERE CardNo=?'''
    read_data2 = '''SELECT * from CreditAccounts WHERE CardNo=?'''
    # read_data3 = "SELECT * from CreditAccounts where CardCode=?"
    curr.execute(read_data1, CardNo)
    for row in curr.fetchall():
        email = row[1]
        if name == row[0]:
            if CardNo == row[2]:
                # processing transaction
                transaction = '''UPDATE DebitAccounts SET Saving=Saving+? WHERE CardNo=?'''
                curr.execute(transaction, [deposit, CardNo])
                conn.commit()
                print("deposit complete")
                conn.close()  # completing transaction
                send_mail_for_deposits_saving(deposit, email)
    else:
        curr.execute(read_data2, CardNo)
        for row in curr.fetchall():
            email2 = row[1]
            if name == row[0]:
                if CardNo == row[3]:
                    # processing transaction
                    transaction = '''UPDATE CreditAccounts SET Saving=Saving+? WHERE CardNo=?'''
                    curr.execute(transaction, [deposit, CardNo])
                    conn.commit()
                    print("deposit complete")
                    conn.close()  # completing transaction
                    send_mail_for_deposits_saving(deposit, email2)



def atm_option(CardCode=str, var=str, withdraw=int):
    if var == "Checkings":
        atm_Checking(CardCode, withdraw)

    if var == "Savings":
        atm_Savings(CardCode, withdraw)

    return "ATM processing, You will be charged 1.3% upon withdrawal."


def atm_Checking(CardCode=str, withdraw=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOV"
    rate_r = 0.013
    read_data1 = '''SELECT * from DebitAccounts WHERE CardCode=?'''
    read_data2 = '''SELECT * from CreditAccounts WHERE CardCode=?'''
    curr.execute(read_data1, CardCode)
    for row in curr.fetchall(CardCode):
        checking = row[5]
        if CardCode == row[3]:
            service = checking * rate_r
            transaction = "UPDATE DebitAccounts SET Checking=Checking-?, WHERE CardCode=?"
            curr.execute(transaction, [withdraw, CardCode])
            fee = "UPDATE DebitAccounts SET Checking=Checking-?, WHERE CardCode=?"
            curr.execute(fee, [service, CardCode])
            serv = "UPDATE B-CreditAccounts SET Checking=Checking+?, WHERE name=?"
            curr.execute(serv, [service, bank])
            conn.commit()
            print("Withdrawal Complete")
            conn.close()
        else:
            curr.execute(read_data2, CardCode)
            for row2 in curr.fetchall(CardCode):
                checking = row[5]
                if CardCode == row2[3]:
                    service = checking * rate_r
                    transaction = "UPDATE CreditAccounts SET Checking=Checking-?, WHERE CardCode=?"
                    curr.execute(transaction, [withdraw, CardCode])
                    fee = "UPDATE CreditAccounts SET Checking=Checking-?, WHERE CardCode=?"
                    curr.execute(fee, [service, CardCode])
                    serv = "UPDATE B-CreditAccounts SET Checking=Checking+?, WHERE name=?"
                    curr.execute(serv, [service, bank])
                    conn.commit()
                    print("Withdrawal Complete")
                    conn.close()



def atm_Savings(CardCode=str, withdraw=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    read_data1 = '''SELECT * from DebitAccounts WHERE CardCode=?'''
    read_data2 = '''SELECT * from CreditAccounts WHERE CardCode=?'''
    curr.execute(read_data1, CardCode)
    for row in curr.fetchall():
        saving = row[6]
        if CardCode == row[3]:
            service = saving * rate_r
            transaction = "UPDATE DebitAccounts SET Saving=Saving-?, WHERE CardCode=?"
            curr.execute(transaction, [withdraw, CardCode])
            fee = "UPDATE DebitAccounts SET Saving=Saving-?, WHERE CardCode=?"
            curr.execute(fee, [service, CardCode])
            serv = "UPDATE B-CreditAccounts SET Saving=Saving+?, WHERE name=?"
            curr.execute(serv, [service, bank])
            conn.commit()
            print("Withdrawal Complete")
            conn.close()
        else:
            curr.execute(read_data2, CardCode)
            for row2 in curr.fetchall():
                saving = row[6]
                if CardCode == row2[3]:
                    service = saving * rate_r
                    transaction = "UPDATE CreditAccounts SET Saving=Saving-?, WHERE CardCode=?"
                    curr.execute(transaction, [withdraw, CardCode])
                    fee = "UPDATE CreditAccounts SET Saving=Saving-?, WHERE CardCode=?"
                    curr.execute(fee, [service, CardCode])
                    serv = "UPDATE B-CreditAccounts SET Saving=Saving+?, WHERE name=?"
                    curr.execute(serv, [service, bank])
                    conn.commit()
                    print("Withdrawal Complete")
                    conn.close()



def send_money(amount=float, name=str, recipient=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    rate_r = 0.013
    read_data1 = '''SELECT * from DebitAccounts WHERE name=?'''
    read_data2 = '''SELECT * from CreditAccounts WHERE name=?'''
    # read_data3 = "SELECT * from B-CreditAccounts where CardCode=?"
    curr.execute(read_data1, name)
    for row1 in curr.fetchall():
        checking = row1[5]
        if name == row1[0]:
            fee = checking * rate_r
            curr.execute('UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank', [fee])
            # processing transaction
            retrieve = "UPDATE DebitAccounts SET Checking=Checking-? name=?"
            curr.execute(retrieve, [amount, name])
            conn.commit()
            print("transaction complete")
            conn.close()
            process = "SELECT * from DebitAccounts WHERE name=?"
            curr.execute(process, recipient)
            for row2 in curr.fetchall():
                email = row2[0]
                if recipient == row2[0]:
                    send = "UPDATE DebitAccounts SET Checking=Checking+? WHERE name=?"
                    curr.execute(send, [amount, recipient])  # completing transaction
                    conn.commit()
                    print("transaction complete")
                    conn.close()
                    send_mail_for_Transactions(name, email, amount)
        else:
            curr.execute(read_data2, name)
            for row3 in curr.fetchall():
                checking = row3[5]
                if name == row3[0]:
                    fee = checking * rate_r
                    curr.execute('UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank', [fee])
                    # processing transaction
                    retrieve = "UPDATE CreditAccounts SET Checking=Checking-? name=?"
                    curr.execute(retrieve, [amount, name])
                    conn.commit()
                    print("transaction complete")
                    conn.close()
                    process = "SELECT * from CreditAccounts WHERE name=?"
                    curr.execute(process, recipient)
                    for row4 in curr.fetchall():
                        email = row4[0]
                        if recipient == row4[0]:
                            send = "UPDATE CreditAccounts SET Checking=Checking+? WHERE name=?"
                            curr.execute(send, [amount, recipient])  # completing transaction
                            conn.commit()
                            print("transaction complete")
                            conn.close()
                            send_mail_for_Transactions(name, email, amount)



def process_payment(CardCode=str):
    invp.get_card_info(CardCode)
    # return "processing payment"


def bank_statement(name=str, CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = '''SELECT * from DebitAccounts WHERE CardNo=?'''
    read_data2 = '''SELECT * from CreditAccounts WHERE CardNo=?'''
    # read_data3 = '''SELECT * from B-CreditAccounts WHERE CardNo=?'''
    curr.execute(read_data1, CardNo)
    for row1 in curr.fetchall():
        email = row1[1]
        if name == row1[0]:
            if CardNo == row1[3]:
                statement = curr.execute("SELECT name, Checking, Saving, Currency from DebitAccounts WHERE CardCode=?")
                result = {'Your Bank Statement': [dict(zip(tuple(statement.keys()), i)) for i in statement.cursor]}

        else:
            curr.execute(read_data2, CardNo)
            for row2 in curr.fetchall():
                email = row2[1]
                if name == row2[0]:
                    if CardNo == row2[3]:
                        statement = curr.execute("SELECT name, Checking, Saving, Currency from CreditAccounts WHERE "
                                                 "CardCode=?")
                        result = "Your Bank Statement"
                        for row in statement:
                            print(row)
    # return "bank statement has been sent to email"


# Currency change (allows account users to convert currency cash account into the main global currencies (USD, EUR,
# GBP, CNY)
def CurrencyExchange_USD(name=str, CardNo=int, gbc=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = gbc
    cex1 = c.get_rate(var2, var1)
    cex2 = c.get_rate(var2, var1)
    rate_r = 0.013
    r_data1 = '''SELECT email, Checking, Saving, Currency FROM DebitAccounts WHERE CardNo=?'''
    r_data2 = '''SELECT email, Checking, Saving, Currency FROM CreditAccounts WHERE CardNo=?'''
    # r_data3 = '''SELECT email, Checking, Saving, Currency FROM DebitAccounts WHERE CardNo=?'''
    curr.execute(r_data1, CardNo)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardNo == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('''UPDATE DebitAccounts SET Checking=Checking-? WHERE name=?''', [checking_fee, name])
            curr.execute('''UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
            curr.execute('''UPDATE BusinessCreditAccounts SET Checking=Checking+? WHERE name=INOVBank''', [rate_r])
            curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
            data1 = '''UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
            curr.execute(data1, [cex1, cex2, var1, name])
            conn.commit()
            print("exchange complete, you were charged 1.3% upon exchange")
            conn.close()
            send_mail_for_currency_exchange(var1, email)
        else:
            curr.execute(r_data2, CardNo)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardNo == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('''UPDATE CreditAccounts SET Current=Current-? WHERE name=?''',
                                 [checking_fee, name])
                    curr.execute('''UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOV Bank''', [rate_r])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOV Bank''', [rate_r])
                    data2 = '''UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
                    curr.execute(data2, [cex1, cex2, var1, name])
                    conn.commit()
                    print("exchange complete, you were charged 1.3% upon exchange")
                    conn.close()
                    send_mail_for_currency_exchange(var1, email)



def CurrencyExchange_EUR(name=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    c = CurrencyRates()
    var2 = "EUR"
    gbc = "USD"
    dex1 = c.get_rate(gbc, var2)
    dex2 = c.get_rate(gbc, var2)
    rate_r = 0.013
    r_data1 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE name=?'''
    r_data2 = '''SELECT email, Checking, Saving, Currency from CreditAccounts WHERE name=?'''
    # r_data3 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE CardCode=?'''
    curr.execute(r_data1, name)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if name == row1[0]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('''UPDATE DebitAccounts SET Current=Current-? WHERE name=?''', [checking_fee, name])
            curr.execute('''UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
            curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
            curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
            data1 = '''UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
            curr.execute(data1, [dex1, dex2, var2, name])
            conn.commit()
            print("exchange complete, you were charged 1.3% upon exchange")
            conn.close()
            send_mail_for_currency_exchange(var2, email)
        else:
            curr.execute(r_data2, name)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if name == row2[0]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE name=?',
                                 [checking_fee, name])
                    curr.execute('''UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOV Bank''', [rate_r])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOV Bank''', [rate_r])
                    data2 = '''UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
                    curr.execute(data2, [dex1, dex2, var2, name])
                    conn.commit()
                    print("exchange complete, you were charged 1.3% upon exchange")
                    conn.close()
                    send_mail_for_currency_exchange(var2, email)



def CurrencyExchange_GBP(name=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    c = CurrencyRates()
    var3 = "GBP"
    gbc = "USD"
    fex3 = c.get_rate(gbc, var3)
    fex4 = c.get_rate(gbc, var3)
    rate_r = 0.013
    r_data1 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE name=?'''
    r_data2 = '''SELECT email, Checking, Saving, Currency from CreditAccounts WHERE name=?'''
    # r_data3 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE CardCode=?'''
    curr.execute(r_data1, name)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if name == row1[0]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('''UPDATE DebitAccounts SET Current=Current-? WHERE name=?''', [checking_fee, name])
            curr.execute('''UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
            curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
            curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
            data1 = '''UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
            curr.execute(data1, [fex3, fex4, var3, name])
            conn.commit()
            print("exchange complete, you were charged 1.3% upon exchange")
            conn.close()
            send_mail_for_currency_exchange(var3, email)
        else:
            curr.execute(r_data2, name)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if name == row2[0]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('''UPDATE CreditAccounts SET Current=Current-? WHERE name=?''',
                                 [checking_fee, name])
                    curr.execute('''UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
                    data2 = '''UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
                    curr.execute(data2, [fex3, fex4, var3, name])
                    conn.commit()
                    print("exchange complete, you were charged 1.3% upon exchange")
                    conn.close()
                    send_mail_for_currency_exchange(var3, email)


def CurrencyExchange_AUS(name=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    c = CurrencyRates()
    var4 = "AUS"
    gbc = "USD"
    gex4 = c.get_rate(gbc, var4)
    gex5 = c.get_rate(gbc, var4)
    rate_r = 0.013
    r_data1 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE name=?'''
    r_data2 = '''SELECT email, Checking, Saving, Currency from CreditAccounts WHERE name=?'''
    # r_data3 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE CardCode=?'''
    curr.execute(r_data1, name)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if name == row1[0]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('''UPDATE DebitAccounts SET Current=Current-? WHERE name=?''', [checking_fee, name])
            curr.execute('''UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
            curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
            curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
            data1 = '''UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
            curr.execute(data1, [gex4, gex5, var4, name])
            conn.commit()
            print("exchange complete, you were charged 1.3% upon exchange")
            conn.close()
            send_mail_for_currency_exchange(var4, email)
        else:
            curr.execute(r_data2, name)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if name == row2[0]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('''UPDATE CreditAccounts SET Current=Current-? WHERE name=?''',
                                 [checking_fee, name])
                    curr.execute('''UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
                    data2 = '''UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
                    curr.execute(data2, [gex4, gex5, var4, name])
                    conn.commit()
                    print("exchange complete, you were charged 1.3% upon exchange")
                    conn.close()
                    send_mail_for_currency_exchange(var4, email)


def CurrencyExchange_CNY(name=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    c = CurrencyRates()
    var5 = "CNY"
    gbc = "USD"
    hex5 = c.get_rate(gbc, var5)
    hex6 = c.get_rate(gbc, var5)
    rate_r = 0.013
    r_data1 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE name=?'''
    r_data2 = '''SELECT email, Checking, Saving, Currency from CreditAccounts WHERE name=?'''
    # r_data3 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE CardCode=?'''
    curr.execute(r_data1, name)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if name == row1[0]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('''UPDATE DebitAccounts SET Current=Current-? WHERE name=?''', [checking_fee, name])
            curr.execute('''UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
            curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
            curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
            data1 = '''UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
            curr.execute(data1, [hex5, hex6, var5, name])
            conn.commit()
            print("exchange complete, you were charged 1.3% upon exchange")
            conn.close()
            send_mail_for_currency_exchange(var5, email)
        else:
            curr.execute(r_data2, name)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if name == row2[0]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('''UPDATE CreditAccounts SET Current=Current-? WHERE name=?''',
                                 [checking_fee, name])
                    curr.execute('''UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
                    data2 = '''UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
                    curr.execute(data2, [hex5, hex6, var5, name])
                    conn.commit()
                    print("exchange complete, you were charged 1.3% upon exchange")
                    conn.close()
                    send_mail_for_currency_exchange(var5, email)


def CurrencyExchange_JPY(name=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    c = CurrencyRates()
    var6 = "JPY"
    gbc = "USD"
    hex6 = c.get_rate(gbc, var6)
    hex7 = c.get_rate(gbc, var6)
    rate_r = 0.013
    r_data1 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE name=?'''
    r_data2 = '''SELECT email, Checking, Saving, Currency from CreditAccounts WHERE name=?'''
    # r_data3 = '''SELECT email, Checking, Saving, Currency from DebitAccounts WHERE CardCode=?'''
    curr.execute(r_data1, name)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if name == row1[0]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute(''''UPDATE DebitAccounts SET Current=Current-? WHERE name=?''', [checking_fee, name])
            curr.execute('''UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
            curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOVBank''', [rate_r])
            curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank''', [rate_r])
            data1 = '''UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
            curr.execute(data1, [hex6, hex7, var6, name])
            conn.commit()
            print("exchange complete, you were charged 1.3% upon exchange")
            conn.close()
            send_mail_for_currency_exchange(var6, email)
        else:
            curr.execute(r_data2, name)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if name == row2[0]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('''UPDATE CreditAccounts SET Current=Current-? WHERE name=?''',
                                 [checking_fee, name])
                    curr.execute('''UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?''', [saving_fee, name])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Current=Current+? WHERE name=INOV Bank''', [rate_r])
                    curr.execute('''UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOV Bank''', [rate_r])
                    data2 = '''UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?'''
                    curr.execute(data2, [hex6, hex7, var6, name])
                    conn.commit()
                    print("exchange complete, you were charged 1.3% upon exchange")
                    conn.close()
                    send_mail_for_currency_exchange(var6, email)


# line 921 and above STATUS: Complete

# global transactions
# 1. North America,  2. Europe, 3. South America, 4. Africa, 5. Asia, 6. Caribbean, 7. Central America
# USD base currency
# 1. North America
def global_transactions_NA(region=int, val=float, curname=str, name=str, name2=str):
    c = CurrencyRates()
    # North America
    if region == "1":
        # reg = "North America"
        if curname == "Canada":
            cur = 'USD'
            cur2 = 'CAD'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Mexico":
            cur = 'USD'
            cur2 = 'MXN'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)


# 2. Europe
def global_transactions_EU(region=int, val=int, curname=str, name=str, name2=str):
    c = CurrencyRates()
    if region == "2":
        # reg = "Europe"
        if curname == "UK":
            cur = 'USD'
            cur2 = 'GBP'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Germany":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "France":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Italy":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Spain":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Netherlands":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Switzerland":
            cur = 'USD'
            cur2 = 'CHF'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Poland":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Sweden":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Russia":
            cur = 'USD'
            cur2 = 'RUB'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)


# South America
def global_transactions_SA(region=int, val=float, curname=str, name=str, name2=str):
    c = CurrencyRates()
    if region == "3":
        # reg = "South America"
        if curname == "Argentina":
            cur = 'USD'
            cur2 = 'ARS'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Bolivia":
            cur = 'USD'
            cur2 = 'BOB'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Brazil":
            cur = 'USD'
            cur2 = 'BRL'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Chile":
            cur = 'USD'
            cur2 = 'CLP'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Colombia":
            cur = 'USD'
            cur2 = 'COP'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Peru":
            cur = 'USD'
            cur2 = 'PEN'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Ecuador":
            # cur = 'USD'
            # cur2 = 'PEN'
            # link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(val, name, name2)
        if curname == "Venezuela":
            cur = 'USD'
            cur2 = 'VES'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Uruguay":
            cur = 'USD'
            cur2 = 'UYU'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)


# Africa
def global_transactions_Africa(region=int, val=float, curname=str, name=str, name2=str):
    c = CurrencyRates()
    if region == "4":
        # reg = "Africa"
        if curname == "Nigeria":
            cur = 'USD'
            cur2 = 'NGN'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "South Africa":
            reg = "Africa"
            cur = 'USD'
            cur2 = 'ZAR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Egypt":
            cur = 'USD'
            cur2 = 'EGP'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Algeria":
            cur = 'USD'
            cur2 = 'DZD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Morocco":
            cur = 'USD'
            cur2 = 'MAD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Kenya":
            cur = 'USD'
            cur2 = 'KES'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Ethiopia":
            cur = 'USD'
            cur2 = 'ETB'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
        if curname == "Ghana":
            cur = 'USD'
            cur2 = 'GHS'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Angola":
            cur = 'USD'
            cur2 = 'AOA'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Tanzania":
            cur = 'USD'
            cur2 = 'TZS'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Ivory Coast":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Cameroon":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)


# Asia
def global_transactions_Asia_Middle_east(region=int, val=float, curname=str, name=str, name2=str):
    c = CurrencyRates()
    if region == "5":
        # reg = "Asia/Middle East"
        if curname == "China":
            cur = 'USD'
            cur2 = 'CNY'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Japan":
            cur = 'USD'
            cur2 = 'JPY'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "India":
            cur = 'USD'
            cur2 = 'INR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "South Korea":
            cur = 'USD'
            cur2 = 'KRW'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Indonesia":
            cur = 'USD'
            cur2 = 'IDR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Saudi Arabia":
            cur = 'USD'
            cur2 = 'SAR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Taiwan":
            cur = 'USD'
            cur2 = 'TWD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Thailand":
            cur = 'USD'
            cur2 = 'THB'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "UAE":
            cur = 'USD'
            cur2 = 'AED'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Israel":
            cur = 'USD'
            cur2 = 'ILS'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Philippines":
            cur = 'USD'
            cur2 = 'PHP'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Hong Kong":
            cur = 'USD'
            cur2 = 'HKD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Singapore":
            cur = 'USD'
            cur2 = 'SGD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Malaysia":
            cur = 'USD'
            cur2 = 'MYR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Bangladesh":
            cur = 'USD'
            cur2 = 'BDT'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Vietnam":
            cur = 'USD'
            cur2 = 'VND'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)


# Caribbean
def global_transactions_Caribbean(region=int, val=float, curname=str, name=str, name2=str):
    c = CurrencyRates()
    if region == "6":
        # reg = "Caribbean"
        if curname == "Antigua":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Bahamas":
            cur = 'USD'
            cur2 = 'BSD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Belize":
            cur = 'USD'
            cur2 = 'BZD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Dominica":
            cur = 'USD'
            cur2 = 'DOP'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Grenada":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Guyana":
            cur = 'USD'
            cur2 = 'GYD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Jamaica":
            cur = 'USD'
            cur2 = 'JMD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Puerto Rico":
            # cur = 'USD'
            # cur2 = 'GYD'
            # link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(val, name, name2)
        if curname == "St. Kitts and Nevis":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "St. Lucia":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "St. Vincent & Grenadines":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Suriname":
            cur = 'USD'
            cur2 = 'SRD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Trinidad & Tobago":
            cur = 'USD'
            cur2 = 'TTD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)


# Central America
def global_transactions_CA(region=int, val=float, curname=str, name=str, name2=str):
    c = CurrencyRates()
    if region == "7":
        # reg = "Central America"
        if curname == "Guatemala":
            cur = 'USD'
            cur2 = 'GTQ'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Panama":
            cur = 'USD'
            cur2 = 'PAB'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Costa Rica":
            cur = 'USD'
            cur2 = 'CRC'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "El Salvador":
            # cur = 'USD'
            # cur2 = 'PAB'
            # link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(val, name, name2)
        if curname == "Honduras":
            cur = 'USD'
            cur2 = 'HNL'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)
        if curname == "Nicaragua":
            cur = 'USD'
            cur2 = 'NIO'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            send_money(link, name, name2)


# email notifications
def send_mail_for_new_pin(p=int, mz=str):
    msg = "{} this is your Temporary password. Please use it to login and get a new DCL"
    new = (msg.format(p))

    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = mz
    password = "ladfpscfaupnptmn"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()
        return 'ok the email has sent '


def send_mail_for_currency_exchange(curr=str, mz=str):
    msg = "you recently change the currency in which your account is in to {}."
    new = (msg.format(curr))

    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = mz
    password = "ladfpscfaupnptmn"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()
        return 'ok the email has sent '


def send_mail_for_newCrypt(Cryp=str, mz=str):
    msg = "{} this is your Digital Credit Code Please memorize the last 6 digits"
    new = (msg.format(Cryp))

    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = mz
    password = "ladfpscfaupnptmn"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()
        return 'ok the email has sent '


def send_mail_for_Transactions(n=str, mail=str, amt=int()):
    email = mail
    trans = amt
    name = n

    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = email
    password = "ladfpscfaupnptmn"
    message = "You have received $" + trans + " from " + name
    # Gmail Accounts
    if "gmail" in email:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in email:
        fromMy = "openbank143@yahoo.com"
        to = email
        subj = 'Transaction'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = " uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()


def send_mail_for_new_account(m2=str, text=str):
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = m2
    password = "ladfpscfaupnptmn"
    message = text
    # Gmail Accounts
    if "gmail" in m2:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        # print("login success")
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in m2:
        fromMy = "openbank143@yahoo.com"
        to = m2
        subj = 'NEW ACCOUNT!!!!!'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()
        return 'ok the email has sent '


def send_mail_for_deposits_checking(depo=int(), m3=str):
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = m3
    password = "ladfpscfaupnptmn"
    message = "You just made a deposit into your Current account of $ " + [{depo}]
    # Gmail Accounts
    if "gmail" in m3:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in m3:
        fromMy = "openbank143@yahoo.com"
        to = m3
        subj = 'Current account Deposit'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()


def send_mail_for_deposits_saving(depo2=int(), m4=str):
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = m4
    password = "ladfpscfaupnptmn"
    message = "You just made a deposit into your savings account of $ " + [{depo2}]
    # Gmail Accounts
    if "gmail" in m4:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in m4:
        fromMy = "openbank143@yahoo.com"
        to = m4
        subj = 'Savings account Deposit'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = " uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()


def send_mail_for_processed_payment(m4=str, email=str):
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = email
    password = "ladfpscfaupnptmn"
    message = m4
    # Gmail Accounts
    if "gmail" in email:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        server.close()
    # Yahoo Accounts
    if "yahoo" in email:
        fromMy = "openbank143@yahoo.com"
        to = email
        subj = 'PAYMENT ORDER'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = " uskgkpnokoilawmt"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        server.close()
