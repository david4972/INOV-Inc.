import psycopg2
from cryptography.fernet import Fernet
import random
import inov


# Virtual Credit and Debit accounts (US only)
def Login_accnt(cardNo):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("temporary crypt password generating...")
    Security = str(Fernet.generate_key())
    while Security.isascii():
        num_of_tries = 0
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
                    count = num_of_tries + 1
                    if count < 3:
                        print("try again")
                    elif count == 3:
                        print("You have been locked lout of logging in")
                        # Email to notify
                    conn.commit()
                    break


# Process of securing account if breached.
# Select Account type to be reviewed
def secure_accnt(accnt, c_code):
    if accnt == "Debit":
        reactivate_accnt_debit(c_code)
    elif accnt == "Credit":
        reactivate_accnt_credit(c_code)


# Check For Debit Account (Based On Input From User)
def reactivate_accnt_debit(cardcode):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute("SELECT * FROM DebitInov WHERE CardCode=%s", [cardcode])
    for row in curr.fetchall():
        code = row[4]
        if cardcode == code:
            print("Directing to login page...")
            # Direct to page for Login_accnt(cardNo) to read input
        else:
            Security_Code_Check()


# Check For Credit Account (Based On Input From User)
def reactivate_accnt_credit(cardcode):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute("SELECT * FROM CreditInov WHERE SecurityCode=%s", [cardcode])
    for row in curr.fetchall():
        code = row[4]
        if cardcode == code:
            print("Directing to login page...")
            # Direct to page for Login_accnt(cardNo) to read input
        else:
            Security_Code_Check()


def Security_Code_Check():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("enter security code: ")
    sec_code = input()
    curr.execute("SELECT * FROM CreditInov WHERE SecurityCode=%s", [sec_code])
    for row in curr.fetchall():
        code = row[4]
        if sec_code == code:
            print("Directing to login page...")
            # Direct to page for Login_accnt(cardNo) to read input
        else:
            print("Retrieve account page Loading...")
            # Direct to page for retrieve_account(accnt_name, accnt_choice) to read input


def retrieve_account(accnt_name, accnt_choice):
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
    if accnt_choice == "Debit":
        curr.execute("SELECT * FROM DebitInov WHERE name=%s", [accnt_name])
        for row in curr.fetchall():
            email = row[1]
            mail_e = str(email)
            curr.execute("UPDATE DebitInov set CardNo=%s, CardCode=%s, SecurityCode=%s  WHERE name=%s",
                         [CardNo, CardCode, Sec_code, accnt_name])
            inov.send_mail_for_account_recovery(CardNo, CardCode, mail_e)
            print("account recovered")
    elif accnt_choice == "Credit":
        curr.execute("SELECT * FROM CreditInov WHERE name=%s", [accnt_name])
        for row in curr.fetchall():
            email = row[1]
            mail_e = str(email)
            curr.execute("UPDATE CreditInov set CardNo=%s, CardCode=%s, SecurityCode=%s  WHERE name=%s",
                         [CardNo, CardCode, Sec_code, accnt_name])
            inov.send_mail_for_account_recovery(CardNo, CardCode, mail_e)
            print("account recovered")


# Virtual International Debit Accounts
def Login_accnt_International(cardNo):
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
        tries = 0
        curr.execute("SELECT * FROM InterDebitInov WHERE CardNo=%s", [cardNo])
        for row in curr.fetchall():
            debit_card_num = row[2]
            if cardNo == debit_card_num:
                print("login successful")
            else:
                count = tries + 1
                if count < 3:
                    print("account not found please try again")
                elif count == 3:
                    print("You have been locked lout of logging in, an email will be sent to you shortly.")
                    # Email to notify
                break


def secure_international_account(c_code):
    reactivate_International_accnt(c_code)


def reactivate_International_accnt(c_code):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute("SELECT * FROM InterDebitInov WHERE SecurityCode=%s", [c_code])
    for row in curr.fetchall():
        code = row[4]
        if c_code == code:
            print("Directing to login page...")
            # Direct to page for Login_accnt_International(cardNo) to read input
        else:
            Security_code_International_debit()


def Security_code_International_debit():
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    print("enter security code: ")
    sec_code = input()
    curr.execute("SELECT * FROM InterDebitInov WHERE SecurityCode=%s", [sec_code])
    for row in curr.fetchall():
        code = row[4]
        if sec_code == code:
            print("Directing to login page...")
            # Direct to page for Login_accnt_International(cardNo) to read input
        else:
            print("Retrieve account page Loading...")
            # Direct to page for retrieve_account(accnt_name) to read input


def retrieve_account_Inter(accnt_name):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    # generating new credentials, security data included.
    CardNo = random.randint(11111, 99999)
    Security = str(Fernet.generate_key())
    Sec_code = str(Security[:10])
    Crypt = str(Security[:5])
    CardCode = Crypt
    curr.execute("SELECT * FROM InterDebitInov WHERE name=%s", [accnt_name])
    for row in curr.fetchall():
        email = row[1]
        mail_e = str(email)
        curr.execute("UPDATE InterDebitInov set CardNo=%s, CardCode=%s, SecurityCode=%s  WHERE name=%s",
                     [CardNo, CardCode, Sec_code, accnt_name])
        inov.send_mail_for_account_recovery(CardNo, CardCode, mail_e)
        print("account recovered")


if __name__ == '__main__':
    Login_accnt()

