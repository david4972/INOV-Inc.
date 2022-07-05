# Digital Bank sample Testing implementation of INOV API

import inov


def Intro():
    print("Welcome to INOVBank, Please select what you'd like to do today")
    print("1) Create Account")
    print("2) send money")
    print("3) deposit money")
    print("4) Currency Exchange")
    select = input()
    if select == "1":
        create_account()
    if select == "2":
        send()
    if select == "3":
        deposit_money()
    if select == "4":
        currency_Exchange()


def create_account():
    name = input("Please enter account name = ")  # account name
    email = input("please enter email = ")  # account email
    address = input("Please enter address = ")  # address of account holder
    print("Please select account you'd like to create")
    print("1. Debit ")
    print("2. Credit")
    print("3. Business Credit")
    print("4. Debit (International) ")
    choice = input()
    if choice == "1":
        inov.create_Debit_account(name, email, address)
    if choice == "2":
        inov.create_Credit_account(name, email, address)
    if choice == "3":
        inov.create_business_account(name, email, address)
    if choice == "4":
        print("please enter the currency code of your country, i.e. USD (United States)")
        country = input()
        inov.create_international_debit_accnt(name, email, address, country)


def send():
    print("Is this an International Transfer?")
    print("1. Yes")
    print("2. No")
    choice = input()
    if choice == "1":
        send_International()
    if choice == "2":
        name = str(input("please enter account name = "))
        recipient = str(input("please enter account name of person receiving money = "))
        amount = float(input("enter amount you will be sending = "))  # requested amount for transactions
        card_num = int(input("please enter your card number = "))
        print("what account do you have?")
        print("1. Debit")
        print("2. Credit")
        ans = input()
        if ans == "1":
            inov.send_money_Debit(amount, card_num, recipient, name)
        if ans == "2":
            inov.send_money_Credit(amount, card_num, recipient, name)


def send_International():
    name = str(input("please enter account name = "))
    recipient = str(input("please enter account name of person receiving money = "))
    amount = float(input("enter amount you will be sending = "))  # requested amount for transactions
    card_num = int(input("please enter your card number = "))
    print("Please select the region you are sending monet too?")
    print("1. North America")
    print("2. Europe")
    print("3. South America")
    print("4. Africa")
    print("5. Asia")
    print("6. Caribbean")
    print("7. Central America")
    region = input()
    print("please enter the country you are sending money too")
    cou = input()
    print("what account do you have?")
    print("1. Debit")
    print("2. Credit")
    ans = input()
    if region == "1":
        inov.international_send_NorthAmerica(region, amount, cou, name, recipient, ans, card_num)
    if ans == "2":
        inov.international_send_Europe(region, amount, cou, name, recipient, ans, card_num)
    if ans == "3":
        inov.international_send_SouthAmerica(region, amount, cou, name, recipient, ans, card_num)
    if ans == "4":
        inov.international_send_Africa(region, amount, cou, name, recipient, ans, card_num)
    if ans == "5":
        inov.international_send_Asia_Middle_East(region, amount, cou, name, recipient, ans, card_num)
    if ans == "6":
        inov.international_send_Carribbean(region, amount, cou, name, recipient, ans, card_num)
    if ans == "7":
        inov.international_send_CentralAmerica(region, amount, cou, name, recipient, ans, card_num)


def currency_Exchange():
    print("Will you be exchanging to USD today?")
    print("1. Yes")
    print("2. No")
    c = input()
    if c == "1":
        currency_Exchange_USD()
    if c == "2":
        print("Will you be exchanging to USD today?")

        name = str(input("please enter account name = "))
        card_num = int(input("please enter your card number = "))
        print("please select account?")
        print("1. Debit")
        print("2. Credit")
        accnt = input()
        print("Please select")
        print("1. Euros")
        print("2. British Pound")
        print("3. Australian Dollar")
        print("4. Chinese Yen")
        ans = input()
        if accnt == "1":
            inov.currency_exchange_debit(card_num, ans)
        if accnt == "2":
            inov.currency_exchange_credit(card_num, ans)


def currency_Exchange_USD():
    code = str(input("Please enter currency code of the currency on your account: "))
    name = str(input("please enter account name = "))
    card_num = int(input("please enter your card number = "))
    print("please select account?")
    print("1. Debit")
    print("2. Credit")
    accnt = input()
    if accnt == "1":
        inov.currency_exchange_debit_USD(name, card_num, code)
    if accnt == "2":
        inov.currency_exchange_credit_USD(name, card_num, code)


def deposit_money():
    print("will you depositing into an international account?")
    print("1. Yes")
    print("2. No")
    inter_accnt = input()
    if inter_accnt == "1":
        deposit_money_International()
    if inter_accnt == "2":
        card_num = int(input("please enter card number = "))  # virtual card of account holder
        amount = float(input("enter amount you will deposit today = "))
        print("which deposit would you like to make?")
        print("1. Checking")
        print("2. Saving")
        opt = input()
        if opt == "1":
            inov.deposit_Checking(amount, card_num)
        if opt == "2":
            inov.deposit_Savings(amount, card_num)


def deposit_money_International():
    card_num = int(input("please enter card number = "))  # virtual card of account holder
    amount = float(input("enter amount you will deposit today = "))
    print("which deposit would you like to make?")
    print("1. Checking")
    print("2. Saving")
    opt = input()
    if opt == "1":
        inov.International_deposit_Checking(amount, card_num)
    if opt == "2":
        inov.International_deposit_Savings(amount, card_num)


if __name__ == '__main__':
    Intro()

