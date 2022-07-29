import psycopg2
import inov
from forex_python.converter import CurrencyRates


# Global transactions (USD only) Debit
def global_transactions_Debit(CardNo=int, curname=str):
    # "North America"
    if curname == "United States":
        United_States = 'USD'
        CurrencyExchange_Debit(CardNo, United_States)
    if curname == "Canada":
        Canada = 'CAD'
        CurrencyExchange_Debit(CardNo, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        CurrencyExchange_Debit(CardNo, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        CurrencyExchange_Debit(CardNo, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        CurrencyExchange_Debit(CardNo, Germany)
    if curname == "France":
        France = 'EUR'
        CurrencyExchange_Debit(CardNo, France)
    if curname == "Italy":
        Italy = 'EUR'
        CurrencyExchange_Debit(CardNo, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        CurrencyExchange_Debit(CardNo, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        CurrencyExchange_Debit(CardNo, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        CurrencyExchange_Debit(CardNo, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        CurrencyExchange_Debit(CardNo, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        CurrencyExchange_Debit(CardNo, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        CurrencyExchange_Debit(CardNo, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        CurrencyExchange_Debit(CardNo, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        CurrencyExchange_Debit(CardNo, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        CurrencyExchange_Debit(CardNo, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        CurrencyExchange_Debit(CardNo, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        CurrencyExchange_Debit(CardNo, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        CurrencyExchange_Debit(CardNo, Peru)
    if curname == "Ecuador":
        Ecuador = 'PEN'
        # link = c.convert(cur2, cur, val)
        CurrencyExchange_Debit(CardNo, Ecuador)
    if curname == "Venezuela":
        Venezuela = 'VES'
        CurrencyExchange_Debit(CardNo, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        CurrencyExchange_Debit(CardNo, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        CurrencyExchange_Debit(CardNo, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        CurrencyExchange_Debit(CardNo, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        CurrencyExchange_Debit(CardNo, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        CurrencyExchange_Debit(CardNo, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        CurrencyExchange_Debit(CardNo, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        CurrencyExchange_Debit(CardNo, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        CurrencyExchange_Debit(CardNo, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        CurrencyExchange_Debit(CardNo, Ghana)
        print("Transaction complete")
    if curname == "Angola":
        Angola = 'AOA'
        CurrencyExchange_Debit(CardNo, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        CurrencyExchange_Debit(CardNo, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        CurrencyExchange_Debit(CardNo, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        CurrencyExchange_Debit(CardNo, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        CurrencyExchange_Debit(CardNo, China)
    if curname == "Japan":
        Japan = 'JPY'
        CurrencyExchange_Debit(CardNo, Japan)
    if curname == "India":
        India = 'INR'
        CurrencyExchange_Debit(CardNo, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        CurrencyExchange_Debit(CardNo, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        CurrencyExchange_Debit(CardNo, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        CurrencyExchange_Debit(CardNo, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        CurrencyExchange_Debit(CardNo, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        CurrencyExchange_Debit(CardNo, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        CurrencyExchange_Debit(CardNo, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        CurrencyExchange_Debit(CardNo, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        CurrencyExchange_Debit(CardNo, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        CurrencyExchange_Debit(CardNo, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        CurrencyExchange_Debit(CardNo, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        CurrencyExchange_Debit(CardNo, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        CurrencyExchange_Debit(CardNo, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        CurrencyExchange_Debit(CardNo, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        CurrencyExchange_Debit(CardNo, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        CurrencyExchange_Debit(CardNo, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        CurrencyExchange_Debit(CardNo, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        CurrencyExchange_Debit(CardNo, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        CurrencyExchange_Debit(CardNo, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        CurrencyExchange_Debit(CardNo, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        CurrencyExchange_Debit(CardNo, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        CurrencyExchange_Debit(CardNo, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        CurrencyExchange_Debit(CardNo, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        CurrencyExchange_Debit(CardNo, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        CurrencyExchange_Debit(CardNo, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        CurrencyExchange_Credit(CardNo, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        CurrencyExchange_Debit(CardNo, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        CurrencyExchange_Debit(CardNo, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        CurrencyExchange_Debit(CardNo, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        CurrencyExchange_Debit(CardNo, Costa_Rica)
    if curname == "El Salvador":
        El_Salvador = 'PAB'
        # link = c.convert(cur2, cur, val)
        CurrencyExchange_Debit(CardNo, El_Salvador)
    if curname == "Honduras":
        Honduras = 'HNL'
        CurrencyExchange_Debit(CardNo, Honduras)
    if curname == "Nicaragua":
        Nicaragua = 'NIO'
        CurrencyExchange_Debit(CardNo, Nicaragua)


# Global transactions (USD only) Credit
def global_transactions_Credit(CardNo=int, curname=str):
    # "North America"
    if curname == "United States":
        United_States = 'USD'
        CurrencyExchange_Credit(CardNo, United_States)
    if curname == "Canada":
        Canada = 'CAD'
        CurrencyExchange_Credit(CardNo, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        CurrencyExchange_Credit(CardNo, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        CurrencyExchange_Credit(CardNo, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        CurrencyExchange_Credit(CardNo, Germany)
    if curname == "France":
        France = 'EUR'
        CurrencyExchange_Credit(CardNo, France)
    if curname == "Italy":
        Italy = 'EUR'
        CurrencyExchange_Credit(CardNo, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        CurrencyExchange_Credit(CardNo, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        CurrencyExchange_Credit(CardNo, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        CurrencyExchange_Credit(CardNo, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        CurrencyExchange_Credit(CardNo, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        CurrencyExchange_Credit(CardNo, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        CurrencyExchange_Credit(CardNo, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        CurrencyExchange_Credit(CardNo, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        CurrencyExchange_Credit(CardNo, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        CurrencyExchange_Credit(CardNo, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        CurrencyExchange_Credit(CardNo, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        CurrencyExchange_Credit(CardNo, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        CurrencyExchange_Credit(CardNo, Peru)
    if curname == "Ecuador":
        Ecuador = 'PEN'
        # link = c.convert(cur2, cur, val)
        CurrencyExchange_Credit(CardNo, Ecuador)
    if curname == "Venezuela":
        Venezuela = 'VES'
        CurrencyExchange_Credit(CardNo, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        CurrencyExchange_Credit(CardNo, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        CurrencyExchange_Credit(CardNo, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        CurrencyExchange_Credit(CardNo, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        CurrencyExchange_Credit(CardNo, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        CurrencyExchange_Credit(CardNo, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        CurrencyExchange_Credit(CardNo, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        CurrencyExchange_Credit(CardNo, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        CurrencyExchange_Credit(CardNo, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        CurrencyExchange_Credit(CardNo, Ghana)
        print("Transaction complete")
    if curname == "Angola":
        Angola = 'AOA'
        CurrencyExchange_Credit(CardNo, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        CurrencyExchange_Credit(CardNo, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        CurrencyExchange_Credit(CardNo, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        CurrencyExchange_Credit(CardNo, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        CurrencyExchange_Credit(CardNo, China)
    if curname == "Japan":
        Japan = 'JPY'
        CurrencyExchange_Credit(CardNo, Japan)
    if curname == "India":
        India = 'INR'
        CurrencyExchange_Credit(CardNo, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        CurrencyExchange_Credit(CardNo, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        CurrencyExchange_Credit(CardNo, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        CurrencyExchange_Credit(CardNo, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        CurrencyExchange_Credit(CardNo, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        CurrencyExchange_Credit(CardNo, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        CurrencyExchange_Credit(CardNo, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        CurrencyExchange_Credit(CardNo, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        CurrencyExchange_Credit(CardNo, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        CurrencyExchange_Credit(CardNo, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        CurrencyExchange_Credit(CardNo, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        CurrencyExchange_Credit(CardNo, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        CurrencyExchange_Credit(CardNo, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        CurrencyExchange_Credit(CardNo, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        CurrencyExchange_Credit(CardNo, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        CurrencyExchange_Credit(CardNo, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        CurrencyExchange_Credit(CardNo, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        CurrencyExchange_Credit(CardNo, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        CurrencyExchange_Credit(CardNo, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        CurrencyExchange_Credit(CardNo, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        CurrencyExchange_Credit(CardNo, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        CurrencyExchange_Credit(CardNo, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        CurrencyExchange_Credit(CardNo, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        CurrencyExchange_Credit(CardNo, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        CurrencyExchange_Credit(CardNo, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        CurrencyExchange_Credit(CardNo, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        CurrencyExchange_Credit(CardNo, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        CurrencyExchange_Credit(CardNo, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        CurrencyExchange_Credit(CardNo, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        CurrencyExchange_Credit(CardNo, Costa_Rica)
    if curname == "El Salvador":
        El_Salvador = 'PAB'
        # link = c.convert(cur2, cur, val)
        CurrencyExchange_Credit(CardNo, El_Salvador)
    if curname == "Honduras":
        Honduras = 'HNL'
        CurrencyExchange_Credit(CardNo, Honduras)
    if curname == "Nicaragua":
        Nicaragua = 'NIO'
        CurrencyExchange_Credit(CardNo, Nicaragua)


# Currency change (allows account users to convert currency cash account into any of the 70 currencies we support)
# USD

# Credit
def CurrencyExchange_Credit(credit_CardNo=int, credit_gbc=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    CurrencyExchange_USD_credit_curr = conn.cursor()
    c = CurrencyRates()
    USD_credit_var = "USD"
    USD_Currency_credit_convert = credit_gbc
    USD_credit_convert_check = c.get_rate(USD_Currency_credit_convert, USD_credit_var)
    checking_price = float(USD_credit_convert_check)
    USD_credit_convert_sav = c.get_rate(USD_Currency_credit_convert, USD_credit_var)
    saving_price = float(USD_credit_convert_sav)
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
        WHERE CardNo=%s''', [checking_price, saving_price, USD_credit_var, credit_CardNo])
        conn.commit()
        print("exchange complete")
        inov.send_mail_for_currency_exchange(USD_credit_var, mail_currency_exchange_credit)


# Debit
def CurrencyExchange_Debit(debit_CardNo=int, debit_gbc=str):
    # Connecting to postgres database server
    conn = psycopg2.connect(
        database="inov", user='postgres', password='', host='localhost', port='5432'
    )
    # Creating a cursor object using the cursor() method
    CurrencyExchange_EUR_debit_curr = conn.cursor()
    c = CurrencyRates()
    var1 = "USD"
    var2 = debit_gbc
    cex1 = c.get_rate(var1, var2)
    checking_price = float(cex1)
    cex2 = c.get_rate(var1, var2)
    saving_price = float(cex2)
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
            WHERE CardNo=%s''', [checking_price, saving_price, var2, debit_CardNo])
        conn.commit()
        print("exchange complete")
        inov.send_mail_for_currency_exchange(var2, mail_currency_exchange_debit)
