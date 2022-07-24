import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="inov", user='postgres', password='', host='localhost', port='5432'
)
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Executing an MYSQL function using the execute() method
cursor.execute("select * from CreditInov")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print("Credit account info: ", data)
