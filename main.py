import sqlite3
import executeSQLFile
import insertAndBuySeatsHovedScenen
import insertAndBuySeatsGamleScene

if __name__ == "__main__":
  dbPath = "db2.db"

  connection = sqlite3.connect(dbPath)
  
  # Disable auto-commit
  connection.isolation_level = None
  cursor = connection.cursor()

  executeSQLFile.executeSQLFromFile("db2_setup.sql", cursor)

  #Kjøpe og sette inn billetter for Hovedscenen
  insertAndBuySeatsHovedScenen.insert_seats_and_buy_tickets(dbPath)
  #Kjøpe og sette inn billetter for GamleScene
  insertAndBuySeatsGamleScene.insert_seats_and_buy_tickets(dbPath)



  connection.close()