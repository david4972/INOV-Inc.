from forex_python.bitcoin import BtcConverter
from cryptography.fernet import Fernet
import sqlite3
import inov
import random
import invp


# Cryptocurrencies as a whole are in a very rough space right now in the modern economy.
# With that being said, there is still hope for it, and we look to be a part of the growing development in the space.


# create new bitcoin account
def create_accnt_BTC(account_name=str, email=str, amt=int):
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    country = "USA"
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    b = BtcConverter()
    BTC_USD = b.convert_btc_to_cur(amt, 'USD')
    BTC_EU = b.convert_btc_to_cur(amt, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(amt, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(amt, 'CNY')
    read_data = "INSERT INTO CryptoDebitAccounts (name, email, number, CardNo, CardCode, SecurityCode, BTC, USD, EU, " \
                "GBP, CNY, Country) " \
                "VALUES ( " \
                "?, " \
                "?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
    val = (account_name, email, CardNo, CardCode, Sec_code, BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, country)
    curr.execute(read_data, val)
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
def link_accnt_BTC(cardNo=int, amt=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = "SELECT * from DebitAccounts WHERE CardNo=? "
    # read_data2 = "SELECT * from CreditAccounts where CardNo=? "
    curr.execute(read_data1, [cardNo])
    for row in curr.fetchall():
        name = row[0]
        email = row[1]
        CardNo = row[2]
        Cardcode = row[3]
        sec_code = row[4]
        country = row[8]
        if cardNo == row[2]:
            # Connecting to sqlite
            conn = sqlite3.connect('InovCrypto.db')
            # Creating a cursor object using the cursor() method
            curr2 = conn.cursor()
            link = "INSERT INTO CryptoDebitAccounts(name, email, CardNo, CardCode, SecurityCode, Country) SELECT name, " \
                   "email, CardNo, CardCode, SecurityCode, Country FROM " \
                   "DebitAccounts WHERE CardNo=? "
            curr2.execute(link, [name, email, CardNo, Cardcode, sec_code, country])
            conn.commit()
            b = BtcConverter()
            BTC_USD = b.convert_btc_to_cur(amt, 'USD')
            BTC_EU = b.convert_btc_to_cur(amt, 'EUR')
            BTC_GBP = b.convert_btc_to_cur(amt, 'GBP')
            BTC_CNY = b.convert_btc_to_cur(amt, 'CNY')
            connect = "UPDATE CryptoDebitAccounts SET CardNo=?, BTC=?, USD=?, EU=?, GBP=?, CNY=? WHERE name=?"
            curr2.execute(connect, [BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY])
            conn.commit()

            dclNo = 'PLEASE READ: Congrats on your new Crypto Debit account!!! This -> {}  is your secured card ' \
                    'number, this number ' \
                    'will ' \
                    'handle ' \
                    'all ' \
                    'payments you make.' \
                    'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                    'these five digits. '
            msg = dclNo.format(cardNo)
            print("Account Linked, Crypto Debit Account created")
            conn.close()
            inov.send_mail_for_new_account(email, msg)


def deposit_Checking_BTC(cardNo=int, amt=int):
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = "SELECT * from CryptoDebitAccounts WHERE CardNo=? "
    curr.execute(read_data1, [cardNo])
    for row in curr.fetchall():
        email = row[1]
        if cardNo == row[2]:
            b = BtcConverter()
            BTC_USD = b.convert_btc_to_cur(amt, 'USD')
            BTC_EU = b.convert_btc_to_cur(amt, 'EUR')
            BTC_GBP = b.convert_btc_to_cur(amt, 'GBP')
            BTC_CNY = b.convert_btc_to_cur(amt, 'CNY')
            deposit = "UPDATE CryptoDebitAccounts SET BTC=BTC+?, USD=USD+?, EU=EU+?, GBP=GBP+?, SET CNY=CNY+? WHERE " \
                      "CardNo=?=?",
            curr.execute(deposit, [BTC_USD, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, cardNo])
            conn.commit()
            print("Deposit processed")
            conn.close()
            inov.send_mail_for_deposits_checking(amt, email)
        else:
            print("Account not found, feel free to try again")


# Process crypto payment
def crypto_payment(CardCode=str):
    invp.get_card_info_Crypto(CardCode)


def send_money(amount=float, name=str, recipient=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    rate_r = 0.013
    read_data1 = '''SELECT * from CryptoDebitAccounts WHERE name=?'''
    # read_data2 = '''SELECT * from CreditAccounts WHERE name=?'''
    # read_data3 = "SELECT * from B-CreditAccounts where CardCode=?"
    curr.execute(read_data1, name)
    for row1 in curr.fetchall():
        # checking = row1[5]
        if name == row1[0]:
            # fee = checking * rate_r
            # curr.execute('UPDATE BusinessCreditAccounts SET Saving=Saving+? WHERE name=INOVBank', [fee])
            # processing transaction
            retrieve = "UPDATE CryptoDebitAccounts SET BTC=BTC-? name=?"
            curr.execute(retrieve, [amount, name])
            conn.commit()
            print("transaction complete")
            conn.close()
            process = "SELECT * from CryptoDebitAccounts WHERE name=?"
            curr.execute(process, recipient)
            for row2 in curr.fetchall():
                email = row2[0]
                if recipient == row2[0]:
                    send = "UPDATE CryptoDebitAccounts SET BTC=BTC+? WHERE name=?"
                    curr.execute(send, [amount, recipient])  # completing transaction
                    conn.commit()
                    print("transaction complete")
                    conn.close()
                    inov.send_mail_for_Transactions(name, email, amount)
