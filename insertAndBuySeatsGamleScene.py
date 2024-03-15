import sqlite3

def insert_seats_and_buy_tickets(db_Path):
    # Connect to the SQLite database
    con = sqlite3.connect(db_Path)
    cursor = con.cursor()

    #Opprette generisk Kunde ID 2
    cursor.execute("""
                    INSERT INTO Kunde (ID, Adresse, Navn, TlfNr) 
                    VALUES
                    ('2', 'Norgesgate 2', 'Kari Nordmann', '87654321')
                    """)
    #Opprette generisk billettType for Størst av alt er kjærligheten ID 2
    cursor.execute("""
                    INSERT INTO BillettType
                    (ID, Navn, StykkeID, SalID, ForestillingStartTid, Pris)
                    VALUES
                    ('2', 'Ordinær', '1', '1', '2024-02-03 18:30:00', '350')
                    """)

    # Function to parse the document and find sold seats
    def parse_and_identify_sold_seats(file_path):
        sold_seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}  # Initialize empty lists to store sold seats for each area
        current_area = None  # To keep track of the current area being processed
        seat_counter = {'Galleri': 1, 'Balkong': 1, 'Parkett': 1}  # Start counters considering 'Galleri' seats numbering

        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line in ['Galleri', 'Balkong', 'Parkett']:
                    current_area = line  # Update the current area
                    row_number = 1  # Reset row number for each new area
                elif line and current_area:  # Make sure we have started processing an area
                    seat_counter = 1 # Start seat numbers at 1 for each new row
                    row_number += 1  # Increment row number for each new row
                    for seat in line:
                        if seat == '1': # If the seat is sold
                            # Add the seat number to the sold_seats list for the current area
                            sold_seats[current_area].append((row_number, seat_counter))
                        seat_counter += 1

        return sold_seats

    # Function to insert seats into the 'Stol' table
    def insert_seats_into_database_and_purchase(sal_id, omrade_navn, rows, sold_seats):
        for row in rows:
            for seat in range(1, row[1] + 1):
                cursor.execute("INSERT INTO Stol (SalID, OmrådeNavn, StolNR, RadNR) VALUES (?, ?, ?, ?)",
                                (sal_id, omrade_navn, seat, row[0]))
                
                # Check if the seat is sold and 
                if (row[0], seat) in sold_seats[omrade_navn]:
                    #insert into Billett table if it is
                    cursor.execute("""
                        INSERT INTO Billett (BillettTypeNavn, SalID, RadNr, StolNr)
                        VALUES (?, ?, ?, ?)""",
                        (2, sal_id, row[0], seat))
                    #insert into BillettKjøp table if it is
                    cursor.execute("""
                                INSERT INTO Billettkjøp (BillettTypeNavn, SalID, OmrådeNavn, RadNr, StolNr, KundeID, KjøpsTid) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                                (1, sal_id, omrade_navn, row[0], seat, 2, '2024-02-03 15:30:00'))
                                

    # Insert seats for 'Galleri'
    galleri_rows = [(1, 33), (2, 18), (3, 17)]  # Rows and number of seats for 'Galleri'

    # Insert seats for 'Balkong'
    balkong_rows = [(1, 28), (2, 27), (3, 22), (4, 17)]  # Rows and number of seats for 'Balkong'

    # Insert seats for 'Parkett'
    parkett_rows = [
        (1, 18), (2, 16), (3, 17), (4, 18),(5, 18), 
        (6, 17), (7, 18), (8, 17), (9, 17), (10, 14)
    ]

    file_path_gamle_scene = './files needed/gamle-scene.txt'
    sold_seats = parse_and_identify_sold_seats(file_path_gamle_scene)

    # Call the function to insert seats for 'Galleri' and 'Parkett'
    insert_seats_into_database_and_purchase(2, 'Galleri', galleri_rows, sold_seats)
    insert_seats_into_database_and_purchase(2, 'Balkong', balkong_rows, sold_seats)
    insert_seats_into_database_and_purchase(2, 'Parkett', parkett_rows, sold_seats)

    # Commit the transaction to the database
    con.commit()

    # Close the database connection
    con.close()