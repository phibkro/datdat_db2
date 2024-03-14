import sys
import sqlite3

# Requires "db.sql" 
if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise Exception(f"{__file__} requires 1 argument")
  
  filepath = sys.argv[1].strip()

  try:
    f = open(sys.argv)
  finally:
    f.close()

connection = sqlite3.connect("db2.db")
cursor = connection.cursor()

def executeSQLFromFile(filename):
  try:
    f = open(filename, "r")
    sqlFile = f.read()
  except OSError:
    print("Failed to read file")
  finally:
    f.close()

  sqlCommands = sqlFile.split(";")

  for command in sqlCommands:
    try:
      cursor.execute(command)
    except sqlite3.OperationalError as msg:
      print("Command skipped: ", msg)