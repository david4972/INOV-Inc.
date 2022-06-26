import sqlite3
import inov
from forex_python.converter import CurrencyRates


# Currency change (allows account users to convert currency cash account into the main global currencies (USD, EUR,
# GBP, CNY)
# USD
def CurrencyExchange_USD_Debit(debit_name=str, debit_CardNo=int, debit_gbc=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_USD_debit_curr = conn.cursor()
    c = CurrencyRates()
    USD_debit_var = "USD"
    USD_Currency_debit_convert = debit_gbc
    USD_debit_convert_check = c.get_rate(USD_Currency_debit_convert, USD_debit_var)
    USD_debit_convert_sav = c.get_rate(USD_Currency_debit_convert, USD_debit_var)
    rate_r = 0.013
    CurrencyExchange_USD_debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=?''', [debit_CardNo])
    for row1 in CurrencyExchange_USD_debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_USD_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
                                                [db_checking_fee, debit_CardNo])
        CurrencyExchange_USD_debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                [db_checking_fee])
        CurrencyExchange_USD_debit_curr.execute('''UPDATE DebitInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [USD_debit_convert_check, USD_debit_convert_sav, USD_debit_var, debit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(USD_debit_var, mail_currency_exchange_debit)


def CurrencyExchange_USD_Credit(credit_name=str, credit_CardNo=int, credit_gbc=str):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_USD_credit_curr = conn.cursor()
    c = CurrencyRates()
    USD_credit_var = "USD"
    USD_Currency_credit_convert = credit_gbc
    USD_credit_convert_check = c.get_rate(USD_Currency_credit_convert, USD_credit_var)
    USD_credit_convert_sav = c.get_rate(USD_Currency_credit_convert, USD_credit_var)
    rate_r = 0.013
    CurrencyExchange_USD_credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=?''', [credit_CardNo])
    for row1 in CurrencyExchange_USD_credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_USD_credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
                                                 [db_checking_fee, credit_CardNo])
        CurrencyExchange_USD_credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                 [db_checking_fee])
        CurrencyExchange_USD_credit_curr.execute('''UPDATE CreditInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [USD_credit_convert_check, USD_credit_convert_sav, USD_credit_var, credit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(USD_credit_var, mail_currency_exchange_credit)


# EUR
def CurrencyExchange_EUR_Debit(debit_name=str, debit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_EUR_debit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "EUR"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_EUR_debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=?''', [debit_CardNo])
    for row1 in CurrencyExchange_EUR_debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_EUR_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
                                                [db_checking_fee, debit_CardNo])
        CurrencyExchange_EUR_debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                [db_checking_fee])
        CurrencyExchange_EUR_debit_curr.execute('''UPDATE DebitInov SET Current=Current/?, Saving=Saving/? Currency=? 
            WHERE name=?''', [cex1, cex2, var2, debit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_debit)


def CurrencyExchange_EUR_Credit(credit_name=str, credit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_EUR_credit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "EUR"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_EUR_credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=?''', [credit_CardNo])
    for row1 in CurrencyExchange_EUR_credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_EUR_credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
                                                 [db_checking_fee, credit_CardNo])
        CurrencyExchange_EUR_credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                 [db_checking_fee])
        CurrencyExchange_EUR_credit_curr.execute('''UPDATE CreditInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [cex1, cex2, var2, credit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_credit)


# GBP
def CurrencyExchange_GBP_Debit(debit_name=str, debit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_GBP_debit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "GBP"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_GBP_debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=?''', [debit_CardNo])
    for row1 in CurrencyExchange_GBP_debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_GBP_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
                                                [db_checking_fee, debit_CardNo])
        CurrencyExchange_GBP_debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                [db_checking_fee])
        CurrencyExchange_GBP_debit_curr.execute('''UPDATE DebitInov SET Current=Current/?, Saving=Saving/? Currency=? 
                WHERE name=?''', [cex1, cex2, var2, debit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_debit)


def CurrencyExchange_GBP_Credit(credit_name=str, credit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_GBP_Credit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "GBP"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_GBP_Credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=?''', [credit_CardNo])
    for row1 in CurrencyExchange_GBP_Credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_GBP_Credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
                                                 [db_checking_fee, credit_CardNo])
        CurrencyExchange_GBP_Credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                 [db_checking_fee])
        CurrencyExchange_GBP_Credit_curr.execute('''UPDATE CreditInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [cex1, cex2, var2, credit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_credit)


def CurrencyExchange_AUS_Debit(debit_name=str, debit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_AUS_debit_curr = conn.cursor()
    c = CurrencyRates()
    AUS_debit_var = "AUS"
    AUS_debit_USD = "USD"
    AUS_debit_convert_check = c.get_rate(AUS_debit_USD, AUS_debit_var)
    AUS_debit_convert_sav = c.get_rate(AUS_debit_USD, AUS_debit_var)
    rate_r = 0.013
    CurrencyExchange_AUS_debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=?''', [debit_CardNo])
    for row1 in CurrencyExchange_AUS_debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_AUS_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
                                                [db_checking_fee, debit_CardNo])
        CurrencyExchange_AUS_debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                [db_checking_fee])
        CurrencyExchange_AUS_debit_curr.execute('''UPDATE DebitInov SET Current=Current/?, Saving=Saving/? Currency=? 
                    WHERE name=?''', [AUS_debit_convert_check, AUS_debit_convert_sav, AUS_debit_var, debit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(AUS_debit_var, mail_currency_exchange_debit)


def CurrencyExchange_AUS_Credit(credit_name=str, credit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_AUS_Credit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "AUS"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_AUS_Credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=?''', [credit_CardNo])
    for row1 in CurrencyExchange_AUS_Credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_AUS_Credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
                                                 [db_checking_fee, credit_CardNo])
        CurrencyExchange_AUS_Credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                 [db_checking_fee])
        CurrencyExchange_AUS_Credit_curr.execute('''UPDATE CreditInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [cex1, cex2, var2, credit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_credit)


def CurrencyExchange_CNY_Debit(debit_name=str, debit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_CNY_Debit_curr = conn.cursor()
    c = CurrencyRates()
    var5 = "CNY"
    gbc = "USD"
    hex5 = c.get_rate(gbc, var5)
    hex6 = c.get_rate(gbc, var5)
    rate_r = 0.013
    CurrencyExchange_CNY_Debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=?''', [debit_CardNo])
    for row1 in CurrencyExchange_CNY_Debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_CNY_Debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
                                                [db_checking_fee, debit_CardNo])
        CurrencyExchange_CNY_Debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                [db_checking_fee])
        CurrencyExchange_CNY_Debit_curr.execute('''UPDATE DebitInov SET Current=Current/?, Saving=Saving/? Currency=? 
                        WHERE name=?''', [hex5, hex6, var5, debit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var5, mail_currency_exchange_debit)


def CurrencyExchange_CNY_Credit(credit_name=str, credit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_CNY_Credit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "CNY"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_CNY_Credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=?''', [credit_CardNo])
    for row1 in CurrencyExchange_CNY_Credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_CNY_Credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
                                                 [db_checking_fee, credit_CardNo])
        CurrencyExchange_CNY_Credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                 [db_checking_fee])
        CurrencyExchange_CNY_Credit_curr.execute('''UPDATE CreditInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [cex1, cex2, var2, credit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_credit)


def CurrencyExchange_JPY_Debit(debit_name=str, debit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_JPY_Debit_curr = conn.cursor()
    c = CurrencyRates()
    var6 = "JPY"
    gbc = "USD"
    hex6 = c.get_rate(gbc, var6)
    hex7 = c.get_rate(gbc, var6)
    rate_r = 0.013
    CurrencyExchange_JPY_Debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=?''', [debit_CardNo])
    for row1 in CurrencyExchange_JPY_Debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_JPY_Debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
                                                [db_checking_fee, debit_CardNo])
        CurrencyExchange_JPY_Debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                [db_checking_fee])
        CurrencyExchange_JPY_Debit_curr.execute('''UPDATE DebitInov SET Current=Current/?, Saving=Saving/? Currency=? 
                            WHERE name=?''', [hex6, hex7, var6, debit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var6, mail_currency_exchange_debit)


def CurrencyExchange_JPY_Credit(credit_name=str, credit_CardNo=int):
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    CurrencyExchange_JPY_Credit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = "JPY"
    cex1 = c.get_rate(var1, var2)
    cex2 = c.get_rate(var1, var2)
    rate_r = 0.013
    CurrencyExchange_JPY_Credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=?''', [credit_CardNo])
    for row1 in CurrencyExchange_JPY_Credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        CurrencyExchange_JPY_Credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
                                                 [db_checking_fee, credit_CardNo])
        CurrencyExchange_JPY_Credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
                                                 [db_checking_fee])
        CurrencyExchange_JPY_Credit_curr.execute('''UPDATE CreditInov SET Current=Current/?, Saving=Saving/? Currency=? 
        WHERE name=?''', [cex1, cex2, var2, credit_name])
        conn.commit()
        print("exchange complete")
        conn.close()
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_credit)

