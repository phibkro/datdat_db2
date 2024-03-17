import sqlite3
import executeSQLFile
import insertAndBuySeatsHovedScenen
import insertAndBuySeatsGamleScene
import buyNineSeats

if __name__ == "__main__":
  dbPath = "db2.db"

  connection = sqlite3.connect(dbPath)
  
  # Disable auto-commit
  connection.isolation_level = None
  cursor = connection.cursor()

  #------------Oppgave 1------------
  executeSQLFile.executeSQLFromFile("db2_setup.sql", cursor)
  #executeSQLFile.executeSQLFromFile("db2_seed.sql", cursor)


  #------------Oppgave 2------------
  #Kjøpe og sette inn billetter for Hovedscenen
  insertAndBuySeatsHovedScenen.insert_seats_and_buy_tickets(cursor)
  #Kjøpe og sette inn billetter for GamleScene
  insertAndBuySeatsGamleScene.insert_seats_and_buy_tickets(cursor)

  # #------------Oppgave 3------------
  print("--------------------Oppgave 3--------------------\n")
  buyNineSeats.buy_nine_seats(cursor)

  connection.commit()

  connection.close()