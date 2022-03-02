from sqlalchemy import create_engine
from forex_python.converter import CurrencyRates
from cryptography.fernet import Fernet
# import IFP
import smtplib
import ccard

# Personal Credit/Debit Account Database
db_connect = create_engine('sqlite:///data.db')
data_d = db_connect.cursor()
# Personal Credit & Debit Account Database
pcd_connect = create_engine('sqlite:///JointAccountdata.db')
pcd = pcd_connect.cursor()
# Business Credit Account Database
cd_connect = create_engine('sqlite:///BusinessAccntdata.db')
cd = cd_connect.cursor()
# Transactions Database
db = create_engine('sqlite:///transactions.db')
dub = db.cursor()


def login_to_account(name=str, cryp=str):
    # Personal Credit/Debit Account
    sort = data_d.execute('SELECT name, SDC, IIF(name=?, SDC=?, \'Login successful\', \'login failed\') FROM '
                        'InovClientsData;', name, cryp)
    print(sort)
    # Business Credit Account
    sort = cd.execute('SELECT name, SDC, IIF(name=?, SDC=?, \'Login successful\', \'login failed\') FROM '
                      'InovClientsBusiness;', name, cryp)
    print(sort)
    # Personal Credit & Debit Account
    sort = pcd.execute('SELECT name, SDC, IIF(name=?, SDC=?, \'Login successful\', \'login failed\') FROM '
                      'InovClientsJointAccountData;', name, cryp)
    print(sort)


# delete account
def delete_accnt(name=str, email=str):
    # Personal Credit/Debit Account
    data_d.execute("DELETE from InovClientsData WHERE name=?, email=?", name, email)
    data_d.close()
    print("account deleted")
    # Business Credit Account
    cd.execute("DELETE from InovClientsBusiness WHERE name=?, email=?", name, email)
    cd.close()
    print("account deleted")
    # Personal Credit & Debit Account
    pcd.execute("DELETE from InovClientsJointAccountData WHERE name=?, WHERE email=?", name, email)
    pcd.close()
    print("account deleted")


# create Business Credit Account
def create_business_accnt(accnt_name2=str, email2=str, addy2=str, cou2=str, cur2=str, account_type=str):
    priv = ccard.americanexpress()
    to_string = str(priv)
    pin = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    scd = f.encrypt(pin)
    business_type = input("what Industry does your business operate in:")
    Credit_Checking_amt = int(input('How much do you want to deposit into your Business Credit Checkings account p.s. '
                                    'min deposit is. 50,000 '
                                    'required max '
                                    'deposit is '
                                    '100,000: '))
    if Credit_Checking_amt > 100000 or Credit_Checking_amt < 50000:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
    Credit_Savings_amt = int(
        input('How much do you want to deposit into your Business Credit Savings account p.s. min deposit is 150,000'
              'required max '
              'deposit is '
              '500,000: '))
    if Credit_Savings_amt > 500000 or Credit_Savings_amt < 150000:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
        read_data = "INSERT INTO InovClientsBusiness (name, email, Pin, SDC, DCL, Type, Atype, Credit, Checking, " \
                    "Saving, " \
                    "Address, " \
                    "Country, " \
                    "Currency) " \
                    "VALUES ( " \
                    "?, " \
                    "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        val = (
            accnt_name2, email2, pin, scd, c_value, business_type, account_type, Credit_Checking_amt,
            Credit_Savings_amt,
            addy2,
            cou2, cur2)
        cd.execute(read_data, val)
        dclNo = '{} this is your secured credit number, this number will be your main account charged with most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        print(dclNo.format(pin))
        print("Account created")
        cd.close()
        # create_accnt(accnt_name2, email2, addy2, cou2, cur2)


