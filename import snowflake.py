import snowflake.connector

print("aman")

# Replace these with your Snowflake credentials
Username = "cosmicball"
password = 'Amys@240740'
account = 'xb14586.ap-southeast-1'
warehouse = 'COMPUTE_WH'
database = 'SNOWFLAKE_SAMPLE_DATA'
schema = 'TPCH_SF1'

# Establish a connection to Snowflake
conn = snowflake.connector.connect(
    user=Username,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Execute a sample query
query = "SELECT * FROM CUSTOMER"

cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Process and print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

