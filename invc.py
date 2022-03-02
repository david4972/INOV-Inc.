from sqlalchemy import create_engine
from forex_python.bitcoin import BtcConverter
from cryptography.fernet import Fernet
# import sqlite3
import smtplib
import ccard

conn_connect = create_engine('sqlite:///data.db')
# conn = sqlite3.connect('data.db')
con = conn_connect.cursor()
db_connect = create_engine('sqlite:///BTCdata.db')
dub = db_connect.cursor()


# Login to account
def login_to_BTC_accnt(name=str, cryp=str):
    sort = dub.execute('SELECT name, SDC, IIF(name=?, SDC=?, \'Login successful\', \'login failed\') FROM '
                       'InovClientsCrypto;', name, cryp)
    print(sort)


# delete account
def delete_BTC_accnt(name=str, email=str):
    dub = db_connect.connect()
    dub.execute("DELETE from InovClientsCrypto WHERE name=?, email=?", name, email)
    dub.close()


# reactivate account
def reactivate_BTC_accnt(name=str, dcl=str):
    data_current = dub.execute("SELECT name, Type FROM InovClientsCrypto WHERE DCL=?", [dcl])
    res = data_current.fetchall()
    for x in res:
        print("Account Name = ", x[0])
        print("Account Type = ", x[1])
    priv = ccard.americanexpress()
    to_string = str(priv)
    pr = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    scd = f.encrypt(pr)
    dclNo = '{} this is your secured credit code, this number will be your main account charged with most ' \
            'transactions you make.' \
            'This is to ensure safer payment and build a more secure wall around your credit.'
    print(dclNo.format(Crypt))
    # Personal Credit/Debit Account
    dub.execute('UPDATE InovClientsCrypto SET DCL=? WHERE name=?', [c_value, name])
    dub.execute('UPDATE InovClientsCrypto SET SDC=? WHERE name=?', [scd, name])


def get_access_INOVBANKACCNT(cryp=str):
    conn = conn_connect()
    sort = conn.execute("select name, email, Country from InovClientsCrypto WHERE SDC=?", cryp)
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print(result)