# create Credit & Debit Account
def create_JointCreditDebit_accnt(accnt_name=str, email=str, addy=str, cou=str, cur=str):
    priv = ccard.americanexpress()
    to_string = str(priv)
    pin = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    scd = f.encrypt(pin)
    Accnt_type1 = 'Credit account'
    Accnt_type2 = 'Debit account'
    Credit_Checking_amt = int(input('How much do you want to deposit into your Credit Checkings account p.s. no '
                                    'min deposit '
                                    'required max '
                                    'deposit is '
                                    '5,000: '))
    if Credit_Checking_amt > 5000 or Credit_Checking_amt < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
    Credit_Savings_amt = int(
        input('How much do you want to deposit into your Credit Savings account p.s. no min deposit '
              'required max '
              'deposit is '
              '15,000: '))
    if Credit_Savings_amt > 15000 or Credit_Savings_amt < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
    Debit_Checking_amt = int(input('How much do you want to deposit into your Debit Checkings account p.s. no '
                                   'min deposit '
                                   'required max '
                                   'deposit is '
                                   '5,000: '))
    if Debit_Checking_amt > 5000 or Debit_Checking_amt < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
    Debit_Savings_amt = int(
        input('How much do you want to deposit into your Debit Savings account p.s. no min deposit '
              'required max '
              'deposit is '
              '15,000: '))
    if Debit_Savings_amt > 15000 or Debit_Savings_amt < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
        read_data = "INSERT INTO InovClientsJointAccountData (name, email, Pin, SDC, DCL, CreditAccount, " \
                    "CreditChecking, " \
                    "CreditSaving, DebitAccount, " \
                    "DebitChecking, " \
                    "DebitSaving, Address, Country, " \
                    "Currency) " \
                    "VALUES ( " \
                    "?, " \
                    "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        val = (accnt_name, email, pin, scd, c_value, Accnt_type1, Credit_Checking_amt, Credit_Savings_amt, Accnt_type2,
               Debit_Checking_amt, Debit_Savings_amt, addy, cou, cur)
        pcd.execute(read_data, val)
        pcd.close()
        dclNo = '{} this is your secured credit number, this number will be your main account charged with most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        print(dclNo.format(pin))
        print("Account created")


# create Credit Account
def create_Credit_accnt(accnt_name=str, email=str, addy=str, cou=str, cur=str):
    priv = ccard.americanexpress()
    to_string = str(priv)
    pin = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    scd = f.encrypt(pin)
    a_type1 = "Credit Account"
    current = int(input('How much do you want to deposit into this account p.s. no min deposit required max '
                        'deposit is '
                        '5,000: '))
    if current > 5000 or current < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
    savings = int(input('How much do you want to deposit into this account p.s. no min deposit required max '
                        'deposit is '
                        '15,000: '))
    if savings > 15000 or savings < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
        sql = "INSERT INTO InovClientsData (name, email, Pin, SDC, DCL, Type, Current, Saving, Address, Country, " \
              "Currency) " \
              "VALUES ( " \
              "?, " \
              "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        val = (accnt_name, email, pin, scd, c_value, a_type1, current, savings, addy, cou, cur)
        data_d.execute(sql, val)
        data_d.close()
        dclNo = '{} this is your secured credit number, this number will be your main account charged with most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        print(dclNo.format(pin))
        print("Account created")


# create Debit Account
def create_Debit_accnt(accnt_name=str, email=str, addy=str, cou=str, cur=str):
    priv = ccard.americanexpress()
    to_string = str(priv)
    pin = to_string[:5]
    c_value = Fernet.generate_key()
    Crypt = c_value[:5]
    f = Fernet(Crypt)
    scd = f.encrypt(pin)
    a_type1 = "Debit Account"
    current = int(input('How much do you want to deposit into this account p.s. no min deposit required max '
                        'deposit is '
                        '5,000: '))
    if current > 5000 or current < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
    savings = int(input('How much do you want to deposit into this account p.s. no min deposit required max '
                        'deposit is '
                        '15,000: '))
    if savings > 15000 or savings < 0:
        print("deposit does not meet requirement, try again")
        # IFP.OpenAccount()
        sql = "INSERT INTO InovClientsData (name, email, Pin, SDC, DCL, Type, Current, Saving, Address, Country, " \
              "Currency) " \
              "VALUES ( " \
              "?, " \
              "?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) "
        val = (accnt_name, email, pin, scd, c_value, a_type1, current, savings, addy, cou, cur)
        data_d.execute(sql, val)
        data_d.close()
        dclNo = '{} this is your secured credit number, this number will be your main account charged with most ' \
                'transactions you make.' \
                'This is to ensure safer payment and build a more secure wall around your credit. Please memorize ' \
                'these first five digits. '
        print(dclNo.format(pin))
        print("Account created")


