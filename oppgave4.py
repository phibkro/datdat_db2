import sqlite3

def hent_forestillinger_på_dato(date, cursor):
  # Query the database to get performances on the given date
  query = """
  SELECT Sal.Navn, Forestilling.StartTid, Stykke.Navn, Sal.ID
  FROM Forestilling
  INNER JOIN SesongStykke 
	ON Forestilling.SesongTypeID == SesongStykke.SesongTypeID 
		AND Forestilling.SesongStykkeÅr == SesongStykke.År
		AND Forestilling.SalID == SesongStykke.SalID
	INNER JOIN Stykke ON SesongStykke.StykkeID == Stykke.ID
	INNER JOIN Sal ON Forestilling.SalID == Sal.ID
  WHERE DATE(?) == DATE(StartTid)
  """
  cursor.execute(query, (date,))
  results = cursor.fetchall()

  return results

def hent_billett_mengde_solgt_på_forestilling(salID, startTid, cursor):
  # Query the database to get performances and ticket counts for the given date
  query = """
  SELECT COUNT(bt.ID)
  FROM Forestilling f
  INNER JOIN BillettType bt ON f.StartTid == bt.ForestillingStartTid
  INNER JOIN Billett b ON b.BillettTypeID == bt.ID
  WHERE f.SalID == ? AND DATE(?) == DATE(f.StartTid)
  """
  cursor.execute(query, (salID, startTid))
  results = cursor.fetchone()

  return results[0]

def main(cursor):
  # Get the date from the user
  date = input("Skriv inn dato (YYYY-MM-DD): ")
  # date = "2024-02-03"

  # print(f"Forestillinger på {date}:")
  forestillinger = hent_forestillinger_på_dato(date, cursor)
  # print(forestillinger)
  for forestilling in forestillinger:
    salNavn, startTid, stykkeNavn, salID = forestilling
    print(f"Billetter solgt for {stykkeNavn} på {startTid} i {salNavn}:")
    print(hent_billett_mengde_solgt_på_forestilling(salID, startTid, cursor))

if __name__ == "__main__":
  # Connect to the database
  conn = sqlite3.connect('db2.db')
  cursor = conn.cursor()

  main(cursor)

  # Close the database connection
  conn.close()