import sqlite3

def actors_in_the_same_act(name):

    dbPath_1 = "oppgave7.db"

    dbPath_2 = "db2.db"


    connection_1 = sqlite3.connect(dbPath_1)
    cursor_1 = connection_1.cursor()

    connection_2 = sqlite3.connect(dbPath_2)
    cursor_2 = connection_2.cursor()

    cursor_1.execute("""CREATE TABLE IF NOT EXISTS TabellNavn (
                        StykkeID INT NOT NULL,
                        AktNR INT,
                        RolleID INT,
                        AnsattID INT,
                        AnsattID2 INT,
                        AnsattStatusID INT,
                        AnsattPosisjonID INT,
                        Navn VARHCAR(255),
                        Epost VARHCAR(255),
                        StykkeID2 INT,
                        StykkeNavn VARHCAR(255),

                        PRIMARY KEY (StykkeID, AktNR, RolleID, AnsattID, AnsattID2, AnsattStatusID, AnsattPosisjonID, Navn, Epost, StykkeID2, StykkeNavn)
                      )""")
    
    cursor_2.execute("""SELECT * 
                   FROM
                   AktRolle INNER JOIN Ansatt ON AktRolle.AnsattID = Ansatt.ID
                     INNER JOIN Stykke ON AktRolle.StykkeID = Stykke.ID
                   WHERE Ansatt.AnsattPosisjonID = 1
                   """)          
    tabell_1 = cursor_2.fetchall()

    connection_2.commit()
    connection_2.close()

    #StykkeID, AktNR, Navn til insatt skuespilleren
    tabell_navn = [(row[0], row[1], row[7]) for row in tabell_1 if row[7] == name]

    for row in tabell_1:
        cursor_1.execute("""INSERT INTO TabellNavn (StykkeID, AktNR, RolleID, AnsattID, AnsattID2, AnsattStatusID, AnsattPosisjonID, Navn, Epost, StykkeID2, StykkeNavn)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
    
    connection_1.commit()

#     for row in tabell_navn:
#         cursor_1.execute("""SELECT TabellNavn.Navn
#                           FROM TabellNavn
#                           WHERE TabellNavn.StykkeID = ? AND TabellNavn.AktNR = ?""", (row[0], row[1]))
# """
actors_in_the_same_act("Emil Olafsson")