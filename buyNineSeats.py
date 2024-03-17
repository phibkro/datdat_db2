import sqlite3
import random

def buy_nine_seats(cursor):

    def parse_and_identify_rows_with_nine_or_more_available_seats(file_path):
        # Open the file for reading
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Initialize variables
        section = None
        row_number = 0
        rows_with_available_seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}
        
        # Process each line in the file
        for line in lines:
            # Check if the line is a section name
            if line.strip() in ['Galleri', 'Balkong', 'Parkett']:
                section = line.strip()
                row_number = 0 # Reset row number for each section
            else:
                row_number += 1
                # Count the number of '0's in the line
                available_seats = line.count('0')
                # If there are 9 or more '0's, add to the list of rows with available seats
                if available_seats >= 9:
                    rows_with_available_seats[section].append((row_number, line))

        return rows_with_available_seats
    
    

    def buy_nine_adult_seats():

        cursor.execute("""
                        INSERT INTO Kunde (ID, Adresse, Navn, TlfNr) 
                        VALUES
                        ('3', 'Norgesgate 3', 'Markus Nordmann', '12348765')
                        """)
        
        file_path_gamle_scene = './files needed/gamle-scene.txt'
        available_section_and_rows = parse_and_identify_rows_with_nine_or_more_available_seats(file_path_gamle_scene)
        
        # Select a random section from the available sections
        random_section = random.choice(list(available_section_and_rows.keys()))
        
        random_row = random.choice(available_section_and_rows[random_section])
        counter = 0
        print(f"Randomly selected section: {random_section}, row: {random_row[0]}")

        for seat_index, seat in enumerate(random_row[1], start=1):
            if seat == '0' and counter < 9:
                # Now seat_index correctly identifies the seat number in the row
                cursor.execute("""
                                INSERT INTO Billett (BillettTypeNavn, SalID, OmrådeNavn, RadNr, StolNr)
                                VALUES (?, ?, ?, ?, ?)
                                """, (2,  2, random_section, random_row[0], seat_index))
                cursor.execute("""
                                INSERT INTO Billettkjøp (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr, KundeID, KjøpsTid) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)
                                """, (2, 2, random_section, random_row[0], seat_index, 3, '2024-02-03 17:30:00'))
                counter += 1

            def print_sold_seats_after_buying(file_path):
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                # Initialize variables
                section = None
                row_number = 0
                
                for line in lines:
                    if line.strip() in ['Galleri', 'Balkong', 'Parkett']:
                        section = line.strip()
                        row_number = 0
                        print(section)  # Ensure section names are printed
                    else:
                        row_number += 1
                        if section == random_section and row_number == random_row[0]:
                            counter = 0
                            for seat_index, seat in enumerate(random_row[1], start=1):
                                if seat == '0' and counter < 9:
                                    print('1', end='')
                                    counter += 1
                                else:
                                    print(seat, end='')
                            # print()  # Move to the next line after printing the modified row
                        else:
                            print(line, end='')  # Use end='' to avoid double newlines


        print_sold_seats_after_buying(file_path_gamle_scene)




    buy_nine_adult_seats()
        

    

