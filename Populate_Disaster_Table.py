import sqlite3

# Connect to the database
conn = sqlite3.connect('Natural_Disaster_Management.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS disaster (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Type TEXT,
                    Location TEXT,
                    Severity TEXT,
                    Year INTEGER,
                    Month TEXT,
                    Day INTEGER
                )''')

# Define the data to insert into the table
data = [
    ('Earthquake', 'Japan', 'Moderate', 2020, 'October', 25),
    ('Floods', 'India', 'High', 2020, 'October', 25),
    ('Tornado', 'United States', 'Extreme', 2020, 'November', 10),
    ('Cyclone', 'Australia', 'High', 2021, 'January', 5),
    ('Wildfire', 'Canada', 'Moderate', 2021, 'February', 15),
    ('Hurricane', 'Mexico', 'Extreme', 2021, 'March', 20),
    ('Blizzard', 'Russia', 'High', 2021, 'December', 10),
    ('Drought', 'Brazil', 'Moderate', 2022, 'April', 30),
    ('Landslide', 'China', 'High', 2022, 'May', 15),
    ('Volcano', 'Italy', 'Extreme', 2022, 'June', 5),
]

# Insert the data into the table
cursor.executemany('''INSERT INTO disaster (Type, Location, Severity, Year, Month, Day)
                    VALUES (?, ?, ?, ?, ?, ?)''', data)

cursor.execute("SELECT * FROM disaster")
print(cursor.fetchall())

# Commit the changes and close the connection
conn.commit()
conn.close()
