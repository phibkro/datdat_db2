--------------------Stykke----------------------------
-- SesongType Table
CREATE TABLE IF NOT EXISTS SesongType (
    SesongTypeID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

-- Stykke Table
CREATE TABLE IF NOT EXISTS Stykke (
    StykkeID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

-- SesongStykke Table
CREATE TABLE IF NOT EXISTS SesongStykke (
    SesongStykkeID INT PRIMARY KEY,
    StykkeID INT,
    SesongTypeID INT,
    SesongÅr INT,
    SalID INT,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID),
    FOREIGN KEY (SesongTypeID) REFERENCES SesongType(SesongTypeID),
    FOREIGN KEY (SalID) REFERENCES Sal(SalID)
);

-------------Akt og Rolle----------------
-- Akt Table
CREATE TABLE IF NOT EXISTS Akt (
    AktNr INT,
    StykkeID INT,
    AktID INT,
    AktNavn VARCHAR(255),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID),
    PRIMARY KEY (AktNr, StykkeID)
);

-- Rolle Table
CREATE TABLE IF NOT EXISTS Rolle (
    RolleID INT PRIMARY KEY,
    RolleNavn VARCHAR(255),
    StykkeID INT,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- AktRolle Table
CREATE TABLE IF NOT EXISTS AktRolle (
    AktID INT,
    RolleNavn VARCHAR(255),
    AnsattID INT,
    FOREIGN KEY (AktID) REFERENCES Akt(AktID),
    FOREIGN KEY (RolleNavn) REFERENCES Rolle(RolleNavn),
    FOREIGN KEY (AnsattID) REFERENCES Anssatt(AnsattID),
    PRIMARY KEY (AktID, RolleNavn)
);

----------------------Forestilling-------------------------
-- Sal Table
CREATE TABLE IF NOT EXISTS Sal (
    SalID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

-- Forestilling Table
CREATE TABLE IF NOT EXISTS Forestilling (
    ForestillingsID INT PRIMARY KEY,
    ForestillingsDatoTid DATETIME,
    SalID INT,
    StykkeID INT,
    FOREIGN KEY (SalID) REFERENCES Sal(SalID),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- Område Table
CREATE TABLE IF NOT EXISTS Område (
    SalID INT,
    OmrådeNavn VARCHAR(255),
    FOREIGN KEY (SalID) REFERENCES Sal(SalID),
    PRIMARY KEY (SalID, OmrådeNavn)
);

-- Stol Table
CREATE TABLE IF NOT EXISTS Stol (
    OmrådeNavn VARCHAR(255),
    StolNo INT,
    RadNo INT,
    StolID INT,
    FOREIGN KEY (OmrådeNavn) REFERENCES Område(OmrådeNavn),
    PRIMARY KEY (OmrådeNavn, StolNo, RadNo)
);

-------------------------Bilett-------------------------
-- BillettType Table
CREATE TABLE IF NOT EXISTS BillettType (
    BillettTypeID INT PRIMARY KEY,
    BillettType VARCHAR(255),
    StykkeID INT,
    Pris INT,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- Billett Table
CREATE TABLE IF NOT EXISTS Billett (
    BillettID INT PRIMARY KEY,
    BillettTypeID INT,
    ForestillingsID DATETIME,
    StolID INT,
    FOREIGN KEY (BillettTypeID) REFERENCES BillettType(BillettTypeID),
    FOREIGN KEY (ForestillingsID) REFERENCES Forestilling(ForestillingsID),
    FOREIGN KEY (StolID) REFERENCES Stol(StolID)
);

--Kunde Table
CREATE TABLE IF NOT EXISTS Kunde (
    KundeID INT PRIMARY KEY,
    Adresse VARCHAR(255),
    Navn VARCHAR(255),
    Mobilnummer INT
);

--Billettkjop Table
CREATE TABLE IF NOT EXISTS Bilettkjop (
    KundeID INT,
    BillettID INT,
    DatoTid DATETIME,
    FOREIGN KEY (KundeID) REFERENCES Kunde(KundeID),
    FOREIGN KEY (BillettID) REFERENCES Billett(BillettID),
    PRIMARY KEY (KundeID, BillettID)
);
-------------------Ansatt---------------------

-- AnsattStatusType Table
CREATE TABLE IF NOT EXISTS AnsattStatusType (
    AnsattStatusTypeID INT PRIMARY KEY,
    StatusType VARCHAR(255)
);

-- Oppgave Table
CREATE TABLE IF NOT EXISTS Posisjon (
    PosisjonID INT PRIMARY KEY,
    PosisjonTekst VARCHAR(255)
);

-- Ansatt Table
CREATE TABLE IF NOT EXISTS Ansatt (
    AnsattID INT PRIMARY KEY,
    AnsattStatusTypeID INT,
    Navn VARCHAR(255),
    Epost VARCHAR(255),
    FOREIGN KEY (AnsattStatusTypeID) REFERENCES AnsattStatusType(AnsattStatusTypeID)
);

CREATE TABLE IF NOT EXISTS Oppgave (
    OppgaveID INT PRIMARY KEY,
    OppgaveTekst VARCHAR(255)
);

-- AnsattOppgave Table
CREATE TABLE IF NOT EXISTS AnsattOppgave (
    ForestillingsID DATETIME,
    AnsattID INT,
    OppgaveID INT,
    FOREIGN KEY (ForestillingsID) REFERENCES Forestilling(ForestillingsID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID),
    PRIMARY KEY (ForestillingsID, AnsattID)
);