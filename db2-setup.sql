--------------------Stykke----------------------------
-- SesongType Table
CREATE TABLE SesongType (
    SesongTypeID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

-- Stykke Table
CREATE TABLE Stykke (
    StykkeID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

-- SesongStykke Table
CREATE TABLE SesongStykke (
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
CREATE TABLE Akt (
    AktNr INT,
    StykkeID INT,
    AktID INT,
    AktNavn VARCHAR(255),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID),
    PRIMARY KEY (AktNr, StykkeID)
);

-- Rolle Table
CREATE TABLE Rolle (
    RolleID INT PRIMARY KEY,
    RolleNavn VARCHAR(255),
    StykkeID INT,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- AktRolle Table
CREATE TABLE AktRolle (
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
CREATE TABLE Sal (
    SalID INT PRIMARY KEY,
    Navn VARCHAR(255)
);

-- Forestilling Table
CREATE TABLE Forestilling (
    ForestillingsID INT PRIMARY KEY,
    ForestillingsDatoTid DATETIME,
    SalID INT,
    StykkeID INT,
    FOREIGN KEY (SalID) REFERENCES Sal(SalID),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- Område Table
CREATE TABLE Område (
    SalID INT,
    OmrådeNavn VARCHAR(255),
    FOREIGN KEY (SalID) REFERENCES Sal(SalID),
    PRIMARY KEY (SalID, OmrådeNavn)
);

-- Stol Table
CREATE TABLE Stol (
    SalID INT,
    OmrådeNavn VARCHAR(255),
    StolNo INT,
    RadNo INT,
    FOREIGN KEY (SalID, OmrådeNavn) REFERENCES Område(SalID, OmrådeNavn),
    PRIMARY KEY (SalID, OmrådeNavn, StolNo, RadNo)
);

-------------------------Bilett-------------------------
-- BillettType Table
CREATE TABLE BillettType (
    BillettTypeID INT PRIMARY KEY,
    Navn VARCHAR(255),
    StykkeID INT,
    Pris INT,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- Billett Table
CREATE TABLE Billett (
    BillettID INT PRIMARY KEY,
    BillettTypeID INT,
    ForestillingsID DATETIME,
    SalID INT, 
    OmrådeNavn VARCHAR(255), 
    StolNo INT, 
    RadNo INT,
    FOREIGN KEY (BillettTypeID) REFERENCES BillettType(BillettTypeID),
    FOREIGN KEY (ForestillingsID) REFERENCES Forestilling(ForestillingsID),
    FOREIGN KEY (SalID, OmrådeNavn, StolNo, RadNo) REFERENCES Stol(SalID, OmrådeNavn, StolNo, RadNo)
);

--Kunde Table
CREATE TABLE Kunde (
    KundeID INT PRIMARY KEY,
    Adresse VARCHAR(255),
    Navn VARCHAR(255),
    Mobilnummer INT
);

--Billettkjop Table
CREATE TABLE Billettkjøp (
    KundeID INT,
    BillettID INT,
    KjøpsTid DATETIME NOT NULL,
    FOREIGN KEY (KundeID) REFERENCES Kunde(KundeID),
    FOREIGN KEY (BillettID) REFERENCES Billett(BillettID),
    PRIMARY KEY (KundeID, BillettID)
);
-------------------Ansatt---------------------

-- AnsattStatusType Table
CREATE TABLE AnsattStatusType (
    AnsattStatusTypeID INT PRIMARY KEY,
    StatusType VARCHAR(255)
);

-- Posisjon Table
CREATE TABLE AnsattPosisjon (
    PosisjonID INT PRIMARY KEY,
    PosisjonTekst VARCHAR(255)
);

-- Ansatt Table
CREATE TABLE Ansatt (
    AnsattID INT PRIMARY KEY,
    AnsattStatusTypeID INT,
    AnsattPosisjonID INT,
    Navn VARCHAR(255),
    Epost VARCHAR(255),
    FOREIGN KEY (AnsattStatusTypeID) REFERENCES AnsattStatusType(AnsattStatusTypeID),
    FOREIGN KEY (AnsattPosisjonID) REFERENCES AnsattPosisjon(PosisjonID)
);

CREATE TABLE Oppgave (
    OppgaveID INT PRIMARY KEY,
    OppgaveTekst VARCHAR(255)
);

-- AnsattOppgave Table
CREATE TABLE AnsattOppgave (
    ForestillingsID DATETIME,
    AnsattID INT,
    OppgaveID INT,
    FOREIGN KEY (ForestillingsID) REFERENCES Forestilling(ForestillingsID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID),
    PRIMARY KEY (ForestillingsID, AnsattID)
);