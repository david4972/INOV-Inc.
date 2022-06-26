import sqlite3
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

    read_data = "INSERT INTO BusinessInov (name, email, industry, CardNo, CardCode, SecurityCode, Checking, " \
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
    read_data = "INSERT INTO CreditInov (name, email, CardNo, CardCode, SecurityCode, Checking, " \
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
    read_data = "INSERT INTO DebitInov (name, email, CardNo, CardCode, SecurityCode, Checking, Saving, " \
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
def deposit_Checking(deposit=float, CardNo=int):
    dep = str(deposit)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov where CardNo=?''', [CardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        if CardNo == row[2]:
            # processing transaction
            curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE CardNo=?''', [deposit, CardNo])
            conn.commit()
            # dep = str(deposit)
            conn.close()
            print("deposit complete")  # completing transaction
            send_mail_for_deposits_checking(dep, mail)
    else:
        curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
        for row in curr.fetchall():
            email2 = row[1]
            mail = str(email2)
            if CardNo == row[2]:
                # processing transaction
                curr.execute('''UPDATE CreditInov SET Checking=Checking+? WHERE CardNo=?''', [deposit, CardNo])
                conn.commit()
                # dep = str(deposit)
                conn.close()
                print("deposit complete")  # completing transaction
                send_mail_for_deposits_checking(dep, mail)


