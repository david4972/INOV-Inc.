from cryptography.fernet import Fernet
import smtplib
import invp
import random
import InternationalTransactions
import CurrencyExchange
import InternationalDebitSend
import psycopg2
import bdms


# CODE STATUS: Complete
# Create Accounts STATUS: Complete
# create Business Credit Account
# create Credit Account
def create_Credit_account(account_name=str, email=str, address=str, Credit_Checking_amt=float,
                          Credit_Savings_amt=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    Curr = "USD"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    curr.execute(
        "INSERT INTO CreditInov (name, email, CardNo, CardCode, SecurityCode, Checking, Saving, Address, Country, "
        "Currency) "
        "VALUES ( "
        "%s, "
        "%s, %s, %s, %s, %s, %s, %s, %s, %s) ",
        [account_name, email, CardNo, CardCode, Sec_code, Credit_Checking_amt, Credit_Savings_amt,
         address,
         country, Curr])
    conn.commit()
    dclNo = "Congrats on your new Credit Bank account!!! This -> {} is your card number. This -> {} is your secured " \
            "card " \
            "code that will be used to secure your account. "
    msg = dclNo.format(CardNo, CardCode)
    send_mail_for_new_account(email, msg)
    conn.close()
    return "Credit Account created"


# create Debit Account
def create_Debit_account(account_name=str, email=str, address=str, Debit_Checking=float, Debit_Saving=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    Curr = "USD"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    curr.execute(
        "INSERT INTO DebitInov (name, email, CardNo, CardCode, SecurityCode, Checking, Saving, Address, Country, "
        "Currency) "
        "VALUES ( "
        "%s, "
        "%s, %s, %s, %s, %s, %s, %s, %s, %s) ",
        [account_name, email, CardNo, CardCode, Sec_code, Debit_Checking, Debit_Saving,
         address,
         country, Curr])
    conn.commit()
    dclNo = "Congrats on your new Debit Bank account!!! This -> {} is your card number. This -> {} is your secured " \
            "card " \
            "code that will be used to secure your account. "
    msg = dclNo.format(CardNo, CardCode)
    conn.close()
    send_mail_for_new_account(email, msg)
    return "Debit Account created"


def create_international_debit_accnt(account_name=str, email=str, address=str, country=str, Inter_Debit_Checking=float,
                                     Inter_Debit_Saving=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    Curr = country
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    curr.execute(
        "INSERT INTO InterDebitInov (name, email, CardNo, CardCode, SecurityCode, Checking, Saving, Address, Country, "
        "Currency) "
        "VALUES ( "
        "%s, "
        "%s, %s, %s, %s, %s, %s, %s, %s, %s) ",
        [account_name, email, CardNo, CardCode, Sec_code, Inter_Debit_Checking, Inter_Debit_Saving,
         address,
         country, Curr])
    conn.commit()
    dclNo = "Congrats on your new International Debit Bank account!!! This -> {} is your card number. This -> {} is " \
            "your secured " \
            "card " \
            "code that will be used to secure your account. "
    msg = dclNo.format(CardNo, CardCode)
    conn.close()
    send_mail_for_new_account(email, msg)
    return "International Debit Account created"


# Deposits STATUS: Complete
def deposit_Checking(deposit=float, CardNo=int):
    dep = str(deposit)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov where CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        if CardNo == row[2]:
            # processing transaction
            curr.execute('''UPDATE DebitInov SET Checking=Checking+%s WHERE CardNo=%s''', [deposit, CardNo])
            conn.commit()
            # dep = str(deposit)
            conn.close()
            send_mail_for_deposits_checking(dep, mail)
            return "deposit complete"  # completing transaction
    else:
        curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
        for row in curr.fetchall():
            email2 = row[1]
            mail = str(email2)
            if CardNo == row[2]:
                # processing transaction
                curr.execute('''UPDATE CreditInov SET Checking=Checking+%s WHERE CardNo=%s''', [deposit, CardNo])
                conn.commit()
                # dep = str(deposit)
                conn.close()
                send_mail_for_deposits_checking(dep, mail)
                return "deposit complete"  # completing transaction


def deposit_Savings(deposit=float, CardNo=int):
    dep = str(deposit)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        if CardNo == row[2]:
            # processing transaction
            curr.execute('''UPDATE DebitInov SET Saving=Saving+%s WHERE CardNo=%s''', [deposit, CardNo])
            conn.commit()
            # dep = str(deposit)
            conn.close()
            print("deposit complete")  # completing transaction
            send_mail_for_deposits_saving(dep, mail)
    else:
        curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
        for row in curr.fetchall():
            email2 = row[1]
            mail = str(email2)
            if CardNo == row[2]:
                # processing transaction
                curr.execute('''UPDATE CreditInov SET Saving=Saving+%s WHERE CardNo=%s''', [deposit, CardNo])
                conn.commit()
                # dep = str(deposit)
                conn.close()
                print("deposit complete")  # completing transaction
                send_mail_for_deposits_saving(dep, mail)


def International_deposit_Checking(deposit=float, CardNo=int):
    dep = str(deposit)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from InterDebitInov where CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        if CardNo == row[2]:
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking+%s WHERE CardNo=%s''', [deposit, CardNo])
            conn.commit()
            # dep = str(deposit)
            conn.close()
            return "deposit complete"  # completing transaction
            # send_mail_for_deposits_checking(dep, mail)


def International_deposit_Savings(deposit=float, CardNo=int):
    dep = str(deposit)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from InterDebitInov WHERE CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        if CardNo == row[2]:
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Saving=Saving+%s WHERE CardNo=%s''', [deposit, CardNo])
            conn.commit()
            # dep = str(deposit)
            conn.close()
            print("deposit complete")  # completing transaction
            send_mail_for_deposits_saving(dep, mail)


# Atm Checking account
def atm_Checking_Debit(CardNo=int, withdraw=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE DebitInov SET Checking=Checking-%s, WHERE CardNo=%s''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+%s, WHERE name=%s''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


def atm_Checking_Credit(CardNo=int, withdraw=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE CreditInov SET Checking=Checking-%s, WHERE CardNo=%s''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+%s, WHERE name=%s''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


# Atm Savings account
def atm_Savings_Debit(CardNo=int, withdraw=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE DebitInov SET Saving=Saving-%s, WHERE CardNo=%s''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+%s, WHERE name=%s''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


def atm_Savings_Credit(CardNo=int, withdraw=float):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    bank = "INOVBank"
    rate_r = 0.013
    curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
    for row in curr.fetchall():
        checking = row[5]
        service = checking * rate_r
        total_val = withdraw + service
        curr.execute('''UPDATE CreditInov SET Saving=Saving-%s, WHERE CardNo=%s''', [total_val, CardNo])
        curr.execute('''UPDATE BusinessInov SET Checking=Checking+%s, WHERE name=%s''', [service, bank])
        conn.commit()
        print("Withdrawal Complete")
        conn.close()


def send_money_Debit(amount=float, CardNo=int, recipient=str):  # send money between Debit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
    for get_cred_name in curr.fetchall():
        name = get_cred_name[0]
        mail_nm = str(name)
        curr.execute('''SELECT * from DebitInov WHERE name=%s''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE DebitInov SET Checking=Checking-%s WHERE CardNo=%s''', [total_val_credit, CardNo])
            curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE DebitInov SET Checking=Checking+%s WHERE name=%s''', [amount, recipient])
            conn.commit()
            conn.close()
            send_mail_for_Transactions(mail_nm, mail, mail_amount)
            return "transaction complete"
        else:
            send_to_Credit(amount, CardNo, recipient, mail_nm)


def send_to_Credit(amount=float, CardNo=int, recipient=str, name=str):  # Send money from Debit to Credit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CreditInov WHERE name=%s''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE DebitInov SET Checking=Checking-%s WHERE CardNo=%s''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE CreditInov SET Checking=Checking+%s WHERE name=%s''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        send_mail_for_Transactions(name, mail, mail_amount)


def send_money_Credit(amount=float, CardNo=int, recipient=str):  # send money between Credit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
    for get_cred_name in curr.fetchall():
        name = get_cred_name[0]
        mail_nm = str(name)
        curr.execute('''SELECT * from CreditInov WHERE name=%s''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE CreditInov SET Checking=Checking-%s WHERE CardNo=%s''', [total_val_credit, CardNo])
            curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE CreditInov SET Checking=Checking+%s WHERE name=%s''', [amount, recipient])
            conn.commit()
            print("transaction complete")
            conn.close()
            send_mail_for_Transactions(mail_nm, mail, mail_amount)
        else:
            send_to_debit(amount, CardNo, recipient, mail_nm)


def send_to_debit(amount=float, CardNo=str, recipient=str, name=str):  # Send money from Credit to Debit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=%s''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-%s WHERE CardNo=%s''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+%s WHERE name=%s''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        send_mail_for_Transactions(name, mail, mail_amount)


def international_send_debit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    InternationalTransactions.global_transactions_Debit(val, Receive_accnt_name, CardNo, curname)


def international_send_credit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    InternationalTransactions.global_transactions_Credit(val, Receive_accnt_name, CardNo, curname)


def international_debit_send(val=float, Receive_accnt_name=str, CardNo=int, curname=str, code=str):
    InternationalDebitSend.global_transactions_International_Debit(val, Receive_accnt_name, CardNo, curname, code)


def currency_exchange_debit(debit_CardNo=int, base=str):
    CurrencyExchange.global_transactions_Credit(debit_CardNo, base)


def currency_exchange_credit(credit_CardNo=int, base=str):
    CurrencyExchange.global_transactions_Credit(credit_CardNo, base)





def process_payment_debit_accnt(CardCode=str):
    invp.get_card_info_Debit(CardCode)


def process_payment_credit_accnt(CardCode=str):
    invp.get_card_info_Credit(CardCode)


def bank_statement_debit(CardNo=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    Debit_accnt_stmt_curr = conn.cursor()
    Debit_accnt_stmt_curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
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
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    credit_accnt_stmt_curr = conn.cursor()
    credit_accnt_stmt_curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
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


# delete account
def delete_accnt_debit(cardNo=int):
    bdms.delete_debit_account(cardNo)


def delete_accnt_credit(cardNo=int):
    bdms.delete_credit_account(cardNo)


def delete_accnt_InternationalDebit(cardNo=int):
    bdms.delete_InternationalDebit_account(cardNo)


# email notifications
def send_mail_for_account_recovery(cardNo=int, cardcode=str, mz=str):
    msg = "{} this is your new virtual card number. {} is your new card code, please keep secured and not protected}"
    new = (msg.format(cardNo, cardcode))

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
    message = "You have received " + trans + " from " + name + " in " + country
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