def deposit_option(name=str, ans=str):
    if ans == "1":
        dep = int(input("How much would you like to deposit today: "))
        deposit_Checking(name, dep)
        print("deposit has been made")
        # EmailSender.send_mail_for_deposits_checking(dep, email)

    if ans == "2":
        dep = int(input("How much would you like to deposit today: "))
        deposit_Savings(name, dep)
        print("deposit has been made")
        # EmailSender.send_mail_for_deposits_saving(dep, email)

    # IFP.intro()


def deposit_Checking(x=str, y=int):
    # Personal Credit/Debit Account
    data_d.execute("UPDATE InovClientsData SET Current=Current+? WHERE name=?", [y, x])
    # Personal Credit & Debit Account
    pcd.execute("UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking+? WHERE name=?", [y, x])
    # Business Credit Account
    cd.execute("UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=?", [y, x])
    data_d.close()
    pcd.close()
    cd.close()


def deposit_Savings(x=str, y=int):
    # Personal Credit/Debit Account
    data_d.execute("UPDATE InovClientsData SET Saving=Saving+? WHERE name=?", [y, x])
    # Personal Credit & Debit Account
    pcd.execute("UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving+? WHERE name=?", [y, x])
    # Business Credit Account
    cd.execute("UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=?", [y, x])
    data_d.close()
    pcd.close()
    cd.close()


def atm_option(name=str, var=str):
    if var == "Checkings":
        dep = int(input("How much would you like to withdraw today: "))
        print("You will be charged 1.3% upon withdrawal")
        rate_r = dep * 0.013
        atm_Checking(name, dep, rate_r)
        print("Money withdrawn, have a great day!")

    if var == "Savings":
        dep = int(input("How much would you like to withdraw today: "))
        print("You will be charged 1.3% upon withdrawal")
        rate_r = dep * 0.013
        atm_Savings(name, dep, rate_r)
        print("Money withdrawn, have a great day!")

    


def atm_Checking(d=str, f=int, r=int):
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [f, d])
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [r, d])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [r])
    # Personal Credit & Debit Account
    pcd.execute("UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?", [f, d])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [r, d])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [r])
    data_d.close()
    pcd.close()
    cd.close()


def atm_Savings(d=str, f=int, r=int):
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [f, d])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [r, d])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [r])
    # Personal Credit & Debit Account
    pcd.execute("UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?", [f, d])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [r, d])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [r])
    data_d.close()
    pcd.close()
    cd.close()


def reactivate_account(name=str, dcl=str):
    # Personal Credit/Debit Account
    data_current = data_d.execute("SELECT name, Type FROM InovClientsData WHERE DCL=?", [dcl])
    res = data_current.fetchall()
    for x in res:
        print("Account Name = ", x[0])
        print("Account Type = ", x[1])
    # Personal Credit & Debit Account
    data_current2 = pcd.execute("SELECT name, Type FROM InovClientsJointAccountData WHERE DCL=?", [dcl])
    res = data_current2.fetchall()
    for x in res:
        print("Account Name = ", x[0])
        print("Account Type = ", x[1])
    # Business Credit Account
    data_current = cd.execute("SELECT name, Type FROM InovClientsBusiness WHERE DCL=?", [dcl])
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
    data_d.execute('UPDATE InovClientsData SET DCL=? WHERE name=?', [c_value, name])
    data_d.execute('UPDATE InovClientsData SET SDC=? WHERE name=?', [scd, name])
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET DCL=? WHERE name=?', [c_value, name])
    pcd.execute('UPDATE InovClientsJointAccountData SET SDC=? WHERE name=?', [scd, name])
    # Business Credit Account
    cd.execute('UPDATE InovClientsBusiness SET DCL=? WHERE name=?', [c_value, name])
    cd.execute('UPDATE InovClientsBusiness SET SDC=? WHERE name=?', [scd, name])
    data_d.close()
    pcd.close()
    cd.close()
    # send_mail_for_new_Crypt(Crypt, email)
    # IFP.intro()


