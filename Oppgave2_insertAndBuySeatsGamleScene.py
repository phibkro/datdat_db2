

def insert_seats_and_buy_tickets(cursor):

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
                    ('2', 'Ordinær', '2', '2', '2024-02-03 18:30:00', '350')
                    """)

    # Function to parse the document and find sold seats
    def parse_and_identify_sold_seats(file_path):
        seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}
        sold_seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}  # Initialize empty lists to store sold seats for each area
        current_area = None  # To keep track of the current area being processed
        seat_counter = {'Galleri': 1, 'Balkong': 1, 'Parkett': 1}  # Starting sesat counters for each section

        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line in ['Galleri', 'Balkong', 'Parkett']:
                    current_area = line  # Update the current area
                elif line and current_area:  # Make sure we have started processing an area
                    seats[current_area].append(line)
            
            for area in reversed(seats):
                current_area = area
                row_number = 0  # Reset row number for each new area
                for line in reversed(seats[area]): 
                    seat_counter = 1 # Start seat numbers at 1 for each new row 
                    row_number += 1  # Increment row number for each new row              
                    for seat in line:
                        if seat == '1':
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
                
                # Check if the seat is sold
                if (row[0], seat) in sold_seats[omrade_navn]:
                    #Insert the seat into Billett table if it is sold
                    cursor.execute("""
                        INSERT INTO Billett (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr)
                        VALUES (?, ?, ?, ?, ?)""",
                        (2, sal_id, omrade_navn, row[0], seat))
                    #Insert into BillettKjøp table if it is sold
                    cursor.execute("""
                                INSERT INTO Billettkjøp (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr, KundeID, KjøpsTid) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                                (2, sal_id, omrade_navn, row[0], seat, 2, '2024-02-03 15:30:00'))
                                

    
    galleri_rows = [(1, 33), (2, 18), (3, 17)]  # Rows and number of seats for 'Galleri'


    balkong_rows = [(1, 28), (2, 27), (3, 22), (4, 17)]  # Rows and number of seats for 'Balkong'


    parkett_rows = [
        (1, 18), (2, 16), (3, 17), (4, 18),(5, 18), 
        (6, 17), (7, 18), (8, 17), (9, 17), (10, 14)
    ]

    # path to text file with the seat layout for 'Gamle Scene'
    file_path_gamle_scene = './files needed/gamle-scene.txt'
    sold_seats = parse_and_identify_sold_seats(file_path_gamle_scene)

    # Call the function to insert seats for 'Galleri' and 'Parkett'
    insert_seats_into_database_and_purchase(2, 'Galleri', galleri_rows, sold_seats)
    insert_seats_into_database_and_purchase(2, 'Balkong', balkong_rows, sold_seats)
    insert_seats_into_database_and_purchase(2, 'Parkett', parkett_rows, sold_seats)

   