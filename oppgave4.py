import sqlite3

def hent_forestillinger_på_dato(date):
  # Query the database to get performances on the given date
  query = """
  SELECT SalID, StartTid
  FROM Forestilling
  WHERE DATE(?) == DATE(StartTid)
  """
  cursor.execute(query, (date,))
  results = cursor.fetchall()

  return results

# Connect to the database
conn = sqlite3.connect('db2.db')
cursor = conn.cursor()

if __name__ == "__main__":
  # Get the date from the user
  # date = input("Enter the date (YYYY-MM-DD): ")

  # test
  date = "2024-02-03"
  print(f"Performances on {date}:")
  print(hent_forestillinger_på_dato(date))

# Close the database connection
conn.close()