def send_money(t=int, n1=str, n2=str):
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [t, n1])
    data_d.execute('UPDATE InovClientsData SET Current=Current+? WHERE name=?', [t, n2])
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [t, n1])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking+? WHERE name=?', [t, n2])
    # Business Credit Account
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking-? WHERE name=?', [t, n1])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=?', [t, n2])
    data_d.close()
    pcd.close()
    cd.close()


def business_loan_checking(bl1=int, n3=str):
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=?', [bl1, n3])
    cd.close()


def business_loan_savings(bl2=int, n4=str):
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=?', [bl2, n4])
    cd.close()


def personal_loan_checking(bl3=int, n5=str):
    data_d.execute('UPDATE InovClientsData SET Current=Current+? WHERE name=?', [bl3, n5])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking+? WHERE name=?', [bl3, n5])
    data_d.close()
    pcd.close()


def personal_loan_savings(bl4=int, n6=str):
    data_d.execute('UPDATE InovClientsData SET Saving=Saving+? WHERE name=?', [bl4, n6])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving+? WHERE name=?', [bl4, n6])
    data_d.close()
    pcd.close()


def bank_statement(n=str, cr=str):
    # Personal Credit/Debit Account
    sort = data_d.execute("select * from InovClientsData WHERE name=?, SDC=?", [n, cr])
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit/Debit Account Data:")
    print(result)
    # Business Credit Account
    sort = cd.execute("select * from InovClientsBusiness WHERE name=?, SDC=?", [n, cr])
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Business Credit Account Data:")
    print(result)
    # Personal Credit & Debit Account
    sort = pcd.execute("select * from InovClientsJointAccountData WHERE name=?, SDC=?", [n, cr])
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Personal Credit & Debit Account Data:")
    print(result)


# Currency change (allows account users to convert currency cash account into the main global currencies (USD, EUR,
# GBP, CNY)
def CurrencyExchange_USD(gov=str):
    c = CurrencyRates()
    var1 = "USD"
    cex1 = c.get_rate('USD', 'USD')
    cex2 = c.get_rate('USD', 'USD')
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?',
                   [cex1, cex2, var1, gov])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [rate_r, gov])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [rate_r, gov])
    cd.execute('UPDATE InovClientsBusiness SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    data_d.close()
    cd.close()
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking/?, CreditSaving=CreditSaving/?, '
                'DebitChecking=DebitChecking/?, DebitSaving=DebitSaving/? '
                'Currency=? '
                'WHERE name=?',
                [cex1, cex2, var1, gov])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking-? WHERE name=?', [rate_r, gov])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [rate_r, gov])
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditSaving=CreditSaving-? WHERE name=?', [rate_r, gov])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving-? WHERE name=?', [rate_r, gov])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    pcd.close()
    cd.close()
    # Business Credit Account
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking/?, Saving=Saving/?, '
               'Currency=? '
               'WHERE name=?',
               [cex1, cex2, var1, gov])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking-? WHERE name=?', [rate_r, gov])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving-? WHERE name=?', [rate_r, gov])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    cd.close()


def CurrencyExchange_EUR(gov2=str):
    c = CurrencyRates()
    var2 = "EUR"
    dex1 = c.get_rate('USD', 'EUR')
    dex2 = c.get_rate('USD', 'EUR')
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?',
                   [dex1, dex2, var2, gov2])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [rate_r, gov2])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [rate_r, gov2])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    data_d.close()
    cd.close()
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking/?, CreditSaving=CreditSaving/?, '
                'DebitChecking=DebitChecking/?, DebitSaving=DebitSaving/? '
                'Currency=? '
                'WHERE name=?',
                [dex1, dex2, var2, gov2])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking-? WHERE name=?', [rate_r, gov2])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [rate_r, gov2])
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditSaving=CreditSaving-? WHERE name=?', [rate_r, gov2])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving-? WHERE name=?', [rate_r, gov2])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    pcd.close()
    cd.close()
    # Business Credit Account
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking/?, Saving=Saving/?, '
               'Currency=? '
               'WHERE name=?',
               [dex1, dex2, var2, gov2])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking-? WHERE name=?', [rate_r, gov2])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving-? WHERE name=?', [rate_r, gov2])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    cd.close()


