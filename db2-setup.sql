--------------------Stykke----------------------------
-- SesongType Table
CREATE TABLE SesongType (
    SesongTypeID INT PRIMARY KEY,
    Navn VARCHAR(255) NOT NULL
);

-- Stykke Table
CREATE TABLE Stykke (
    StykkeID INT PRIMARY KEY,
    Navn VARCHAR(255) NOT NULL
);

-- SesongStykke Table
CREATE TABLE SesongStykke (
    SesongStykkeID INT PRIMARY KEY,
    StykkeID INT NOT NULL,
    SesongTypeID INT NOT NULl,
    SesongÅr INT NOT NULL,
    SalID INT NOT NULL,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID),
    FOREIGN KEY (SesongTypeID) REFERENCES SesongType(SesongTypeID),
    FOREIGN KEY (SalID) REFERENCES Sal(SalID)
);

-------------Akt og Rolle----------------
-- Akt Table
CREATE TABLE Akt (
    AktNr INT NOT NULL,
    StykkeID INT NOT NULL,
    AktID INT NOT NULL,
    AktNavn VARCHAR(255),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID),
    PRIMARY KEY (AktNr, StykkeID)
);

-- Rolle Table
CREATE TABLE Rolle (
    RolleID INT PRIMARY KEY,
    RolleNavn VARCHAR(255) NOT NULL,
    StykkeID INT NOT NULL,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- AktRolle Table
CREATE TABLE AktRolle (
    AktID INT NOT NULL,
    RolleNavn VARCHAR(255) NOT NULL,
    AnsattID INT NOT NULL,
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
    SalID INT NOT NULL,
    StykkeID INT NOT NULL,
    FOREIGN KEY (SalID) REFERENCES Sal(SalID),
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- Område Table
CREATE TABLE Område (
    SalID INT NOT NULL,
    OmrådeNavn VARCHAR(255),
    FOREIGN KEY (SalID) REFERENCES Sal(SalID),
    PRIMARY KEY (SalID, OmrådeNavn)
);

-- Stol Table
CREATE TABLE Stol (
    SalID INT NOT NULL,
    OmrådeNavn VARCHAR(255),
    StolNo INT NOT NULL,
    RadNo INT,
    FOREIGN KEY (SalID, OmrådeNavn) REFERENCES Område(SalID, OmrådeNavn),
    PRIMARY KEY (SalID, OmrådeNavn, StolNo, RadNo)
);

-------------------------Bilett-------------------------
-- BillettType Table
CREATE TABLE BillettType (
    BillettTypeID INT PRIMARY KEY,
    Navn VARCHAR(255),
    StykkeID INT NOT NULL,
    Pris INT,
    FOREIGN KEY (StykkeID) REFERENCES Stykke(StykkeID)
);

-- Billett Table
CREATE TABLE Billett (
    BillettID INT PRIMARY KEY,
    BillettTypeID INT NOT NULL,
    ForestillingsID INT NOT NULL,
    SalID INT NOT NULL, 
    OmrådeNavn VARCHAR(255), 
    StolNo INT NOT NULL, 
    RadNo INT,
    FOREIGN KEY (BillettTypeID) REFERENCES BillettType(BillettTypeID),
    FOREIGN KEY (ForestillingsID) REFERENCES Forestilling(ForestillingsID),
    FOREIGN KEY (SalID, OmrådeNavn, StolNo, RadNo) REFERENCES Stol(SalID, OmrådeNavn, StolNo, RadNo)
);

--Kunde Table
CREATE TABLE Kunde (
    KundeID INT PRIMARY KEY,
    Adresse VARCHAR(255),
    Navn VARCHAR(255) NOT NULL,
    Mobilnummer INT UNIQUE NOT NULL
);

--Billettkjop Table
CREATE TABLE Billettkjøp (
    KundeID INT NOT NULL,
    BillettID INT NOT NULL,
    KjøpsTid DATETIME NOT NULL,
    FOREIGN KEY (KundeID) REFERENCES Kunde(KundeID),
    FOREIGN KEY (BillettID) REFERENCES Billett(BillettID),
    PRIMARY KEY (KundeID, BillettID)
);
-------------------Ansatt---------------------

-- AnsattStatusType Table
CREATE TABLE AnsattStatusType (
    AnsattStatusTypeID INT PRIMARY KEY,
    StatusType VARCHAR(255) NOT NULL
);

-- Posisjon Table
CREATE TABLE AnsattPosisjon (
    PosisjonID INT PRIMARY KEY,
    PosisjonTekst VARCHAR(255) NOT NULL
);

-- Ansatt Table
CREATE TABLE Ansatt (
    AnsattID INT PRIMARY KEY,
    AnsattStatusTypeID INT NOT NULL,
    AnsattPosisjonID INT NOT NULL,
    Navn VARCHAR(255) NOT NULL,
    Epost VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (AnsattStatusTypeID) REFERENCES AnsattStatusType(AnsattStatusTypeID),
    FOREIGN KEY (AnsattPosisjonID) REFERENCES AnsattPosisjon(PosisjonID)
);

CREATE TABLE Oppgave (
    OppgaveID INT PRIMARY KEY,
    OppgaveTekst VARCHAR(255) NOT NULL
);

-- AnsattOppgave Table
CREATE TABLE AnsattOppgave (
    ForestillingsID INT NOT NULL,
    AnsattID INT NOT NULL,
    OppgaveID INT NOT NULL,
    FOREIGN KEY (ForestillingsID) REFERENCES Forestilling(ForestillingsID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID),
    PRIMARY KEY (ForestillingsID, AnsattID)
);