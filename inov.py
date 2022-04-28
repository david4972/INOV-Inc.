from data import get_database
from forex_python.converter import CurrencyRates
from cryptography.fernet import Fernet
import smtplib
import ccard


def intro():
    text = "WELCOME TO INOV!!!!!! We are a Saas startup that build creative, innovative and simpler " \
           "apis for more transparent financial services. " \
           "We only operate in the US as of right now but we look to expand."
    return text


# CODE STATUS: Complete
# Create Accounts STATUS: Complete
# create Business Credit Account
def create_business_account(account_name=str, email=str, address=str):
    db = get_database()
    curr = db.cursor()
    country = "USA"
    Curr = "USD"
    priv = ccard.americanexpress()
    to_string = str(priv)
    CardNo = to_string[:5]
    Security = Fernet.generate_key()
    Crypt = Security[:5]
    f = Fernet(Crypt)
    CardCode = f.encrypt(CardNo)
    business_type = input("what Industry does your business operate in:")
    Credit_Checking_amt = int(input('How much do you want to deposit into your Business Credit Checkings account p.s. '
                                    'min deposit is. 50,000 '
                                    'required max '
                                    'deposit is '
                                    '100,000: '))
    if Credit_Checking_amt > 100000 or Credit_Checking_amt < 50000:
        print("deposit does not meet requirement, try again")
    Credit_Savings_amt = int(
        input('How much do you want to deposit into your Business Credit Savings account p.s. min deposit is 150,000'
              'required max '
              'deposit is '
              '500,000: '))
    if Credit_Savings_amt > 500000 or Credit_Savings_amt < 150000:
        print("deposit does not meet requirement, try again")

        read_data = "INSERT INTO B-CreditAccounts (name, email, industry, CardNo, CardCode, SecurityCode, Checking, " \
                    "Saving, " \
                    "Address, " \
                    "Country, " \
                    "Currency) " \
                    "VALUES ( " \
                    "?, " \
                    "?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        val = (account_name, email, business_type, CardNo, CardCode, Security, Credit_Checking_amt, Credit_Savings_amt,
               address,
               country, Curr)
        curr.execute(read_data, val)
        curr.commit()
        dclNo = 'Congrats on your new Business Credit account!!! This -> {}  is your secured Business credit card ' \
                'number, this number ' \
                'will ' \
                'be your main account charged with ' \
                'most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        msg = dclNo.format(CardNo)
        send_mail_for_new_account(email, msg)
        return True


# create Credit Account
def create_Credit_account(account_name=str, email=str, address=str):
    db = get_database()
    curr = db.cursor()
    country = "USA"
    Curr = "USD"
    priv = ccard.americanexpress()
    to_string = str(priv)
    CardNo = to_string[:5]
    Security = Fernet.generate_key()
    Crypt = Security[:5]
    f = Fernet(Crypt)
    CardCode = f.encrypt(CardNo)
    Credit_Checking_amt = int(input('How much do you want to deposit into your Credit Checkings account p.s. no '
                                    'min deposit '
                                    'required max '
                                    'deposit is '
                                    '5,000: '))
    if Credit_Checking_amt > 5000 or Credit_Checking_amt < 0:
        print("deposit does not meet requirement, try again")
    Credit_Savings_amt = int(
        input('How much do you want to deposit into your Credit Savings account p.s. no min deposit '
              'required max '
              'deposit is '
              '15,000: '))
    if Credit_Savings_amt > 15000 or Credit_Savings_amt < 0:
        print("deposit does not meet requirement, try again")
        read_data = "INSERT INTO CreditAccounts (name, email, CardNo, CardCode, SecurityCode, Checking, " \
                    "Saving, " \
                    " Address, Country, " \
                    "Currency) " \
                    "VALUES ( " \
                    "?, " \
                    "?, ?, ?, ?, ?, ?, ?, ?, ?) "
        val = (account_name, email, CardNo, CardCode, Security, Credit_Checking_amt, Credit_Savings_amt,
               address,
               country, Curr)
        curr.execute(read_data, val)
        curr.commit()
        dclNo = 'Congrats on your new Business Credit account!!! This -> {}  is your secured Business credit card ' \
                'number, this number ' \
                'will ' \
                'be your main account charged with ' \
                'most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        msg = dclNo.format(CardNo)
        send_mail_for_new_account(email, msg)
        return True