def CurrencyExchange_GBP(gov3=str):
    c = CurrencyRates()
    var3 = "GBP"
    fex3 = c.get_rate('USD', 'GBP')
    fex4 = c.get_rate('USD', 'GBP')
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?',
                   [fex3, fex4, var3, gov3])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [rate_r, gov3])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [rate_r, gov3])
    cd.execute('UPDATE InovClientsBusiness SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    data_d.close()
    cd.close()
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking/?, CreditSaving=CreditSaving/?, '
                'DebitChecking=DebitChecking/?, DebitSaving=DebitSaving/? '
                'Currency=? '
                'WHERE name=?',
                [fex3, fex4, var3, gov3])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking-? WHERE name=?', [rate_r, gov3])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [rate_r, gov3])
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditSaving=CreditSaving-? WHERE name=?', [rate_r, gov3])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving-? WHERE name=?', [rate_r, gov3])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    pcd.close()
    cd.close()
    # Business Credit Account
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking/?, Saving=Saving/?, '
               'Currency=? '
               'WHERE name=?',
               [fex3, fex4, var3, gov3])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking-? WHERE name=?', [rate_r, gov3])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving-? WHERE name=?', [rate_r, gov3])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    cd.close()


def CurrencyExchange_AUS(gov4=str):
    c = CurrencyRates()
    var4 = "AUS"
    gex4 = c.get_rate('USD', 'AUS')
    gex5 = c.get_rate('USD', 'AUS')
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?',
                   [gex4, gex5, var4, gov4])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [rate_r, gov4])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [rate_r, gov4])
    cd.execute('UPDATE InovClientsBusiness SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    data_d.close()
    cd.close()
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking/?, CreditSaving=CreditSaving/?, '
                'DebitChecking=DebitChecking/?, DebitSaving=DebitSaving/? '
                'Currency=? '
                'WHERE name=?',
                [gex4, gex5, var4, gov4])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking-? WHERE name=?', [rate_r, gov4])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [rate_r, gov4])
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditSaving=CreditSaving-? WHERE name=?', [rate_r, gov4])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving-? WHERE name=?', [rate_r, gov4])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    pcd.close()
    cd.close()
    # Business Credit Account
    cd.execute('UPDATE InovClientsJointAccountData SET Checking=CreditChecking/?, Saving=CreditSaving/?, '
               'Currency=? '
               'WHERE name=?',
               [gex4, gex5, var4, gov4])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    cd.execute('UPDATE InovClientsJointAccountData SET Checking=Checking-? WHERE name=?', [rate_r, gov4])
    cd.execute('UPDATE InovClientsJointAccountData SET Saving=Saving-? WHERE name=?', [rate_r, gov4])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    cd.close()


def CurrencyExchange_CNY(gov5=str):
    c = CurrencyRates()
    var5 = "CNY"
    hex5 = c.get_rate('USD', 'CNY')
    hex6 = c.get_rate('USD', 'CNY')
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?',
                   [hex5, hex6, var5, gov5])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [rate_r, gov5])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [rate_r, gov5])
    cd.execute('UPDATE InovClientsBusiness SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    data_d.close()
    cd.close()
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking/?, CreditSaving=CreditSaving/?, '
                'DebitChecking=DebitChecking/?, DebitSaving=DebitSaving/? '
                'Currency=? '
                'WHERE name=?',
                [hex5, hex6, var5, gov5])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking-? WHERE name=?', [rate_r, gov5])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [rate_r, gov5])
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditSaving=CreditSaving-? WHERE name=?', [rate_r, gov5])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving-? WHERE name=?', [rate_r, gov5])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    pcd.close()
    cd.close()
    # Business Credit Account
    cd.execute('UPDATE InovClientsJointAccountData SET Checking=CreditChecking/?, Saving=CreditSaving/?, '
               'Currency=? '
               'WHERE name=?',
               [hex5, hex6, var5, gov5])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    cd.execute('UPDATE InovClientsJointAccountData SET Checking=Checking-? WHERE name=?', [rate_r, gov5])
    cd.execute('UPDATE InovClientsJointAccountData SET Saving=Saving-? WHERE name=?', [rate_r, gov5])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    cd.close()


