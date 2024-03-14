import sys
import sqlite3

def executeSQLFromFile(filename, cursor):
  try:
    f = open(filename, "r")
    sqlFile = f.read()
    sqlCommands = sqlFile.split(";")

    cursor.execute("BEGIN")
    for command in sqlCommands:
      try:
        cursor.execute(command)
        print(f"{command}\nSuccessfully executed")
      except sqlite3.OperationalError as msg:
        print(f"Command skipped: {msg}")
    cursor.execute("COMMIT;")
  except OSError:
    print("Failed to read file")
  finally:
    f.close()

if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise Exception(f"{__file__} requires 1 argument")
  
  filepath = sys.argv[1].strip()
  dbPath = "db2.db"

  connection = sqlite3.connect(dbPath)
  connection.isolation_level = None
  cursor = connection.cursor()
  executeSQLFromFile(filepath, cursor)