# create Debit Account
def create_Debit_account(account_name=str, email=str, address=str):
    db = get_database()
    curr = db.cursor()
    country = "USA"
    Curr = "USD"
    priv = ccard.americanexpress()
    to_string = str(priv)
    CardNo = to_string[:5]
    Security = Fernet.generate_key()
    Crypt = Security[:5]
    f = Fernet(Crypt)
    CardCode = f.encrypt(CardNo)
    Debit_Checking = int(input('How much do you want to deposit into this account p.s. no min deposit required max '
                               'deposit is '
                               '5,000: '))
    if Debit_Checking > 5000 or Debit_Checking < 0:
        print("deposit does not meet requirement, try again")
    Debit_Saving = int(input('How much do you want to deposit into this account p.s. no min deposit required max '
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
        val = (account_name, email, CardNo, CardCode, Security, Debit_Checking, Debit_Saving,
               address,
               country, Curr)
        curr.execute(read_data, val)
        curr.commit()
        dclNo = 'Congrats on your new Business Credit account!!! This -> {}  is your secured Business credit card ' \
                'number, this number ' \
                'will ' \
                'be your main account charged with ' \
                'most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        msg = dclNo.format(CardNo)
        send_mail_for_new_account(email, msg)
        return True


# Deposits STATUS: Complete
def deposit_option(name=str, deposit=int, ans=str, CardCode=str):
    if ans == "1":
        deposit_Checking(name, deposit, CardCode)
        return "processing deposit"

    if ans == "2":
        deposit_Savings(name, deposit)
        return "processing deposit"


def deposit_Checking(name=str, deposit=int, CardCode=str):
    db = get_database()
    curr = db.cursor()
    read_data1 = "SELECT * from DebitAccounts where CardCode=? where name=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    curr.execute(read_data1, [CardCode, name])
    for row in curr.fetchall(CardCode, name):
        email = row[1]
        if name == row[0]:
            if CardCode == row[3]:
                # processing transaction
                transaction = "UPDATE DebitAccounts SET Checking=Checking+? WHERE CardCode=?"
                curr.execute(transaction, [deposit, CardCode])
                curr.commit()  # completing transaction
                send_mail_for_deposits_checking(deposit, email)
    else:
        curr.execute(read_data2, CardCode)
        for row in curr.fetchall(CardCode):
            email2 = row[1]
            if name == row[0]:
                if CardCode == row[3]:
                    # processing transaction
                    transaction = "UPDATE DebitAccounts SET Checking=Checking+? WHERE CardCode=?"
                    curr.execute(transaction, [deposit, CardCode])
                    curr.commit()  # completing transaction
                    send_mail_for_deposits_checking(deposit, email2)
    return "deposit complete"


def deposit_Savings(name=str, deposit=int, CardCode=str):
    # send_mail_for_deposits_saving(dep, email)
    db = get_database()
    curr = db.cursor()
    read_data1 = "SELECT * from DebitAccounts where CardCode=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=?"
    curr.execute(read_data1, CardCode)
    for row in curr.fetchall(CardCode):
        email = row[1]
        if name == row[0]:
            if CardCode == row[3]:
                # processing transaction
                transaction = "UPDATE DebitAccounts SET Saving=Saving+? WHERE CardCode=?"
                curr.execute(transaction, [deposit, CardCode])
                curr.commit()  # completing transaction
                send_mail_for_deposits_saving(deposit, email)
    else:
        curr.execute(read_data2, CardCode)
        for row in curr.fetchall(CardCode):
            email2 = row[1]
            if name == row[0]:
                if CardCode == row[3]:
                    # processing transaction
                    transaction = "UPDATE CreditAccounts SET Saving=Saving+? WHERE CardCode=?"
                    curr.execute(transaction, [deposit, CardCode])
                    curr.commit()  # completing transaction
                    send_mail_for_deposits_saving(deposit, email2)
    return "deposit complete"


def atm_option(CardCode=str, var=str, withdraw=int):
    if var == "Checkings":
        atm_Checking(CardCode, withdraw)

    if var == "Savings":
        atm_Savings(CardCode, withdraw)

    return "ATM processing, You will be charged 1.3% upon withdrawal."


def atm_Checking(CardCode=str, withdraw=int):
    db = get_database()
    curr = db.cursor()
    bank = "INOV"
    rate_r = 0.013
    read_data1 = "SELECT * from DebitAccounts where CardCode=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    curr.execute(read_data1, CardCode)
    for row in curr.fetchall(CardCode):
        email = row[1]
        checking = row[5]
        if CardCode == row[3]:
            service = checking * rate_r
            transaction = "UPDATE DebitAccounts SET Checking=Checking-?, WHERE CardCode=?"
            curr.execute(transaction, [withdraw, CardCode])
            curr.commit()
            fee = "UPDATE DebitAccounts SET Checking=Checking-?, WHERE CardCode=?"
            curr.execute(fee, [service, CardCode])
            curr.commit()
            serv = "UPDATE B-CreditAccounts SET Checking=Checking+?, WHERE name=?"
            curr.execute(serv, [service, bank])
            # send notif
        else:
            curr.execute(read_data2, CardCode)
            for row2 in curr.fetchall(CardCode):
                email = row2[1]
                checking = row[5]
                if CardCode == row2[3]:
                    service = checking * rate_r
                    transaction = "UPDATE CreditAccounts SET Checking=Checking-?, WHERE CardCode=?"
                    curr.execute(transaction, [withdraw, CardCode])
                    curr.commit()
                    fee = "UPDATE CreditAccounts SET Checking=Checking-?, WHERE CardCode=?"
                    curr.execute(fee, [service, CardCode])
                    curr.commit()
                    serv = "UPDATE B-CreditAccounts SET Checking=Checking+?, WHERE name=?"
                    curr.execute(serv, [service, bank])
                    # send notif
    return "Withdrawal Complete"


def atm_Savings(CardCode=str, withdraw=int):
    db = get_database()
    curr = db.cursor()
    bank = "INOV"
    rate_r = 0.013
    read_data1 = "SELECT * from DebitAccounts where CardCode=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    curr.execute(read_data1, CardCode)
    for row in curr.fetchall(CardCode):
        email = row[1]
        saving = row[6]
        if CardCode == row[3]:
            service = saving * rate_r
            transaction = "UPDATE DebitAccounts SET Saving=Saving-?, WHERE CardCode=?"
            curr.execute(transaction, [withdraw, CardCode])
            curr.commit()
            fee = "UPDATE DebitAccounts SET Saving=Saving-?, WHERE CardCode=?"
            curr.execute(fee, [service, CardCode])
            curr.commit()
            serv = "UPDATE B-CreditAccounts SET Saving=Saving+?, WHERE name=?"
            curr.execute(serv, [service, bank])
            # send notif
        else:
            curr.execute(read_data2, CardCode)
            for row2 in curr.fetchall(CardCode):
                email = row2[1]
                saving = row[6]
                if CardCode == row2[3]:
                    service = saving * rate_r
                    transaction = "UPDATE CreditAccounts SET Saving=Saving-?, WHERE CardCode=?"
                    curr.execute(transaction, [withdraw, CardCode])
                    curr.commit()
                    fee = "UPDATE CreditAccounts SET Saving=Saving-?, WHERE CardCode=?"
                    curr.execute(fee, [service, CardCode])
                    curr.commit()
                    serv = "UPDATE B-CreditAccounts SET Saving=Saving+?, WHERE name=?"
                    curr.execute(serv, [service, bank])
                    # send notif
    return "Withdrawal Complete"


"""""
def reactivate_account(name=str, Security=str):
    db = get_database()
    curr = db.cursor()
    read_data = "SELECT * from DebitAccounts WHERE SecurityCode=?"
    curr.execute(read_data, Security)
    for row in curr.fetchall(Security):
        email = row[2]
        if Security == row[6]:
            country = "USA"
            Curr = "USD"
            priv = ccard.americanexpress()
            to_string = str(priv)
            CardNo = to_string[:5]
            Security = Fernet.generate_key()
            Crypt = Security[:5]
            f = Fernet(Crypt)
            CardCode = f.encrypt(CardNo)
            secure =  'UPDATE InovClientsData SET SecurityCode=? WHERE name=?'
            curr.execute(secure, Security)
            curr.commit()
            code = 'UPDATE InovClientsData SET CardCode=? WHERE name=?'
            curr.execute(code, CardCode)
            curr.commit()
            Cou = 'UPDATE InovClientsData SET Country=? WHERE name=?'
            curr.execute(Cou, country
            currenc = 'UPDATE InovClientsData SET Currency=? WHERE name=?'
            curr.execute(currenc, curr)
            dclNo = '{} this is your secured credit code, this number will be your main account charged with most ' \
           'transactions you make.' \
           'This is to ensure safer payment and build a more secure wall around your credit.'
            # print(dclNo.format(Crypt))
   # Personal Credit & Debit Account
   pcd.execute('UPDATE InovClientsJointAccountData SET DCL=? WHERE name=?', [c_value, name])
   pcd.execute('UPDATE InovClientsJointAccountData SET SDC=? WHERE name=?', [scd, name])
   # Business Credit Account
   cd.execute('UPDATE InovClientsBusiness SET DCL=? WHERE name=?', [c_value, name])
   cd.execute('UPDATE InovClientsBusiness SET SDC=? WHERE name=?', [scd, name])
   data_d.close()
   pcd.close()
   cd.close()
   # send_mail_for_new_Crypt(Crypt, email)
   # IFP.intro()
    """""


def send_money(amount=int, CardCode=str, recipient=str):
    db = get_database()
    curr = db.cursor()
    rate_r = 0.013
    read_data1 = "SELECT * from DebitAccounts where CardCode=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    read_data3 = "SELECT * from B-CreditAccounts where CardCode=?"
    curr.execute(read_data1, CardCode)
    for row1 in curr.fetchall(CardCode):
        name = row1[0]
        # email = row1[1]
        checking = row1[5]
        if CardCode == row1[3]:
            fee = checking * rate_r
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [fee])
            curr.commit()
            # processing transaction
            retrieve = "UPDATE DebitAccounts SET Checking=Checking-? CardCode=?"
            curr.execute(retrieve, [amount, CardCode])
            curr.commit()
            process = "SELECT * from DebitAccounts where name=?"
            curr.execute(process, recipient)
            for row2 in curr.fetchall(recipient):
                email = row2[0]
                if recipient == row2[0]:
                    send = "UPDATE DebitAccounts SET Checking=Checking+? where name=?"
                    curr.execute(send, [amount, recipient])  # completing transaction
                    curr.commit()
                    send_mail_for_Transactions(name, email, amount)
        else:
            curr.execute(read_data2, CardCode)
            for row3 in curr.fetchall(CardCode):
                name = row3[0]
                # email = row3[1]
                checking = row3[5]
                if CardCode == row3[3]:
                    fee = checking * rate_r
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [fee])
                    curr.commit()
                    # processing transaction
                    retrieve = "UPDATE CreditAccounts SET Checking=Checking-? CardCode=?"
                    curr.execute(retrieve, [amount, CardCode])
                    curr.commit()
                    process = "SELECT * from CreditAccounts where name=?"
                    curr.execute(process, recipient)
                    for row4 in curr.fetchall(recipient):
                        email = row4[0]
                        if recipient == row4[0]:
                            send = "UPDATE CreditAccounts SET Checking=Checking+? where name=?"
                            curr.execute(send, [amount, recipient])  # completing transaction
                            curr.commit()
                            send_mail_for_Transactions(name, email, amount)
    else:
        curr.execute(read_data3, CardCode)
        for row5 in curr.fetchall(CardCode):
            name = row5[0]
            # email = row5[1]
            checking = row5[5]
            if CardCode == row5[3]:
                fee = checking * rate_r
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [fee])
                curr.commit()
                # processing transaction
                retrieve = "UPDATE DebitAccounts SET Checking=Checking-? CardCode=?"
                curr.execute(retrieve, [amount, CardCode])
                curr.commit()
                process = "SELECT * from DebitAccounts where name=?"
                curr.execute(process, recipient)
                for row6 in curr.fetchall(recipient):
                    email = row6[0]
                    if recipient == row6[0]:
                        send = "UPDATE DebitAccounts SET Checking=Checking+? where name=?"
                        curr.execute(send, [amount, recipient])  # completing transaction
                        curr.commit()
                        send_mail_for_Transactions(name, email, amount)
    return "transaction complete"


