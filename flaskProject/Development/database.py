import mysql.connector

def create_database():
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac"
    )
    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS your_database_name")  # Replace 'your_database_name' with your desired database name

    # Close connection
    cursor.close()
    conn.close()

def get_db():
    # Create database if it doesn't exist
    create_database()

    # Connect to MySQL database
    db = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac",
        database="your_database_name"  # Replace 'your_database_name' with your desired database name
    )
    return db
