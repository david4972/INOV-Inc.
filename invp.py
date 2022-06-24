import sqlite3
import inov


def get_card_info(CardCode=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()

    read_data1 = "SELECT * from DebitAccounts WHERE CardCode=? "
    read_data2 = "SELECT * from CreditAccounts WHERE CardCode=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # Debit
    curr.execute(read_data1, [CardCode])
    for row in curr.fetchall():
        name = row[0]
        if CardCode == row[3]:
            price = int
            conn.commit()
            conn.close()
            charge_card(CardCode, name, price)
    # Credit
    else:
        curr.execute(read_data2, [CardCode])
        for row in curr.fetchall(CardCode):
            name = row[0]
            if CardCode == row[3]:
                price = int
                conn.commit()
                conn.close()
                charge_card(CardCode, name, price)


def charge_card(ccode=str, name=str, price=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = "SELECT * from DebitAccounts where CardCode=? where name=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # Debit
    curr.execute(read_data1, [ccode, name])
    for row in curr.fetchall(ccode, name):
        email = row[1]
        if name == row[0]:
            if ccode == row[3]:
                # charge card
                charge = "UPDATE DebitAccounts SET Checking=Checking-? WHERE CardCode=?"
                curr.execute(charge, [price, ccode])
                conn.commit()
                conn.close()  # completing charge
                process_payment(ccode, price, email)
    # Credit
    else:
        curr.execute(read_data2, [ccode, name])
        for row in curr.fetchall(ccode, name):
            email = row[1]
            if name == row[0]:
                if ccode == row[3]:
                    # charge card
                    charge = "UPDATE CreditAccounts SET Checking=Checking-? WHERE CardCode=?"
                    curr.execute(charge, [price, ccode])
                    conn.commit()
                    conn.close()  # completing charge
                    process_payment(ccode, price, email)


def process_payment(cardcode=str, price=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    Vendor = "INOV"
    read_data1 = "SELECT * from DebitAccounts where CardCode=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    curr.execute(read_data1, [cardcode])
    for row in curr.fetchall():
        name = row[0]
        address = row[7]
        email = row[1]
        if cardcode == row[3]:
            message = "Payment order From ======= " \
                      "name = -> {}" \
                      "amount = -> {}" \
                      "Vendor = -> {}" \
                      "address = -> {}"
            conn.commit()
            conn.close()
            msg = message.format(name, price, Vendor, address)
            inov.send_mail_for_processed_payment(msg, email)

    else:
        curr.execute(read_data2, [cardcode])
        for row in curr.fetchall():
            name = row[0]
            address = row[7]
            email = row[1]
            if cardcode == row[3]:
                message = "Payment order From ======= " \
                          "name = -> {}" \
                          "amount = -> {}" \
                          "Vendor = -> {}" \
                          "address = -> {}"
                conn.commit()
                conn.close()
                msg = message.format(name, price, Vendor, address)
                inov.send_mail_for_processed_payment(msg, email)


# Crypto Payments

def get_card_info_Crypto(CardCode=str):
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()

    read_data1 = "SELECT * from CryptoDebitAccounts WHERE CardCode=? "
    # read_data2 = "SELECT * from CreditAccounts WHERE CardCode=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # Debit
    curr.execute(read_data1, [CardCode])
    for row in curr.fetchall():
        name = row[0]
        if CardCode == row[3]:
            price = int
            conn.commit()
            conn.close()
            charge_card(CardCode, name, price)
    # Credit
    else:
        print("payment cannot be processed, try again")


def charge_card_Crypto(ccode=str, name=str, price=int):
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    read_data1 = "SELECT * from CryptoDebitAccounts where CardCode=? where name=?"
    # read_data2 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # Debit
    curr.execute(read_data1, [ccode, name])
    for row in curr.fetchall(ccode, name):
        email = row[1]
        if name == row[0]:
            if ccode == row[3]:
                # charge card
                charge = "UPDATE CryptoDebitAccounts SET Checking=Checking-? WHERE CardCode=?"
                curr.execute(charge, [price, ccode])
                conn.commit()
                conn.close()  # completing charge
                process_payment(ccode, price, email)


def process_payment_Crypto(cardcode=str, price=int):
    # Connecting to sqlite
    conn = sqlite3.connect('InovCrypto.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    Vendor = "INOV"
    read_data1 = "SELECT * from CryptoDebitAccounts where CardCode=?"
    # read_data2 = "SELECT * from CreditAccounts where CardCode=?"
    curr.execute(read_data1, [cardcode])
    for row in curr.fetchall():
        name = row[0]
        address = row[7]
        email = row[1]
        if cardcode == row[3]:
            message = "Payment order From ======= " \
                          "name = -> {}" \
                          "amount = -> {}" \
                          "Vendor = -> {}" \
                          "address = -> {}"
            conn.commit()
            conn.close()
            msg = message.format(name, price, Vendor, address)
            inov.send_mail_for_processed_payment(msg, email)
