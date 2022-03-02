from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///BTCdata.db')
conn_connect = create_engine('sqlite:///data.db')


# account bank statements
def get_bank_statement(pin=int):
    conn = db_connect.connect()
    # BTC Holdings
    sort = conn.execute("select name, BTC from InovClientsCrypto WHERE SDC=?", [pin])
    result1 = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("BTC Holdings of clients:")
    print(result1)
    # USD Holdings
    sort2 = conn.execute("select name, USD from InovClientsCrypto WHERE SDC=?", [pin])
    result2 = {'data': [dict(zip(tuple(sort2.keys()), i)) for i in sort2.cursor]}
    print("Dollar Balance of clients:")
    print(result2)
    # EUR Holdings
    sort3 = conn.execute("select name, EU from InovClientsCrypto WHERE SDC=?", [pin])
    result3 = {'data': [dict(zip(tuple(sort3.keys()), i)) for i in sort3.cursor]}
    print("Euro Balance of clients:")
    print(result3)
    # GBP Holdings
    sort4 = conn.execute("select name, GBP from InovClientsCrypto WHERE SDC=?", [pin])
    result4 = {'data': [dict(zip(tuple(sort4.keys()), i)) for i in sort4.cursor]}
    print("Pound Sterling Balance of clients:")
    print(result4)
    # CNY Holdings
    sort5 = conn.execute("select name, CNY from InovClientsCrypto WHERE SDC=?", [pin])
    result5 = {'data': [dict(zip(tuple(sort5.keys()), i)) for i in sort5.cursor]}
    print("Chinese Yuan Balance of clients:")
    print(result5)


# account country of origin
def getCountry():
    conn = db_connect.connect()
    sort = conn.execute("select name, Country from InovClientsCrypto ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Clients Country of Residence")
    print(result)


# account pin
def getPIN():
    conn = db_connect.connect()
    sort = conn.execute("select name, SDC from InovClientsCrypto ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Pins of clients:")
    print(result)


# account Digital credit line
def getDCL():
    conn = db_connect.connect()
    sort = conn.execute("select name, DCL from InovClientsCrypto ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Digital credit of clients:")
    print(result)


# account balance in Bitcoin
def getBTC():
    conn = db_connect.connect()
    sort = conn.execute("select name, BTC from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("BTC Holdings of clients:")
    print(result)


# account balance in United States Dollar
def getUSD():
    conn = db_connect.connect()
    sort = conn.execute("select name, USD from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Dollar Balance of clients:")
    print(result)


# account balance in Euros
def getEUR():
    conn = db_connect.connect()
    sort = conn.execute("select name, EU from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Euro Balance of clients:")
    print(result)


# account balance in British Pound
def getGBP():
    conn = db_connect.connect()
    sort = conn.execute("select name, GBP from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Pound Sterling Balance of clients:")
    print(result)


# account balance in Chinese Yuan
def getCNY():
    conn = db_connect.connect()
    sort = conn.execute("select name, CNY from InovClientsData ")
    result = {'data': [dict(zip(tuple(sort.keys()), i)) for i in sort.cursor]}
    print("Chinese Yuan Balance of clients:")
    print(result)