# create new bitcoin account
def create_accnt_BTC(name=str, email=str, ph=int, sdc=int, dcl=int, Btcamt=int, cou=str):
    priv = ccard.visa()
    to_string = str(priv)
    pr = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    sdc = f.encrypt(pr)
    b = BtcConverter()
    BTC_USD = b.convert_btc_to_cur(Btcamt, 'USD')
    BTC_EU = b.convert_btc_to_cur(Btcamt, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(Btcamt, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(Btcamt, 'CNY')
    read_data = "INSERT INTO InovClientsCrypto (name, email, number, SDC, DCL, BTC, USD, EU, GBP, CNY, Country) " \
                "VALUES ( " \
                "?, " \
                "?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
    val = (name, email, pr, sdc, dcl, Btcamt, BTC_USD, BTC_EU, BTC_GBP, BTC_CNY, cou)
    dub.execute(read_data, val)
    dub.close()


# Link regular account to bitcoin account (if regular account is already there)
def link_accnt_BTC(name=str, cryp=str, ph=int, sdc=int, dcl=int, Btcamt=int):
    get_access_INOVBANKACCNT(cryp)
    dub.execute("INSERT INTO InovClientsCrypto(name, email, Country) SELECT name, email, Country FROM InovClientsData"
                "WHERE SDC=?", [cryp])
    b = BtcConverter()
    BTC_USD = b.convert_btc_to_cur(Btcamt, 'USD')
    BTC_EU = b.convert_btc_to_cur(Btcamt, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(Btcamt, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(Btcamt, 'CNY')
    dub.execute('UPDATE InovClientsCrypto SET number=? WHERE name=?', [ph, name])
    dub.execute('UPDATE InovClientsCrypto SET SDC=? WHERE name=?', [sdc, name])
    dub.execute('UPDATE InovClientsCrypto SET DCL=? WHERE name=?', [dcl, name])
    dub.execute('UPDATE InovClientsCrypto SET BTC=? WHERE name=?', [Btcamt, name])
    dub.execute('UPDATE InovClientsCrypto SET USD=? WHERE name=?', [BTC_USD, name])
    dub.execute('UPDATE InovClientsCrypto SET EU=? WHERE name=?', [BTC_EU, name])
    dub.execute('UPDATE InovClientsCrypto SET GBP=? WHERE name=?', [BTC_GBP, name])
    dub.execute('UPDATE InovClientsCrypto SET CNY=? WHERE name=?', [BTC_CNY, name])
    dub.close()
    dub.close()


def enter_deposit_Checking_BTC(pin=int, btc=int):
    b = BtcConverter()
    BTC_USD = b.convert_btc_to_cur(btc, 'USD')
    BTC_EU = b.convert_btc_to_cur(btc, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(btc, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(btc, 'CNY')
    dub.execute("UPDATE InovClientsCrypto SET BTC=BTC+? WHERE name=?", [btc, pin])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD+? WHERE name=?", [BTC_USD, pin])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU+? WHERE name=?", [BTC_EU, pin])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP+? WHERE name=?", [BTC_GBP, pin])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY+? WHERE name=?", [BTC_CNY, pin])
    dub.close()


def enter_deposit_Checking_USD(pin=int, usd=int):
    b = BtcConverter()
    btc_val = b.convert_to_btc(usd, 'USD')
    BTC_EU = b.convert_btc_to_cur(btc_val, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(btc_val, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(btc_val, 'CNY')
    dub.execute("UPDATE InovClientsCrypto SET BTC=BTC+? WHERE SDC=?", [btc_val, pin])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD+? WHERE SDC=?", [usd, pin])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU+? WHERE SDC=?", [BTC_EU, pin])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP+? WHERE SDC=?", [BTC_GBP, pin])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY+? WHERE SDC=?", [BTC_CNY, pin])
    dub.close()


def enter_deposit_Checking_EU(pin=int, eu=int):
    b = BtcConverter()
    btc_val = b.convert_to_btc(eu, 'EUR')
    BTC_USD = b.convert_btc_to_cur(btc_val, 'USD')
    BTC_GBP = b.convert_btc_to_cur(btc_val, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(btc_val, 'CNY')
    dub.execute("UPDATE InovClientsCrypto SET BTC=BTC+? WHERE SDC=?", [btc_val, pin])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD+? WHERE SDC=?", [BTC_USD, pin])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU+? WHERE SDC=?", [eu, pin])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP+? WHERE SDC=?", [BTC_GBP, pin])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY+? WHERE SDC=?", [BTC_CNY, pin])
    dub.close()


def enter_deposit_Checking_GBP(pin=int, gbp=int):
    b = BtcConverter()
    btc_val = b.convert_to_btc(gbp, 'GBP')
    BTC_USD = b.convert_btc_to_cur(btc_val, 'USD')
    BTC_EU = b.convert_btc_to_cur(btc_val, 'EUR')
    BTC_CNY = b.convert_btc_to_cur(btc_val, 'CNY')
    dub.execute("UPDATE InovClientsCrypto SET BTC=BTC+? WHERE SDC=?", [btc_val, pin])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD+? WHERE SDC=?", [BTC_USD, pin])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU+? WHERE SDC=?", [BTC_EU, pin])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP+? WHERE SDC=?", [gbp, pin])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY+? WHERE SDC=?", [BTC_CNY, pin])
    dub.close()


def enter_deposit_Checking_CNY(pin=int, cny=int):
    b = BtcConverter()
    btc_val = b.convert_to_btc(cny, 'CNY')
    BTC_USD = b.convert_btc_to_cur(btc_val, 'USD')
    BTC_EU = b.convert_btc_to_cur(btc_val, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(btc_val, 'GBP')

    dub.execute("UPDATE InovClientsCrypto SET BTC=BTC+? WHERE SDC=?", [btc_val, pin])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD+? WHERE SDC=?", [BTC_USD, pin])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU+? WHERE SDC=?", [BTC_EU, pin])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP+? WHERE SDC=?", [BTC_GBP, pin])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY+? WHERE SDC=?", [cny, pin])
    dub.close()


