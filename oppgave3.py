import sqlite3
import random

def buy_nine_seats(cursor):

    def parse_and_identify_rows_with_nine_or_more_available_seats(file_path):
        seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}
        seats_reversed = {'Galleri': [], 'Balkong': [], 'Parkett': []}
        current_area = None  # To keep track of the current area being processed
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line in ['Galleri', 'Balkong', 'Parkett']:
                    current_area = line  # Update the current area
                elif line and current_area:  # Make sure we have started processing an area
                    seats[current_area].append(line)
     
        row_number = 0
        rows_with_available_seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}
        
        for area in reversed(seats):
            current_area = area
            row_number = 0  # Reset row number for each new area
            for line in reversed(seats[area]):
                row_number += 1 
                seats_reversed[current_area].append(line)
                # Count the number of '0's in the line
                available_seats = line.count('0')
                # If there are 9 or more '0's, add to the list of rows with available seats
                if available_seats >= 9:
                    rows_with_available_seats[current_area].append((row_number, line))
                
        
        return rows_with_available_seats, seats_reversed
    

    def buy_nine_adult_seats():

        cursor.execute("""
                        INSERT INTO Kunde (ID, Adresse, Navn, TlfNr) 
                        VALUES
                        ('3', 'Norgesgate 3', 'Markus Nordmann', '12348765')
                        """)
        
        file_path_gamle_scene = './files needed/gamle-scene.txt'
        available_section_and_rows, seats_reversed = parse_and_identify_rows_with_nine_or_more_available_seats(file_path_gamle_scene)
        
        # Select a random section from the available sections
        random_section = random.choice(list(available_section_and_rows.keys()))
        
        random_row = random.choice(available_section_and_rows[random_section])
        counter = 0
        print(f"Randomly selected section: {random_section}, row: {random_row[0]}\n")
        print(f"Buying 9 adult seats costs 350x9 = 3150 NOK\n")
        print(f"Updated seating arrangement after buying 9 adult seats in section {random_section} and row: {random_row[0]}\n")

        for seat_index, seat in enumerate(random_row[1], start=1):
            
            if seat == '0' and counter < 9:
                # Now seat_index correctly identifies the seat number in the row
                cursor.execute("""
                                INSERT INTO Billett (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr)
                                VALUES (?, ?, ?, ?, ?)
                                """, (2,  2, random_section, random_row[0], seat_index))
                cursor.execute("""
                                INSERT INTO Billettkjøp (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr, KundeID, KjøpsTid) 
                                VALUES (?, ?, ?, ?, ?, ?, ?)
                                """, (2, 2, random_section, random_row[0], seat_index, 3, '2024-02-03 17:30:00'))
                counter += 1
                #print(f"Seat {seat_index} in row {random_row[0]} in section {random_section} has been bought")
            

            def print_sold_seats_after_buying(file_path, random_row, random_section, counter):
                seats = {'Galleri': [], 'Balkong': [], 'Parkett': []}
                current_area = None  # To keep track of the current area being processed
                to_print = {'Dato': [], 'Galleri': [], 'Balkong': [], 'Parkett': []}

                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    to_print['Dato'].append(lines[0].strip())

                    for line in lines:
                        line = line.strip()
                        if line in ['Galleri', 'Balkong', 'Parkett']:
                            current_area = line  # Update the current area
                        elif line and current_area:  # Make sure we have started processing an area
                            seats[current_area].append(line)
            
                # Assuming the structure of seats_reversed and other variables
                for area, rows in seats_reversed.items():
                    print(f"{area}:")  # Print the area name
                    row_number_Galleri = 4
                    row_number_Balkong = 5
                    row_number_Parkett = 11
                    for row in reversed(rows):
                        if area == 'Galleri':
                            row_number_Galleri -= 1
                            row_number = row_number_Galleri
                        elif area == 'Balkong':
                            row_number_Balkong -= 1
                            row_number = row_number_Balkong
                        elif area == 'Parkett':
                            row_number_Parkett -= 1
                            row_number = row_number_Parkett

                        if area == random_section and row_number == random_row[0]:
                            counter = 0  # Reset the counter for each new row
                            line_to_add = ""
                            print(f"Row {row_number}: ", end='')  # Print the row number
                            for seat_index, seat in enumerate(row, start=1):
                                if seat == '0' and counter < 9:
                                    line_to_add += '1'  # Mark seat as sold
                                    counter += 1
                                else:
                                    line_to_add += seat  # Add seat as is
                            print(line_to_add)  # Print the updated row
                        else:
                            print(f"Row {row_number}: {row}")  # Print the row as is for other rows
                    print()  # Add an extra newline for better readability between sections


        print_sold_seats_after_buying(file_path_gamle_scene, random_row, random_section, 0)
            
    buy_nine_adult_seats()
        

    