def deposit_Savings(deposit=float, CardNo=int):
    dep = str(deposit)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE CardNo=?''', [CardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        if CardNo == row[2]:
            # processing transaction
            curr.execute('''UPDATE DebitInov SET Saving=Saving+? WHERE CardNo=?''', [deposit, CardNo])
            conn.commit()
            # dep = str(deposit)
            conn.close()
            print("deposit complete")  # completing transaction
            send_mail_for_deposits_saving(dep, mail)
    else:
        curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
        for row in curr.fetchall():
            email2 = row[1]
            mail = str(email2)
            if CardNo == row[2]:
                # processing transaction
                curr.execute('''UPDATE CreditInov SET Saving=Saving+? WHERE CardNo=?''', [deposit, CardNo])
                conn.commit()
                # dep = str(deposit)
                conn.close()
                print("deposit complete")  # completing transaction
                send_mail_for_deposits_saving(dep, mail)


# Atm Checking account
def atm_Checking_Debit(CardNo=int, withdraw=float):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from DebitInov WHERE CardNo=?''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE DebitInov SET Checking=Checking-?, WHERE CardNo=?''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+?, WHERE name=?''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


def atm_Checking_Credit(CardNo=int, withdraw=float):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE CreditInov SET Checking=Checking-?, WHERE CardNo=?''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+?, WHERE name=?''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


# Atm Savings account
def atm_Savings_Debit(CardNo=int, withdraw=float):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from DebitInov WHERE CardNo=?''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE DebitInov SET Saving=Saving-?, WHERE CardNo=?''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+?, WHERE name=?''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


def atm_Savings_Credit(CardNo=int, withdraw=float):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE CreditInov SET Saving=Saving-?, WHERE CardNo=?''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+?, WHERE name=?''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()



def send_money_Debit(amount=float, CardNo=int, recipient=str, name=str):  # send money between Debit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        send_mail_for_Transactions(name, mail, mail_amount)
    else:
        send_to_Credit(amount, CardNo, recipient, name)


def send_to_Credit(amount=float, CardNo=int, recipient=str, name=str):  # Send money from Debit to Credit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        send_mail_for_Transactions(name, mail, mail_amount)


def send_money_Credit(amount=float, CardNo=int, recipient=str, name=str):  # send money between Credit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CreditInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE CreditInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        send_mail_for_Transactions(name, mail, mail_amount)
    else:
        send_to_debit(amount, CardNo, recipient, name)


def send_to_debit(amount=float, CardNo=str, recipient=str, name=str):  # Send money from Credit to Debit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        send_mail_for_Transactions(name, mail, mail_amount)


def process_payment_debit_accnt(CardCode=str):
    invp.get_card_info_Debit(CardCode)


def process_payment_credit_accnt(CardCode=str):
    invp.get_card_info_Credit(CardCode)


def bank_statement_debit(CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    Debit_accnt_stmt_curr = conn.cursor()
    Debit_accnt_stmt_curr.execute('''SELECT * from DebitInov WHERE CardNo=?''', [CardNo])
    for Debit_accnt_stmt_row in Debit_accnt_stmt_curr.fetchall():
        stmt_debit_name = Debit_accnt_stmt_row[0]
        mail_name_stmt = str(stmt_debit_name)
        stmt_debit_email = Debit_accnt_stmt_row[1]
        mail_email_stmt = str(stmt_debit_email)
        stmt_debit_Checking = Debit_accnt_stmt_row[5]
        mail_checking_stmt = str(stmt_debit_Checking)
        stmt_debit_Saving = Debit_accnt_stmt_row[6]
        mail_saving_stmt = str(stmt_debit_Saving)
        stmt_debit_Currency = Debit_accnt_stmt_row[9]
        mail_debit_currency_stmt = str(stmt_debit_Currency)
        Debit_message = "Bank Statement of {}" \
                        "Account name =  {}" \
                        "Checking Balance =  {}" \
                        "Saving Balance =  {}" \
                        "Currency =  {}"
        Debit_msg = Debit_message.format(mail_name_stmt, mail_checking_stmt, mail_saving_stmt, mail_debit_currency_stmt)
        send_mail_for_processed_payment(Debit_msg, mail_email_stmt)


def bank_statement_credit(CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    credit_accnt_stmt_curr = conn.cursor()
    credit_accnt_stmt_curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
    for credit_accnt_stmt_row in credit_accnt_stmt_curr.fetchall():
        stmt_credit_name = credit_accnt_stmt_row[0]
        credit_mail_name_stmt = str(stmt_credit_name)
        stmt_credit_email = credit_accnt_stmt_row[1]
        credit_mail_email_stmt = str(stmt_credit_email)
        stmt_credit__Checking = credit_accnt_stmt_row[5]
        credit_mail_checking_stmt = str(stmt_credit__Checking)
        stmt_credit__Saving = credit_accnt_stmt_row[6]
        credit_mail_saving_stmt = str(stmt_credit__Saving)
        stmt_credit__Currency = credit_accnt_stmt_row[9]
        credit_mail_debit_currency_stmt = str(stmt_credit__Currency)
        Debit_message = "Bank Statement of {}" \
                        "Account name =  {}" \
                        "Checking Balance =  {}" \
                        "Saving Balance =  {}" \
                        "Currency =  {}"
        Debit_msg = Debit_message.format(credit_mail_name_stmt, credit_mail_name_stmt, credit_mail_checking_stmt,
                                         credit_mail_saving_stmt, credit_mail_debit_currency_stmt)
        send_mail_for_bank_statement(Debit_msg, credit_mail_email_stmt)


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
    msg = "you recently change the currency in which your account is in to {}. you were charged 1.3% upon exchange."
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


def send_mail_for_Transactions(n=str, mail=str, amt=str):
    email = mail
    trans = amt
    name = n
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = email
    password = "ladfpscfaupnptmn"
    message = "You have received $ " + trans + " from " + name
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


def send_mail_for_International_Transactions(n=str, mail=str, amt=str, country=str):
    email = mail
    trans = amt
    name = n
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = email
    password = "ladfpscfaupnptmn"
    message = "You have received $ " + trans + " from " + name + " in " + country
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


def send_mail_for_deposits_checking(depo=str, m3=str):
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = m3
    password = "ladfpscfaupnptmn"
    message = "You just made a deposit into your Checkings account of $ " + depo
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


def send_mail_for_deposits_saving(depo2=str, m4=str):
    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = m4
    password = "ladfpscfaupnptmn"
    message = "You just made a deposit into your Savings account of $ " + depo2
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


def send_mail_for_bank_statement(m4=str, email=str):
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
