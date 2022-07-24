import psycopg2
from cryptography.fernet import Fernet
import random
import inov


# Virtual Credit and Debit accounts (USD only)
def Login_accnt():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("temporary crypt password generating...")
    Security = str(Fernet.generate_key())
    print(Security)
    while Security.isascii():
        print("please enter card number: ")
        cardNo = int(input())
        curr.execute("SELECT * FROM DebitInov WHERE CardNo=%s", [cardNo])
        for row in curr.fetchall():
            debit_card_num = row[2]
            if cardNo == debit_card_num:
                print("login successful")
            else:
                curr.execute("SELECT * FROM CreditInov WHERE CardNo=%s", [cardNo])
                for row2 in curr.fetchall():
                    credit_card_num = row2[2]
                    if cardNo == credit_card_num:
                        print("login successful")
                    else:
                        print("Login process failed")
        break
    conn.commit()


def get_back_accnt():
    reactivate_accnt_debit()


def reactivate_accnt_debit():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("please enter card code: ")
    card_code = input()
    curr.execute("SELECT * FROM DebitInov WHERE SecurityCode=%s", [card_code])
    for row in curr.fetchall():
        code = row[4]
        if card_code == code:
            Login_accnt()
        else:
            reactivate_accnt_credit()


def reactivate_accnt_credit():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("please enter card code: ")
    card_code = input()
    curr.execute("SELECT * FROM CreditInov WHERE SecurityCode=%s", [card_code])
    for row in curr.fetchall():
        code = row[4]
        if card_code == code:
            Login_accnt()
        else:
            retrieve_account()


def retrieve_account():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    print("please enter the name your account is in: ")
    accnt_name = input()
    print("please select")
    print("1. Debit")
    print("2. Credit")
    accnt_choice = input()
    if accnt_choice == "1":
        curr.execute("SELECT * FROM DebitInov WHERE name=%s", [accnt_name])
        for row in curr.fetchall():
            email = row[1]
            mail_e = str(email)
            curr.execute("UPDATE DebitInov set CardNo=%s, CardCode=%s, SecurityCode=%s  WHERE name=%s",
                         [CardNo, CardCode, Sec_code, accnt_name])
            inov.send_mail_for_account_recovery(CardNo, CardCode, mail_e)
            print("account recovered")
    if accnt_choice == "2":
        curr.execute("SELECT * FROM CreditInov WHERE name=%s", [accnt_name])
        for row in curr.fetchall():
            email = row[1]
            mail_e = str(email)
            curr.execute("UPDATE CreditInov set CardNo=%s, CardCode=%s, SecurityCode=%s  WHERE name=%s",
                         [CardNo, CardCode, Sec_code, accnt_name])
            inov.send_mail_for_account_recovery(CardNo, CardCode, mail_e)
            print("account recovered")


# Virtual International Debit Accounts
def Login_accnt_International():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("temporary crypt password generating...")
    Security = str(Fernet.generate_key())
    print(Security)
    while Security.isascii():
        print("please enter card number: ")
        cardNo = int(input())
        curr.execute("SELECT * FROM InterDebitInov WHERE CardNo=%s", [cardNo])
        for row in curr.fetchall():
            debit_card_num = row[2]
            if cardNo == debit_card_num:
                print("login successful")
            else:
                print("account not found please try again")
                break
    Login_accnt_International()


def get_back_accnt_Inter():
    reactivate_accnt_debit()


def reactivate_accnt_debit_Inter():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("please enter card code: ")
    card_code = input()
    curr.execute("SELECT * FROM InterDebitInov WHERE SecurityCode=%s", [card_code])
    for row in curr.fetchall():
        code = row[4]
        if card_code == code:
            Login_accnt_International()
        else:
            retrieve_account_Inter()


def retrieve_account_Inter():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    print("please enter the name your account is in: ")
    accnt_name = input()
    curr.execute("SELECT * FROM DebitInov WHERE name=%s", [accnt_name])
    for row in curr.fetchall():
        email = row[1]
        mail_e = str(email)
        curr.execute("UPDATE InterDebitInov set CardNo=%s, CardCode=%s, SecurityCode=%s  WHERE name=%s",
                         [CardNo, CardCode, Sec_code, accnt_name])
        inov.send_mail_for_account_recovery(CardNo, CardCode, mail_e)
        print("account recovered")


if __name__ == '__main__':
    Login_accnt()

