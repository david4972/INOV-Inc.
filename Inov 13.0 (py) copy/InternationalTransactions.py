import psycopg2
import inov
import requests
import json


# global transactions
# 1. North America,  2. Europe, 3. South America, 4. Africa, 5. Asia, 6. Caribbean, 7. Central America
# Supports 70 Countries across all 7 Continents
# USD base currency
# 1. North America
# Global transactions (USD only) Debit
def global_transactions_Debit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    USD = 'USD'
    # "North America"
    if curname == "Canada":
        Canada = 'CAD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Germany)
    if curname == "France":
        France = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, France)
    if curname == "Italy":
        Italy = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Peru)
    if curname == "Ecuador":
        # cur2 = 'PEN'
        # link = c.convert(cur2, cur, val)
        send_to_debit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Venezuela":
        Venezuela = 'VES'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Ghana)
    if curname == "Angola":
        Angola = 'AOA'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, China)
    if curname == "Japan":
        Japan = 'JPY'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Japan)
    if curname == "India":
        India = 'INR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Costa_Rica)
    if curname == "El Salvador":
        # cur2 = 'PAB'
        # link = c.convert(cur2, cur, val)
        send_to_debit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Honduras":
        Honduras = 'HNL'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Honduras)
    if curname == "Nicaragua":
        Nicaragua = 'NIO'
        exchange_transaction_amt_debit(val, CardNo, Receive_accnt_name, Nicaragua)


# Global transactions (USD only) Credit
def global_transactions_Credit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    USD = 'USD'
    # "North America"
    if curname == "Canada":
        Canada = 'CAD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Germany)
    if curname == "France":
        France = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, France)
    if curname == "Italy":
        Italy = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Peru)
    if curname == "Ecuador":
        # cur2 = 'PEN'
        # link = c.convert(cur2, cur, val)
        send_to_credit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Venezuela":
        Venezuela = 'VES'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Ghana)
        print("Transaction complete")
    if curname == "Angola":
        Angola = 'AOA'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, China)
    if curname == "Japan":
        Japan = 'JPY'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Japan)
    if curname == "India":
        India = 'INR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Costa_Rica)
    if curname == "El Salvador":
        # cur2 = 'PAB'
        # link = c.convert(cur2, cur, val)
        send_to_credit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Honduras":
        Honduras = 'HNL'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, Honduras)
    if curname == "Nicaragua":
        cur2 = 'NIO'
        exchange_transaction_amt_credit(val, CardNo, Receive_accnt_name, cur2)


def exchange_transaction_amt_debit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    string_amt = str(val)
    chara = "/"
    String_url = 'https://v6.exchangerate-api.com/v6/2816493d654f23cda23c4ccc/pair/USD/'
    combine = String_url + curname + chara + string_amt
    url = combine
    access = requests.get(url)
    data = json.loads(access.text)
    amt_c = data['conversion_result']
    new_amt = float.__round__(amt_c)
    send_to_debit_International(new_amt, CardNo, Receive_accnt_name, curname)


def send_to_debit_International(amount=float, CardNo=int, recipient=str,
                                curname=str):  # send money between Debit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE CardNo=%s''', [CardNo])
    for get_inter_name in curr.fetchall():
        name = get_inter_name[0]
        s_name = str(name)
        curr.execute('''SELECT * from InterDebitInov WHERE name=%s''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE DebitInov SET Checking=Checking-%s WHERE CardNo=%s''', [total_val_credit, CardNo])
            # curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking+%s WHERE name=%s''', [amount, recipient])
            conn.commit()
            conn.close()
            inov.send_mail_for_International_Transactions(s_name, mail, mail_amount, curname)
            return "transaction complete"
        else:
            send_to_credit_International(amount, CardNo, recipient, curname)


def exchange_transaction_amt_credit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    string_amt = str(val)
    chara = "/"
    String_url = 'https://v6.exchangerate-api.com/v6/2816493d654f23cda23c4ccc/pair/USD/'
    combine = String_url + curname + chara + string_amt
    url = combine
    access = requests.get(url)
    data = json.loads(access.text)
    amt_c = data['conversion_result']
    new_amt = float.__round__(amt_c)
    send_to_credit_International(new_amt, CardNo, Receive_accnt_name, curname)


def send_to_credit_International(amount=float, CardNo=str, recipient=str,
                                 curname=str):  # Send money from Credit to Debit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CreditInov WHERE CardNo=%s''', [CardNo])
    for get_inter_name in curr.fetchall():
        name = get_inter_name[0]
        s_name = str(name)
        curr.execute('''SELECT * from InterDebitInov WHERE name=%s''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE CreditInov SET Checking=Checking-%s WHERE CardNo=%s''', [total_val_credit, CardNo])
            # curr.execute('''UPDATE BusinessInov SET Saving=Saving+%s WHERE name=%s''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking+%s WHERE name=%s''', [amount, recipient])
            conn.commit()
            conn.close()
            inov.send_mail_for_International_Transactions(s_name, mail, mail_amount, curname)
            return "transaction complete"

