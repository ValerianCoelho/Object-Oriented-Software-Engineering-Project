import sqlite3

# Connect to the database
conn = sqlite3.connect('donations_data.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS donations (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Email TEXT,
                    Amount REAL,
                    Country TEXT
                )''')

# Define the data to insert into the table
data = [
    ('John Doe', 'johndoe@example.com', 100.50, 'United States'),
    ('Jane Smith', 'janesmith@example.com', 250.75, 'Canada'),
    ('Michael Johnson', 'michaeljohnson@example.com', 50.25, 'Australia'),
    ('Sarah Williams', 'sarahwilliams@example.com', 75.00, 'United Kingdom'),
    ('David Lee', 'davidlee@example.com', 200.00, 'Germany'),
    ('Emily Chen', 'emilychen@example.com', 150.50, 'China'),
    ('Daniel Kim', 'danielkim@example.com', 300.25, 'South Korea'),
    ('Maria Lopez', 'marialopez@example.com', 75.75, 'Mexico'),
    ('Mohammed Ali', 'mohammedali@example.com', 500.00, 'United Arab Emirates'),
    ('Sophie Dubois', 'sophiedubois@example.com', 100.00, 'France')
]

# Insert the data into the table
cursor.executemany('INSERT INTO donations (Name, Email, Amount, Country) VALUES (?, ?, ?, ?)', data)

cursor.execute("SELECT * FROM donations")
print(cursor.fetchall())

# Commit the changes and close the connection
conn.commit()
conn.close()