def use_atm_Checking(name=str, f=int):
    r = 0.03
    b = BtcConverter()
    fa = (f * r)
    fp = (fa + f)
    fy = (fp - f)
    # Amount withdrew
    BTC_USD = b.convert_btc_to_cur(f, 'USD')
    BTC_EU = b.convert_btc_to_cur(f, 'EUR')
    BTC_GBP = b.convert_btc_to_cur(f, 'GBP')
    BTC_CNY = b.convert_btc_to_cur(f, 'CNY')
    # service fee charged
    BTC_USD_Rate = b.convert_btc_to_cur(fy, 'USD')
    BTC_EU_Rate = b.convert_btc_to_cur(fy, 'EUR')
    BTC_GBP_Rate = b.convert_btc_to_cur(fy, 'GBP')
    BTC_CNY_Rate = b.convert_btc_to_cur(fy, 'CNY')
    # Atm Withdrawal
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [f, name])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD-? WHERE name=?", [BTC_USD, name])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU-? WHERE name=?", [BTC_EU, name])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP-? WHERE name=?", [BTC_GBP, name])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY-? WHERE name=?", [BTC_CNY, name])
    # dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [r, name])
    # Service fee transaction
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=INOVCrypto', [fy, name])
    dub.execute("UPDATE InovClientsCrypto SET USD=USD-? WHERE name=INOVCrypto", [BTC_USD_Rate, name])
    dub.execute("UPDATE InovClientsCrypto SET EU=EU-? WHERE name=INOVCrypto", [BTC_EU_Rate, name])
    dub.execute("UPDATE InovClientsCrypto SET GBP=GBP-? WHERE name=INOVCrypto", [BTC_GBP_Rate, name])
    dub.execute("UPDATE InovClientsCrypto SET CNY=CNY-? WHERE name=INOVCrypto", [BTC_CNY_Rate, name])

    # dub.execute('UPDATE InovClientsData SET Current=Current+? WHERE name=INOV Financials Inc.', [r])
    dub.close()


def get_new_pin(n=str):
    priv = ccard.visa()
    to_string = str(priv)
    pr = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    sdc = f.encrypt(pr)
    dub.execute('UPDATE InovClientsCrypto SET DCL=? WHERE name=?', [c_value, n])
    dub.execute('UPDATE InovClientsCrypto SET SDC=? WHERE name=?', [sdc, n])
    # pinNo = '{}  this is a generated code that will be used to manage your account for Securitization.'
    # print(pinNo.format(new_p))
    dclNo = '{} this is your secured credit number, this number will be your main account charged with most ' \
            'transactions you make.' \
            'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
            'these six digits. '
    print(dclNo.format(pr))
    dub.close()


def send_money_BTC(bt=int, n1=str, n2=str):
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [bt, n1])

    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC+? WHERE name=?', [bt, n2])
    dub.close()


def send_money_USD(t=int, n1=str, n2=str):
    b = BtcConverter()
    USD_BTC = b.convert_to_btc(t, 'USD')
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [USD_BTC, n1])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD-? WHERE name=?', [t, n1])

    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC+? WHERE name=?', [USD_BTC, n2])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD+? WHERE name=?', [t, n2])
    dub.close()


def send_money_EU(t=int, n1=str, n2=str):
    b = BtcConverter()
    EU_BTC = b.convert_to_btc(t, 'EUR')
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [EU_BTC, n1])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD-? WHERE name=?', [t, n1])

    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC+? WHERE name=?', [EU_BTC, n2])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD+? WHERE name=?', [t, n2])
    dub.close()


def send_money_GBP(t=int, n1=str, n2=str):
    b = BtcConverter()
    GBP_BTC = b.convert_to_btc(t, 'GBP')
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [GBP_BTC, n1])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD-? WHERE name=?', [t, n1])

    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC+? WHERE name=?', [GBP_BTC, n2])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD+? WHERE name=?', [t, n2])
    dub.close()


def send_money_CNY(t=int, n1=str, n2=str):
    b = BtcConverter()
    CNY_BTC = b.convert_to_btc(t, 'CNY')
    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC-? WHERE name=?', [CNY_BTC, n1])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD-? WHERE name=?', [t, n1])

    dub.execute('UPDATE InovClientsCrypto SET BTC=BTC+? WHERE name=?', [CNY_BTC, n2])
    dub.execute('UPDATE InovClientsCrypto SET USD=USD+? WHERE name=?', [t, n2])
    dub.close()


