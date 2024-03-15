import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('db2.db')
cursor = con.cursor()

# Function to insert seats into the 'Stol' table
def insert_seats_into_database_gamle_scene(sal_id, omrade_navn, rows):
    for row in rows:
        for seat in range(1, row[1] + 1):
            cursor.execute("INSERT INTO Stol (SalID, OmrådeNavn, StolNR, RadNR) VALUES (?, ?, ?, ?)",
                               (sal_id, omrade_navn, seat, row[0]))

# Insert seats for 'Galleri'
galleri_rows = [(1, 33), (2, 18), (3, 17)]  # Rows and number of seats for 'Galleri'

# Insert seats for 'Balkong'
balkong_rows = [(1, 28), (2, 27), (3, 22), (4, 17)]  # Rows and number of seats for 'Balkong'

# Insert seats for 'Parkett'
parkett_rows = [
    (1, 18), (2, 16), (3, 17), (4, 18),(5, 18), 
    (6, 17), (7, 18), (8, 17), (9, 17), (10, 14)
]

# Call the function to insert seats for 'Galleri' and 'Parkett'
insert_seats_into_database_gamle_scene(2, 'Galleri', galleri_rows)
insert_seats_into_database_gamle_scene(2, 'Balkong', balkong_rows)
insert_seats_into_database_gamle_scene(2, 'Parkett', parkett_rows)

# Commit the transaction to the database
con.commit()

# Close the database connection
con.close()