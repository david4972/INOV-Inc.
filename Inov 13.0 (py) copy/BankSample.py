# Digital Bank sample Testing implementation of INOV API

import inov


def Intro():
    print("Welcome to INOVBank, Please select what you'd like to do today")
    print("1) Create Account")
    print("2) send money")
    print("3) deposit money")
    print("4) Currency Exchange")
    print("5) Delete account")
    print("6) Exit")
    select = input()
    if select == "1":
        create_account()
    if select == "2":
        send()
    if select == "3":
        deposit_money()
    if select == "4":
        currency_Exchange()
    if select == "5":
        delete_account()
    if select == "6":
        exit(0)


def create_account():
    name = input("Please enter account name = ")  # account name
    email = input("please enter email = ")  # account email
    address = input("Please enter address = ")  # address of account holder
    Check_amount = float(
        input("enter amount you will deposit into your new checking account today = "))  # Checking amount
    Sav_amount = float(input("enter amount you will deposit into your new saving account today = "))
    print("Please select account you'd like to create")
    print("1. Debit ")
    print("2. Credit")
    print("3. Debit (International) ")
    choice = input()
    if choice == "1":
        inov.create_Debit_account(name, email, address, Check_amount, Sav_amount)
    if choice == "2":
        inov.create_Credit_account(name, email, address, Check_amount, Sav_amount)
    if choice == "3":
        print("please enter the currency code of your country, i.e. USD (United States)")
        country = input()
        inov.create_international_debit_accnt(name, email, address, country, Check_amount, Sav_amount)


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
    card_num = int(input("please enter your card number = "))
    recipient = str(input("please enter account name of person receiving money = "))
    amount = float(input("enter amount you will be sending = "))  # requested amount for transactions
    print("please enter the country you are sending money too")
    cou = input()
    print("what account do you have?")
    print("1. Debit")
    print("2. Credit")
    ans = input()
    if ans == "1":
        inov.international_send_debit(amount, recipient, card_num, cou)
    if ans == "2":
        inov.international_send_credit(amount, recipient, card_num, cou)



def currency_Exchange():
    card_num = int(input("please enter your card number = "))
    print("please select account?")
    print("1. Debit")
    print("2. Credit")
    accnt = input()
    ans = input("please enter name of Country you'd like to exchange account too = ")
    if accnt == "1":
        inov.currency_exchange_debit(card_num, ans)
    if accnt == "2":
        inov.currency_exchange_credit(card_num, ans)



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


def delete_account():
    card_num = int(input("please enter card number = "))  # virtual card of account holder
    print("which account do you have?")
    print("1. Credit")
    print("2. Debit")
    print("3. International Debit")
    opt = input()
    if opt == "1":
        inov.delete_accnt_credit(card_num)
    if opt == "2":
        inov.delete_accnt_debit(card_num)
    if opt == "3":
        inov.delete_accnt_InternationalDebit(card_num)


if __name__ == '__main__':
    Intro()
