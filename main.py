import sqlite3
import executeSQLFile

if __name__ == "__main__":
  dbPath = "db2.db"

  connection = sqlite3.connect(dbPath)
  
  # Disable auto-commit
  connection.isolation_level = None
  cursor = connection.cursor()

  executeSQLFile.executeSQLFromFile("db2-setup.sql", cursor)
  executeSQLFile.executeSQLFromFile("db2-seed.sql", cursor)

  connection.close()