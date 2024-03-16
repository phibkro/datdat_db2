import sqlite3

def insert_seats_and_buy_tickets(db_Path):
    # Connect to the SQLite database
    con = sqlite3.connect(db_Path)
    cursor = con.cursor()

    #Opprette generisk Kunde ID 1
    cursor.execute("""
                    INSERT INTO Kunde (ID, Adresse, Navn, TlfNr) 
                    VALUES
                    ('1', 'Norgesgate 1', 'Ola Nordmann', '12345678')
                    """)
    #Opprette generisk billettType for Kongsemnene ID 1
    cursor.execute("""
                    INSERT INTO BillettType
                    (ID, Navn, StykkeID, SalID, ForestillingStartTid, Pris)
                    VALUES
                    ('1', 'Ordinær', '1', '1', '2024-02-03 19:00:00', '450')
                    """)

    # Function to parse the document and find sold seats
    def parse_and_identify_sold_seats(file_path):
        sold_seats = {'Galleri': [], 'Parkett': []}  # Initialize empty lists to store sold seats for each area
        current_area = None  # To keep track of the current area being processed
        seat_counter = {'Galleri': 505, 'Parkett': 1}  # Start counters considering 'Galleri' seats numbering

        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line in ['Galleri', 'Parkett']:
                    current_area = line  # Update the current area
                elif line and current_area:  # Make sure we have started processing an area
                    for seat in line:
                        if seat == '1':
                            # Add the seat number to the sold_seats list for the current area
                            sold_seats[current_area].append(seat_counter[current_area])
                        if seat != 'x':  # Increment seat counter for actual seats only
                            seat_counter[current_area] += 1

        return sold_seats

    # Function to insert seats into the 'Stol' table with continuous numbering
    def insert_seats_into_database_and_purchase(sal_id, omrade_navn, start_seat_num, end_seat_num, skipped_seats, sold_seats):
        seat_counter = start_seat_num
        while seat_counter <= end_seat_num:
            # Calculate the row number based on seat_counter; 28 seats per row for 'Parkett'
            if omrade_navn == 'Parkett':
                rad_nr = (seat_counter - 1) // 28 + 1
            else:  # For 'Galleri', adjust row calculation since different from 'Parkett'
                rad_nr = (seat_counter - 505) // 5 + 1  #  5 seats per row for 'Galleri

            # Skip the seat numbers that are not present
            if seat_counter not in skipped_seats:
                # Insert the seat into the database
                cursor.execute("INSERT INTO Stol (SalID, OmrådeNavn, StolNR, RadNR) VALUES (?, ?, ?, ?)",
                            (sal_id, omrade_navn, seat_counter, rad_nr))
                
                # Check if the seat is sold and insert into Billett table if it is
                if seat_counter in sold_seats:
                    
                    # Insert into Billett table
                    cursor.execute("INSERT INTO Billett (BillettTypeNavn, SalID, RadNr, StolNr) VALUES (?, ?, ?, ?)",
                                (1, sal_id, rad_nr, seat_counter)) 
                    cursor.execute("""
                                INSERT INTO Billettkjøp (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr, KundeID, KjøpsTid) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                                (1, sal_id, omrade_navn, rad_nr, seat_counter, 1, '2024-02-03 16:00:00'))

            seat_counter += 1

    # Skipped seats for 'Parkett' (specific rows might have specific skipped seats)
    parkett_skipped_seats = [467, 468, 469, 470, 495, 496, 497, 498]

    #Solgte billetter
    file_path_Hovedscenen = './files needed/hovedscenen.txt'
    sold_seats = parse_and_identify_sold_seats(file_path_Hovedscenen)

    # Insert seats for 'Parkett'
    insert_seats_into_database_and_purchase(1, 'Parkett', 1, 504, parkett_skipped_seats, sold_seats['Parkett'])

    # 'Galleri' has seats from 505 to 524 and no skipped seats
    insert_seats_into_database_and_purchase(1, 'Galleri', 505, 524, [], sold_seats['Galleri'])

    # Commit the transaction to the database
    con.commit()

    # Close the database connection
    con.close()
