import sqlite3
import oppgave1
import Oppgave2_insertAndBuySeatsHovedScenen
import Oppgave2_insertAndBuySeatsGamleScene
import oppgave3

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

  connection.commit()

  connection.close()