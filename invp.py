from data import get_database
import smtplib


def get_card_info(CardCode=str, name=str):
    db = get_database()
    curr = db.cursor()

    read_data1 = "SELECT * from DebitAccounts where CardCode=? where name=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # read_data3 = "SELECT * from CreditAccounts where CardCode=? where name=?"
    # Debit
    curr.execute(read_data1, [CardCode, name])
    for row in curr.fetchall(CardCode, name):
        email = row[1]
        if name == row[0]:
            if CardCode == row[3]:
                price = int
                charge_card(CardCode, name, price)
    # Credit
    else:
        curr.execute(read_data2, [CardCode, name])
        for row in curr.fetchall(CardCode, name):
            email = row[1]
            if name == row[0]:
                if CardCode == row[3]:
                    price = int
                    charge_card(CardCode, name, price)


def charge_card(ccode=str, name=str, price=int):
    db = get_database()
    curr = db.cursor()
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
                curr.commit()  # completing charge
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
                    curr.commit()  # completing charge
                    process_payment(ccode, price, email)


def process_payment(cardcode=str, price=int, email=str):
    db = get_database()
    curr = db.cursor()
    Vendor = "INOV"
    read_data1 = "SELECT * from DebitAccounts where CardCode=? where email=?"
    read_data2 = "SELECT * from CreditAccounts where CardCode=? where email=?"
    curr.execute(read_data1, [cardcode, email])
    for row in curr.fetchall(cardcode, email):
        name = row[0]
        address = row[7]
        if email == row[1]:
            if cardcode == row[3]:
                message = "Payment order From ======= " \
                          "name = -> {}" \
                          "amount = -> {}" \
                          "Vendor = -> {}" \
                          "address = -> {}"
                msg = message.format(name, price, Vendor, address)
                send_mail_for_processed_payment(msg, email)

    else:
        curr.execute(read_data2, [cardcode, email])
        for row in curr.fetchall(cardcode, email):
            name = row[0]
            address = row[7]
            if email == row[1]:
                if cardcode == row[3]:
                    message = "Payment order From ======= " \
                              "name = -> {}" \
                              "amount = -> {}" \
                              "Vendor = -> {}" \
                              "address = -> {}"
                    msg = message.format(name, price, Vendor, address)
                    send_mail_for_processed_payment(msg, email)