def get_current_prices():
    b = BtcConverter()
    USD_price = b.get_latest_price('USD')
    EU_price = b.get_latest_price('EUR')
    GBP_price = b.get_latest_price('GBP')
    CNY_price = b.get_latest_price('CNY')
    print("Latest prices:")
    print(USD_price)
    print(EU_price)
    print(GBP_price)
    print(CNY_price)


# email notifications
def send_mail_for_personal_loan(mw=str, pl=int, c=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mw
    password = "Forsure34"

    message = "You have just Received a Personal Loan from OIB that has deposited $ " + [
        {pl}] + "into your " + c + " account."
    # Gmail Accounts
    if "gmail" in mw:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mw:
        fromMy = "openbank143@yahoo.com"
        to = mw
        subj = 'Personal Loan'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)


def send_mail_for_business_loan(bl2=int, mt=str, c=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mt
    password = "Forsure34"
    message = "You have received a Business loan from OIB that has been deposited  $" + [
        {bl2}] + "into your " + c + " account"
    # Gmail Accounts
    if "gmail" in mt:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mt:
        fromMy = "openbank143@yahoo.com"
        to = mt
        subj = 'Business Loan'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)


def send_mail_for_new_pin(p=int, mz=str):
    msg = "{} this is your Temporary password. Please use it to login and get a new DCL"
    new = (msg.format(p))

    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mz
    password = "Forsure34"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        print('ok the email has sent ')


def send_mail_for_new_Crypt(Cryp=int, mz=str):
    msg = "{} this is your Digital Credit Code Please memorize the last 6 digits"
    new = (msg.format(Cryp))

    sender_email = "openinternationalbanking@gmail.com"
    rec_email = mz
    password = "Forsure34"
    message = new
    # Gmail Accounts
    if "gmail" in mz:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in mz:
        fromMy = "openbank143@yahoo.com"
        to = mz
        subj = 'New Pin Number'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        print('ok the email has sent ')


def send_mail_for_Transactions(n=str, m=str, ts=int):
    email = m
    trans = ts
    name = n

    sender_email = "monetarytransatlantic@gmail.com"
    rec_email = email
    password = "Forsure34"
    message = "You have received $" + trans + " from " + name
    # Gmail Accounts
    if "gmail" in email:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in email:
        fromMy = 'dokoronkwo167@yahoo.com'
        to = email
        subj = 'Transaction'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = 'dokoronkwo167@yahoo.com'
        password2 = "jiegwhlsvpkrpuag"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)


def send_mail_for_new_account(m2=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = m2
    password = "Forsure34"
    message = "CONGRATS!!! You have just opened a new account with INOV Financials Inc. " \
              "INOV is a fintech platform " \
              "that gives users full control over their traditional banking and personal finance." \
              "To see more things you can do on the go with INOV feel free to check the application."
    # Gmail Accounts
    if "gmail" in m2:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in m2:
        fromMy = "openbank143@yahoo.com"
        to = m2
        subj = 'NEW ACCOUNT!!!!!'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)
        print('ok the email has sent ')


def send_mail_for_deposits_checking(depo=int, m3=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = m3
    password = "Forsure34"
    message = "You just made a deposit into your Current account of $ " + [{depo}]
    # Gmail Accounts
    if "gmail" in m3:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in m3:
        fromMy = "openbank143@yahoo.com"
        to = m3
        subj = 'Current account Deposit'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)


def send_mail_for_deposits_saving(depo2=int, m4=str):
    sender_email = "openinternationalbanking@gmail.com"
    rec_email = m4
    password = "Forsure34"
    message = "You just made a deposit into your savings account of $ " + [{depo2}]
    # Gmail Accounts
    if "gmail" in m4:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, rec_email, message)
    # Yahoo Accounts
    if "yahoo" in m4:
        fromMy = "openbank143@yahoo.com"
        to = m4
        subj = 'Savings account Deposit'

        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromMy, to, subj, message)

        username = "openbank143@yahoo.com"
        password2 = "holiday20!"
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password2)
        server.sendmail(fromMy, to, msg)

