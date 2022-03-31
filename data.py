import sqlite3
# Bank database
DB_NAME = 'inv.db'


def get_database():
    conn = sqlite3.connect('inv.db')
    return conn


# Debit Account table
def debit_accounts_table():
    Debit = [
        '''CREATE TABLE DebitAccounts
            (name VARCHAR(255),
            email VARCHAR(255),
            CardNo VARCHAR(255),
            CardCode VARCHAR(255),
            SecurityCode  VARCHAR(250),
            Checking INT(150),
            Saving INT(150),
            Address VARCHAR(255),
            Country VARCHAR(255),
            Currency VARCHAR(255))'''
    ]

    db = get_database()
    cur = db.cursor()
    for table in Debit:
        cur.execute(table)


# Credit Account table
def credit_accounts_table():
    Credit = [
        '''CREATE TABLE CreditAccounts
            (name VARCHAR(255),
            email VARCHAR(255),
            CardNo VARCHAR(255),
            CardCode VARCHAR(255),
            SecurityCode  VARCHAR(250),
            Checking INT(150),
            Saving INT(150),
            Address VARCHAR(255),
            Country VARCHAR(255),
            Currency VARCHAR(255))'''
    ]

    db = get_database()
    cur = db.cursor()
    for table in Credit:
        cur.execute(table)


# Business Credit Account table
def Business_credit_accounts_table():
    B_Credit = [
        '''CREATE TABLE B-CreditAccounts
            (name VARCHAR(255),
            email VARCHAR(255),
            industry VARCHAR(255),
            CardNo VARCHAR(255),
            CardCode VARCHAR(255),
            SecurityCode  VARCHAR(250),
            Checking INT(150),
            Saving INT(150),
            Address VARCHAR(255),
            Country VARCHAR(255),
            Currency VARCHAR(255))'''
    ]

    db = get_database()
    cur = db.cursor()
    for table in B_Credit:
        cur.execute(table)
