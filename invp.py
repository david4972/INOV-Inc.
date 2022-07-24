import inov
from forex_python.bitcoin import BtcConverter
import psycopg2


# virtual debit processing
def get_card_info_Debit(CardCode=str):
    price = float(input())
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    Debit_curr1 = conn.cursor()
    # Debit
    Debit_curr1.execute('''SELECT * from DebitInov WHERE CardCode=%s''', [CardCode])
    for get_debit_row in Debit_curr1.fetchall():
        Debit_accnt_name = get_debit_row[0]
        mail_name = str(Debit_accnt_name)
        Debit_accnt_email = get_debit_row[1]
        mail_email = str(Debit_accnt_email)
        conn.commit()
        conn.close()
        charge_card_Debit(CardCode, mail_name, price, mail_email)


def charge_card_Debit(ccode=str, name_debit=str, price=float, email_debit=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    charge_debit_curr = conn.cursor()
    # Debit
    charge_debit_curr.execute('''SELECT * from DebitInov WHERE CardCode=%s''', [ccode])
    for charge_row in charge_debit_curr.fetchall():
        debit_accnt_address = charge_row[7]
        mail_address = str(debit_accnt_address)
        # charge card
        charge_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-%s WHERE CardCode=%s''', [price, ccode])
        conn.commit()
        conn.close()  # completing charge
        process_payment_Debit(price, name_debit, email_debit, mail_address)


def process_payment_Debit(price=float, name_process_debit=str, email_process_debit=str, address_process_debit=str):
    mail_price = str(price)
    Debit_Vendor = "INOV"
    Debit_message = "Payment order From ======= " \
                    "name = -> {}" \
                    "amount = -> {}" \
                    "Vendor = -> {}" \
                    "address = -> {}"

    Debit_msg = Debit_message.format(name_process_debit, mail_price, Debit_Vendor, address_process_debit)
    inov.send_mail_for_processed_payment(Debit_msg, email_process_debit)


# virtual credit processing
def get_card_info_Credit(CardCode=str):
    price = float(input())
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    Credit_curr1 = conn.cursor()
    # Credit
    Credit_curr1.execute('''SELECT * from CreditInov WHERE CardCode=%s''', [CardCode])
    for get_credit_row in Credit_curr1.fetchall():
        Credit_accnt_name = get_credit_row[0]
        mail_name = str(Credit_accnt_name)
        Credit_accnt_email = get_credit_row[1]
        mail = str(Credit_accnt_email)
        conn.commit()
        conn.close()
        charge_card_Credit(CardCode, mail_name, price, mail)


def charge_card_Credit(ccode=str, name_Credit=str, price=float, email_Credit=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    charge_credit_curr = conn.cursor()
    # Credit
    charge_credit_curr.execute('''SELECT * from CreditInov WHERE CardCode=%s''', [ccode])
    for charge_credit_row in charge_credit_curr.fetchall():
        credit_accnt_address = charge_credit_row[7]
        credit_accnt_mail_address = str(credit_accnt_address)
        # charge card
        charge_credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-%s WHERE CardCode=%s''', [price, ccode])
        conn.commit()
        conn.close()  # completing charge
        process_payment_Debit(price, name_Credit, email_Credit, credit_accnt_mail_address)


def process_payment_Credit(price=float, name_process_credit=str, email_process_credit=str, address_process_credit=str):
    mail_price = str(price)
    Credit_Vendor = "INOV"
    Credit_message = "Payment order From ======= " \
                     "name = -> {}" \
                     "amount = -> {}" \
                     "Vendor = -> {}" \
                     "address = -> {}"

    Credit_msg = Credit_message.format(name_process_credit, mail_price, Credit_Vendor, address_process_credit)
    inov.send_mail_for_processed_payment(Credit_msg, email_process_credit)


# Crypto Payments
def get_card_info_Crypto(CardCode=str):
    price = float(input())
    b = BtcConverter()
    BTC_USD = float(b.convert_btc_to_cur(price, 'USD'))
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    Crypto_debit_curr = conn.cursor()
    # Crypto
    Crypto_debit_curr.execute('''SELECT * from CryptoDebitAccounts WHERE CardCode=%s''', [CardCode])
    for Crypto_debit_row in Crypto_debit_curr.fetchall():
        name_crypto = Crypto_debit_row[0]
        mail_name_crypto = str(name_crypto)
        email_crypto = Crypto_debit_row[1]
        mail_crypto = str(email_crypto)
        conn.commit()
        conn.close()
        charge_card_Crypto(CardCode, mail_name_crypto, BTC_USD, mail_crypto)


def charge_card_Crypto(ccode=str, name_crypt=str, price=float, email_crypt=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    charge_crypto_curr = conn.cursor()
    # Credit
    charge_crypto_curr.execute('''SELECT * from CryptoDebitAccounts WHERE CardCode=%s''', [ccode])
    for charge_crypto_row in charge_crypto_curr.fetchall():
        crypto_address = charge_crypto_row[7]
        crypto_mail_address = str(crypto_address)
        # charge card
        charge_crypto_row.execute('''UPDATE CryptoDebitAccounts SET Bitcoin=Bitcoin-%s WHERE CardCode=%s''', [price, ccode])
        conn.commit()
        conn.close()  # completing charge
        process_payment_Debit(price, name_crypt, email_crypt, crypto_mail_address)


def process_payment_Crypto(price=float, name_process_crypto=str, email_process_crypto=str, address_process_crypto=str):
    mail_price = str(price)
    Crypto_Vendor = "INOV"
    Crypto_message = "Payment order From ======= " \
                     "name = -> {}" \
                     "amount BTC = -> {}" \
                     "Vendor = -> {}" \
                     "address = -> {}"
    Crypto_msg = Crypto_message.format(name_process_crypto, mail_price, Crypto_Vendor, address_process_crypto)
    inov.send_mail_for_processed_payment(Crypto_msg, email_process_crypto)