'''
def business_loan_checking(bl1=int, n3=str):
   cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=?', [bl1, n3])
   cd.close()


def business_loan_savings(bl2=int, n4=str):
   cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=?', [bl2, n4])
   cd.close()


def personal_loan_checking(bl3=int, n5=str):
   data_d.execute('UPDATE InovClientsData SET Current=Current+? WHERE name=?', [bl3, n5])
   pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking+? WHERE name=?', [bl3, n5])
   data_d.close()
   pcd.close()


def personal_loan_savings(bl4=int, n6=str):
   data_d.execute('UPDATE InovClientsData SET Saving=Saving+? WHERE name=?', [bl4, n6])
   pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving+? WHERE name=?', [bl4, n6])
   data_d.close()
   pcd.close()
'''


def bank_statement(name=str, CardCode=str):
    db = get_database()
    curr = db.cursor()
    read_data1 = "SELECT * from DebitAccounts where CardCode=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    read_data3 = "SELECT * from B-CreditAccounts where CardCode=?"
    curr.execute(read_data1, CardCode)
    for row1 in curr.fetchall(CardCode):
        email = row1[1]
        if name == row1[0]:
            if CardCode == row1[3]:
                statement = curr.execute("SELECT name, Checking, Saving, Currency from DebitAccounts where CardCode=?")
                result = {'Your Bank Statement': [dict(zip(tuple(statement.keys()), i)) for i in statement.cursor]}

        else:
            curr.execute(read_data2, CardCode)
            for row2 in curr.fetchall(CardCode):
                email = row2[1]
                if name == row2[0]:
                    if CardCode == row2[3]:
                        statement = curr.execute(
                            "SELECT name, Checking, Saving, Currency from CreditAccounts where CardCode=?")
                        result = {
                            'Your Bank Statement': [dict(zip(tuple(statement.keys()), i)) for i in statement.cursor]}

    else:
        curr.execute(read_data3, CardCode)
        for row3 in curr.fetchall(CardCode):
            email = row3[1]
            if name == row3[0]:
                if CardCode == row3[3]:
                    statement = curr.execute(
                        "SELECT name, Checking, Saving, Currency from B-CreditAccounts where CardCode=?")
                    result = {
                        'Your Bank Statement': [dict(zip(tuple(statement.keys()), i)) for i in statement.cursor]}
    # return "bank statement has been sent to email"


