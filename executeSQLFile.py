import sys
import sqlite3

def executeSQLFromFile(filename, cursor):
  try:
    f = open(filename, "r")
    sqlFile = f.read()
    sqlCommands = sqlFile.split(";")

    # start transaction
    cursor.execute("BEGIN")
    # enable foreign key constraint
    cursor.execute("PRAGMA foreign_keys = on;")

    for command in sqlCommands:
      try:
        cursor.execute(command)
      except sqlite3.OperationalError as msg:
        print(command)
        print(f"Command skipped: {msg}")

    # commit to end transaction and write to file
    cursor.execute("COMMIT;")
  except OSError:
    print("Failed to read file")
  finally:
    f.close()

# only runs if manually calling this in terminal
if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise Exception(f"{__file__} requires 1 argument")
  
  filepath = sys.argv[1].strip()
  dbPath = "db2.db"

  connection = sqlite3.connect(dbPath)

  # Disable auto-commit
  connection.isolation_level = None
  cursor = connection.cursor()
  executeSQLFromFile(filepath, cursor)