def CurrencyExchange_JPY(gov6=str):
    c = CurrencyRates()
    var6 = "JPY"
    hex6 = c.get_rate('USD', 'JPY')
    hex7 = c.get_rate('USD', 'JPY')
    # Personal Credit/Debit Account
    data_d.execute('UPDATE InovClientsData SET Current=Current/?, Saving=Saving/? Currency=? WHERE name=?',
                   [hex6, hex7, var6, gov6])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    data_d.execute('UPDATE InovClientsData SET Current=Current-? WHERE name=?', [rate_r, gov6])
    data_d.execute('UPDATE InovClientsData SET Saving=Saving-? WHERE name=?', [rate_r, gov6])
    cd.execute('UPDATE InovClientsBusiness SET Current=Current+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    data_d.close()
    cd.close()
    # Personal Credit & Debit Account
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking/?, CreditSaving=CreditSaving/?, '
                'DebitChecking=DebitChecking/?, DebitSaving=DebitSaving/? '
                'Currency=? '
                'WHERE name=?',
                [hex6, hex7, var6, gov6])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditChecking=CreditChecking-? WHERE name=?', [rate_r, gov6])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitChecking=DebitChecking-? WHERE name=?', [rate_r, gov6])
    pcd.execute('UPDATE InovClientsJointAccountData SET CreditSaving=CreditSaving-? WHERE name=?', [rate_r, gov6])
    pcd.execute('UPDATE InovClientsJointAccountData SET DebitSaving=DebitSaving-? WHERE name=?', [rate_r, gov6])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    pcd.close()
    cd.close()
    # Business Credit Account
    cd.execute('UPDATE InovClientsJointAccountData SET Checking=CreditChecking/?, Saving=CreditSaving/?, '
               'Currency=? '
               'WHERE name=?',
               [hex6, hex7, var6, gov6])
    print("You will be charged 1.3% upon this exchange")
    rate_r = 1.50
    cd.execute('UPDATE InovClientsJointAccountData SET Checking=Checking-? WHERE name=?', [rate_r, gov6])
    cd.execute('UPDATE InovClientsJointAccountData SET Saving=Saving-? WHERE name=?', [rate_r, gov6])
    cd.execute('UPDATE InovClientsBusiness SET Checking=Checking+? WHERE name=INOV Bank.', [rate_r])
    cd.execute('UPDATE InovClientsBusiness SET Saving=Saving+? WHERE name=INOV Bank.', [rate_r])
    cd.close()