# Currency change (allows account users to convert currency cash account into the main global currencies (USD, EUR,
# GBP, CNY)
def CurrencyExchange_USD(name=str, CardCode=str, gbc=str):
    db = get_database()
    curr = db.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = gbc
    cex1 = c.get_rate(var2, var1)
    cex2 = c.get_rate(var2, var1)
    rate_r = 0.013
    r_data1 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data2 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data3 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    curr.execute(r_data1, CardCode)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardCode == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('UPDATE DebitAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
            curr.execute('UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
            curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
            curr.commit()
            data1 = "UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
            curr.execute(data1, [cex1, cex2, var1, name])
            curr.commit()
            send_mail_for_currency_exchange(CardCode, email)
        else:
            curr.execute(r_data2, CardCode)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardCode == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                                 [checking_fee, CardCode])
                    curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                    curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                    curr.commit()
                    data2 = "UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                    curr.execute(data2, [cex1, cex2, var1, name])
                    curr.commit()
                    send_mail_for_currency_exchange(CardCode, email)
    else:
        curr.execute(r_data3, CardCode)
        for row3 in curr.fetchall():
            email = row3[1]
            Checking_balance = row3[5]
            Saving_balance = row3[6]
            if CardCode == row3[3]:
                checking_fee = Checking_balance * rate_r
                saving_fee = Saving_balance * rate_r
                curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                             [checking_fee, CardCode])
                curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                curr.commit()
                data3 = "UPDATE B-CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                curr.execute(data3, [cex1, cex2, var1, name])
                curr.commit()
                send_mail_for_currency_exchange(CardCode, email)
    # return "exchange complete, you were charged 1.3% upon exchange"


