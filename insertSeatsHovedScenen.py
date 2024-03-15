import sqlite3

# Connect to the SQLite database
con = sqlite3.connect('db2.db')
cursor = con.cursor()

# Function to insert seats into the 'Stol' table with continuous numbering
def insert_seats_into_database(sal_id, omrade_navn, start_seat_num, end_seat_num, skipped_seats):
    seat_counter = start_seat_num
    while seat_counter <= end_seat_num:
        # Calculate the row number based on seat_counter; 28 seats per row for 'Parkett'
        if omrade_navn == 'Parkett':
            rad_nr = (seat_counter - 1) // 28 + 1
        else:  # For 'Galleri', adjust row calculation since it is different from 'Parkett'
            rad_nr = (seat_counter - 505) // 5 + 1  #  5 seats per row for 'Galleri

        # Skip the seat numbers that are not present
        if seat_counter not in skipped_seats:
            # Insert the seat into the database
            cursor.execute("INSERT INTO Stol (SalID, OmrådeNavn, StolNR, RadNR) VALUES (?, ?, ?, ?)",
                           (sal_id, omrade_navn, seat_counter, rad_nr))

        seat_counter += 1

# Skipped seats for 'Parkett' (specific rows might have specific skipped seats)
parkett_skipped_seats = [467, 468, 469, 470, 495, 496, 497, 498]

# Insert seats for 'Parkett'
insert_seats_into_database(1, 'Parkett', 1, 504, parkett_skipped_seats)

# 'Galleri' has seats from 505 to 524 and no skipped seats
insert_seats_into_database(1, 'Galleri', 505, 524, [])

# Commit the transaction to the database
con.commit()

# Close the database connection
con.close()
