import sqlite3
import inov
from forex_python.converter import CurrencyRates


# global transactions
# 1. North America,  2. Europe, 3. South America, 4. Africa, 5. Asia, 6. Caribbean, 7. Central America
# Supports 70 Countries across all 7 Continents
# USD base currency
# 1. North America
def global_transactions_NA(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    # North America
    if region == "1":
        # reg = "North America"
        if curname == "Canada":
            cur = 'USD'
            cur2 = 'CAD'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Mexico":
            cur = 'USD'
            cur2 = 'MXN'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


# 2. Europe
def global_transactions_EU(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    if region == "2":
        # reg = "Europe"
        if curname == "UK":
            cur = 'USD'
            cur2 = 'GBP'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Germany":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "France":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Italy":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Spain":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Netherlands":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Switzerland":
            cur = 'USD'
            cur2 = 'CHF'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Poland":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Sweden":
            cur = 'USD'
            cur2 = 'EUR'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Russia":
            cur = 'USD'
            cur2 = 'RUB'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


# South America
def global_transactions_SA(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    if region == "3":
        # reg = "South America"
        if curname == "Argentina":
            cur = 'USD'
            cur2 = 'ARS'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Bolivia":
            cur = 'USD'
            cur2 = 'BOB'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Brazil":
            cur = 'USD'
            cur2 = 'BRL'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Chile":
            cur = 'USD'
            cur2 = 'CLP'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Colombia":
            cur = 'USD'
            cur2 = 'COP'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Peru":
            cur = 'USD'
            cur2 = 'PEN'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Ecuador":
            # cur = 'USD'
            # cur2 = 'PEN'
            # link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(val, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(val, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Venezuela":
            cur = 'USD'
            cur2 = 'VES'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Uruguay":
            cur = 'USD'
            cur2 = 'UYU'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


# Africa
def global_transactions_Africa(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    if region == "4":
        # reg = "Africa"
        if curname == "Nigeria":
            cur = 'USD'
            cur2 = 'NGN'
            link = c.convert(cur, cur2, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "South Africa":
            cur = 'USD'
            cur2 = 'ZAR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Egypt":
            cur = 'USD'
            cur2 = 'EGP'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Algeria":
            cur = 'USD'
            cur2 = 'DZD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Morocco":
            cur = 'USD'
            cur2 = 'MAD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Kenya":
            cur = 'USD'
            cur2 = 'KES'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Ethiopia":
            cur = 'USD'
            cur2 = 'ETB'
            link = c.convert(cur2, cur, val)
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Ghana":
            cur = 'USD'
            cur2 = 'GHS'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Angola":
            cur = 'USD'
            cur2 = 'AOA'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Tanzania":
            cur = 'USD'
            cur2 = 'TZS'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Ivory Coast":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Cameroon":
            cur = 'USD'
            cur2 = 'XAF'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


# Asia
def global_transactions_Asia_Middle_east(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    if region == "5":
        # reg = "Asia/Middle East"
        if curname == "China":
            cur = 'USD'
            cur2 = 'CNY'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Japan":
            cur = 'USD'
            cur2 = 'JPY'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "India":
            cur = 'USD'
            cur2 = 'INR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "South Korea":
            cur = 'USD'
            cur2 = 'KRW'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Indonesia":
            cur = 'USD'
            cur2 = 'IDR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Saudi Arabia":
            cur = 'USD'
            cur2 = 'SAR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Taiwan":
            cur = 'USD'
            cur2 = 'TWD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Thailand":
            cur = 'USD'
            cur2 = 'THB'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "UAE":
            cur = 'USD'
            cur2 = 'AED'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Israel":
            cur = 'USD'
            cur2 = 'ILS'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Philippines":
            cur = 'USD'
            cur2 = 'PHP'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Hong Kong":
            cur = 'USD'
            cur2 = 'HKD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Singapore":
            cur = 'USD'
            cur2 = 'SGD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Malaysia":
            cur = 'USD'
            cur2 = 'MYR'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Bangladesh":
            cur = 'USD'
            cur2 = 'BDT'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Vietnam":
            cur = 'USD'
            cur2 = 'VND'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


# Caribbean
def global_transactions_Caribbean(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    if region == "6":
        # reg = "Caribbean"
        if curname == "Antigua":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Bahamas":
            cur = 'USD'
            cur2 = 'BSD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Belize":
            cur = 'USD'
            cur2 = 'BZD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Dominica":
            cur = 'USD'
            cur2 = 'DOP'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Grenada":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Guyana":
            cur = 'USD'
            cur2 = 'GYD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Jamaica":
            cur = 'USD'
            cur2 = 'JMD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Puerto Rico":
            # cur = 'USD'
            # cur2 = 'GYD'
            # link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(val, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(val, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "St. Kitts and Nevis":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "St. Lucia":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "St. Vincent & Grenadines":
            cur = 'USD'
            cur2 = 'XCD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Suriname":
            cur = 'USD'
            cur2 = 'SRD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Trinidad & Tobago":
            cur = 'USD'
            cur2 = 'TTD'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


# Central America
def global_transactions_CA(region=int, val=float, curname=str, Sender_accnt_name=str, Receive_accnt_name=str, account=str, CardNo=int):
    c = CurrencyRates()
    if region == "7":
        # reg = "Central America"
        if curname == "Guatemala":
            cur = 'USD'
            cur2 = 'GTQ'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
        if curname == "Panama":
            cur = 'USD'
            cur2 = 'PAB'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Costa Rica":
            cur = 'USD'
            cur2 = 'CRC'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "El Salvador":
            # cur = 'USD'
            # cur2 = 'PAB'
            # link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(val, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(val, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Honduras":
            cur = 'USD'
            cur2 = 'HNL'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")
        if curname == "Nicaragua":
            cur = 'USD'
            cur2 = 'NIO'
            link = c.convert(cur2, cur, val)
            print("Transaction processing")
            if account == "1":
                send_money_Debit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            if account == "2":
                send_money_Credit_International(link, CardNo, Receive_accnt_name, Sender_accnt_name, curname)
            else:
                print("Transaction not processed")


def send_money_Debit_International(amount=float, CardNo=int, recipient=str, name=str, curname=str):  # send money between Debit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        inov.send_mail_for_International_Transactions(name, mail, mail_amount, curname)
    else:
        send_to_Credit_International(amount, CardNo, recipient, name)


def send_to_Credit_International(amount=float, CardNo=int, recipient=str, name=str, curname=str):  # Send money from Debit to Credit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        inov.send_mail_for_International_Transactions(name, mail, mail_amount, curname)


def send_money_Credit_International(amount=float, CardNo=int, recipient=str, name=str, curname=str):  # send money between Credit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CreditInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE CreditInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        inov.send_mail_for_International_Transactions(name, mail, mail_amount, curname)
    else:
        send_to_debit_International(amount, CardNo, recipient, name)


def send_to_debit_International(amount=float, CardNo=str, recipient=str, name=str, curname=str):  # Send money from Credit to Debit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE name=?''', [recipient])
    for credit_row in curr.fetchall():
        email = credit_row[1]
        mail = e_mail(email)
        rate_r = 0.013
        curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
        fee = amount * rate_r
        total_val_credit = amount + fee
        curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
        curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
        # processing transaction
        curr.execute('''UPDATE DebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
        conn.commit()
        print("transaction complete")
        conn.close()
        inov.send_mail_for_International_Transactions(name, mail, mail_amount, curname)