def CurrencyExchange_EUR(name=str, CardCode=str):
    db = get_database()
    curr = db.cursor()
    c = CurrencyRates()
    var2 = "EUR"
    gbc = "USD"
    dex1 = c.get_rate(gbc, var2)
    dex2 = c.get_rate(gbc, var2)
    rate_r = 0.013
    r_data1 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data2 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data3 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    curr.execute(r_data1, CardCode)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardCode == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('UPDATE DebitAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
            curr.execute('UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
            curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
            curr.commit()
            data1 = "UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
            curr.execute(data1, [dex1, dex2, var2, name])
            curr.commit()
            send_mail_for_currency_exchange(CardCode, email)
        else:
            curr.execute(r_data2, CardCode)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardCode == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                                 [checking_fee, CardCode])
                    curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                    curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                    curr.commit()
                    data2 = "UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                    curr.execute(data2, [dex1, dex2, var2, name])
                    curr.commit()
                    send_mail_for_currency_exchange(CardCode, email)
    else:
        curr.execute(r_data3, CardCode)
        for row3 in curr.fetchall():
            email = row3[1]
            Checking_balance = row3[5]
            Saving_balance = row3[6]
            if CardCode == row3[3]:
                checking_fee = Checking_balance * rate_r
                saving_fee = Saving_balance * rate_r
                curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
                curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                curr.commit()
                data3 = "UPDATE B-CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                curr.execute(data3, [dex1, dex2, var2, name])
                curr.commit()
                send_mail_for_currency_exchange(CardCode, email)

    # return "exchange complete, you were charged 1.3% upon exchange"


def CurrencyExchange_GBP(name=str, CardCode=str):
    db = get_database()
    curr = db.cursor()
    c = CurrencyRates()
    var3 = "GBP"
    gbc = "USD"
    fex3 = c.get_rate(gbc, var3)
    fex4 = c.get_rate(gbc, var3)
    rate_r = 0.013
    r_data1 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data2 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data3 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    curr.execute(r_data1, CardCode)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardCode == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('UPDATE DebitAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
            curr.execute('UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
            curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
            curr.commit()
            data1 = "UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
            curr.execute(data1, [fex3, fex4, var3, name])
            curr.commit()
            send_mail_for_currency_exchange(CardCode, email)
        else:
            curr.execute(r_data2, CardCode)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardCode == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                                 [checking_fee, CardCode])
                    curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                    curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                    curr.commit()
                    data2 = "UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                    curr.execute(data2, [fex3, fex4, var3, name])
                    curr.commit()
                    send_mail_for_currency_exchange(CardCode, email)
    else:
        curr.execute(r_data3, CardCode)
        for row3 in curr.fetchall():
            email = row3[1]
            Checking_balance = row3[5]
            Saving_balance = row3[6]
            if CardCode == row3[3]:
                checking_fee = Checking_balance * rate_r
                saving_fee = Saving_balance * rate_r
                curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
                curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                curr.commit()
                data3 = "UPDATE B-CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                curr.execute(data3, [fex3, fex4, var3, name])
                curr.commit()
                send_mail_for_currency_exchange(CardCode, email)

    # return "exchange complete, you were charged 1.3% upon exchange"


def CurrencyExchange_AUS(name=str, CardCode=str):
    db = get_database()
    curr = db.cursor()
    c = CurrencyRates()
    var4 = "AUS"
    gbc = "USD"
    gex4 = c.get_rate(gbc, var4)
    gex5 = c.get_rate(gbc, var4)
    rate_r = 0.013
    r_data1 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data2 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data3 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    curr.execute(r_data1, CardCode)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardCode == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('UPDATE DebitAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
            curr.execute('UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
            curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
            curr.commit()
            data1 = "UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
            curr.execute(data1, [gex4, gex5, var4, name])
            curr.commit()
            send_mail_for_currency_exchange(CardCode, email)
        else:
            curr.execute(r_data2, CardCode)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardCode == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                                 [checking_fee, CardCode])
                    curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                    curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                    curr.commit()
                    data2 = "UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                    curr.execute(data2, [gex4, gex5, var4, name])
                    curr.commit()
                    send_mail_for_currency_exchange(CardCode, email)
    else:
        curr.execute(r_data3, CardCode)
        for row3 in curr.fetchall():
            email = row3[1]
            Checking_balance = row3[5]
            Saving_balance = row3[6]
            if CardCode == row3[3]:
                checking_fee = Checking_balance * rate_r
                saving_fee = Saving_balance * rate_r
                curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
                curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                curr.commit()
                data3 = "UPDATE B-CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                curr.execute(data3, [gex4, gex5, var4, name])
                curr.commit()
                send_mail_for_currency_exchange(CardCode, email)

    # return "exchange complete, you were charged 1.3% upon exchange"


def CurrencyExchange_CNY(name=str, CardCode=str):
    db = get_database()
    curr = db.cursor()
    c = CurrencyRates()
    var5 = "CNY"
    gbc = "USD"
    hex5 = c.get_rate(gbc, var5)
    hex6 = c.get_rate(gbc, var5)
    rate_r = 0.013
    r_data1 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data2 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data3 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    curr.execute(r_data1, CardCode)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardCode == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('UPDATE DebitAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
            curr.execute('UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
            curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
            curr.commit()
            data1 = "UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
            curr.execute(data1, [hex5, hex6, var5, name])
            curr.commit()
            send_mail_for_currency_exchange(CardCode, email)
        else:
            curr.execute(r_data2, CardCode)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardCode == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                                 [checking_fee, CardCode])
                    curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                    curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                    curr.commit()
                    data2 = "UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                    curr.execute(data2, [hex5, hex6, var5, name])
                    curr.commit()
                    send_mail_for_currency_exchange(CardCode, email)
    else:
        curr.execute(r_data3, CardCode)
        for row3 in curr.fetchall():
            email = row3[1]
            Checking_balance = row3[5]
            Saving_balance = row3[6]
            if CardCode == row3[3]:
                checking_fee = Checking_balance * rate_r
                saving_fee = Saving_balance * rate_r
                curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
                curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                curr.commit()
                data3 = "UPDATE B-CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                curr.execute(data3, [hex5, hex6, var5, name])
                curr.commit()
                send_mail_for_currency_exchange(CardCode, email)

    # return "exchange complete, you were charged 1.3% upon exchange"


def CurrencyExchange_JPY(name=str, CardCode=str):
    db = get_database()
    curr = db.cursor()
    c = CurrencyRates()
    var6 = "JPY"
    gbc = "USD"
    hex6 = c.get_rate(gbc, var6)
    hex7 = c.get_rate(gbc, var6)
    rate_r = 0.013
    r_data1 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data2 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    r_data3 = "SELECT email, Checking, Saving, Currency from DebitAccounts where CardCode=?"
    curr.execute(r_data1, CardCode)
    for row1 in curr.fetchall():
        email = row1[1]
        Checking_balance = row1[5]
        Saving_balance = row1[6]
        if CardCode == row1[3]:
            checking_fee = Checking_balance * rate_r
            saving_fee = Saving_balance * rate_r
            curr.execute('UPDATE DebitAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
            curr.execute('UPDATE DebitAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
            curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
            curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
            curr.commit()
            data1 = "UPDATE DebitAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
            curr.execute(data1, [hex6, hex7, var6, name])
            curr.commit()
            send_mail_for_currency_exchange(CardCode, email)
        else:
            curr.execute(r_data2, CardCode)
            for row2 in curr.fetchall():
                email = row2[1]
                Checking_balance = row2[5]
                Saving_balance = row2[6]
                if CardCode == row2[3]:
                    checking_fee = Checking_balance * rate_r
                    saving_fee = Saving_balance * rate_r
                    curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?',
                                 [checking_fee, CardCode])
                    curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                    curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                    curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                    curr.commit()
                    data2 = "UPDATE CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                    curr.execute(data2, [hex6, hex7, var6, name])
                    curr.commit()
                    send_mail_for_currency_exchange(CardCode, email)
    else:
        curr.execute(r_data3, CardCode)
        for row3 in curr.fetchall():
            email = row3[1]
            Checking_balance = row3[5]
            Saving_balance = row3[6]
            if CardCode == row3[3]:
                checking_fee = Checking_balance * rate_r
                saving_fee = Saving_balance * rate_r
                curr.execute('UPDATE CreditAccounts SET Current=Current-? WHERE CardCode=?', [checking_fee, CardCode])
                curr.execute('UPDATE CreditAccounts SET Saving=Saving-? WHERE name=?', [saving_fee, CardCode])
                curr.execute('UPDATE B-CreditAccounts SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
                curr.execute('UPDATE B-CreditAccounts SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
                curr.commit()
                data3 = "UPDATE B-CreditAccounts SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?"
                curr.execute(data3, [hex6, hex7, var6, name])
                curr.commit()
                send_mail_for_currency_exchange(CardCode, email)

    # return "exchange complete, you were charged 1.3% upon exchange"


# line 921 and above STATUS: Complete

# global transactions
# 1. North America,  2. Europe, 3. South America, 4. Africa, 5. Asia, 6. Caribbean, 7. Central America
# USD base currency
# 1. North America
def global_transactions_NA(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    # North America
    if region == "1":
        # reg = "North America"
        if curname == "Canada":
            cur = 'USD'
            cur2 = 'CAD'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Mexico":
            cur = 'USD'
            cur2 = 'MXN'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
    return "Transaction processing"


# 2. Europe
def global_transactions_EU(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    if region == "2":
        # reg = "Europe"
        if curname == "UK":
            cur = 'USD'
            cur2 = 'GBP'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Germany":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "France":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Italy":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Spain":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Netherlands":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Switzerland":
            cur = 'USD'
            cur2 = 'CHF'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Poland":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Sweden":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Russia":
            cur = 'USD'
            cur2 = 'RUB'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
    return "Transaction processing"


# South America
def global_transactions_SA(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    if region == "3":
        # reg = "South America"
        if curname == "Argentina":
            cur = 'USD'
            cur2 = 'ARS'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Bolivia":
            cur = 'USD'
            cur2 = 'BOB'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Brazil":
            cur = 'USD'
            cur2 = 'BRL'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Chile":
            cur = 'USD'
            cur2 = 'CLP'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Colombia":
            cur = 'USD'
            cur2 = 'COP'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Peru":
            cur = 'USD'
            cur2 = 'PEN'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Ecuador":
            # cur = 'USD'
            # cur2 = 'PEN'
            # link = c.convert(cur2, cur, val)
            send_money(val, CardCode, name2)
        if curname == "Venezuela":
            cur = 'USD'
            cur2 = 'VES'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "Uruguay":
            cur = 'USD'
            cur2 = 'UYU'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
    return "Transaction processing"


# Africa
def global_transactions_Africa(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    if region == "4":
        # reg = "Africa"
        if curname == "Nigeria":
            cur = 'USD'
            cur2 = 'NGN'
            link = c.convert(cur, cur2, val)
            send_money(link, CardCode, name2)
        if curname == "South Africa":
            reg = "Africa"
            cur = 'USD'
            cur2 = 'ZAR'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Egypt":
            cur = 'USD'
            cur2 = 'EGP'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Algeria":
            cur = 'USD'
            cur2 = 'DZD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Morocco":
            cur = 'USD'
            cur2 = 'MAD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Kenya":
            cur = 'USD'
            cur2 = 'KES'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Ethiopia":
            cur = 'USD'
            cur2 = 'ETB'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Ghana":
            cur = 'USD'
            cur2 = 'GHS'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Angola":
            cur = 'USD'
            cur2 = 'AOA'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Tanzania":
            cur = 'USD'
            cur2 = 'TZS'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Ivory Coast":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Cameroon":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
    return "Transaction processing"


# Asia
def global_transactions_Asia_Middle_east(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    if region == "5":
        # reg = "Asia/Middle East"
        if curname == "China":
            cur = 'USD'
            cur2 = 'CNY'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Japan":
            cur = 'USD'
            cur2 = 'JPY'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "India":
            cur = 'USD'
            cur2 = 'INR'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "South Korea":
            cur = 'USD'
            cur2 = 'KRW'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Indonesia":
            cur = 'USD'
            cur2 = 'IDR'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Saudi Arabia":
            cur = 'USD'
            cur2 = 'SAR'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Taiwan":
            cur = 'USD'
            cur2 = 'TWD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Thailand":
            cur = 'USD'
            cur2 = 'THB'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "UAE":
            cur = 'USD'
            cur2 = 'AED'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Israel":
            cur = 'USD'
            cur2 = 'ILS'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Philippines":
            cur = 'USD'
            cur2 = 'PHP'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Hong Kong":
            cur = 'USD'
            cur2 = 'HKD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Singapore":
            cur = 'USD'
            cur2 = 'SGD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Malaysia":
            cur = 'USD'
            cur2 = 'MYR'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Bangladesh":
            cur = 'USD'
            cur2 = 'BDT'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Vietnam":
            cur = 'USD'
            cur2 = 'VND'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
    return "Transaction processing"


# Caribbean
def global_transactions_Caribbean(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    if region == "6":
        # reg = "Caribbean"
        if curname == "Antigua":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Bahamas":
            cur = 'USD'
            cur2 = 'BSD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Belize":
            cur = 'USD'
            cur2 = 'BZD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Dominica":
            cur = 'USD'
            cur2 = 'DOP'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Grenada":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Guyana":
            cur = 'USD'
            cur2 = 'GYD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Jamaica":
            cur = 'USD'
            cur2 = 'JMD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Puerto Rico":
            # cur = 'USD'
            # cur2 = 'GYD'
            # link = c.convert(cur2, cur, val)
            send_money(val, CardCode, name2)
        if curname == "St. Kitts and Nevis":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "St. Lucia":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "St. Vincent & Grendalines":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Suriname":
            cur = 'USD'
            cur2 = 'SRD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Trinidad & Tobago":
            cur = 'USD'
            cur2 = 'TTD'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
    return "Transaction processing"


# Central America
def global_transactions_CA(region=int, val=int, curname=str, CardCode=str, name2=str):
    c = CurrencyRates()
    if region == "7":
        # reg = "Central America"
        if curname == "Guatemala":
            cur = 'USD'
            cur2 = 'GTQ'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Panama":
            cur = 'USD'
            cur2 = 'PAB'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Costa Rica":
            cur = 'USD'
            cur2 = 'CRC'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "El Salvador":
            # cur = 'USD'
            # cur2 = 'PAB'
            # link = c.convert(cur2, cur, val)
            send_money(val, CardCode, name2)
        if curname == "Honduras":
            cur = 'USD'
            cur2 = 'HNL'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
        if curname == "Nicaragua":
            cur = 'USD'
            cur2 = 'NIO'
            link = c.convert(cur2, cur, val)
            send_money(link, CardCode, name2)
    return "Transaction complete"


'''
def loan_option(n=str, em=str, ans=str):
   if ans == "1":
       Business_loan_system(n, em)
   else:
       personal_loan_system(n, em)


def personal_loan_system(name=str, email=str):
   print("Personal loans are given at an interest rate of 1.5%")
   print("Loan amounts for range from 5,000 - 100,000")
   personal_loan = int(input("please enter loan amount: "))
   if personal_loan == 5000:
       r = 0.015
       n = 12
       p = personal_loan * (1 - (1 + r) ^ -n) / r
       result = "Your Loan has been granted INOV, you will be paying {} monthly over a 12 month " \
                "period "
       print(result.format(p))
   if 5000 > personal_loan <= 75000:
       r = 0.015
       n = 24
       p = personal_loan * (1 - (1 + r) ^ -n) / r
       result = "Your Loan has been granted INOV, you will be paying {} monthly over a 24 month " \
                "period "
       print(result.format(p))
   if 75000 > personal_loan <= 100000:
       r = 0.015
       n = 24
       p = personal_loan * (1 - (1 + r) ^ -n) / r
       result = "Your Loan has been granted from Inov Bank, you will be paying {} monthly over " \
                "a " \
                "36 month period "
       print(result.format(p))
   print("Where would you like to deposit this loan")
   print("========== (1). Current ==========")
   print("========== (2). Savings ==========")
   choice = input()
   if choice == "1":
       personal_loan_checking(personal_loan, name)
   if choice == "2":
       personal_loan_savings(personal_loan, name)

   send_mail_for_personal_loan(email, personal_loan, choice)


def Business_loan_system(name=str, email=str):
   print("Personal loans are given at an interest rate of 1.5-2.4%")
   print("Loan amounts for range from 750,000 - 2,000,000")
   personal_loan = int(input("please enter loan amount: "))
   if personal_loan == 750000:
       r = 0.015
       n = 12
       p = personal_loan * (1 - (1 + r) ^ -n) / r
       result = "Your Loan has been granted INOV, you will be paying {} monthly over a 12 month " \
                "period "
       print(result.format(p))
   if 750000 > personal_loan <= 1000000:
       r = 0.019
       n = 24
       p = personal_loan * (1 - (1 + r) ^ -n) / r
       result = "Your Loan has been granted INOV, you will be paying {} monthly over a 24 month " \
                "period "
       print(result.format(p))
   if 1000000 > personal_loan <= 200000:
       r = 0.024
       n = 36
       p = personal_loan * (1 - (1 + r) ^ -n) / r
       result = "Your Loan has been granted from Inov Bank, you will be paying {} monthly over " \
                "a " \
                "36 month period "
       print(result.format(p))
   print("Where would you like to deposit this loan")
   print("========== (1). Current ==========")
   print("========== (2). Savings ==========")
   choice = input()
   if choice == "1":
       business_loan_checking(personal_loan, name)
   if choice == "2":
       business_loan_savings(personal_loan, name)

   send_mail_for_business_loan(email, personal_loan, choice)
   '''

# email notifications
'''
def send_mail_for_personal_loan(mw=str, pl=int, c=str):
   sender_email = "openinternationalbanking@gmail.com"
   rec_email = mw
   password = "Forsure34"

   message = "You have just Received a Personal Loan from OIB that has deposited $ " + [
       {pl}] + "into your " + c + " account."
   # Gmail Accounts
   if "gmail" in mw:
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login(sender_email, password)
       print("login success")
       server.sendmail(sender_email, rec_email, message)
   # Yahoo Accounts
   if "yahoo" in mw:
       fromMy = "openbank143@yahoo.com"
       to = mw
       subj = 'Personal Loan'

       msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

       username = "openbank143@yahoo.com"
       password2 = "holiday20!"
       server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
       server.starttls()
       server.login(username, password2)
       server.sendmail(fromMy, to, msg)


def send_mail_for_business_loan(bl2=int, mt=str, c=str):
   sender_email = "openinternationalbanking@gmail.com"
   rec_email = mt
   password = "Forsure34"
   message = "You have received a Business loan from OIB that has been deposited  $" + [
       {bl2}] + "into your " + c + " account"
   # Gmail Accounts
   if "gmail" in mt:
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls()
       server.login(sender_email, password)
       print("login success")
       server.sendmail(sender_email, rec_email, message)
   # Yahoo Accounts
   if "yahoo" in mt:
       fromMy = "openbank143@yahoo.com"
       to = mt
       subj = 'Business Loan'

       msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

       username = "openbank143@yahoo.com"
       password2 = "holiday20!"
       server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
       server.starttls()
       server.login(username, password2)
       server.sendmail(fromMy, to, msg)
       '''


def send_mail_for_new_pin(p=int, mz=str):
    msg = "{} this is your Temporary password. Please use it to login and get a new DCL"
    new = (msg.format(p))

    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mz
    password = "Forsure34"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        return 'ok the email has sent '


def send_mail_for_currency_exchange(Cryp=str, mz=str):
    msg = "you recently change the currency in whoch your account is in."
    new = (msg.format(Cryp))

    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mz
    password = "Forsure34"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        return 'ok the email has sent '


def send_mail_for_new_Crypt(Cryp=str, mz=str):
    msg = "{} this is your Digital Credit Code Please memorize the last 6 digits"
    new = (msg.format(Cryp))

    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mz
    password = "Forsure34"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        return 'ok the email has sent '


def send_mail_for_Transactions(n=str, mail=str, amt=int):
    email = mail
    trans = amt
    name = n

    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = email
    password = "Forsure34"
    message = "You have received $" + trans + " from " + name
    # Gmail Accounts
    if "gmail" in email:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in email:
        fromMy = 'dokoronkwo167@yahoo.com'
        to = email
        subj = 'Transaction'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = 'dokoronkwo167@yahoo.com'
        password2 = "jiegwhlsvpkrpuag"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)


def send_mail_for_new_account(m2=str, text=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = m2
    password = "Forsure34"
    message = text
    # Gmail Accounts
    if "gmail" in m2:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in m2:
        fromMy = "openbank143@yahoo.com"
        to = m2
        subj = 'NEW ACCOUNT!!!!!'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        return 'ok the email has sent '


def send_mail_for_deposits_checking(depo=int, m3=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = m3
    password = "Forsure34"
    message = "You just made a deposit into your Current account of $ " + [{depo}]
    # Gmail Accounts
    if "gmail" in m3:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in m3:
        fromMy = "openbank143@yahoo.com"
        to = m3
        subj = 'Current account Deposit'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)


def send_mail_for_deposits_saving(depo2=int, m4=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = m4
    password = "Forsure34"
    message = "You just made a deposit into your savings account of $ " + [{depo2}]
    # Gmail Accounts
    if "gmail" in m4:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in m4:
        fromMy = "openbank143@yahoo.com"
        to = m4
        subj = 'Savings account Deposit'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
