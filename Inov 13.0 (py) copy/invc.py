from forex_python.bitcoin import BtcConverter
from cryptography.fernet import Fernet
import psycopg2
from Inov import inov
import random
import invp


# Cryptocurrencies as a whole are in a very rough space right now in the modern economy.
# With that being said, there is still hope for it, and we look to be a part of the growing development in the space.


# create new bitcoin account
def create_accnt_BTC_Debit(account_name=str, email=str, amt=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    b = BtcConverter()
    BTC_USD = float(b.convert_btc_to_cur(amt, 'USD'))
    BTC_EU = float(b.convert_btc_to_cur(amt, 'EUR'))
    BTC_GBP = float(b.convert_btc_to_cur(amt, 'GBP'))
    BTC_CNY = float(b.convert_btc_to_cur(amt, 'CNY'))
    curr.execute("INSERT INTO CryptoDebitAccounts (name, email, number, CardNo, CardCode, SecurityCode, Bitcoin, USD, EU, "
                 "GBP, CNY, Country) "
                 "VALUES ( "
                 "%s, "
                 "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ",
                 [account_name, email, CardNo, CardCode, Sec_code, BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, country])
    conn.commit()
    dclNo = "PLEASE READ: Congrats on your new Crypto Debit account!!! This -> {} is your card number. This -> {} is " \
            "your secured " \
            "card " \
            "code that will be used to secure your account. "
    msg = dclNo.format(CardNo, CardCode)
    print("Crypto Debit Account Created")
    conn.close()
    inov.send_mail_for_new_account(email, msg)


# link bank account to create crypto account (available to those who have accounts with regular bank)
def link_accnt_BTC_Debit(cardNo=int, amt=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [cardNo])
    for row in curr.fetchall():
        email = row[1]
        Debit_mail_email_crypto = str(email)
        curr.execute('''INSERT INTO CryptoDebitAccounts(name, email, CardNo, CardCode, SecurityCode, Country) SELECT name," \
               "email, CardNo, CardCode, SecurityCode, Country FROM " \
               "DebitInov WHERE CardNo=%s''', [cardNo])
        b = BtcConverter()
        BTC_USD = float(b.convert_btc_to_cur(amt, 'USD'))
        BTC_EU = float(b.convert_btc_to_cur(amt, 'EUR'))
        BTC_GBP = float(b.convert_btc_to_cur(amt, 'GBP'))
        BTC_CNY = float(b.convert_btc_to_cur(amt, 'CNY'))
        curr.execute('''UPDATE CryptoDebitAccounts SET Bitcoin=%s, USD=%s, EU=%s, GBP=%s, CNY=%s WHERE CardNo=%s''',
                     [BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, cardNo])
        dclNo = 'PLEASE READ: Congrats on your new Crypto Debit account!!! This -> {}  is your secured card ' \
                'number, this number ' \
                'will ' \
                'handle ' \
                'all ' \
                'payments you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these five digits. '
        msg = dclNo.format(cardNo)
        conn.commit()
        print("Account Linked, Crypto Debit Account created")
        conn.close()
        inov.send_mail_for_new_account(Debit_mail_email_crypto, msg)


def deposit_BTC_Debit(cardNo=int, amt=int):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = "SELECT * from CryptoDebitAccounts WHERE CardNo=? "
    curr.execute(read_data1, [cardNo])
    for row in curr.fetchall():
        email = row[1]
        mail = str(email)
        b = BtcConverter()
        BTC_USD = float(b.convert_btc_to_cur(amt, 'USD'))
        BTC_EU = float(b.convert_btc_to_cur(amt, 'EUR'))
        BTC_GBP = float(b.convert_btc_to_cur(amt, 'GBP'))
        BTC_CNY = float(b.convert_btc_to_cur(amt, 'CNY'))
        curr.execute('''UPDATE CryptoDebitAccounts SET Bitcoin=Bitcoin+%s, USD=USD+%s, EU=EU+%s, GBP=GBP+%s, CNY=CNY+%s WHERE 
        CardNo=%s''', [BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, cardNo])
        conn.commit()
        print("Deposit processed")
        conn.close()
        inov.send_mail_for_deposits_checking(amt, mail)
    else:
        print("Account not found, feel free to try again")


# Process crypto payment
def crypto_payment(CardCode=str):
    invp.get_card_info_Crypto(CardCode)


def send_money_BTC(amount=float, CardNo=int, recipient=str, name=str):
    Bank_fee = "INOVBank"
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    rate_r = 0.013
    curr.execute('''SELECT * from CryptoDebitAccounts WHERE name=%s''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = str(email)
        b = BtcConverter()
        BTC_USD = float(b.convert_btc_to_cur(amount, 'USD'))
        mail_amount = str(BTC_USD)
        BTC_EU = float(b.convert_btc_to_cur(amount, 'EUR'))
        BTC_GBP = float(b.convert_btc_to_cur(amount, 'GBP'))
        BTC_CNY = float(b.convert_btc_to_cur(amount, 'CNY'))
        fee = BTC_USD * rate_r
        total_val = BTC_USD + fee
        curr.execute('''UPDATE CryptoDebitAccounts SET Bitcoin=Bitcoin-%s, USD=USD-%s, EU=EU-%s, GBP=GBP-%s, CNY=CNY-%s WHERE 
        CardNo=%s''', [total_val, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE CryptoDebitAccounts SET Bitcoin=Bitcoin+%s, USD=USD+%s, EU=EU+%s, GBP=GBP+%s, CNY=CNY+%s WHERE 
        name=%s''', [BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        inov.send_mail_for_Transactions(name, mail, mail_amount)
