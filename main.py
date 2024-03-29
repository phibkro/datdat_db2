import sqlite3
import oppgave1
import Oppgave2_insertAndBuySeatsHovedScenen
import Oppgave2_insertAndBuySeatsGamleScene
import oppgave3
import oppgave4
import oppgave7
if __name__ == "__main__":
  dbPath = "db2.db"

  # Create the database file if it does not exist
  open(dbPath, 'a').close()

  # Connect to the database
  connection = sqlite3.connect(dbPath)
  
  # Disable auto-commit
  connection.isolation_level = None
  cursor = connection.cursor()

  # Drop all tables
  # Query for all table names
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  tables = cursor.fetchall()
  # Drop each table
  for table in tables:
      cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")

  #------------Oppgave 1------------
  oppgave1.executeSQLFromFile("db2_setup.sql", cursor)
  oppgave1.executeSQLFromFile("db2-seed.sql", cursor)


  #------------Oppgave 2------------
  #Kjøpe og sette inn billetter for Hovedscenen
  Oppgave2_insertAndBuySeatsHovedScenen.insert_seats_and_buy_tickets(cursor)
  #Kjøpe og sette inn billetter for GamleScene
  Oppgave2_insertAndBuySeatsGamleScene.insert_seats_and_buy_tickets(cursor)

  # #------------Oppgave 3------------
  print("--------------------Oppgave 3--------------------\n")
  oppgave3.buy_nine_seats(cursor)

  # Oppgave 4

  print("--------------------Oppgave 4--------------------\n")
  oppgave4.main(cursor)


  print("--------------------Oppgave 5--------------------\n")
  try:
    oppgave5 = open("Oppgave5.sql", "r")
    fem = oppgave5.read()
    cursor.execute(fem)
    for row in cursor.fetchall():
      print(row)
    print("\n")
  finally:
    oppgave5.close()

  print("--------------------Oppgave 6--------------------\n")
  try:
    oppgave6 = open("Oppgave6.sql", "r")
    fem = oppgave6.read()
    cursor.execute(fem)
    for row in cursor.fetchall():
      print(row)

  finally:
    oppgave6.close()
  print("\n")

  print("--------------------Oppgave 7--------------------\n")
  oppgave7.actors_in_the_same_act()
  
    
  # finally
  connection.commit()

  connection.close()