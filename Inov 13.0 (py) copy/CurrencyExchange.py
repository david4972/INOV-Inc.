import psycopg2
import inov
import requests
import json


# Global transactions (USD only) Debit
def global_transactions_Debit(CardNo=int, curname=str):
    # "North America"
    if curname == "United States":
        United_States = 'USD'
        exchange_code_debit(CardNo, United_States)
    if curname == "Canada":
        Canada = 'CAD'
        exchange_code_debit(CardNo, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        exchange_code_debit(CardNo, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        exchange_code_debit(CardNo, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        exchange_code_debit(CardNo, Germany)
    if curname == "France":
        France = 'EUR'
        exchange_code_debit(CardNo, France)
    if curname == "Italy":
        Italy = 'EUR'
        exchange_code_debit(CardNo, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        exchange_code_debit(CardNo, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        exchange_code_debit(CardNo, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        exchange_code_debit(CardNo, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        exchange_code_debit(CardNo, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        exchange_code_debit(CardNo, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        exchange_code_debit(CardNo, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        exchange_code_debit(CardNo, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        exchange_code_debit(CardNo, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        exchange_code_debit(CardNo, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        exchange_code_debit(CardNo, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        exchange_code_debit(CardNo, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        exchange_code_debit(CardNo, Peru)
    if curname == "Ecuador":
        Ecuador = 'PEN'
        # link = c.convert(cur2, cur, val)
        exchange_code_debit(CardNo, Ecuador)
    if curname == "Venezuela":
        Venezuela = 'VES'
        exchange_code_debit(CardNo, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        exchange_code_debit(CardNo, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        exchange_code_debit(CardNo, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        exchange_code_debit(CardNo, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        exchange_code_debit(CardNo, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        exchange_code_debit(CardNo, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        exchange_code_debit(CardNo, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        exchange_code_debit(CardNo, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        exchange_code_debit(CardNo, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        exchange_code_debit(CardNo, Ghana)
    if curname == "Angola":
        Angola = 'AOA'
        exchange_code_debit(CardNo, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        exchange_code_debit(CardNo, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        exchange_code_debit(CardNo, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        exchange_code_debit(CardNo, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        exchange_code_debit(CardNo, China)
    if curname == "Japan":
        Japan = 'JPY'
        exchange_code_debit(CardNo, Japan)
    if curname == "India":
        India = 'INR'
        exchange_code_debit(CardNo, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        exchange_code_debit(CardNo, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        exchange_code_debit(CardNo, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        exchange_code_debit(CardNo, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        exchange_code_debit(CardNo, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        exchange_code_debit(CardNo, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        exchange_code_debit(CardNo, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        exchange_code_debit(CardNo, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        exchange_code_debit(CardNo, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        exchange_code_debit(CardNo, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        exchange_code_debit(CardNo, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        exchange_code_debit(CardNo, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        exchange_code_debit(CardNo, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        exchange_code_debit(CardNo, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        exchange_code_debit(CardNo, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        exchange_code_debit(CardNo, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        exchange_code_debit(CardNo, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        exchange_code_debit(CardNo, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        exchange_code_debit(CardNo, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        exchange_code_debit(CardNo, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        exchange_code_debit(CardNo, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        exchange_code_debit(CardNo, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        exchange_code_debit(CardNo, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        exchange_code_debit(CardNo, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        exchange_code_debit(CardNo, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        exchange_code_debit(CardNo, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        exchange_code_debit(CardNo, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        exchange_code_debit(CardNo, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        exchange_code_debit(CardNo, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        exchange_code_debit(CardNo, Costa_Rica)
    if curname == "El Salvador":
        El_Salvador = 'PAB'
        # link = c.convert(cur2, cur, val)
        exchange_code_debit(CardNo, El_Salvador)
    if curname == "Honduras":
        Honduras = 'HNL'
        exchange_code_debit(CardNo, Honduras)
    if curname == "Nicaragua":
        Nicaragua = 'NIO'
        exchange_code_debit(CardNo, Nicaragua)


# Global transactions (USD only) Credit
def global_transactions_Credit(CardNo=int, curname=str):
    # "North America"
    if curname == "United States":
        United_States = 'USD'
        exchange_code_credit(CardNo, United_States)
    if curname == "Canada":
        Canada = 'CAD'
        exchange_code_credit(CardNo, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        exchange_code_credit(CardNo, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        exchange_code_credit(CardNo, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        exchange_code_credit(CardNo, Germany)
    if curname == "France":
        France = 'EUR'
        exchange_code_credit(CardNo, France)
    if curname == "Italy":
        Italy = 'EUR'
        exchange_code_credit(CardNo, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        exchange_code_credit(CardNo, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        exchange_code_credit(CardNo, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        exchange_code_credit(CardNo, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        exchange_code_credit(CardNo, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        exchange_code_credit(CardNo, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        exchange_code_credit(CardNo, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        exchange_code_credit(CardNo, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        exchange_code_credit(CardNo, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        exchange_code_credit(CardNo, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        exchange_code_credit(CardNo, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        exchange_code_credit(CardNo, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        exchange_code_credit(CardNo, Peru)
    if curname == "Ecuador":
        Ecuador = 'PEN'
        # link = c.convert(cur2, cur, val)
        exchange_code_credit(CardNo, Ecuador)
    if curname == "Venezuela":
        Venezuela = 'VES'
        exchange_code_credit(CardNo, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        exchange_code_credit(CardNo, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        exchange_code_credit(CardNo, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        exchange_code_credit(CardNo, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        exchange_code_credit(CardNo, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        exchange_code_credit(CardNo, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        exchange_code_credit(CardNo, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        exchange_code_credit(CardNo, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        exchange_code_credit(CardNo, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        exchange_code_credit(CardNo, Ghana)
        print("Transaction complete")
    if curname == "Angola":
        Angola = 'AOA'
        exchange_code_credit(CardNo, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        exchange_code_credit(CardNo, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        exchange_code_credit(CardNo, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        exchange_code_credit(CardNo, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        exchange_code_credit(CardNo, China)
    if curname == "Japan":
        Japan = 'JPY'
        exchange_code_credit(CardNo, Japan)
    if curname == "India":
        India = 'INR'
        exchange_code_credit(CardNo, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        exchange_code_credit(CardNo, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        exchange_code_credit(CardNo, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        exchange_code_credit(CardNo, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        exchange_code_credit(CardNo, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        exchange_code_credit(CardNo, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        exchange_code_credit(CardNo, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        exchange_code_credit(CardNo, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        exchange_code_credit(CardNo, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        exchange_code_credit(CardNo, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        exchange_code_credit(CardNo, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        exchange_code_credit(CardNo, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        exchange_code_credit(CardNo, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        exchange_code_credit(CardNo, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        exchange_code_credit(CardNo, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        exchange_code_credit(CardNo, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        exchange_code_credit(CardNo, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        exchange_code_credit(CardNo, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        exchange_code_credit(CardNo, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        exchange_code_credit(CardNo, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        exchange_code_credit(CardNo, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        exchange_code_credit(CardNo, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        exchange_code_credit(CardNo, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        exchange_code_credit(CardNo, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        exchange_code_credit(CardNo, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        exchange_code_credit(CardNo, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        exchange_code_credit(CardNo, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        exchange_code_credit(CardNo, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        exchange_code_credit(CardNo, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        exchange_code_credit(CardNo, Costa_Rica)
    if curname == "El Salvador":
        El_Salvador = 'PAB'
        # link = c.convert(cur2, cur, val)
        exchange_code_credit(CardNo, El_Salvador)
    if curname == "Honduras":
        Honduras = 'HNL'
        exchange_code_credit(CardNo, Honduras)
    if curname == "Nicaragua":
        Nicaragua = 'NIO'
        exchange_code_credit(CardNo, Nicaragua)


# Currency change (allows account users to convert currency cash account into any of the 70 currencies we support)
# USD
def exchange_code_credit(CardNo=int, country_name=str):
    String_url = 'https://v6.exchangerate-api.com/v6/2816493d654f23cda23c4ccc/pair/USD/'
    combine = String_url + country_name
    url = combine
    access = requests.get(url)
    data = json.loads(access.text)
    rate = data['conversion_rate']
    new_rate = float.__round__(rate)
    CurrencyExchange_Credit(CardNo, new_rate, country_name)


def exchange_code_debit(CardNo=int, country_name=str):
    String_url = 'https://v6.exchangerate-api.com/v6/2816493d654f23cda23c4ccc/pair/USD/'
    combine = String_url + country_name
    url = combine
    access = requests.get(url)
    data = json.loads(access.text)
    rate = data['conversion_rate']
    new_rate = float.__round__(rate)
    CurrencyExchange_Debit(CardNo, new_rate, country_name)


# Credit
def CurrencyExchange_Credit(credit_CardNo=int, credit_gbc=float, country_name=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    CurrencyExchange_USD_credit_curr = conn.cursor()
    rate_r = 0.013
    CurrencyExchange_USD_credit_curr.execute('''SELECT * FROM CreditInov WHERE CardNo=%s''', [credit_CardNo])
    for row1 in CurrencyExchange_USD_credit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_credit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        # CurrencyExchange_USD_credit_curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''',
        # [db_checking_fee, credit_CardNo])
        # CurrencyExchange_USD_credit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
        # [db_checking_fee])
        CurrencyExchange_USD_credit_curr.execute('''UPDATE CreditInov SET Checking=Checking*%s, Saving=Saving*%s, Currency=%s 
        WHERE CardNo=%s''', [credit_gbc, credit_gbc, country_name, credit_CardNo])
        conn.commit()
        print("exchange complete")
        inov.send_mail_for_currency_exchange(country_name, mail_currency_exchange_credit)


# Debit
def CurrencyExchange_Debit(debit_CardNo=int, debit_gbc=float, country_name=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    CurrencyExchange_EUR_debit_curr = conn.cursor()
    rate_r = 0.013
    CurrencyExchange_EUR_debit_curr.execute('''SELECT * FROM DebitInov WHERE CardNo=%s''', [debit_CardNo])
    for row1 in CurrencyExchange_EUR_debit_curr.fetchall():
        email = row1[1]
        mail_currency_exchange_debit = str(email)
        deb_Checking_balance = row1[5]
        db_checking_fee = deb_Checking_balance * rate_r
        # CurrencyExchange_EUR_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''',
        # [db_checking_fee, debit_CardNo])
        # CurrencyExchange_EUR_debit_curr.execute('''UPDATE BusinessInov SET Checking=Checking+? WHERE name=INOVBank''',
        # [db_checking_fee])
        CurrencyExchange_EUR_debit_curr.execute('''UPDATE DebitInov SET Checking=Checking*%s, Saving=Saving*%s, Currency=%s 
            WHERE CardNo=%s''', [debit_gbc, debit_gbc, country_name, debit_CardNo])
        conn.commit()
        print("exchange complete")
        inov.send_mail_for_currency_exchange(country_name, mail_currency_exchange_debit)