# global transactions
# 1. North America,  2. Europe, 3. South America, 4. Africa, 5. Asia, 6. Caribbean, 7. Central America
# USD base currency
def global_transactions_USD(region=int, val=int, curname=str, curname2=str, cur=str, cur2=str, name=str, name2=str):
    c = CurrencyRates()
    # North America
    if region == "1":
        reg = "North America"
        if curname == "USA" and curname2 == "Canada":
            cur = 'USD'
            cur2 = 'CAD'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Mexico":
            cur = 'USD'
            cur2 = 'MXN'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
    # Europe
    if region == "2":
        reg = "Europe"
        if curname == "USA" and curname2 == "UK":
            cur = 'USD'
            cur2 = 'GBP'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Germany":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "France":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Italy":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Spain":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Netherlands":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Switzerland":
            cur = 'USD'
            cur2 = 'CHF'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Poland":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Sweden":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
        if curname == "USA" and curname2 == "Russia":
            cur = 'USD'
            cur2 = 'RUB'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, " \
                        "?) "
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
            print("Transaction complete")
    # South America
    if region == "3":
        reg = "South America"
        if curname == "USA" and curname2 == "Argentina":
            cur = 'USD'
            cur2 = 'ARS'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Bolivia":
            cur = 'USD'
            cur2 = 'BOB'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Brazil":
            cur = 'USD'
            cur2 = 'BRL'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Chile":
            cur = 'USD'
            cur2 = 'CLP'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Colombia":
            cur = 'USD'
            cur2 = 'COP'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Peru":
            cur = 'USD'
            cur2 = 'PEN'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "US dollar" and curname2 == "Ecuador":
            # cur = 'USD'
            # cur2 = 'PEN'
            # link = c.convert(cur2, cur, val)
            send_money(val, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, val, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Venezuela":
            cur = 'USD'
            cur2 = 'VES'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Uruguay":
            cur = 'USD'
            cur2 = 'UYU'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
    # Africa
    if region == "4":
        reg = "Africa"
        if curname == "USA" and curname2 == "Nigeria":
            cur = 'USD'
            cur2 = 'NGN'
            link = c.convert(cur, cur2, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "South Africa":
            reg = "Africa"
            cur = 'USD'
            cur2 = 'ZAR'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Egypt":
            cur = 'USD'
            cur2 = 'EGP'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Algeria":
            cur = 'USD'
            cur2 = 'DZD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Morocco":
            cur = 'USD'
            cur2 = 'MAD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Kenya":
            cur = 'USD'
            cur2 = 'KES'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Ethiopia":
            cur = 'USD'
            cur2 = 'ETB'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Ghana":
            cur = 'USD'
            cur2 = 'GHS'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Angola":
            cur = 'USD'
            cur2 = 'AOA'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Tanzania":
            cur = 'USD'
            cur2 = 'TZS'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Ivory Coast":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Cameroon":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
    # Asia
    if region == "5":
        reg = "Asia/Middle East"
        if curname == "USA" and curname2 == "China":
            cur = 'USD'
            cur2 = 'CNY'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Japan":
            cur = 'USD'
            cur2 = 'JPY'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "India":
            cur = 'USD'
            cur2 = 'INR'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "South Korea":
            cur = 'USD'
            cur2 = 'KRW'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Indonesia":
            cur = 'USD'
            cur2 = 'IDR'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Saudi Arabia":
            cur = 'USD'
            cur2 = 'SAR'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Taiwan":
            cur = 'USD'
            cur2 = 'TWD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Thailand":
            cur = 'USD'
            cur2 = 'THB'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "UAE":
            cur = 'USD'
            cur2 = 'AED'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Israel":
            cur = 'USD'
            cur2 = 'ILS'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Philippines":
            cur = 'USD'
            cur2 = 'PHP'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Hong Kong":
            cur = 'USD'
            cur2 = 'HKD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Singapore":
            cur = 'USD'
            cur2 = 'SGD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Malaysia":
            cur = 'USD'
            cur2 = 'MYR'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Bangladesh":
            cur = 'USD'
            cur2 = 'BDT'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Vietnam":
            cur = 'USD'
            cur2 = 'VND'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
    # Caribbean
    if region == "6":
        reg = "Caribbean"
        if curname == "USA" and curname2 == "Antigua":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Bahamas":
            cur = 'USD'
            cur2 = 'BSD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Belize":
            cur = 'USD'
            cur2 = 'BZD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Dominica":
            cur = 'USD'
            cur2 = 'DOP'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Grenada":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Guyana":
            cur = 'USD'
            cur2 = 'GYD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Jamaica":
            cur = 'USD'
            cur2 = 'JMD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Puerto Rico":
            # cur = 'USD'
            # cur2 = 'GYD'
            # link = c.convert(cur2, cur, val)
            send_money(val, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, val, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "St. Kitts and Nevis":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "St. Lucia":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "St. Vincent & Grendalines":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Suriname":
            cur = 'USD'
            cur2 = 'SRD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Trinidad & Tobago":
            cur = 'USD'
            cur2 = 'TTD'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
    # Central America
    if region == "7":
        reg = "Central America"
        if curname == "USA" and curname2 == "Guatemala":
            cur = 'USD'
            cur2 = 'GTQ'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Panama":
            cur = 'USD'
            cur2 = 'PAB'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Costa Rica":
            cur = 'USD'
            cur2 = 'CRC'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "El Salvador":
            # cur = 'USD'
            # cur2 = 'PAB'
            # link = c.convert(cur2, cur, val)
            send_money(val, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, val, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Honduras":
            cur = 'USD'
            cur2 = 'HNL'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()
        if curname == "USA" and curname2 == "Nicaragua":
            cur = 'USD'
            cur2 = 'NIO'
            link = c.convert(cur2, cur, val)
            send_money(link, name, name2)
            data_link = "INSERT INTO BankTransactions (name, Value, Region, Currency) VALUES (?, ?, ?, ?)"
            data_src = (name, link, reg, cur2)
            dub.execute(data_link, data_src)
            db.commit()


def loan_option(n=str, em=str, ans=str):
    if ans == "1":
        Business_loan_system(n, em)
    else:
        personal_loan_system(n, em)


def personal_loan_system(name=str, email=str):
    print("Personal loans are given at an interest rate of 1.5%")
    print("Loan amounts for range from 5,000 - 100,000")
    personal_loan = int(input("please enter loan amount: "))
    if personal_loan == 5000:
        r = 0.015
        n = 12
        p = personal_loan * (1 - (1 + r) ^ -n) / r
        result = "Your Loan has been granted INOV, you will be paying {} monthly over a 12 month " \
                 "period "
        print(result.format(p))
    if 5000 > personal_loan <= 75000:
        r = 0.015
        n = 24
        p = personal_loan * (1 - (1 + r) ^ -n) / r
        result = "Your Loan has been granted INOV, you will be paying {} monthly over a 24 month " \
                 "period "
        print(result.format(p))
    if 75000 > personal_loan <= 100000:
        r = 0.015
        n = 24
        p = personal_loan * (1 - (1 + r) ^ -n) / r
        result = "Your Loan has been granted from Inov Bank, you will be paying {} monthly over " \
                 "a " \
                 "36 month period "
        print(result.format(p))
    print("Where would you like to deposit this loan")
    print("========== (1). Current ==========")
    print("========== (2). Savings ==========")
    choice = input()
    if choice == "1":
        personal_loan_checking(personal_loan, name)
    if choice == "2":
        personal_loan_savings(personal_loan, name)

    send_mail_for_personal_loan(email, personal_loan, choice)


def Business_loan_system(name=str, email=str):
    print("Personal loans are given at an interest rate of 1.5-2.4%")
    print("Loan amounts for range from 750,000 - 2,000,000")
    personal_loan = int(input("please enter loan amount: "))
    if personal_loan == 750000:
        r = 0.015
        n = 12
        p = personal_loan * (1 - (1 + r) ^ -n) / r
        result = "Your Loan has been granted INOV, you will be paying {} monthly over a 12 month " \
                 "period "
        print(result.format(p))
    if 750000 > personal_loan <= 1000000:
        r = 0.019
        n = 24
        p = personal_loan * (1 - (1 + r) ^ -n) / r
        result = "Your Loan has been granted INOV, you will be paying {} monthly over a 24 month " \
                 "period "
        print(result.format(p))
    if 1000000 > personal_loan <= 200000:
        r = 0.024
        n = 36
        p = personal_loan * (1 - (1 + r) ^ -n) / r
        result = "Your Loan has been granted from Inov Bank, you will be paying {} monthly over " \
                 "a " \
                 "36 month period "
        print(result.format(p))
    print("Where would you like to deposit this loan")
    print("========== (1). Current ==========")
    print("========== (2). Savings ==========")
    choice = input()
    if choice == "1":
        business_loan_checking(personal_loan, name)
    if choice == "2":
        business_loan_savings(personal_loan, name)

    send_mail_for_business_loan(email, personal_loan, choice)


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


def send_mail_for_new_Crypt(Cryp=str, mz=str):
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
