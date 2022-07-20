import sqlite3
import inov
from forex_python import converter


# global transactions
# 1. North America,  2. Europe, 3. South America, 4. Africa, 5. Asia, 6. Caribbean, 7. Central America
# Supports 70 Countries across all 7 Continents
# USD base currency
# 1. North America
# Global transactions (USD only) Debit
def global_transactions_Debit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    c = converter
    USD = 'USD'
    # "North America"
    if curname == "Canada":
        Canada = 'CAD'
        USDCanadalink = c.convert(USD, Canada, c.Decimal(val))
        USDCanadaquote = float(USDCanadalink.__round__())
        send_to_debit_International(USDCanadaquote, Receive_accnt_name, CardNo, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        USDMexicolink = c.convert(USD, Mexico, c.Decimal(val))
        USDMexicoquote = float(USDMexicolink.__round__())
        send_to_debit_International(USDMexicoquote, CardNo, Receive_accnt_name, CardNo, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        USDGBPlink = c.convert(USD, 'GBP', c.Decimal(val))
        USDGBPquote = float(USDGBPlink.__round__())
        send_to_debit_International(USDGBPquote, CardNo, Receive_accnt_name, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        USDGermanylink = c.convert(USD, Germany, c.Decimal(val))
        USDGermanyquote = float(USDGermanylink.__round__())
        send_to_debit_International(USDGermanyquote, CardNo, Receive_accnt_name, Germany)
    if curname == "France":
        France = 'EUR'
        USDFrancelink = c.convert(USD, France, c.Decimal(val))
        USDFrancequote = float(USDFrancelink.__round__())
        send_to_debit_International(USDFrancequote, CardNo, Receive_accnt_name, France)
    if curname == "Italy":
        Italy = 'EUR'
        USDItalylink = c.convert(USD, Italy, c.Decimal(val))
        USDItalyquote = float(USDItalylink.__round__())
        send_to_debit_International(USDItalyquote, CardNo, Receive_accnt_name, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        USDSpainlink = c.convert(USD, Spain, c.Decimal(val))
        USDSpainquote = float(USDSpainlink.__round__())
        send_to_debit_International(USDSpainquote, CardNo, Receive_accnt_name, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        USDNetherlandslink = c.convert(USD, Netherlands, c.Decimal(val))
        USDNetherlandsquote = float(USDNetherlandslink.__round__())
        send_to_debit_International(USDNetherlandsquote, CardNo, Receive_accnt_name, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        USDSwitzerlandlink = c.convert(USD, Switzerland, c.Decimal(val))
        USDSwitzerlandquote = float(USDSwitzerlandlink)
        send_to_debit_International(USDSwitzerlandquote, CardNo, Receive_accnt_name, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        USDPolandlink = c.convert(USD, Poland, c.Decimal(val))
        USDPolandquote = float(USDPolandlink.__round__())
        send_to_debit_International(USDPolandquote, CardNo, Receive_accnt_name, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        USDSwedenlink = c.convert(USD, Sweden, c.Decimal(val))
        USDSwedenquote = float(USDSwedenlink.__round__())
        send_to_debit_International(USDSwedenquote, CardNo, Receive_accnt_name, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        USDRussialink = c.convert(USD, Russia, c.Decimal(val))
        USDRussiaquote = float(USDRussialink.__round__())
        send_to_debit_International(USDRussiaquote, CardNo, Receive_accnt_name, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        USDArgentinalink = c.convert(USD, Argentina, c.Decimal(val))
        USDArgentinaquote = float(USDArgentinalink.__round__())
        send_to_debit_International(USDArgentinaquote, CardNo, Receive_accnt_name, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        USDBolivialink = c.convert(USD, Bolivia, c.Decimal(val))
        USDBoliviaquote = float(USDBolivialink.__round__())
        send_to_debit_International(USDBoliviaquote, CardNo, Receive_accnt_name, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        USDBrazillink = c.convert(USD, Brazil, c.Decimal(val))
        USDBrazilquote = float(USDBrazillink.__round__())
        send_to_debit_International(USDBrazilquote, CardNo, Receive_accnt_name, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        USDChilelink = c.convert(USD, Chile, c.Decimal(val))
        USDChilequote = float(USDChilelink.__round__())
        send_to_debit_International(USDChilequote, CardNo, Receive_accnt_name, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        USDColombialink = c.convert(USD, Colombia, c.Decimal(val))
        USDColombiaquote = float(USDColombialink.__round__())
        send_to_debit_International(USDColombiaquote, CardNo, Receive_accnt_name, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        USDPerulink = c.convert(USD, Peru, c.Decimal(val))
        USDPeruquote = float(USDPerulink.__round__())
        send_to_debit_International(USDPeruquote, CardNo, Receive_accnt_name, Peru)
    if curname == "Ecuador":
        # cur2 = 'PEN'
        # link = c.convert(cur2, cur, val)
        send_to_debit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Venezuela":
        Venezuela = 'VES'
        USDVenezuelalink = c.convert(USD, Venezuela, c.Decimal(val))
        USDVenezuelaquote = float(USDVenezuelalink.__round__())
        send_to_debit_International(USDVenezuelaquote, CardNo, Receive_accnt_name, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        USDUruguaylink = c.convert(USD, Uruguay, c.Decimal(val))
        USDUruguayquote = float(USDUruguaylink.__round__())
        send_to_debit_International(USDUruguayquote, CardNo, Receive_accnt_name, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        USDNigerialink = c.convert(USD, Nigeria, c.Decimal(val))
        USDNigeriaquote = float(USDNigerialink.__round__())
        send_to_debit_International(USDNigeriaquote, CardNo, Receive_accnt_name, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        USDSouth_Africalink = c.convert(USD, South_Africa, c.Decimal(val))
        USDSouth_Africaquote = float(USDSouth_Africalink.__round__())
        send_to_debit_International(USDSouth_Africaquote, CardNo, Receive_accnt_name, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        USDEgyptlink = c.convert(USD, Egypt, c.Decimal(val))
        USDEgyptquote = float(USDEgyptlink.__round__())
        send_to_debit_International(USDEgyptquote, CardNo, Receive_accnt_name, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        USDAlgerialink = c.convert(USD, Algeria, c.Decimal(val))
        USDAlgeriaquote = float(USDAlgerialink.__round__())
        send_to_debit_International(USDAlgeriaquote, CardNo, Receive_accnt_name, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        USDMoroccolink = c.convert(USD, Morocco, c.Decimal(val))
        USDMoroccoquote = float(USDMoroccolink.__round__())
        send_to_debit_International(USDMoroccoquote, CardNo, Receive_accnt_name, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        USDKenyalink = c.convert(USD, Kenya, c.Decimal(val))
        USDKenyaquote = float(USDKenyalink.__round__())
        send_to_debit_International(USDKenyaquote, CardNo, Receive_accnt_name, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        USDEthiopialink = c.convert(USD, Ethiopia, c.Decimal(val))
        USDEthiopiaquote = float(USDEthiopialink.__round__())
        send_to_debit_International(USDEthiopiaquote, CardNo, Receive_accnt_name, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        USDGhanalink = c.convert(USD, Ghana, c.Decimal(val))
        USDGhanaquote = float(USDGhanalink.__round__())
        print("Transaction processing")
        send_to_debit_International(USDGhanaquote, CardNo, Receive_accnt_name, Ghana)
        print("Transaction complete")
    if curname == "Angola":
        Angola = 'AOA'
        USDAngolalink = c.convert(USD, Angola, c.Decimal(val))
        USDAngolaquote = float(USDAngolalink.__round__())
        send_to_debit_International(USDAngolaquote, CardNo, Receive_accnt_name, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        USDTanzanialink = c.convert(USD, Tanzania, c.Decimal(val))
        USDTanzaniaquote = float(USDTanzanialink.__round__())
        send_to_debit_International(USDTanzaniaquote, CardNo, Receive_accnt_name, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        USDIvory_Coastlink = c.convert(USD, Ivory_Coast, c.Decimal(val))
        USDIvory_Coastquote = float(USDIvory_Coastlink.__round__())
        send_to_debit_International(USDIvory_Coastquote, CardNo, Receive_accnt_name, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        USDCameroonlink = c.convert(USD, Cameroon, c.Decimal(val))
        USDCameroonquote = float(USDCameroonlink.__round__())
        send_to_debit_International(USDCameroonquote, CardNo, Receive_accnt_name, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        USDChinalink = c.convert(USD, China, c.Decimal(val))
        USDChinaquote = float(USDChinalink.__round__())
        send_to_debit_International(USDChinaquote, CardNo, Receive_accnt_name, China)
    if curname == "Japan":
        Japan = 'JPY'
        USDJapanlink = c.convert(USD, Japan, c.Decimal(val))
        USDJapanquote = float(USDJapanlink.__round__())
        send_to_debit_International(USDJapanquote, CardNo, Receive_accnt_name, Japan)
    if curname == "India":
        India = 'INR'
        USDIndialink = c.convert(USD, India, c.Decimal(val))
        USDIndiaquote = float(USDIndialink.__round__())
        send_to_debit_International(USDIndiaquote, CardNo, Receive_accnt_name, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        USDSouth_Korealink = c.convert(USD, South_Korea, c.Decimal(val))
        USDSouth_Koreaquote = float(USDSouth_Korealink.__round__())
        send_to_debit_International(USDSouth_Koreaquote, CardNo, Receive_accnt_name, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        USDIndonesialink = c.convert(USD, Indonesia, c.Decimal(val))
        USDIndonesiaquote = float(USDIndonesialink.__round__())
        send_to_debit_International(USDIndonesiaquote, CardNo, Receive_accnt_name, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        USDSaudi_Arabialink = c.convert(USD, Saudi_Arabia, c.Decimal(val))
        USDSaudi_Arabiaquote = float(USDSaudi_Arabialink.__round__())
        send_to_debit_International(USDSaudi_Arabiaquote, CardNo, Receive_accnt_name, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        USDTaiwanlink = c.convert(USD, Taiwan, c.Decimal(val))
        USDTaiwanquote = float(USDTaiwanlink.__round__())
        send_to_debit_International(USDTaiwanquote, CardNo, Receive_accnt_name, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        USDThailandlink = c.convert(USD, Thailand, c.Decimal(val))
        USDThailandquote = float(USDThailandlink.__round__())
        send_to_debit_International(USDThailandquote, CardNo, Receive_accnt_name, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        USDUAElink = c.convert(USD, UAE, c.Decimal(val))
        USDUAEquote = float(USDUAElink.__round__())
        send_to_debit_International(USDUAEquote, CardNo, Receive_accnt_name, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        USDIsraellink = c.convert(USD, Israel, c.Decimal(val))
        USDIsraelquote = float(USDIsraellink.__round__())
        send_to_debit_International(USDIsraelquote, CardNo, Receive_accnt_name, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        USDPhilippineslink = c.convert(USD, Philippines, c.Decimal(val))
        USDPhilippinesquote = float(USDPhilippineslink.__round__())
        send_to_debit_International(USDPhilippinesquote, CardNo, Receive_accnt_name, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        USDHong_Konglink = c.convert(USD, Hong_Kong, c.Decimal(val))
        USDHong_Kongquote = float(USDHong_Konglink.__round__())
        send_to_debit_International(USDHong_Kongquote, CardNo, Receive_accnt_name, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        USDSingaporelink = c.convert(USD, Singapore, c.Decimal(val))
        USDSingaporequote = float(USDSingaporelink.__round__())
        send_to_debit_International(USDSingaporequote, CardNo, Receive_accnt_name, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        USDMalaysialink = c.convert(USD, Malaysia, c.Decimal(val))
        USDMalaysiaquote = float(USDMalaysialink.__round__())
        send_to_debit_International(USDMalaysiaquote, CardNo, Receive_accnt_name, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        USDBangladeshlink = c.convert(USD, Bangladesh, c.Decimal(val))
        USDBangladeshquote = float(USDBangladeshlink.__round__())
        send_to_debit_International(USDBangladeshquote, CardNo, Receive_accnt_name, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        USDVietnamlink = c.convert(USD, Vietnam, c.Decimal(val))
        USDVietnamquote = float(USDVietnamlink.__round__())
        send_to_debit_International(USDVietnamquote, CardNo, Receive_accnt_name, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        USDAntigualink = c.convert(USD, Antigua, c.Decimal(val))
        USDAntiguaquote = float(USDAntigualink.__round__())
        send_to_debit_International(USDAntiguaquote, CardNo, Receive_accnt_name, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        USDBahamaslink = c.convert(USD, Bahamas, c.Decimal(val))
        USDBahamasquote = float(USDBahamaslink.__round__())
        send_to_debit_International(USDBahamasquote, CardNo, Receive_accnt_name, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        USDBelizelink = c.convert(USD, Belize, c.Decimal(val))
        USDBelizequote = float(USDBelizelink.__round__())
        send_to_debit_International(USDBelizequote, CardNo, Receive_accnt_name, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        USDDominicalink = c.convert(USD, Dominica, c.Decimal(val))
        USDDominicaquote = float(USDDominicalink.__round__())
        send_to_debit_International(USDDominicaquote, CardNo, Receive_accnt_name, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        USDGrenadalink = c.convert(USD, Grenada, c.Decimal(val))
        USDGrenadaquote = float(USDGrenadalink.__round__())
        send_to_debit_International(USDGrenadaquote, CardNo, Receive_accnt_name, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        USDGuyanalink = c.convert(USD, Guyana, c.Decimal(val))
        USDGuyanaquote = float(USDGuyanalink.__round__())
        send_to_debit_International(USDGuyanaquote, CardNo, Receive_accnt_name, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        USDJamaicalink = c.convert(USD, Jamaica, c.Decimal(val))
        USDJamaicaquote = float(USDJamaicalink.__round__())
        send_to_debit_International(USDJamaicaquote, CardNo, Receive_accnt_name, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        USDPuerto_Ricolink = c.convert(USD, Puerto_Rico, c.Decimal(val))
        USDPuerto_Ricoquote = float(USDPuerto_Ricolink.__round__())
        send_to_debit_International(USDPuerto_Ricoquote, CardNo, Receive_accnt_name, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        USDSt_Kittslink = c.convert(USD, St_Kitts, c.Decimal(val))
        USDSt_Kittsquote = float(USDSt_Kittslink.__round__())
        send_to_debit_International(USDSt_Kittsquote, CardNo, Receive_accnt_name, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        USDst_lucialink = c.convert(USD, st_lucia, c.Decimal(val))
        USDst_luciaquote = float(USDst_lucialink.__round__())
        send_to_debit_International(USDst_luciaquote, CardNo, Receive_accnt_name, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        USDst_vincentlink = c.convert(USD, st_vincent, c.Decimal(val))
        USDst_vincentquote = float(USDst_vincentlink.__round__())
        send_to_debit_International(USDst_vincentquote, CardNo, Receive_accnt_name, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        USDSurinamelink = c.convert(USD, Suriname, c.Decimal(val))
        USDSurinamequote = float(USDSurinamelink.__round__())
        send_to_debit_International(USDSurinamequote, CardNo, Receive_accnt_name, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        USDTrinidadlink = c.convert(USD, Trinidad, c.Decimal(val))
        USDTrinidadquote = float(USDTrinidadlink.__round__())
        send_to_debit_International(USDTrinidadquote, CardNo, Receive_accnt_name, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        USDGuatemalalink = c.convert(USD, Guatemala, c.Decimal(val))
        USDGuatemalaquote = float(USDGuatemalalink.__round__())
        send_to_debit_International(USDGuatemalaquote, CardNo, Receive_accnt_name, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        USDPanamalink = c.convert(USD, Panama, c.Decimal(val))
        USDPanamaquote = float(USDPanamalink.__round__())
        send_to_debit_International(USDPanamaquote, CardNo, Receive_accnt_name, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        USDCosta_Ricalink = c.convert(USD, Costa_Rica, c.Decimal(val))
        USDCosta_Ricaquote = float(USDCosta_Ricalink.__round__())
        send_to_debit_International(USDCosta_Ricaquote, CardNo, Receive_accnt_name, Costa_Rica)
    if curname == "El Salvador":
        # cur2 = 'PAB'
        # link = c.convert(cur2, cur, val)
        send_to_debit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Honduras":
        Honduras = 'HNL'
        USDHonduraslink = c.convert(USD, Honduras, c.Decimal(val))
        USDHondurasquote = float(USDHonduraslink.__round__())
        send_to_debit_International(USDHondurasquote, CardNo, Receive_accnt_name, Honduras)
    if curname == "Nicaragua":
        Nicaragua = 'NIO'
        USDNicaragualink = c.convert(USD, Nicaragua, c.Decimal(val))
        USDNicaraguaquote = float(USDNicaragualink.__round__())
        send_to_debit_International(USDNicaraguaquote, CardNo, Receive_accnt_name, Nicaragua)


# Global transactions (USD only) Credit
def global_transactions_Credit(val=float, Receive_accnt_name=str, CardNo=int, curname=str):
    c = converter
    USD = 'USD'
    # "North America"
    if curname == "Canada":
        Canada = 'CAD'
        USDCanadalink = c.convert(USD, Canada, c.Decimal(val))
        USDCanadaquote = float(USDCanadalink.__round__())
        send_to_credit_International(USDCanadaquote, Receive_accnt_name, CardNo, Canada)
    if curname == "Mexico":
        Mexico = 'MXN'
        USDMexicolink = c.convert(USD, Mexico, c.Decimal(val))
        USDMexicoquote = float(USDMexicolink.__round__())
        send_to_credit_International(USDMexicoquote, CardNo, Receive_accnt_name, CardNo, Mexico)
        # "Europe"
    if curname == "UK":
        GBP = 'GBP'
        USDGBPlink = c.convert(USD, 'GBP', c.Decimal(val))
        USDGBPquote = float(USDGBPlink.__round__())
        send_to_credit_International(USDGBPquote, CardNo, Receive_accnt_name, GBP)
    if curname == "Germany":
        Germany = 'EUR'
        USDGermanylink = c.convert(USD, Germany, c.Decimal(val))
        USDGermanyquote = float(USDGermanylink.__round__())
        send_to_credit_International(USDGermanyquote, CardNo, Receive_accnt_name, Germany)
    if curname == "France":
        France = 'EUR'
        USDFrancelink = c.convert(USD, France, c.Decimal(val))
        USDFrancequote = float(USDFrancelink.__round__())
        send_to_credit_International(USDFrancequote, CardNo, Receive_accnt_name, France)
    if curname == "Italy":
        Italy = 'EUR'
        USDItalylink = c.convert(USD, Italy, c.Decimal(val))
        USDItalyquote = float(USDItalylink.__round__())
        send_to_credit_International(USDItalyquote, CardNo, Receive_accnt_name, Italy)
    if curname == "Spain":
        Spain = 'EUR'
        USDSpainlink = c.convert(USD, Spain, c.Decimal(val))
        USDSpainquote = float(USDSpainlink.__round__())
        send_to_credit_International(USDSpainquote, CardNo, Receive_accnt_name, Spain)
    if curname == "Netherlands":
        Netherlands = 'EUR'
        USDNetherlandslink = c.convert(USD, Netherlands, c.Decimal(val))
        USDNetherlandsquote = float(USDNetherlandslink.__round__())
        send_to_credit_International(USDNetherlandsquote, CardNo, Receive_accnt_name, Netherlands)
    if curname == "Switzerland":
        Switzerland = 'CHF'
        USDSwitzerlandlink = c.convert(USD, Switzerland, c.Decimal(val))
        USDSwitzerlandquote = float(USDSwitzerlandlink)
        send_to_credit_International(USDSwitzerlandquote, CardNo, Receive_accnt_name, Switzerland)
    if curname == "Poland":
        Poland = 'EUR'
        USDPolandlink = c.convert(USD, Poland, c.Decimal(val))
        USDPolandquote = float(USDPolandlink.__round__())
        send_to_credit_International(USDPolandquote, CardNo, Receive_accnt_name, Poland)
    if curname == "Sweden":
        Sweden = 'EUR'
        USDSwedenlink = c.convert(USD, Sweden, c.Decimal(val))
        USDSwedenquote = float(USDSwedenlink.__round__())
        send_to_credit_International(USDSwedenquote, CardNo, Receive_accnt_name, Sweden)
    if curname == "Russia":
        Russia = 'RUB'
        USDRussialink = c.convert(USD, Russia, c.Decimal(val))
        USDRussiaquote = float(USDRussialink.__round__())
        send_to_credit_International(USDRussiaquote, CardNo, Receive_accnt_name, Russia)
        # reg = "South America
    if curname == "Argentina":
        Argentina = 'ARS'
        USDArgentinalink = c.convert(USD, Argentina, c.Decimal(val))
        USDArgentinaquote = float(USDArgentinalink.__round__())
        send_to_credit_International(USDArgentinaquote, CardNo, Receive_accnt_name, Argentina)
    if curname == "Bolivia":
        Bolivia = 'BOB'
        USDBolivialink = c.convert(USD, Bolivia, c.Decimal(val))
        USDBoliviaquote = float(USDBolivialink.__round__())
        send_to_credit_International(USDBoliviaquote, CardNo, Receive_accnt_name, Bolivia)
    if curname == "Brazil":
        Brazil = 'BRL'
        USDBrazillink = c.convert(USD, Brazil, c.Decimal(val))
        USDBrazilquote = float(USDBrazillink.__round__())
        send_to_credit_International(USDBrazilquote, CardNo, Receive_accnt_name, Brazil)
    if curname == "Chile":
        Chile = 'CLP'
        USDChilelink = c.convert(USD, Chile, c.Decimal(val))
        USDChilequote = float(USDChilelink.__round__())
        send_to_credit_International(USDChilequote, CardNo, Receive_accnt_name, Chile)
    if curname == "Colombia":
        Colombia = 'COP'
        USDColombialink = c.convert(USD, Colombia, c.Decimal(val))
        USDColombiaquote = float(USDColombialink.__round__())
        send_to_credit_International(USDColombiaquote, CardNo, Receive_accnt_name, Colombia)
    if curname == "Peru":
        Peru = 'PEN'
        USDPerulink = c.convert(USD, Peru, c.Decimal(val))
        USDPeruquote = float(USDPerulink.__round__())
        send_to_credit_International(USDPeruquote, CardNo, Receive_accnt_name, Peru)
    if curname == "Ecuador":
        # cur2 = 'PEN'
        # link = c.convert(cur2, cur, val)
        send_to_credit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Venezuela":
        Venezuela = 'VES'
        USDVenezuelalink = c.convert(USD, Venezuela, c.Decimal(val))
        USDVenezuelaquote = float(USDVenezuelalink.__round__())
        send_to_credit_International(USDVenezuelaquote, CardNo, Receive_accnt_name, Venezuela)
    if curname == "Uruguay":
        Uruguay = 'UYU'
        USDUruguaylink = c.convert(USD, Uruguay, c.Decimal(val))
        USDUruguayquote = float(USDUruguaylink.__round__())
        send_to_credit_International(USDUruguayquote, CardNo, Receive_accnt_name, Uruguay)
    # reg = "Africa"
    if curname == "Nigeria":
        Nigeria = 'NGN'
        USDNigerialink = c.convert(USD, Nigeria, c.Decimal(val))
        USDNigeriaquote = float(USDNigerialink.__round__())
        send_to_credit_International(USDNigeriaquote, CardNo, Receive_accnt_name, Nigeria)
    if curname == "South Africa":
        South_Africa = 'ZAR'
        USDSouth_Africalink = c.convert(USD, South_Africa, c.Decimal(val))
        USDSouth_Africaquote = float(USDSouth_Africalink.__round__())
        send_to_credit_International(USDSouth_Africaquote, CardNo, Receive_accnt_name, South_Africa)
    if curname == "Egypt":
        Egypt = 'EGP'
        USDEgyptlink = c.convert(USD, Egypt, c.Decimal(val))
        USDEgyptquote = float(USDEgyptlink.__round__())
        send_to_credit_International(USDEgyptquote, CardNo, Receive_accnt_name, Egypt)
    if curname == "Algeria":
        Algeria = 'DZD'
        USDAlgerialink = c.convert(USD, Algeria, c.Decimal(val))
        USDAlgeriaquote = float(USDAlgerialink.__round__())
        send_to_credit_International(USDAlgeriaquote, CardNo, Receive_accnt_name, Algeria)
    if curname == "Morocco":
        Morocco = 'MAD'
        USDMoroccolink = c.convert(USD, Morocco, c.Decimal(val))
        USDMoroccoquote = float(USDMoroccolink.__round__())
        send_to_credit_International(USDMoroccoquote, CardNo, Receive_accnt_name, Morocco)
    if curname == "Kenya":
        Kenya = 'KES'
        USDKenyalink = c.convert(USD, Kenya, c.Decimal(val))
        USDKenyaquote = float(USDKenyalink.__round__())
        send_to_credit_International(USDKenyaquote, CardNo, Receive_accnt_name, Kenya)
    if curname == "Ethiopia":
        Ethiopia = 'ETB'
        USDEthiopialink = c.convert(USD, Ethiopia, c.Decimal(val))
        USDEthiopiaquote = float(USDEthiopialink.__round__())
        send_to_credit_International(USDEthiopiaquote, CardNo, Receive_accnt_name, Ethiopia)
    if curname == "Ghana":
        Ghana = 'GHS'
        USDGhanalink = c.convert(USD, Ghana, c.Decimal(val))
        USDGhanaquote = float(USDGhanalink.__round__())
        print("Transaction processing")
        send_to_credit_International(USDGhanaquote, CardNo, Receive_accnt_name, Ghana)
        print("Transaction complete")
    if curname == "Angola":
        Angola = 'AOA'
        USDAngolalink = c.convert(USD, Angola, c.Decimal(val))
        USDAngolaquote = float(USDAngolalink.__round__())
        send_to_credit_International(USDAngolaquote, CardNo, Receive_accnt_name, Angola)
    if curname == "Tanzania":
        Tanzania = 'TZS'
        USDTanzanialink = c.convert(USD, Tanzania, c.Decimal(val))
        USDTanzaniaquote = float(USDTanzanialink.__round__())
        send_to_credit_International(USDTanzaniaquote, CardNo, Receive_accnt_name, Tanzania)
    if curname == "Ivory Coast":
        Ivory_Coast = 'XAF'
        USDIvory_Coastlink = c.convert(USD, Ivory_Coast, c.Decimal(val))
        USDIvory_Coastquote = float(USDIvory_Coastlink.__round__())
        send_to_credit_International(USDIvory_Coastquote, CardNo, Receive_accnt_name, Ivory_Coast)
    if curname == "Cameroon":
        Cameroon = 'XAF'
        USDCameroonlink = c.convert(USD, Cameroon, c.Decimal(val))
        USDCameroonquote = float(USDCameroonlink.__round__())
        send_to_credit_International(USDCameroonquote, CardNo, Receive_accnt_name, Cameroon)
    # reg = "Asia/Middle East"
    if curname == "China":
        China = 'CNY'
        USDChinalink = c.convert(USD, China, c.Decimal(val))
        USDChinaquote = float(USDChinalink.__round__())
        send_to_credit_International(USDChinaquote, CardNo, Receive_accnt_name, China)
    if curname == "Japan":
        Japan = 'JPY'
        USDJapanlink = c.convert(USD, Japan, c.Decimal(val))
        USDJapanquote = float(USDJapanlink.__round__())
        send_to_credit_International(USDJapanquote, CardNo, Receive_accnt_name, Japan)
    if curname == "India":
        India = 'INR'
        USDIndialink = c.convert(USD, India, c.Decimal(val))
        USDIndiaquote = float(USDIndialink.__round__())
        send_to_credit_International(USDIndiaquote, CardNo, Receive_accnt_name, India)
    if curname == "South Korea":
        South_Korea = 'KRW'
        USDSouth_Korealink = c.convert(USD, South_Korea, c.Decimal(val))
        USDSouth_Koreaquote = float(USDSouth_Korealink.__round__())
        send_to_credit_International(USDSouth_Koreaquote, CardNo, Receive_accnt_name, South_Korea)
    if curname == "Indonesia":
        Indonesia = 'IDR'
        USDIndonesialink = c.convert(USD, Indonesia, c.Decimal(val))
        USDIndonesiaquote = float(USDIndonesialink.__round__())
        send_to_credit_International(USDIndonesiaquote, CardNo, Receive_accnt_name, Indonesia)
    if curname == "Saudi Arabia":
        Saudi_Arabia = 'SAR'
        USDSaudi_Arabialink = c.convert(USD, Saudi_Arabia, c.Decimal(val))
        USDSaudi_Arabiaquote = float(USDSaudi_Arabialink.__round__())
        send_to_credit_International(USDSaudi_Arabiaquote, CardNo, Receive_accnt_name, Saudi_Arabia)
    if curname == "Taiwan":
        Taiwan = 'TWD'
        USDTaiwanlink = c.convert(USD, Taiwan, c.Decimal(val))
        USDTaiwanquote = float(USDTaiwanlink.__round__())
        send_to_credit_International(USDTaiwanquote, CardNo, Receive_accnt_name, Taiwan)
    if curname == "Thailand":
        Thailand = 'THB'
        USDThailandlink = c.convert(USD, Thailand, c.Decimal(val))
        USDThailandquote = float(USDThailandlink.__round__())
        send_to_credit_International(USDThailandquote, CardNo, Receive_accnt_name, Thailand)
    if curname == "UAE":
        UAE = 'AED'
        USDUAElink = c.convert(USD, UAE, c.Decimal(val))
        USDUAEquote = float(USDUAElink.__round__())
        send_to_credit_International(USDUAEquote, CardNo, Receive_accnt_name, UAE)
    if curname == "Israel":
        Israel = 'ILS'
        USDIsraellink = c.convert(USD, Israel, c.Decimal(val))
        USDIsraelquote = float(USDIsraellink.__round__())
        send_to_credit_International(USDIsraelquote, CardNo, Receive_accnt_name, Israel)
    if curname == "Philippines":
        Philippines = 'PHP'
        USDPhilippineslink = c.convert(USD, Philippines, c.Decimal(val))
        USDPhilippinesquote = float(USDPhilippineslink.__round__())
        send_to_credit_International(USDPhilippinesquote, CardNo, Receive_accnt_name, Philippines)
    if curname == "Hong Kong":
        Hong_Kong = 'HKD'
        USDHong_Konglink = c.convert(USD, Hong_Kong, c.Decimal(val))
        USDHong_Kongquote = float(USDHong_Konglink.__round__())
        send_to_credit_International(USDHong_Kongquote, CardNo, Receive_accnt_name, Hong_Kong)
    if curname == "Singapore":
        Singapore = 'SGD'
        USDSingaporelink = c.convert(USD, Singapore, c.Decimal(val))
        USDSingaporequote = float(USDSingaporelink.__round__())
        send_to_credit_International(USDSingaporequote, CardNo, Receive_accnt_name, Singapore)
    if curname == "Malaysia":
        Malaysia = 'MYR'
        USDMalaysialink = c.convert(USD, Malaysia, c.Decimal(val))
        USDMalaysiaquote = float(USDMalaysialink.__round__())
        send_to_credit_International(USDMalaysiaquote, CardNo, Receive_accnt_name, Malaysia)
    if curname == "Bangladesh":
        Bangladesh = 'BDT'
        USDBangladeshlink = c.convert(USD, Bangladesh, c.Decimal(val))
        USDBangladeshquote = float(USDBangladeshlink.__round__())
        send_to_credit_International(USDBangladeshquote, CardNo, Receive_accnt_name, Bangladesh)
    if curname == "Vietnam":
        Vietnam = 'VND'
        USDVietnamlink = c.convert(USD, Vietnam, c.Decimal(val))
        USDVietnamquote = float(USDVietnamlink.__round__())
        send_to_credit_International(USDVietnamquote, CardNo, Receive_accnt_name, Vietnam)
    # Carribean
    if curname == "Antigua":
        Antigua = 'XCD'
        USDAntigualink = c.convert(USD, Antigua, c.Decimal(val))
        USDAntiguaquote = float(USDAntigualink.__round__())
        send_to_credit_International(USDAntiguaquote, CardNo, Receive_accnt_name, Antigua)
    if curname == "Bahamas":
        Bahamas = 'BSD'
        USDBahamaslink = c.convert(USD, Bahamas, c.Decimal(val))
        USDBahamasquote = float(USDBahamaslink.__round__())
        send_to_credit_International(USDBahamasquote, CardNo, Receive_accnt_name, Bahamas)
    if curname == "Belize":
        Belize = 'BZD'
        USDBelizelink = c.convert(USD, Belize, c.Decimal(val))
        USDBelizequote = float(USDBelizelink.__round__())
        send_to_credit_International(USDBelizequote, CardNo, Receive_accnt_name, Belize)
    if curname == "Dominica":
        Dominica = 'DOP'
        USDDominicalink = c.convert(USD, Dominica, c.Decimal(val))
        USDDominicaquote = float(USDDominicalink.__round__())
        send_to_credit_International(USDDominicaquote, CardNo, Receive_accnt_name, Dominica)
    if curname == "Grenada":
        Grenada = 'XCD'
        USDGrenadalink = c.convert(USD, Grenada, c.Decimal(val))
        USDGrenadaquote = float(USDGrenadalink.__round__())
        send_to_credit_International(USDGrenadaquote, CardNo, Receive_accnt_name, Grenada)
    if curname == "Guyana":
        Guyana = 'GYD'
        USDGuyanalink = c.convert(USD, Guyana, c.Decimal(val))
        USDGuyanaquote = float(USDGuyanalink.__round__())
        send_to_credit_International(USDGuyanaquote, CardNo, Receive_accnt_name, Guyana)
    if curname == "Jamaica":
        Jamaica = 'JMD'
        USDJamaicalink = c.convert(USD, Jamaica, c.Decimal(val))
        USDJamaicaquote = float(USDJamaicalink.__round__())
        send_to_credit_International(USDJamaicaquote, CardNo, Receive_accnt_name, Jamaica)
    if curname == "Puerto Rico":
        Puerto_Rico = 'GYD'
        USDPuerto_Ricolink = c.convert(USD, Puerto_Rico, c.Decimal(val))
        USDPuerto_Ricoquote = float(USDPuerto_Ricolink.__round__())
        send_to_credit_International(USDPuerto_Ricoquote, CardNo, Receive_accnt_name, Puerto_Rico)
    if curname == "St. Kitts":
        St_Kitts = 'XCD'
        USDSt_Kittslink = c.convert(USD, St_Kitts, c.Decimal(val))
        USDSt_Kittsquote = float(USDSt_Kittslink.__round__())
        send_to_credit_International(USDSt_Kittsquote, CardNo, Receive_accnt_name, St_Kitts)
    if curname == "St. Lucia":
        st_lucia = 'XCD'
        USDst_lucialink = c.convert(USD, st_lucia, c.Decimal(val))
        USDst_luciaquote = float(USDst_lucialink.__round__())
        send_to_credit_International(USDst_luciaquote, CardNo, Receive_accnt_name, st_lucia)
    if curname == "St. Vincent & Grenadines":
        st_vincent = 'XCD'
        USDst_vincentlink = c.convert(USD, st_vincent, c.Decimal(val))
        USDst_vincentquote = float(USDst_vincentlink.__round__())
        send_to_credit_International(USDst_vincentquote, CardNo, Receive_accnt_name, st_vincent)
    if curname == "Suriname":
        Suriname = 'SRD'
        USDSurinamelink = c.convert(USD, Suriname, c.Decimal(val))
        USDSurinamequote = float(USDSurinamelink.__round__())
        send_to_credit_International(USDSurinamequote, CardNo, Receive_accnt_name, Suriname)
    if curname == "Trinidad & Tobago":
        Trinidad = 'TTD'
        USDTrinidadlink = c.convert(USD, Trinidad, c.Decimal(val))
        USDTrinidadquote = float(USDTrinidadlink.__round__())
        send_to_credit_International(USDTrinidadquote, CardNo, Receive_accnt_name, Trinidad)
    # reg = "Central America"
    if curname == "Guatemala":
        Guatemala = 'GTQ'
        USDGuatemalalink = c.convert(USD, Guatemala, c.Decimal(val))
        USDGuatemalaquote = float(USDGuatemalalink.__round__())
        send_to_credit_International(USDGuatemalaquote, CardNo, Receive_accnt_name, Guatemala)
    if curname == "Panama":
        Panama = 'PAB'
        USDPanamalink = c.convert(USD, Panama, c.Decimal(val))
        USDPanamaquote = float(USDPanamalink.__round__())
        send_to_credit_International(USDPanamaquote, CardNo, Receive_accnt_name, Panama)
    if curname == "Costa Rica":
        Costa_Rica = 'CRC'
        USDCosta_Ricalink = c.convert(USD, Costa_Rica, c.Decimal(val))
        USDCosta_Ricaquote = float(USDCosta_Ricalink.__round__())
        send_to_credit_International(USDCosta_Ricaquote, CardNo, Receive_accnt_name, Costa_Rica)
    if curname == "El Salvador":
        # cur2 = 'PAB'
        # link = c.convert(cur2, cur, val)
        send_to_credit_International(val, CardNo, Receive_accnt_name, USD)
    if curname == "Honduras":
        Honduras = 'HNL'
        USDHonduraslink = c.convert(USD, Honduras, c.Decimal(val))
        USDHondurasquote = float(USDHonduraslink.__round__())
        send_to_credit_International(USDHondurasquote, CardNo, Receive_accnt_name, Honduras)
    if curname == "Nicaragua":
        cur = 'USD'
        cur2 = 'NIO'
        link = c.convert(cur, cur2, c.Decimal(val))
        quote = float(link.__round__())
        send_to_credit_International(quote, CardNo, Receive_accnt_name, cur2)


def send_money_International_Debit(amount=float, CardNo=int, recipient=str,
                                   curname=str):  # send money between Debit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from InterDebitInov WHERE CardNo=?''', [CardNo])
    for get_inter_name in curr.fetchall():
        name = get_inter_name[0]
        s_name = str(name)
        curr.execute('''SELECT * from InterDebitInov WHERE name=?''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
            curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
            conn.commit()
            conn.close()
            inov.send_mail_for_International_Transactions(s_name, mail, mail_amount, curname)
            return "transaction complete"


def send_to_debit_International(amount=float, CardNo=int, recipient=str,
                                curname=str):  # send money between Debit Accounts
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from DebitInov WHERE CardNo=?''', [CardNo])
    for get_inter_name in curr.fetchall():
        name = get_inter_name[0]
        s_name = str(name)
        curr.execute('''SELECT * from InterDebitInov WHERE name=?''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE DebitInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
            curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
            conn.commit()
            conn.close()
            inov.send_mail_for_International_Transactions(s_name, mail, mail_amount, curname)
            return "transaction complete"
        else:
            send_to_credit_International(amount, CardNo, recipient, curname)


def send_to_credit_International(amount=float, CardNo=str, recipient=str,
                                 curname=str):  # Send money from Credit to Debit
    Bank_fee = "INOVBank"
    e_mail = str
    mail_amount = str(amount)
    # Connecting to sqlite
    conn = sqlite3.connect('inov.db')
    # Creating a cursor object using the cursor() method
    curr = conn.cursor()
    curr.execute('''SELECT * from CreditInov WHERE CardNo=?''', [CardNo])
    for get_inter_name in curr.fetchall():
        name = get_inter_name[0]
        s_name = str(name)
        curr.execute('''SELECT * from InterDebitInov WHERE name=?''', [recipient])
        for credit_row in curr.fetchall():
            email = credit_row[1]
            mail = e_mail(email)
            rate_r = 0.013
            fee = amount * rate_r
            total_val_credit = amount + fee
            curr.execute('''UPDATE CreditInov SET Checking=Checking-? WHERE CardNo=?''', [total_val_credit, CardNo])
            curr.execute('''UPDATE BusinessInov SET Saving=Saving+? WHERE name=?''', [fee, Bank_fee])
            # processing transaction
            curr.execute('''UPDATE InterDebitInov SET Checking=Checking+? WHERE name=?''', [amount, recipient])
            conn.commit()
            conn.close()
            inov.send_mail_for_International_Transactions(s_name, mail, mail_amount, curname)
            return "transaction complete"
