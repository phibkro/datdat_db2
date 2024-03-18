import sqlite3

def insert_customer(cursor, customer_id, address, name, phone_number):
  cursor.execute("""
          INSERT INTO Kunde (ID, Adresse, Navn, TlfNr) 
          VALUES (?, ?, ?, ?)
          """, (customer_id, address, name, phone_number))

def insert_ticket_type(cursor, ticket_type_id, name, play_id, hall_id, start_time, price):
  cursor.execute("""
          INSERT INTO BillettType
          (ID, Navn, StykkeID, SalID, ForestillingStartTid, Pris)
          VALUES (?, ?, ?, ?, ?, ?)
          """, (ticket_type_id, name, play_id, hall_id, start_time, price))

def parse_and_identify_sold_seats(file_path):
  seats = {}
  sold_seats = {}

  with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      if line:
        current_area = line
        seats[current_area] = []
        sold_seats[current_area] = []

    for area in seats:
      current_area = area
      for line in reversed(seats[area]):
        for seat in line:
          if seat == '1':
            sold_seats[current_area].append(seat)

  return sold_seats

def insert_seats_and_purchase(cursor, hall_id, area_name, rows, sold_seats, ticket_type_id, purchase_time):
  for row in rows:
    for seat in range(1, row[1] + 1):
      cursor.execute("INSERT INTO Stol (SalID, OmrådeNavn, StolNR, RadNR) VALUES (?, ?, ?, ?)",
              (hall_id, area_name, seat, row[0]))

      if seat in sold_seats[area_name]:
        cursor.execute("""
          INSERT INTO Billett (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr)
          VALUES (?, ?, ?, ?, ?)""",
          (ticket_type_id, hall_id, area_name, row[0], seat))

        cursor.execute("""
          INSERT INTO Billettkjøp (BillettTypeID, SalID, OmrådeNavn, RadNr, StolNr, KundeID, KjøpsTid) 
          VALUES (?, ?, ?, ?, ?, ?, ?)""",
          (ticket_type_id, hall_id, area_name, row[0], seat, customer_id, purchase_time))

def gamle_scene_insert_seats_and_buy_tickets(cursor):
  insert_customer(cursor, '2', 'Norgesgate 2', 'Kari Nordmann', '87654321')
  insert_ticket_type(cursor, '2', 'Ordinær', '1', '2', '2024-02-03 18:30:00', '350')

  file_path_gamle_scene = './files needed/gamle-scene.txt'
  sold_seats = parse_and_identify_sold_seats(file_path_gamle_scene)

  galleri_rows = [(1, 33), (2, 18), (3, 17)]
  balkong_rows = [(1, 28), (2, 27), (3, 22), (4, 17)]
  parkett_rows = [
    (1, 18), (2, 16), (3, 17), (4, 18),(5, 18), 
    (6, 17), (7, 18), (8, 17), (9, 17), (10, 14)
  ]

  insert_seats_and_purchase(cursor, 2, 'Galleri', galleri_rows, sold_seats, '2', '2024-02-03 15:30:00')
  insert_seats_and_purchase(cursor, 2, 'Balkong', balkong_rows, sold_seats, '2', '2024-02-03 15:30:00')
  insert_seats_and_purchase(cursor, 2, 'Parkett', parkett_rows, sold_seats, '2', '2024-02-03 15:30:00')

def hovedscene_insert_seats_and_buy_tickets(cursor):
  insert_customer(cursor, '1', 'Norgesgate 1', 'Ola Nordmann', '12345678')
  insert_ticket_type(cursor, '1', 'Ordinær', '1', '1', '2024-02-03 19:00:00', '450')

  file_path_hovedscenen = './files needed/hovedscenen.txt'
  sold_seats = parse_and_identify_sold_seats(file_path_hovedscenen)

  parkett_rows = [
    (1, 18), (2, 16), (3, 17), (4, 18),(5, 18), 
    (6, 17), (7, 18), (8, 17), (9, 17), (10, 14)
  ]

  insert_seats_and_purchase(cursor, 1, 'Parkett', parkett_rows, sold_seats, '1', '2024-02-03 16:00:00')

  galleri_rows = [(1, 20), (2, 20), (3, 20)]
  insert_seats_and_purchase(cursor, 1, 'Galleri', galleri_rows, sold_seats, '1', '2024-02-03 16:00:00')
